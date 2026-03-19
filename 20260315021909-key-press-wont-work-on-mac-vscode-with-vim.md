---
id: 20260315021909
title: vscode(mac)の vimで長押しできない
aliases: ["20260315021909"]
created: 2026-03-15 14:19
tags: [reference/experience, reference/ai]
publish: true
draft: false
lastmod: 2026-03-20 01:19
---
ターミナルで以下のコマンドを打って、vscodeを再起動したら解決した。
```bash
defaults write com.microsoft.VSCode ApplePressAndHoldEnabled -bool false
```
---
## Ref
2026/03/15
- ChatGPT との会話
- 経験