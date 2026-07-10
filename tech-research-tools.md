---
tags:
  - 科研工具
  - 学习资源
authors:
  - liugu2023
---
# 文献与科研工具指南

> 写课程论文、毕业设计或投稿文章时，文献管理和排版工具能减少很多重复整理工作。下面这些工具都有免费用法。
>
> 信息核实时间：2026 年 7 月。

## 文献管理：Zotero

[Zotero](https://www.zotero.org/) 是免费开源的文献管理器，浏览器插件一键抓取文献、自动生成参考文献格式（支持国标 GB/T 7714）、配合 Word / WPS 插件在论文里插入引用。

**免费扩容同步（坚果云 WebDAV）：**

Zotero 官方免费同步空间只有 300 MB，但**只有 PDF 附件占空间**，条目、笔记、批注不占。附件同步可以改用坚果云 WebDAV 免费扩容：

1. 坚果云官网 → 账户信息 → 安全选项 → 添加应用密码（注意：用生成的应用密码，不是登录密码）
2. Zotero → 设置 → 同步 → 文件同步方式改为 WebDAV，服务器地址填 `dav.jianguoyun.com/dav`
3. 点 Verify Server 验证通过即可

- 坚果云免费版限制：每月 1 GB 上传 / 3 GB 下载流量，对文献同步完全够用
- 2025 年下半年起坚果云推出了**官方 Zotero 插件**，可自动完成上述配置，不想手动填的可以去其 Release 页下载（注意区分 Zotero 7 / 8 版本）
- 已知坑：坚果云注册邮箱含下划线可能导致 WebDAV 验证失败，换个邮箱即可

**推荐插件**：Zotero 中文社区（[zotero-chinese.com](https://zotero-chinese.com/)）维护了插件商店和中文文档，翻译、茉莉花（中文文献元数据）、Better BibTeX 等按需安装。

## 论文排版：LaTeX / Typst

**Overleaf（在线 LaTeX）**

- 免费版够写单人课程论文和毕设，但要知道两个限制：**每个项目只能邀请 1 位协作者**、**编译超时 20 秒**（图多的大文档容易超）
- 超时的应对：草稿模式、压缩图片，或者把项目下载到本地用 TeX Live + VS Code 编译（完全免费且无限制）

**Typst（排版工具）**

- 语法比 LaTeX 更简洁，编译速度快，官方在线编辑器 [typst.app](https://typst.app/) 免费用
- 中文社区已有不少大学论文模板和简历模板；写简历、作业报告、笔记非常合适
- 局限：部分期刊 / 学校只收 LaTeX 或 Word 格式，投稿前先确认要求

## 找文献

- **[Google Scholar](https://scholar.google.com/)**：文献检索首选（国内访问不稳定时可用镜像或校园网环境尝试）
- **[arXiv](https://arxiv.org/)**：物理、数学、计算机领域的预印本，全部免费
- **[Semantic Scholar](https://www.semanticscholar.org/) / [Connected Papers](https://www.connectedpapers.com/)**：顺藤摸瓜找相关文献、可视化引用网络
- **校内数据库**：知网、Web of Science 等在校园网内可直接访问，校外访问方式见[在线服务板块](./campus-service-index.md)

## 参考链接

- [Zotero 中文社区同步指南](https://zotero-chinese.com/user-guide/sync)
- [坚果云 WebDAV 配置官方帮助](https://help.jianguoyun.com/?p=3168)
- [Overleaf 免费版限制官方文档](https://docs.overleaf.com/getting-started/free-and-premium-plans/plan-limits)
- [Typst 官网](https://typst.app/)

---

**作者**：[liugu2023](https://github.com/liugu2023) ![liugu2023](https://avatars.githubusercontent.com/liugu2023?s=40)
