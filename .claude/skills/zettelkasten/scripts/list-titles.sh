#!/usr/bin/env bash
# cells/ 以下の全ノートのファイル名とh1タイトルを出力する
# 出力形式: <ID>\t<title>

CELLS_DIR="$(cd "$(dirname "$0")/../../../.." && pwd)/cells"

for f in "$CELLS_DIR"/[0-9]*.md; do
  [ -f "$f" ] || continue
  title=$(grep -m1 '^# ' "$f" | sed 's/^# //')
  basename_no_ext=$(basename "$f" .md)
  printf '%s\t%s\n' "$basename_no_ext" "$title"
done
