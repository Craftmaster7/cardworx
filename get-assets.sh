#!/usr/bin/env bash
# Run by the GitHub Action or locally; idempotent.
# Downloads every image the site needs into ./assets (Wix originals + Higgsfield generations).
cd "$(dirname "$0")"; mkdir -p assets
for f in assets-manifest.txt generated-manifest.txt; do
  while IFS='|' read -r name url; do
    [ -z "$name" ] && continue
    [ -s "assets/$name" ] && { echo "  have $name"; continue; }
    echo "  $name"; curl -fsL "$url" -o "assets/$name" || { echo "  FAILED $name"; rm -f "assets/$name"; }
  done < "$f"
done
echo "Done. $(ls assets | wc -l) files in assets/"
