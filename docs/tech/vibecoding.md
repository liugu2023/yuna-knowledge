# Vibe Coding 工具简介

「Vibe coding」指的是用自然语言向 AI 描述需求，由 AI 代理（agent）直接读写代码、运行命令、完成开发任务的编程方式。开发者更多扮演「提需求 + 审查」的角色。以下介绍目前主流的工具。

## 终端 CLI 类

### Claude Code

- **厂商**：Anthropic
- **形态**：命令行工具（也有桌面应用、VS Code / JetBrains 插件、Web 版）
- **特点**：agentic 能力强，可以自主搜索代码库、编辑多个文件、运行测试和 git 操作；支持 MCP（Model Context Protocol）扩展外部工具；支持 Skills、Hooks、子代理（subagent）等高级玩法
- **付费方式**：随 Claude Pro / Max 订阅使用，或按 API 用量计费
- **官网**：<https://claude.com/claude-code>

### OpenAI Codex

- **厂商**：OpenAI
- **形态**：Codex CLI（开源命令行工具）+ Codex 云端代理（可在网页上派发任务，跑在云端沙箱里，完成后提 PR）
- **特点**：CLI 与 ChatGPT 订阅打通；云端模式适合并行派发多个独立任务
- **官网**：<https://openai.com/codex>

### Gemini CLI

- **厂商**：Google
- **形态**：开源命令行工具
- **特点**：有免费额度，上手门槛低；依托 Gemini 模型的长上下文

### 其他

- **Aider**：老牌开源 CLI 结对编程工具，可搭配任意模型 API
- **OpenCode**：开源的终端 agent，支持多种模型供应商

## IDE / 编辑器类

- **Cursor**：基于 VS Code 的 AI 编辑器，Tab 补全和 agent 模式都很成熟，vibe coding 的代表性产品
- **Windsurf**：同为 AI 优先的编辑器
- **GitHub Copilot**：最早普及的 AI 补全工具，现已加入 agent 模式；**学生认证 GitHub Education 后免费**（参见[校园邮箱板块](../campus/mail/index.md)的教育优惠部分）

## 怎么选？

- 想在终端里干活、喜欢可编程可定制 → Claude Code / Codex CLI
- 想要图形界面、平滑上手 → Cursor / Copilot
- 预算有限 → Gemini CLI 免费额度、GitHub 学生包的免费 Copilot
- 不想用官方 API 或订阅 → 参见 [cc-switch](./cc-switch.md) 与 [API 中转站简介](./relay.md)

## 待补充

<!-- TODO: 各工具在校园网环境下的连通性实测、订阅价格对比表 -->
