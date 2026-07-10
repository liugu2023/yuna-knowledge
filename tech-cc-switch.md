---
tags:
  - AI工具
  - 开发工具
  - 中转配置
authors:
  - liugu2023
---
# cc-switch 简介

[cc-switch](https://github.com/farion1231/cc-switch) 是一个开源的跨平台桌面工具，用来管理和一键切换 Claude Code、Codex、Gemini CLI 等 AI 编程工具的 API 供应商配置。当你同时用官方 API、第三方供应商、[中转站](./tech-relay.md)等多个渠道时，不用再手动改环境变量或配置文件。

## 它解决什么问题

Claude Code 等工具通过 `ANTHROPIC_BASE_URL`、`ANTHROPIC_API_KEY` 之类的环境变量决定请求发到哪里。想在多个供应商之间切换，就得反复手改配置——容易错、也麻烦。cc-switch 把各家供应商的配置保存成档案，点一下即可切换，原理就是动态覆盖这些环境变量/配置文件。

## 主要功能

- **多供应商管理**：为 Claude Code、Codex、OpenCode、Gemini CLI 等工具分别保存多套供应商配置，一键切换，各工具分组互不干扰
- **系统托盘常驻**：右键托盘菜单即可秒切
- **MCP 统一管理**：一次配置 MCP 服务器，多个工具共用
- **用量统计**：Token 消耗、缓存命中率、按模型/供应商分类的费用展示
- **自动备份**：定期备份配置数据库

## 安装

- 各平台安装包：[GitHub Releases](https://github.com/farion1231/cc-switch/releases/latest)
- macOS：`brew tap farion1231/ccswitch && brew install --cask cc-switch`
- Arch Linux：`paru -S cc-switch-bin`

## 相关链接

- 官网：
- 中文文档：[README_ZH](https://github.com/farion1231/cc-switch/blob/main/README_ZH.md)

## 待补充

<!-- TODO: 图文配置教程（添加供应商、切换、验证生效） -->

---

**作者**：[liugu2023](https://github.com/liugu2023) ![liugu2023](https://avatars.githubusercontent.com/liugu2023?s=40)
