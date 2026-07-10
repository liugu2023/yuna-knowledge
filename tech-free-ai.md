---
tags:
  - AI工具
  - 免费资源
  - API
authors:
  - liugu2023
---
# 免费 AI API 额度

> 这页记录几个仍有免费额度的 AI API 平台，适合课程练习、个人项目和接口测试。
>
> 免费额度是所有云服务里变动最快的（曾有平台一夜之间砍掉 80% 以上的免费额度），使用前务必去官网核实。

## 海外平台

### Google Gemini（AI Studio）

- 注册 Google 账号即可在 [AI Studio](https://aistudio.google.com) 获取 API Key，**无需信用卡**
- 免费层可调用包括 Gemini 3 Pro / Flash 在内的主力模型
- 注意两点：免费层的数据会被 Google 用于改进产品（勿传敏感内容）；2025 年 12 月 Google 曾无预告大幅下调免费额度（Flash 日请求数从约 250 次降到 20~50 次），额度之后仍可能变化

### OpenRouter

- 一个账号、一套 OpenAI 兼容接口，聚合调用几乎所有主流模型
- 提供约 24~28 个**完全免费**的模型（DeepSeek R1、Llama 3.3 70B、Qwen3 Coder、Gemma 3 等），无需信用卡
- 免费层限制：20 次/分钟、50 次/天；一次性充值 10 美元后提升到 1000 次/天
- 避坑：调用免费模型必须带 `HTTP-Referer` 和 `X-Title` 两个请求头，否则报 402 错误

### Groq

- 自研 LPU 芯片，推理延迟较低（首字延迟通常 200ms 以内），适合实时对话类应用
- 免费层仅限中小参数模型，不适合复杂推理任务

### Cerebras

- 免费层：5 次/分钟、3 万 tokens/分钟、100 万 tokens/天
- 可用模型包括 gpt-oss-120b、GLM 系列等

## 国内平台

### 智谱 AI（GLM）

- 新用户注册送 2000 万 tokens
- **GLM-4-Flash、GLM-Z1-Flash 永久免费**、不限 token 量（只限并发数），可作为国内接口的备用选择

### 硅基流动（SiliconCloud）

- DeepSeek-V3、Qwen3 系列等主流开源模型提供免费额度，新用户注册送 tokens

### 其他

- **Kimi（月之暗面）**：不限 token 只限频率，适合超长文档处理
- **火山引擎 / 百度千帆**：新用户各有百万级 token 赠送额度

## 实用策略

1. **多平台组合**：各平台的速率限制相互独立，组合使用可以分散限额压力
2. **写好重试逻辑**：免费 API 都有 RPM / RPD 限制，代码里加指数退避重试，429 错误自动等待
3. **准备备用平台**：一个平台不可用时自动切到下一个（可配合 [cc-switch](./tech-cc-switch.md) 或网关类工具管理多个供应商）
4. **免费层只用于学习和开发**：生产环境需要付费版的 SLA 保障
5. 需要经国内中转访问海外模型的场景，请先阅读 [API 中转站简介](./tech-relay.md)了解风险

<!-- TODO: 待补充各平台在校园网环境下的实测连通性；各家具体限额数字变化很快，此处只保留量级参考，精确数值以官网为准 -->

## 参考链接

- [Free LLM APIs in 2026: 13 家供应商对比](https://klymentiev.com/blog/free-llm-api)
- [FreeLLM-API-KeyHub（国内免费大模型 API 汇总）](https://github.com/guihuashaoxiang/FreeLLM-API-KeyHub)
- [2026 年免费大模型 API 平台汇总](https://www.xmsumi.com/detail/2885)

---

**作者**：[liugu2023](https://github.com/liugu2023) ![liugu2023](https://avatars.githubusercontent.com/liugu2023?s=40)
