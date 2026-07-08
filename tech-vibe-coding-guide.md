---
tags:
  - Vibe Coding
  - AI工具
  - 开发工具
authors:
  - kindness314
---
# Vibe Coding 使用指南

## 目录

1. Claude Code CLI 接入与 CC-Switch
2. OpenAI Codex CLI 接入
3. SDK 与 cURL 直调
4. Node.js 环境准备
5. 开篇：3 分钟搞懂四个词
6. 协作心法 1：先搞懂 AI 怎么花 token
7. 协作心法 2：把任务说清楚
8. 协作心法 3：两个省钱习惯
9. 协作心法 4：CLAUDE.md / AGENTS.md 模板
10. Context7：让 AI 查最新文档
11. Serena：符号级代码导航
12. Playwright MCP：AI 自己开浏览器
13. Exa：AI 联网搜索
14. DeepWiki：把 GitHub 仓库变成百科
15. CodeGraph：给仓库建代码地图
16. Codex 插件：双模型互相挑错
17. 官方插件市场
18. Understand-Anything：代码库知识图谱
19. Skill 入门：教 AI 新套路
20. Superpowers：开发方法论插件
21. Trellis：让 vibe coding 不失控
22. GSD：Git. Ship. Done
23. Task Master：把 PRD 拆成任务清单
24. Open Design：AI 设计工作台

---

## 01 · Claude Code CLI 接入与 CC-Switch

推荐用 CC-Switch 管理 Claude Code 的 provider 配置，便于在官方与自定义网关之间切换。

### 1. 安装 Node.js 与 Claude Code

如果还没有 Node.js，先参考下方 Node.js 安装章节。

```bash
npm install -g @anthropic-ai/claude-code
claude --version
```

### 2. 安装 CC-Switch

```bash
npm install -g cc-switch
cc --version
```

### 3. 创建 API Key

在控制台的 `API 密钥` 页面新建 Key：

- 选择服务分组，决定可用模型和折扣倍率。
- 给 Key 设置识别名，例如 `my-cc`。
- 保存后复制生成的 Key。Key 通常只显示一次，务必先保存。

### 4. 用 CC-Switch 添加网关

```bash
cc add suixiang \
  --base-url https://api.your-domain.com \
  --token sk-xxxxxxxxxxxxxxx
```

`suixiang` 是 provider 的本地名称，可以自行修改。

查看 provider 列表：

```bash
cc list
```

预期能看到官方 provider 与新添加的 provider。

### 5. 切换并验证

```bash
cc use suixiang
claude
```

如果 Claude Code 能正常回复，说明接入成功。

切回官方：

```bash
cc use anthropic
```

### 直接使用环境变量

如果不想安装 CC-Switch，也可以直接配置环境变量。

macOS / Linux：

```bash
export ANTHROPIC_BASE_URL="https://api.your-domain.com"
export ANTHROPIC_AUTH_TOKEN="sk-xxxxxxxxxxxxxxx"
```

Windows PowerShell：

```powershell
$env:ANTHROPIC_BASE_URL = "https://api.your-domain.com"
$env:ANTHROPIC_AUTH_TOKEN = "sk-xxxxxxxxxxxxxxx"
```

永久生效时，可把配置写入 `~/.bashrc`、`~/.zshrc` 或 Windows 用户环境变量。

### 常见问题

- `401 Unauthorized`：检查 `AUTH_TOKEN` 是否拼错，或 Key 是否被禁用。
- 连接超时：检查 `BASE_URL` 是否正确，Anthropic 路径不要带尾部 `/v1`。
- 模型不可用：确认服务分组是否支持该模型。
- `cc use` 后仍连接官方：新开一个终端窗口，CC-Switch 写入的 shell 环境变量通常需要新窗口生效。

### CC-Switch 快速参考

安装：

```bash
npm install -g cc-switch
cc --version
```

添加 provider：

```bash
cc add suixiang \
  --base-url https://api.your-domain.com \
  --token sk-xxxxxxxxxxxxxxx
```

切换和查看：

```bash
cc use suixiang
cc use anthropic
cc list
```

切换后建议新开终端窗口。

---

## 02 · OpenAI Codex CLI 接入

Codex 走 OpenAI 协议路径，只需把 `base_url` 指向目标网关。

### 1. 安装 Codex

```bash
npm install -g @openai/codex
```

### 2. 创建 Key

