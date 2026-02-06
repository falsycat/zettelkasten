---
id: 20260207123640
title: 情報は品質を分類した上で一箇所にまとめるべき
aliases:
  - "20260207123640"
created: 2026-02-07 00:36
tags:
  - permanent
publish: true
draft: false
lastmod: 2026-02-07 00:41
---
- 異なる品質の情報を一箇所に保存するデータアーキテクチャを、[[20260207120908-lakehouse|Lakehouse]]と呼ぶ
- 品質による情報の分類の方法は[[20260207121010-medallion-architecture|メダリオンアーキテクチャ]]を参照
- 一元管理することで、出典を辿りやすくなり、AIにも食わせやすくなる
## 関連
- [[20260126125033-zettelkasten|zettelkasten]]
	- 情報をまとめて第2の脳を構築する手法
	- [[20260207122637-zettelkasten-is-lakehouse|zettelkastenはある意味Lakehouseである]]
- [[20260201031607-try-databricks|Databricksを使ってみた]]
	- Databricksは[[20260207120908-lakehouse|Lakehouse]]を最初に提唱したプロダクト
	- 保存だけでなく、処理・可視化までできちゃう