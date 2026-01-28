---
lastmod: 2026-01-24 10:45
---
## Draft Notes
```dataview
TABLE WITHOUT ID
  link(file.link, title) AS "Note"
FROM !"system"
WHERE draft = true OR endswith(file.name, "-draft_")
LIMIT 30
```
## Weak Reference Notes
```dataview
TABLE WITHOUT ID
  link(file.link, title) AS "Note",
  length(file.inlinks) AS "Links"
FROM !"system" AND #reference 
SORT length(file.inlinks) ASC
LIMIT 30
```
## Weak Permanent Notes
```dataview
TABLE WITHOUT ID
  link(file.link, title) AS "Note",
  length(file.inlinks)+length(file.outlinks) AS "Links"
FROM #permanent AND !"system"
SORT length(file.inlinks)+length(file.outlinks) ASC
LIMIT 30
```