在控制台的 `API 密钥` 页面创建 Key。因为 Codex 使用 OpenAI 协议，创建 Key 时选择支持 GPT 模型的服务分组。

### 3. 配置 Codex

推荐使用 `~/.codex/config.toml`：

```toml
model_provider = "suixiang"
model = "gpt-5"

[model_providers.suixiang]
name = "随想 AI"
base_url = "https://api.your-domain.com/v1"
wire_api = "responses"
env_key = "SUIXIANG_API_KEY"
```

写入环境变量：

```bash
export SUIXIANG_API_KEY="sk-xxxxxxxxxxxxxxx"
```

### 4. 验证

```bash
codex --help
codex "帮我写一个 fibonacci 函数"
```

Codex 默认会读取当前目录上下文，建议在项目根目录运行。

### 多账户切换

如果同时使用官方账号和自定义网关账号，可以用 CC-Switch 这类工具管理切换。

---

## 03 · SDK 与 cURL 直调

除了 CLI，也可以直接用官方 SDK 或 cURL 调用网关。通常只需要修改 `base_url`。

### Python · Anthropic SDK

```python
from anthropic import Anthropic

client = Anthropic(
    base_url="https://api.your-domain.com",
    api_key="sk-xxxxxxxxxxxxxxx",
)

msg = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "你好"}],
)

print(msg.content[0].text)
```

### Python · OpenAI SDK

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.your-domain.com/v1",
    api_key="sk-xxxxxxxxxxxxxxx",
)

resp = client.chat.completions.create(
    model="gpt-5",
    messages=[{"role": "user", "content": "你好"}],
)

print(resp.choices[0].message.content)
```

### Node.js · Anthropic SDK

```js
import Anthropic from "@anthropic-ai/sdk"

const client = new Anthropic({
  baseURL: "https://api.your-domain.com",
  apiKey: "sk-xxxxxxxxxxxxxxx",
})

const msg = await client.messages.create({
  model: "claude-sonnet-4-6",
  max_tokens: 1024,
  messages: [{ role: "user", content: "你好" }],
})

console.log(msg.content[0].text)
```

### cURL · OpenAI 协议

```bash
curl https://api.your-domain.com/v1/chat/completions \
  -H "Authorization: Bearer sk-xxxxxxxxxxxxxxx" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5",
    "messages": [{"role":"user","content":"hi"}]
  }'
```

网关可同时兼容 OpenAI、Anthropic、Gemini 等协议路径时，一份 Key 可复用到多个客户端。

---

## 04 · Node.js 环境准备

### Windows

Windows 推荐使用官方 MSI 安装包。

### 1. 下载 Node.js LTS

访问 <https://nodejs.org/zh-cn/download>，下载 Windows Installer `.msi`，选择 64-bit 与 LTS 版本。

### 2. 安装

- 双击 `.msi` 文件。
- 保持默认选项，并确认勾选 `Add to PATH`。
- 安装完成后新开 PowerShell。

### 3. 验证

```powershell
node -v
npm -v
```

### 多版本切换

如需切换多个 Node.js 版本，可使用 nvm-windows：

- 下载地址：
- 安装 `nvm-setup.exe`
- 常用命令：

```powershell
nvm install 20
nvm use 20
```

内网或下载慢时可切换 npm 镜像：

```bash
npm config set registry https://registry.npmmirror.com
```

### macOS

macOS 推荐使用 Homebrew + nvm。

### 1. 安装 Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

安装后按提示把 `brew` 加入 PATH。

### 2. 安装 nvm

```bash
brew install nvm

mkdir -p ~/.nvm
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.zshrc
echo '[ -s "$(brew --prefix)/opt/nvm/nvm.sh" ] && \. "$(brew --prefix)/opt/nvm/nvm.sh"' >> ~/.zshrc
source ~/.zshrc
```

### 3. 安装 Node.js LTS

```bash
nvm install --lts
nvm use --lts
nvm alias default 'lts/*'
```

### 4. 验证

```bash
node -v
npm -v
which node
```

常见问题：

- `command not found: nvm`：重新打开终端或执行 `source ~/.zshrc`。
- 装包慢：执行 `npm config set registry https://registry.npmmirror.com`。
- 不想使用 nvm 时可以直接 `brew install node`，但后续版本切换不方便。

### Linux

Linux 推荐使用 nvm，避免系统包管理器中的 Node.js 版本滞后。

