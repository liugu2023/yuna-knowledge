---
tags:
  - 云服务
  - 免费资源
  - 建站
authors:
  - liugu2023
---
# 免费云资源指南

> 这页整理适合个人项目、课程作业展示和小型服务的免费云资源，按用途分类。
>
> 免费额度政策随时可能调整，部署重要项目前请核实官方最新条款。

## 按需求选

| 需求 | 推荐 |
|------|------|
| 静态网站 / 博客 / 课程作业展示 | Cloudflare Pages、GitHub Pages、Vercel、Netlify |
| Next.js 应用 | Vercel |
| 需要一台真正的"服务器"（VPS） | Oracle Cloud Always Free |
| 数据库 + 登录鉴权 + 存储 | Supabase |
| 只要一个 Postgres 数据库 | Neon |
| 容器 / 后端服务托管 | Render、Koyeb（有冷启动限制） |

## 静态托管：长期免费层

GitHub Pages、Cloudflare Pages、Netlify、Vercel 都有长期免费层：无需信用卡，也不是短期试用额度。

- **Cloudflare Pages**：免费额度适合个人站点（详见 [Cloudflare 免费额度说明](./tech-cloudflare.md)）
- **GitHub Pages**：与仓库天然集成，适合项目文档和个人主页
- **Vercel**：对 Next.js 支持最好，开发体验佳
- **Netlify**：框架无关，构建配置灵活

> 曾经的免费托管明星 **Heroku 和 Fly.io 已不再提供免费层**，网上的老教程不要再照着做了。Railway 也已改为试用额度制。

## Oracle Cloud Always Free：免费 VPS

Oracle 云的 Always Free 套餐配置较高，适合需要真实服务器环境的场景：

- **Ampere A1 Flex（ARM）**：最高 4 核 vCPU + 24 GB 内存 + 200 GB 存储，可以跑 Docker、建站、自托管各种服务
- 永久免费，不是限时试用
- 注册需要一张信用卡做身份验证，但免费账户有严格配额上限，**不会产生扣费**
- 代价：一切运维（安全、备份、系统管理）自己负责

## 数据库与后端即服务（BaaS）

- **Supabase**（免费层）：500 MB Postgres 数据库、5 万月活用户、1 GB 文件存储、5 GB 流量、Edge Functions；最多 2 个活跃项目，**闲置 1 周会被暂停**
- **Neon**：Serverless Postgres，支持多项目 / 分支隔离，不用时自动"休眠"省额度，适合开发测试
- 其他可选：MongoDB Atlas、Turso、Upstash（Redis 缓存）、Firebase / Firestore

## 学生专属云额度

- **DigitalOcean**：GitHub 学生包含 200 美元额度（1 年有效），详见[学生权益指南](./tech-student-pack.md)
- **Azure for Students**：100 美元额度，无需信用卡

## 注意事项

1. **区分"永久免费"和"试用额度"**：Oracle Always Free、Cloudflare 免费层是前者；GCP / AWS 的新用户赠金是后者，到期或用完就开始扣费。
2. **绑了信用卡的平台设置预算告警**，防止配置失误产生账单。
3. **免费层不适合关键生产服务**：无 SLA 保障，额度政策说变就变。
4. 国内访问部分海外平台速度不稳定，静态站可考虑配合 Cloudflare CDN。

## 参考链接

- [Oracle Cloud Free Tier 官方文档](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm)
- [2026 免费云部署平台对比](https://snapdeploy.dev/blog/free-cloud-deployment-platforms-2026-comparison)
- [Awesome-Web-Hosting-2026（150+ 免费平台清单）](https://github.com/iSoumyaDey/Awesome-Web-Hosting-2026)
