---
tags:
  - Vibe Coding
  - AI工具
authors:
  - liugu2023
---
# Vibe Coding 工具简介

「Vibe coding」通常指用自然语言描述需求，让 AI 编程代理读取代码、修改文件、运行命令和检查结果。人仍然要负责说清需求、审查改动、保护数据，并决定是否采用结果。

如果你还分不清 Prompt、Token、Agent、工具调用和 MCP，可以先看 [LLM 常用术语解释](./tech-llm-glossary.md)。实际操作见 [Vibe Coding 使用指南](./tech-vibe-coding-guide.md)。

## 中国大陆使用提示

Claude、OpenAI 和 Gemini API 的官方支持地区目前均不包含中国大陆。账号注册、订阅付款、API 调用和校园网连通性不能按“默认可用”理解。代理或中转只能改变接入线路，不代表符合上游服务条款，也不能消除隐私、资金和数据跨境风险。

官方地区说明：

- [OpenAI API 支持地区](https://help.openai.com/en/articles/5347006-openai-api-supported-countries-and-territories)
- [Anthropic 支持地区](https://www.anthropic.com/supported-countries)
- [Gemini API 可用地区](https://ai.google.dev/gemini-api/docs/available-regions)

不要把课程账号密码、API Key、身份证信息、未公开论文、实验数据或实习代码发给不清楚数据政策的服务。

## 终端 CLI 类

### Claude Code

- **厂商**：Anthropic
- **形态**：终端工具，并提供桌面、IDE 和 Web 等入口
- **特点**：可以搜索代码库、修改多个文件、运行测试和 Git 命令；支持 MCP、Skills、Hooks 和子代理
- **使用方式**：可通过符合条件的 Claude 订阅登录，或按 API 用量计费；具体额度以官方说明为准

Claude Code 当前推荐原生安装。旧的 npm 安装方式仍可能工作，但官方已标记为 deprecated。

### OpenAI Codex

- **厂商**：OpenAI
- **形态**：开源 Codex CLI，以及 IDE、应用和云端任务等入口
- **特点**：适合在本地仓库中读写代码、运行验证，也可以把独立任务交给云端环境并行处理
- **使用方式**：支持符合条件的 ChatGPT 订阅登录；API 与订阅的权限和账单不是一回事

### Gemini CLI

- **厂商**：Google
- **形态**：开源命令行工具
- **特点**：支持 Gemini 模型和工具调用，个人账号通常有试用或免费配额
- **限制**：免费额度、模型和地区政策会变化；中国大陆不在 Gemini API 官方可用地区

### 其他开源工具

- **Aider**：开源 CLI 结对编程工具，支持多种模型供应商和兼容接口
- **OpenCode**：开源终端 Agent，支持多种模型供应商

社区工具的发布者、更新频率和权限模型不同。安装前应阅读仓库、许可证和安全说明，不要因为命令可以复制就直接运行。

## IDE / 编辑器类

- **Cursor**：基于 VS Code 的 AI 编辑器，提供补全和 Agent 功能
- **Windsurf**：AI 优先的代码编辑器
- **GitHub Copilot**：提供代码补全、聊天和 Agent 功能

通过 GitHub Education 验证的学生，在计划开放时可以申请 Copilot Student。截至 2026 年 7 月核验时，GitHub Student Developer Pack 页面提示新的学生计划注册暂时暂停；已有权益和后续开放状态以账户页面及 [GitHub Copilot 计划说明](https://docs.github.com/en/copilot/get-started/plans-for-github-copilot) 为准。聊天、Agent 和高级模型也不是所有功能无限使用。

## 怎么选

- 想从图形界面开始：先试学校或 GitHub Education 能合法获得的 IDE 工具。
- 已经熟悉终端和 Git：再尝试 Claude Code、Codex CLI、Gemini CLI 或开源工具。
- 预算有限：先核对学生权益、免费层的地区要求和用量上限，不要只看宣传中的“免费”。
- 需要切换多套配置：可使用 [cc-switch](./tech-cc-switch.md)，但它只是本地配置管理器。
- 考虑第三方 API：先阅读 [API 中转站简介](./tech-relay.md)，再决定是否承担相应风险。

无论使用哪种工具，都先让 Git 管好版本，查看每次 diff，并在执行删除、发布、付款、发送邮件等不可逆操作前停下来确认。
