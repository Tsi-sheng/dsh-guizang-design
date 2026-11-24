# 归藏设计 · Codex 移植

本目录同时提供 Codex 插件与本地市场清单。安装：

    codex plugin marketplace add Tsi-sheng/dsh-guizang-design --ref codex
    codex plugin add guizang-design@guizang-codex

Codex 加载 skills/ 的网页 PPT、卡片、网页排版、中文改稿、语气档案和原生 PowerPoint 技能。网页模式使用上游 HTML 模板和浏览器演讲者视图。PowerPoint 模式使用 guizang-powerpoint，读取同一套主题 token，可在保留文稿对象与动画的基础上生成新文件。

DSH 的侧栏、会话采集和 React 客户端属于 DSH 宿主。Codex 通过技能入口工作，语气档案从用户提供的样本开始。上游项目入口、素材来源和各技能许可证随 Fork 保留。
作品库由 guizang-library 提供聊天入口，可列出官方示例、组合工作流、登记本地作品和按原作继续制作。