### 1. 安装 nvm

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
```

如果使用 zsh：

```bash
source ~/.zshrc
```

### 2. 安装 Node.js LTS

```bash
nvm install --lts
nvm use --lts
nvm alias default 'lts/*'
```

### 3. 验证

```bash
node -v
npm -v
```

### 系统包管理器备选

Ubuntu / Debian：

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```

CentOS / RHEL / Fedora：

```bash
curl -fsSL https://rpm.nodesource.com/setup_lts.x | sudo bash -
sudo dnf install -y nodejs
```

### npm 全局目录权限

如果使用系统包管理器安装 Node.js，`npm install -g` 可能需要权限。可把全局目录改到用户目录：

```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

Linux 服务器上也可以优先考虑 Python SDK 或 cURL 直调，CLI 更适合桌面开发环境。

---

## 05 · 开篇：3 分钟搞懂四个词

### 四个核心概念

- MCP：给 AI 增加外部能力的接口，例如联网、打开浏览器、查询文档。Claude Code 和 Codex 都支持。
- Plugin：一键安装的功能包，通常自带斜杠命令。Claude Code 与 Codex 的插件商店互不通用。
- Skill：用 Markdown 编写的能力说明，放入指定目录即可生效。两家使用同一套开放标准，但目录不同。
- Workflow：给 AI 套上的工作流程，用来防止任务改着改着失控。

### 装备速览

| 类型 | 工具 | 用途 |
| --- | --- | --- |
| MCP | Context7 | 查询最新官方文档 |
| MCP | Serena | 符号级代码阅读 |
| MCP | Playwright MCP | 让 AI 操作浏览器、验收前端 |
| MCP | Exa | 联网搜索最新资料 |
| MCP | DeepWiki | 把 GitHub 仓库变成可问答百科 |
| MCP | CodeGraph | 建代码地图，查调用关系 |
| 插件 | Codex 插件 | Claude 写码，Codex/GPT 复查 |
| 插件 | Superpowers | 注入开发方法论 |
| 插件 | 官方插件市场 | 代码审查、前端设计、GitHub 集成等 |
| 插件 | Understand-Anything | 项目知识图谱 |
| Skill | Agent Skills | 用 Markdown 教 AI 新套路 |
| Workflow | Trellis | 计划、执行、沉淀经验 |
| Workflow | GSD | spec 驱动开发 |
| Workflow | Task Master | PRD 拆任务清单 |
| 设计工具 | Open Design | 生成网页、海报、PPT、视频原型 |

### 三种安装方式

MCP：

```bash
claude mcp add 名字 -- 启动命令
codex mcp add 名字 -- 启动命令
```

插件：

```text
Claude Code: /plugin
Codex: /plugins
```

Skill：

```text
Claude Code: ~/.claude/skills/
Codex: ~/.agents/skills/
```

### 场景速查

| 场景 | 推荐工具 |
| --- | --- |
| 担心 AI 使用过时 API | Context7 |
| 仓库太大、token 消耗高 | Serena、CodeGraph |
| 前端改完要自动验收 | Playwright MCP |
| 查询最新资料、版本、价格 | Exa |
| 快速读懂开源项目 | DeepWiki、Understand-Anything |
| bug 修不动，想换模型复查 | Codex 插件 |
| 项目改着改着失控 | Trellis |
| 生成海报、网页原型、PPT | Open Design |

---

## 06 · 协作心法 1：先搞懂 AI 怎么花 token

AI 编程 CLI 背后通常是 agent。它接到任务后会经历：读代码、猜意图、尝试修改、运行验证、失败后再调。每一步都会消耗 token。

最费钱的通常不是写代码，而是猜。需求越含糊，AI 越需要用想象补空；猜错后就会返工、重读、重试。

省 token 的核心不是少打字，而是一开始把任务说清楚，减少后续返工。

三步：

1. 学习 AI：理解它会读、猜、试错。
2. 要求 AI：把任务、边界、目标说清楚。
3. 约束 AI：把重复规则写进配置文件。

---

## 07 · 协作心法 2：把任务说清楚

### 1. 开口前先划边界

| 维度 | 含糊说法 | 具体说法 |
| --- | --- | --- |
| 技术栈 | 做个前端页 | Vue 3 + Tailwind，组件用 shadcn-vue |
| 内容 | 放点介绍 | 一句 slogan + 3 个卖点卡 + 一个按钮 |
| 风格 | 好看点 | 黑白极简、大标题、留白多，参考 Linear 官网 |
| 动效 | 加点动画 | 卡片滚入时淡入上移，不用第三方动画库 |
| 边界 | 未说明 | 静态页，不加 loading 和错误处理 |

拿不准的地方可以直接写：`这块你拿不准就先问我`。

### 2. 反馈要给坐标

不要只说：

```text
不对，重做。
```

更好的反馈：

```text
登录按钮点了没反应。问题在 LoginForm.vue 的 onSubmit。
login() 那个 promise 没有 await，所以转圈状态没起来。
改成 await，失败时在 catch 里弹 toast。
```

反馈时尽量说清楚四件事：

- 哪里错。
- 怎么改。
- 为什么。
- 我要什么结果。

### 3. 复杂任务先要计划

Claude Code：

```text
先别动代码，说下思路：改哪些文件、怎么改、有什么风险。
我点头你再写。
```

Codex：

```text
先出方案，等我确认再写。
```

### 4. 大任务拆给子 agent

需要大量搜索、调研、扫描文件的任务，可以交给子 agent，让主对话只保留结论和决策，减少上下文噪音。

---

## 08 · 协作心法 3：两个省钱习惯

### 1. 做好一段就 commit

一段功能完成并自测后，马上提交：

```bash
git add -A
git commit -m "feat: 登录按钮加转圈和错误提示"
```

好处：

- AI 可以从 commit 历史理解这次修改的基础。
- 后续改崩时可以回到干净状态。

丢弃未提交改动：

```bash
git restore .
```

### 2. 换任务就清上下文

同一件事干到一半不要清上下文；换到不相关任务时应清理。

Claude Code：

```text
/clear
```

Codex：

```text
/new
```

判断标准：接下来这件事是否需要刚才的上下文。用不上就清。

---

## 09 · 协作心法 4：CLAUDE.md / AGENTS.md 模板

把常用规则写进配置文件，减少每次重复说明。

Claude Code：

```text
~/.claude/CLAUDE.md
<项目根>/CLAUDE.md
```

Codex：

```text
~/.codex/AGENTS.md
<项目根>/AGENTS.md
```

两者都是普通 Markdown。项目级配置优先级更高。

### 推荐写入内容

- 读代码方式：先看结构，再下钻到函数。
- 遇到第三方库：先查最新文档，不凭记忆写 API。
- 不允许做的事：不要跳过测试、不要加未要求的兜底逻辑。
- 沟通方式：默认中文，先给结论。
- 项目坑点：大目录、无权限目录、特殊构建流程等。

### 通用模板

```markdown
## 协作准则

