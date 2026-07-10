---
tags:
  - Cloudflare
  - 免费资源
  - 建站
authors:
  - liugu2023
---
# Cloudflare 免费额度说明

Cloudflare 是常见的 CDN / 边缘计算服务商。它的 Free Plan 不需要绑定信用卡（个别服务除外），适合个人网站、博客和小型 API 服务。

> 免费额度可能随时调整，具体数字请以 [Cloudflare 官方文档](https://developers.cloudflare.com/) 和定价页为准。

## 核心免费服务一览

| 服务 | 用途 | 免费额度（大致） |
| --- | --- | --- |
| CDN + DNS | 网站加速、域名解析 | 不限流量，免费 SSL 证书 |
| Pages | 静态网站托管 | 不限请求数和带宽，每月 500 次构建 |
| Workers | 边缘无服务器函数 | 每天约 10 万次请求 |
| R2 | 对象存储（兼容 S3） | 每月 10GB 存储，**流出流量免费** |
| D1 | 无服务器 SQLite 数据库 | 有免费读写额度 |
| KV | 键值存储 | 有免费读写额度 |
| Tunnel | 内网穿透 | 免费，无需公网 IP |
| Turnstile | 验证码（reCAPTCHA 替代品） | 免费 |
| Email Routing | 自定义域名邮件转发 | 免费 |
| Zero Trust / Access | 团队访问控制 | 50 用户以内免费 |

## 常见用法

### 1. 免费托管个人网站 / 博客

用 **Cloudflare Pages** 托管静态网站（Hexo、Hugo、VitePress、Astro 等构建产物）：

1. 把项目推到 GitHub
2. 在 Cloudflare Dashboard 中创建 Pages 项目，关联仓库
3. 配置构建命令和输出目录，之后每次 push 自动部署
4. 免费获得 `*.pages.dev` 域名，也可绑定自己的域名

### 2. 免费运行后端逻辑

**Workers** 可以在边缘节点运行 JavaScript/TypeScript（也支持 Python、Rust 编译到 WASM），适合写小型 API、Webhook、定时任务、反向代理等。搭配 KV / D1 / R2 可以做一些小型全栈项目。

### 3. 免费对象存储

**R2** 兼容 S3 API，最大的亮点是**没有流出流量费**（传统云厂商的对象存储流量费往往比存储费贵得多），适合放图床、静态资源、备份文件。

### 4. 内网穿透

**Cloudflare Tunnel**（`cloudflared`）可以把本地或校园网内的服务暴露到公网，不需要公网 IP、不需要开端口，配合自己的域名使用。宿舍电脑、NAS 或自建服务都可以用这个方式试。

### 5. 域名相关

- **Cloudflare Registrar** 按成本价卖域名，无溢价（这个不免费，但便宜）
- 任何在其他注册商买的域名都可以把 DNS 托管到 Cloudflare，免费享受 CDN、SSL 和 DDoS 防护

## 注意事项

- Cloudflare 免费节点对中国大陆的访问速度一般（就近解析常落到美西），对速度敏感的服务需自行斟酌
- 免费套餐禁止大量代理视频流等滥用行为，详见其服务条款
- Workers 免费版单次请求有 CPU 时间限制，不适合重计算任务

## 待补充

<!-- TODO: 结合校园网环境的实测速度、优选 IP 等实践经验 -->

---

**作者**：[liugu2023](https://github.com/liugu2023) ![liugu2023](https://avatars.githubusercontent.com/liugu2023?s=40)
