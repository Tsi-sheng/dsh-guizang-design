---
name: guizang-powerpoint
description: 在 Codex 中用归藏电子杂志或瑞士设计语言制作可编辑的 PowerPoint，或给现有 PPTX 套用归藏主题并保留讲者备注和原生动画。
---

对于 HTML 演示，使用同一插件的 guizang-ppt-skill。对于 PPTX，从相邻 guizang-ppt-skill 的 references/themes.md、layouts.md 或对应 Swiss 文件选择主题与构图。依用户已选的视觉方向决定摄影、字形和强调色。新建文件时用演示环境提供的 PowerPoint 工具生成原生内容；文字、图表与反馈连线分别编辑。

为现有 PPTX 换主题时，先核对内容、图表、讲者备注和动画，再确定源文稿的颜色语义。scripts/theme_pptx.py 读取上游 HTML 模板的实际 token，改写幻灯片、母版、版式、主题和图表中的显式 RGB 色。需要 Python 3 和 lxml。示例：

    python scripts/theme_pptx.py input.pptx output.pptx --theme dune --map FFFFFF=paper --map 000000=ink --map 336699=accent

从本技能目录运行示例或使用脚本绝对路径。保留照片与数据色的意义；深底页、矩阵、反白文字需分别检查对比。同色承担不同语义时，在演示编辑器中单独处理该对象。变更布局、内容和字体时在副本内进行。渲染交付文件，核对图表数据、媒体、备注、分类动画对象与播放顺序。
