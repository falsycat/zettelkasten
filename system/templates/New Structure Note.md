---
<%*
const id = tp.file.creation_date("YYYYMMDDhhmmss");
await tp.file.move(id+"-new-structure-note-draft_");
-%>
id: <% id %>
title: 
aliases: ["<% id %>"]
created: <% tp.file.creation_date() %>
tags: structure
publish: false
---