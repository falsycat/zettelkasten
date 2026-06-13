# agent: add-notes

ユーザーの入力を最小単位のzettelkastenノートに分割して `cells/` へ保存する。

## ステップ

### 1. 入力を最小単位に分割

**1ノート = 1アイデア/1事実/1意見** の原則。

- 独立した複数の概念 → 別ノート
- 1概念が複数文 → 1ノートにまとめる
- 既存ノートと重複する内容 → 新規作成せず、リンクで参照

### 2. 既存ノートを調査

```bash
# タイトル一覧を取得
bash .claude/skills/zettelkasten/scripts/list-titles.sh

# キーワードで本文を横断検索
grep -rl "キーワード" cells/
```

### 3. ファイル名の連番を確認

```bash
date +%Y%m%d
ls cells/ | grep "^$(date +%Y%m%d)" | sort
```

### 4. ノートを作成・保存

`references/note-format.md` のフォーマット・`references/tags.md` のタグ定義に従って `cells/YYYYMMDDNN-slug.md` に書き込む。

- 既存ノートは変更しない
- 関連ノートがない場合は Related セクションを省略
- 複数ノート作成後、内容をまとめる `#struct` ノートが適切なら追加