### 沟通
- 默认中文。代码、命令、路径、报错保持原文。
- 先给结论 + 关键理由，别长篇大论。
- 可能变化的信息（版本、价格、库 API）先查证再说，别凭记忆。
- 没验证过别说“完成”“通过”“可提交”。

### 干活原则
- 先把需求问清楚再动手；先小范围，别一上来铺很大。
- 改之前先读相关文件、配置、最近几条 commit。
- 我要方案 / 计划时，别擅自改源码。
- 优先最小改动，别加没要求的兜底和包装。
- 复杂活先出计划等我确认；简单活直接做。
- 别动我没提交的改动；有冲突先停下问我。

### 读代码
- 先看文件 / 模块骨架，再下钻到具体函数。
- 找字符串 / 配置用 rg；别用全盘递归 grep。
- 大目录（node_modules 等）和没权限的目录，绕开别扫。

### 改完要做
- 跑 lint / 类型检查 / 测试，绿了再说完成。
- 给 interface 加方法，记得把所有 mock / stub 一起补。

### 不许做
- 别 mock 掉测试、跳过测试当“通过”。
- 别凭训练数据猜第三方库的新版 API。
- 别在我没要求时加降级 / 兜底分支，这会改变可见行为。

### 提交
- 中文提交信息，格式：类型: 简短描述
- 类型：feat / fix / refactor / docs / test / chore
```

四个协作原则：

1. 配置先放好：项目里有 `CLAUDE.md` 或 `AGENTS.md`。
2. 说清楚再下达：带上技术栈、内容、风格、边界。
3. 纠错给坐标：说明哪里错、怎么改、为什么。
4. 勤提交、勤清场：一段稳了就 commit，换任务就 `/clear` 或 `/new`。

---

## 10 · Context7：让 AI 查最新文档

Context7 用于让 AI 在写代码前查询最新官方文档，减少过时 API 问题。

接入：

```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
codex mcp add context7 -- npx -y @upstash/context7-mcp@latest
```

使用示例：

```text
用 context7 查一下 Vue 3.6 的 defineModel 怎么用，然后帮我改这个组件。
```

适合新框架、新版本、新库相关任务。

---

## 11 · Serena：符号级代码导航

Serena 能按函数、类、引用关系读取代码，适合大仓库，减少整文件读取带来的 token 消耗。

安装 uv：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

接入：

```bash
claude mcp add serena -- uvx --from git+https://github.com/oraios/serena \
  serena start-mcp-server --context ide-assistant

