---
id: 20260220115803
title: QuartzでサイドバーにRecent Notesを表示する
aliases:
  - "20260220115803"
created: 2026-02-20 23:58
tags: reference
publish: true
draft: true
lastmod: 2026-01-24 11:00
---
## 経緯
- zettelkastenでquartzを使っていくにあたり、サイドバーにはExplorerではなく、Recent Notesを表示したい
	- Explorerだとノートの木構造を表示できるが、ファイルを全く構造化しないzettelkastenだと相性が悪い
- 単純に `quartz.layout.ts`で`Explorer()`を`RecentNotes()`へ置き換えただけではまともに動かなかった
	- 


---
## Ref
2026/02/20
- 