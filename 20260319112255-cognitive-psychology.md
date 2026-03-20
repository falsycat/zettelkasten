---
id: 20260319112255
title: 認知心理学
aliases: ["20260319112255"]
created: 2026-03-19 23:22
tags: [reference/ai, structure]
publish: true
draft: false
lastmod: 2026-03-20 01:09
---
認知心理学とは、人間が刺激を受けてから意思決定を行うまでを体系的に記述する学問である。
## 意思決定プロセス
心は以下のような手順で情報処理する。
1. 感覚
2. [[20260320010738-perception|知覚]]
3. [[20260320101704-attention|注意]]
4. 記憶
5. 思考・推論
6. 言語・意思決定
```mermaid
flowchart TD
  D0([物理エネルギー<br>光・音・圧力・化学物質]):::data
  P1[感覚<br>物理エネルギー → 神経信号]:::proc
  D1([神経信号]):::data
  P2[知覚<br>神経信号 → 意味ある表象]:::proc
  D2([知覚的表象]):::data
  P3[注意<br>情報の選択・フィルタリング]:::proc
  D3([選択された情報]):::data
  P4[記憶<br>符号化・保持・検索]:::proc
  D4([貯蔵された知識]):::data
  P5[思考・推論<br>概念操作・問題解決]:::proc
  D5([処理済み情報]):::data
  P6[言語・意思決定<br>判断・行動の選択]:::proc
  D6([行動・反応]):::data

  D0 --> P1 --> D1 --> P2 --> D2 --> P3 --> D3 --> P4 --> D4 --> P5 --> D5 --> P6 --> D6

  D4 -.->|トップダウン| P2

  classDef data fill:#F1EFE8,stroke:#888780,color:#444441
  classDef proc fill:#EEEDFE,stroke:#534AB7,color:#3C3489
```
---
## Ref
2026/03/19
- Claude との会話