---
id: 20260220115803
title: QuartzでサイドバーにRecent Notesを表示する
aliases: ["20260220115803"]
created: 2026-02-20 23:58
tags: [reference/experience]
publish: true
draft: false
lastmod: 2026-02-21 00:23
---
## 経緯
- [[20260126125033-zettelkasten|zettelkasten]]でquartzを使っていくにあたり、サイドバーにはExplorerではなく、Recent Notesを表示したい
	- Explorerだとノートの木構造を表示できるが、ファイルを全く構造化しないzettelkastenだと相性が悪い
- 単純に `quartz.layout.ts`で`Explorer()`を`RecentNotes()`へ置き換えただけではうまくいかなかった
	- デスクトップだといい感じに表示される
	- スマホだとRecentNotesがハンバーガーメニューに格納されないため、レイアウトが崩れてしまう
## やりたいこと
- どんな環境でも美しく表示されるようにRecent Notesを表示したい
	- デスクトップではサイドバーに表示したい
	- スマホでは別に位置にこだわりはないが、どこかに表示したい
## 解決策
- デスクトップではサイドバーに、スマホではフッター部分に表示するようにする
	- `Component.MobileOnly`でwrapすることで、スマホだけに表示できる
	- `Component.DesktopOnly`でwrapすることで、デスクトップだけに表示できる
### コード
```ts
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [/*...*/],
  afterBody: [
    Component.MobileOnly(Component.RecentNotes({
      limit: 3,
      showTags: true,
    })),
  ],
  left: [
    // ...
    // Component.Explorer(),
    Component.DesktopOnly(Component.RecentNotes({
      limit: 10,
      showTags: false,
    })),
  ],
  right: [/*...*/],
}
```
---
## Ref
2026/02/20
- [Higher-Order Layout Components](https://quartz.jzhao.xyz/layout-components)
- Geminiとの会話より