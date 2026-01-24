---
<%*
const id = tp.file.creation_date("YYYYMMDDhhmmss");
await tp.file.move(id+"-new-reference-note");
-%>
id: <% id %>
title: 
aliases: ["<% id %>"]
created: <% tp.file.creation_date() %>
tags: reference
publish: false
draft: true
---
# New Reference Note

---
## Ref
<% tp.file.creation_date("YYYY/MM/DD") %>
- 