codex mcp add serena -- uvx --from git+https://github.com/oraios/serena \
  serena start-mcp-server --context ide-assistant
```

首次进入项目：

```text
用 serena 激活当前项目并完成 onboarding。
```

适合“找出谁调用了某函数”“重命名某个服务类”等任务。

---

## 12 · Playwright MCP：AI 自己开浏览器

Playwright MCP 让 AI 打开浏览器、点击页面、填表单、截图、查看 console 错误，适合前端验收。

接入：

```bash
claude mcp add playwright -- npx -y @playwright/mcp@latest
codex mcp add playwright -- npx -y @playwright/mcp@latest
```

使用示例：

```text
打开 localhost:3000，点“登录”按钮，截图给我看。
```

首次运行会下载浏览器内核。调试时不加参数可观察浏览器操作；后台静默运行可在启动命令末尾加 `--headless`。

---

## 13 · Exa：AI 联网搜索

Exa 用于查询最新资讯、版本、价格、报错解法，并返回来源链接。

### 1. 获取 Key

访问 <https://dashboard.exa.ai> 注册并复制 API Key。

### 2. 接入

Claude Code：

```bash
claude mcp add exa -e EXA_API_KEY=你的Key -- npx -y exa-mcp-server
```

Codex：

```bash
codex mcp add exa --env EXA_API_KEY=你的Key -- npx -y exa-mcp-server
```

### 3. 使用

```text
搜一下 Tailwind 4 正式版有哪些破坏性变更。
```

版本、价格、新闻等时效性问题，优先让 AI 搜索，不要凭记忆回答。

---

## 14 · DeepWiki：把 GitHub 仓库变成百科

DeepWiki 是在线服务，可把公开 GitHub 仓库变成可问答的知识库。

接入：

```bash
claude mcp add --transport http deepwiki https://mcp.deepwiki.com/mcp
codex mcp add deepwiki --url https://mcp.deepwiki.com/mcp
```

使用示例：

```text
用 deepwiki 查 vuejs/core：响应式系统是怎么实现的？
```

Exa 适合全网搜索，DeepWiki 适合深挖某一个仓库。冷门仓库可先在 <https://deepwiki.com> 搜索确认是否已收录。

---

## 15 · CodeGraph：给仓库建代码地图

CodeGraph 用于构建代码关系图，查询调用关系和影响范围。

安装：

```bash
npm install -g @colbymchenry/codegraph
```

在项目根目录建索引：

```bash
codegraph init
```

接入：

```bash
claude mcp add codegraph -- codegraph serve --mcp
codex mcp add codegraph -- codegraph serve --mcp
```

使用示例：

```text
这个项目的支付回调是怎么走的？从入口到落库讲一遍。
```

索引建立后，文件改动会自动同步。

---

## 16 · Codex 插件：双模型互相挑错

把 OpenAI Codex 装进 Claude Code，可用于第二模型复查代码或诊断疑难 bug。

### 1. 安装 Codex CLI

```bash
npm install -g @openai/codex
```

### 2. 在 Claude Code 中安装插件

```text
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
```

### 3. 使用

```text
这个 bug 我修了三次都不对，让 codex 来诊断一下。
```

适合“Claude 动手写，Codex/GPT 复查”的流程。

---

## 17 · 官方插件市场

Claude Code 与 Codex 都有插件入口：

```text
Claude Code: /plugin
Codex: /plugins
```

Claude Code 推荐插件：

```text
/plugin install code-review@claude-plugins-official
/plugin install frontend-design@claude-plugins-official
/plugin install github@claude-plugins-official
```

常用命令：

```text
/code-review
```

写 TypeScript、Go、Rust 等项目时，可安装对应语言服务插件，让 AI 修改代码时实时获取类型报错。

---

## 18 · Understand-Anything：代码库知识图谱

Understand-Anything 用于把陌生代码库生成可交互知识图谱，适合接手老项目或读开源源码。仅适用于 Claude Code 插件。

安装：

```text
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything@understand-anything
```

运行分析：

```text
/understand
```

打开图谱：

```text
/understand-dashboard
```

生成项目上手指南：

```text
/understand-onboard
```

---

## 19 · Skill 入门：教 AI 新套路

Skill 是用 Markdown 编写的能力说明，放进目录后即可被 AI 使用。

### 目录

Claude Code：

```text
~/.claude/skills/
项目/.claude/skills/
```

Codex：

```text
~/.agents/skills/
项目/.agents/skills/
```

### 从官方仓库安装

```bash
git clone https://github.com/anthropics/skills
cp -r skills/想要的技能目录 ~/.claude/skills/
```

Codex 用户拷到：

```text
~/.agents/skills/
```

### 使用

Claude Code：

```text
把这份报告导出成 PDF。
```

Codex：

```text
$技能名 把这份报告导出成 PDF。
```

自己写 Skill：新建文件夹，放入 `SKILL.md`，开头写 `name` 和 `description`，正文写流程、规则和注意事项。

---

## 20 · Superpowers：开发方法论插件

Superpowers 是 Claude Code 插件，用于给 AI 注入头脑风暴、计划、TDD、系统化调试等开发方法论。

安装：

```text
/plugin install superpowers@claude-plugins-official
```

使用方式：正常描述需求即可。

```text
我想给项目加一个导出功能。
```

扩展市场：

```text
/plugin marketplace add obra/superpowers-marketplace
```

Superpowers 关注“怎么思考问题”，Trellis 关注“任务怎么流转”，两者可同时使用。

---

## 21 · Trellis：让 vibe coding 不失控

Trellis 用于把需求梳理、计划、实现、自查和经验沉淀串成流程。

安装：

```bash
npm install -g @mindfoldhq/trellis
```

项目初始化：

```bash
trellis init
```

使用示例：

```text
我想加一个导出功能，先帮我把需求理清楚。
```

AI 会按“理需求 → 写计划 → 实现 → 自查”的流程工作，关键决策会落到文档里。

跨会话查询记忆：

```bash
trellis mem "上次那个支付 bug 怎么修的"
```

---

## 22 · GSD：Git. Ship. Done

GSD 是 spec 驱动工作流，适合从零开始的新项目，把需求先固化成 spec，再分阶段实现和验收。

安装：

```bash
npx @opengsd/gsd-core@latest
```

安装时选择目标 CLI，例如 Claude Code、Codex、Cursor、Gemini CLI。

开始项目：

```text
/gsd-new-project
```

流程：

1. 定 spec。
2. 拆阶段。
3. 分段实现。
4. 验收。
5. ship。

已有项目需要流程管控时，优先看 Trellis。

---

## 23 · Task Master：把 PRD 拆成任务清单

Task Master 用于把 PRD 拆成带依赖关系的任务清单，适合大需求分步执行。

接入：

```bash
claude mcp add taskmaster-ai -- npx -y task-master-ai
codex mcp add taskmaster-ai -- npx -y task-master-ai
```

配置：

- 在项目根目录 `.env` 或 MCP 配置的 env 中填模型 API Key。
- 支持 Anthropic、OpenAI、OpenRouter 等模型服务。

使用：

```text
用 taskmaster 解析 docs/prd.md，拆成任务清单。
下一个该做哪个任务？
```

也可在终端直接使用：

```bash
npm i -g task-master-ai
task-master init
task-master parse-prd
```

---

## 24 · Open Design：AI 设计工作台

Open Design 是本地优先的开源 AI 设计工作台，可生成网页、海报、PPT、视频原型。

下载：

```text
https://github.com/nexu-io/open-design/releases
```

模型配置可使用 BYOK：

```text
base_url: https://api.your-domain.com/v1
api_key:  sk-你的Key
```

使用示例：

```text
给我的咖啡店做一张周年庆海报，复古风。
```

建议先选择 Design System，再输入需求，以提高出品稳定性。
