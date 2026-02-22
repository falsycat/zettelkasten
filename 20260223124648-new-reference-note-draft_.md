---
id: 20260223124648
title: QuartzのGraphでページ毎に色を替える
aliases: ["20260223124648"]
created: 2026-02-23 00:46
tags: [reference/experience, reference/web]
publish: true
draft: false
lastmod: 2026-02-23 00:59
---
## 経緯
- QuartzのGraph Viewは、[[20260126125033-zettelkasten|zettelkasten]]においてノートの関連を辿るのに役立っている
- ただし、全ノートが同じ様に表示されるため、Permanent/Referenceの区別がつかない
- 単にReferenceが多い島なのか、Permanentが多い島なのかを区別できないため、結局Obsidian側のGraph Viewで見るハメになっている
## やりたいこと
- QuartzにおけるGraph Viewで、ノートのタグに応じてノードの色を分けたい
## 解決策
- `quartz/components/scripts/graph.inline.ts`を直接変更する
### コード
```diff
diff --git a/quartz/components/scripts/graph.inline.ts b/quartz/components/scripts/graph.inline.ts
index a669b05..9cfce05 100644
--- a/quartz/components/scripts/graph.inline.ts
+++ b/quartz/components/scripts/graph.inline.ts
@@ -195,13 +195,14 @@ async function renderGraph(graph: HTMLElement, fullSlug: FullSlug) {
 
   // calculate color
   const color = (d: NodeData) => {
-    const isCurrent = d.id === slug
-    if (isCurrent) {
-      return computedStyleMap["--secondary"]
-    } else if (visited.has(d.id) || d.id.startsWith("tags/")) {
+    if (d.id === slug) {
       return computedStyleMap["--tertiary"]
-    } else {
+    } else if (d.tags.includes("structure")) {
+      return computedStyleMap["--secondary"]
+    } else if (d.tags.includes("permanent")) {
       return computedStyleMap["--gray"]
+    } else {
+      return computedStyleMap["--lightgray"]
     }
   }
```
---
## Ref
2026/02/23
- [quartz/quartz/components/scripts/graph.inline.ts at ec00a40aefca73596ab76e3ebe3a8e1129b43688 · jackyzha0/quartz · GitHub](https://github.com/jackyzha0/quartz/blob/ec00a40aefca73596ab76e3ebe3a8e1129b43688/quartz/components/scripts/graph.inline.ts#L30)
- [Graph View Node Custom Colors · Issue #1209 · jackyzha0/quartz · GitHub](https://github.com/jackyzha0/quartz/issues/1209)