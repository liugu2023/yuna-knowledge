---
tags:
  - 维护
  - 待办
  - 导航
authors:
  - xhx
---
# 按分类整理的待办清单

> 这是基于当前内容分类的**新版 TODO**，聚焦“每个类目下还缺什么”。
> 原来的 `TODO.md` 继续保留，按单项跟踪实测细节；本清单用于从分类视角看缺口。

## 建议分类

### 校园相关

- **校园必备服务**：每个在校师生都必须打交道的基础设施服务
  - 校园网：[`campus-network-index.md`](./campus-network-index.md)，[`campus-network-connect.md`](./campus-network-connect.md)，[`campus-network-qa.md`](./campus-network-qa.md)（待补充），[`campus-network-vpn.md`](./campus-network-vpn.md)
  - 校园服务门户（一网通办）：[`campus-service-index.md`](./campus-service-index.md)
  - 校园邮箱：[`campus-mail-index.md`](./campus-mail-index.md)
  - 正版化：[`campus-ms-index.md`](./campus-ms-index.md)

- **校园生活指南**：特定校园场景下的操作说明（多数待创建）
  - 教务系统与选课
  - 图书馆使用
  - 新生指南
  - 毕业离校指南

### 免费资源与前沿工具

- **免费资源**：利用学生身份或免费额度获取的服务
  - [`tech-student-pack.md`](./tech-student-pack.md)
  - [`tech-cloudflare.md`](./tech-cloudflare.md)
  - [`tech-free-cloud.md`](./tech-free-cloud.md)
  - [`tech-free-ai.md`](./tech-free-ai.md)
  - [`tech-domain.md`](./tech-domain.md)

- **学习与科研**：课程学习、论文写作、文献查找相关工具
  - [`tech-research-tools.md`](./tech-research-tools.md)
  - [`tech-mooc.md`](./tech-mooc.md)
  - [`tech-git-github.md`](./tech-git-github.md)
  - [`tech-oss-alternatives.md`](./tech-oss-alternatives.md)

- **前沿工具**：AI 编程与自托管/网络工具
  - [`tech-vibecoding.md`](./tech-vibecoding.md)
  - [`tech-cc-switch.md`](./tech-cc-switch.md)
  - [`tech-relay.md`](./tech-relay.md)
  - [`tech-self-hosting.md`](./tech-self-hosting.md)

---

## 具体待办清单

### 校园相关

### 校园必备服务

- [`campus-network-qa.md`](./campus-network-qa.md)（已创建，待补充）：校园网常见问题。
- 校园网各场景实测：宿舍有线/无线稳定性、运营商宽带绑定、选课高峰表现。
- 校园服务门户（一网通办）可补充：缴费等其他高频服务。

### 校园生活指南

- `campus-intro-freshman-guide.md`（待创建）：新生指南（报到、一卡通、宿舍网络首次配置）。
- `campus-intro-academic-guide.md`（待创建）：教务系统与选课（时间线、绩点规则、选课操作）。
- `campus-intro-library-guide.md`（待创建）：图书馆使用（借书、占座、数据库入口）。
- `campus-intro-graduation-guide.md`（待创建）：毕业离校指南（档案、户口、离校手续）。

> 目前教务、图书馆的部分内容散落在 [`campus-service-index.md`](./campus-service-index.md) 中，等生活指南文档补齐后可拆分迁移。

### 免费资源与前沿工具

### 免费资源

- [`tech-student-pack.md`](./tech-student-pack.md)：补充燕大学生申请 GitHub 学生包的实测记录。
- [`tech-cloudflare.md`](./tech-cloudflare.md)：校园网访问 Cloudflare 的实测速度、优选 IP 经验。
- [`tech-free-cloud.md`](./tech-free-cloud.md)：国内注册 Oracle Cloud 实测（信用卡、开区、被拒原因）。
- [`tech-free-ai.md`](./tech-free-ai.md)：各 AI 平台在校园网环境下的连通性实测。
- [`tech-domain.md`](./tech-domain.md)：Namecheap .me 领取截图教程、.me/.tech 在 Cloudflare 的续费价格。

### 学习与科研

- [`tech-git-github.md`](./tech-git-github.md)：校园网访问 GitHub 的实测情况与推荐加速方案。
- [`tech-mooc.md`](./tech-mooc.md)：燕大对 MOOC 学分抵扣的政策核实。
- [`tech-oss-alternatives.md`](./tech-oss-alternatives.md)：确认燕大正版化平台是否提供 MATLAB 校园版授权。
- [`tech-research-tools.md`](./tech-research-tools.md)：
  - 燕大本科毕设是否有官方 LaTeX/Typst 模板；
  - 图书馆购买的数据库列表、校外访问（WebVPN）入口。

### 前沿工具

- [`tech-vibecoding.md`](./tech-vibecoding.md)：各工具在校园网环境下的连通性实测、订阅价格对比表。
- [`tech-cc-switch.md`](./tech-cc-switch.md)：图文配置教程（添加供应商、切换、验证生效）。
- [`tech-relay.md`](./tech-relay.md)：站点推荐、计费概念（倍率/分组）、延迟实测。
- [`tech-self-hosting.md`](./tech-self-hosting.md)：
  - 燕大校园网环境下 Cloudflare Tunnel / Tailscale 的连通性与速度；
  - 端到端实战：Oracle 免费机 + Docker + Cloudflare Tunnel 部署 Memos。
