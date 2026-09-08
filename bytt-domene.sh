#!/bin/bash
# Byter Kneadly frå dr-grimen.github.io/kneadly til eit eige domene.
#
#   ./bytt-domene.sh kneadlymini.com
#
# Køyr denne FØRST når domenet er kjøpt OG DNS-postane er lagt inn.
# Legg du CNAME-fila ut før DNS peikar rett, blir butikken utilgjengeleg
# til DNS har spreidd seg.

set -euo pipefail
D="${1:-}"
[ -z "$D" ] && { echo "Bruk: ./bytt-domene.sh dittdomene.com"; exit 1; }

cd "$(dirname "$0")"
GAMMAL="dr-grimen.github.io/kneadly"

echo "→ sjekkar at DNS peikar på GitHub Pages…"
IP=$(dig +short "$D" A | head -1 || true)
case "$IP" in
  185.199.10[89].153|185.199.11[01].153) echo "  OK: $D → $IP" ;;
  "") echo "  ✗ $D har ingen A-post enno. Legg inn DNS først."; exit 1 ;;
  *)  echo "  ✗ $D peikar på $IP, ikkje GitHub Pages. Sjekk A-postane."; exit 1 ;;
esac

echo "→ oppdaterer URL-ar i alle filer…"
echo "$D" > CNAME
for f in *.html build_pages.py robots.txt sitemap.xml; do
  [ -f "$f" ] || continue
  sed -i '' "s|https://$GAMMAL/|https://$D/|g; s|https://$GAMMAL|https://$D|g" "$f"
done
python3 build_pages.py >/dev/null

echo "→ det som står att av gamle URL-ar:"
grep -rn "$GAMMAL" ./*.html ./*.py ./*.xml ./*.txt 2>/dev/null || echo "  ingen"

echo "→ commit + push…"
git add -A
git commit -q -m "Point the store at $D

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
git push -q origin main

echo "→ set custom domain på GitHub Pages…"
~/bin/gh api -X PUT "repos/Dr-grimen/kneadly/pages" -f "cname=$D" >/dev/null 2>&1 \
  || ~/bin/gh api -X POST "repos/Dr-grimen/kneadly/pages" -f "cname=$D" >/dev/null 2>&1 \
  || echo "  (kunne ikkje setje via API — set det manuelt i repo Settings → Pages)"

echo "→ ventar på HTTPS-sertifikat (kan ta nokre minutt)…"
for i in $(seq 1 30); do
  CODE=$(curl -s -o /dev/null -w '%{http_code}' "https://$D/" || echo 000)
  echo "   forsøk $i: https://$D → $CODE"
  [ "$CODE" = "200" ] && { echo "✓ FERDIG. Butikken svarer på https://$D"; exit 0; }
  sleep 20
done
echo "Sertifikatet er ikkje klart enno. Sjekk repo Settings → Pages → Enforce HTTPS om ei stund."
