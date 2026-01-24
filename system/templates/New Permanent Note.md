---
<%*
const id = tp.file.creation_date("YYYYMMDDhhmmss");
await tp.file.move(id+"-new-permanent-note");
-%>
id: <% id %>
title: 
aliases: ["<% id %>"]
created: <% tp.file.creation_date() %>
tags: permanent
publish: false
draft: true
---
