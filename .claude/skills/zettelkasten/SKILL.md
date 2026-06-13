# zettelkasten skill

falsycat のzettelkasten（第二の脳）リポジトリ。ノートは `cells/` に格納される。

## Agents

| エージェント | 概要 |
|---|---|
| [add-notes](agents/add-notes.md) | 自然言語の入力をノートに分割して保存する |
| [suggest-bridge-notes](agents/suggest-bridge-notes.md) | 孤立したクラスタ間を橋渡しする新規ノートを提案する（作成はしない） |

## Scripts

| スクリプト | 概要 | 出力形式 |
|---|---|---|
| [list-titles.sh](scripts/list-titles.sh) | 全ノートの ID とタイトルを一覧する | `<ID>\t<title>` |
| [list-deps.sh](scripts/list-deps.sh) | ノート間のリンク依存関係をエッジ一覧で出力する | `<source_id>\t<target_id>` |

## References

| リファレンス | 内容 |
|---|---|
| [note-format](references/note-format.md) | ノートのフォーマット・命名規則・リンク記法 |
| [tags](references/tags.md) | タグの種類と用途 |
