#!/usr/bin/env bash
# cells/ 以下の全ノートのリンク依存関係をエッジ一覧として出力する
# 出力形式: <source_id>\t<target_id>
# source_id が target_id を参照していることを意味する

CELLS_DIR="$(cd "$(dirname "$0")/../../../.." && pwd)/cells"

for f in "$CELLS_DIR"/[0-9]*.md; do
  [ -f "$f" ] || continue
  source=$(basename "$f" .md | grep -o '^[0-9]\{10\}')
  [ -z "$source" ] && continue

  # [[YYYYMMDDNN]] および [[YYYYMMDDNN|テキスト]] を抽出
  grep -oE '\[\[[0-9]{10}(\|[^]]+)?\]\]' "$f" \
    | grep -oE '[0-9]{10}' \
    | while read -r target; do
        [ "$source" != "$target" ] && printf '%s\t%s\n' "$source" "$target"
      done
done
