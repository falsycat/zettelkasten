---
id: 20260226121448
title: AntigravityのClaude/GPTのQuota制限が厳しい
aliases: ["20260226121448"]
created: 2026-02-26 00:14
tags: [reference/experience, reference/web]
publish: true
draft: false
lastmod: 2026-02-26 00:35
---
## 経緯
- AntigravityでClaudeを使おうとしたら、Quota制限にひっかかった
- 復活いつかなと思って確認したら、5,6日後だった
- Google AI Proに課金しているのに、なぜ遅いのか疑問に思った
## 調査結果
- 残念なことに、ClaudeとGPTについては、Geminiとは異なるQuota制限が課せられていた
	- Gemini Pro: 5時間で復活
	- Gemini Flash: 5時間で復活
	- Claude+GPT: 7日で復活
![[Pasted image 20260226003310.png]]
## 所感
- まじかよ。。。
- Google AI Ultraは流石に払えん。。。
---
## Ref
2026/02/26
- 経験より
- [#273 課金しても止まる？Antigravityの17時間待ち制限と回避策｜ちーみつ｜知識ゼロからの「AI活用」実験ログ](https://note.com/chi3jp/n/n144c618a5ee4)