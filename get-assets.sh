#!/usr/bin/env bash
# Downloads every image the site needs into ./assets (Wix originals + Higgsfield generations).
cd "$(dirname "$0")"; mkdir -p assets
for f in assets-manifest.txt generated-manifest.txt; do
  while IFS='|' read -r name url; do
    [ -z "$name" ] && continue
    echo "  $name"; curl -sL "$url" -o "assets/$name"
  done < "$f"
done
echo "Done. $(ls assets | wc -l) files in assets/"
