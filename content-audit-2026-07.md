---
tags:
  - 维护
  - 内容审计
  - 中国大陆适用性
authors:
  - liugu2023
---

**本文作者：**
- ![liugu2023](https://avatars.githubusercontent.com/liugu2023?s=40)@[liugu2023](https://github.com/liugu2023)

---

# 全站内容时效性与中国大陆适用性审计

核验日期：2026 年 7 月 10 日。

> 修订状态：2026 年 7 月 10 日已完成第一轮集中修订。本报告保留修改前的问题、文件位置和判断依据，用作审计基线；当前原文已发生变化，行号不再保证对应。仍需校内账号或在校网络核验的事项见 [`TODO.md`](./TODO.md)。

本次审计覆盖仓库根目录全部 28 份 Markdown，并检查了其中 95 个不同的外部链接。核验重点包括：

- 产品、模型、免费额度、学生权益和软件版本是否仍然有效；
- 中国大陆是否属于服务商官方支持地区；
- 是否依赖境外网络、国际支付、境外手机号或特定地区账号；
- 在国内建站、自托管和处理个人信息时是否缺少备案、校规或数据合规提醒；
- 校园服务入口和规则是否能从燕山大学公开页面确认。

“官网能打开”不等于“中国大陆可稳定使用”。同样，校内系统入口能打开，也不表示登录后的套餐、审批时间、积分和处罚规则没有变化。

## 风险等级

| 等级 | 含义 |
|------|------|
| P0 | 已确认错误、命令不可用，或可能造成费用、数据丢失、安全和合规问题，应先改 |
| P1 | 内容可能仍有参考价值，但缺少地区限制、核验日期或官方依据 |
| P2 | 主要是导航、表述和维护方式问题，不会立刻误导操作 |
| OK | 本轮未发现实质性的时效或中国大陆适用性问题 |
| 待补 | 正文为空或公开资料不足，无法完成内容核验 |

## 结论摘要

### 应立即处理的内容

1. `tech-vibe-coding-guide.md` 中的 CC-Switch CLI 教程不可用。官方项目是桌面应用，npm 中不存在文档所写的 `cc-switch` 包，也没有 `cc add`、`cc use`、`cc list` 这些命令。
2. `tech-student-pack.md` 的 Copilot、Namecheap、DigitalOcean、Termius、Figma 和 Zed 等权益与当前官方页面不一致或无法确认。
3. `tech-free-cloud.md` 对 Oracle、AWS 和 GCP 的扣费逻辑写得过于绝对，其中“不会产生扣费”“赠金到期就开始扣费”均不准确。
4. `tech-domain.md` 仍写 Namecheap 免费 `.me`，并把 `.cn` 和 ICP 备案混成同一件事。是否需要备案主要取决于服务是否部署在中国大陆，不只看域名后缀。
5. `tech-free-ai.md` 写死了大量免费模型和赠送额度；OpenRouter 请求头说明错误，Kimi API“不限 Token”也不应保留。
6. `campus-network-index.md` 的 60GB、免流网站、设备数和运营商套餐没有找到公开校方依据。
7. `campus-ms-index.md` 把已经停止安全支持的 Windows 和 Office 版本当成普通安装选项。
8. `campus-service-index.md` 的绩点、评教、图书馆处罚和劳动教育 80 小时等规则缺少现行政策依据。
9. `tech-git-github.md` 把 `git checkout <提交号>`解释成“回到历史版本”，长篇指南又直接建议 `git restore .`，对新生有误删改动风险。
10. `tech-research-tools.md` 的 Overleaf 免费编译时间已经变化，Google Scholar 镜像建议存在安全风险。
11. `tech-mooc.md` 把 Coursera 旁听和助学金规则写成固定流程，多个数字无法从当前官方资料确认。
12. OpenAI、Anthropic 和 Gemini API 的官方支持地区均不包含中国大陆。现有 AI 文档没有把这一前提放在显眼位置。

### 中国大陆共性限制

| 类型 | 当前结论 |
|------|----------|
| OpenAI、Anthropic、Gemini API | 中国大陆不在官方支持地区；代理或中转不等于符合服务条款 |
| GitHub、Coursera、Overleaf 等境外网站 | 可能可以访问，但连接、下载、定位、支付和验证不稳定，不能承诺校园网能解决 |
| Cloudflare Free/Pro | 不包含 Cloudflare China Network；没有中国大陆节点和低延迟保证 |
| Oracle、Vercel、Netlify、Supabase 等海外云 | 没有普通中国大陆区域，注册、国际卡、延迟和跨境数据均需单独考虑 |
| 境外域名注册商 | 可以持有域名，但将来使用中国大陆服务器备案时，可能需要转入工信部批准的境内注册服务机构 |
| API 中转站 | 存在资金、模型替换、请求日志、个人信息和数据出境风险；技术可连接不代表合规 |
| 校园网与校内服务 | 套餐、免流、积分和审批规则需要登录后或在校实测，公开网页无法完全核实 |

## 全部文档审计表

| 文件 | 等级 | 结论 |
|------|------|------|
| `README.md` | P2 | 实际内容是第二份 TODO，不是仓库说明；与 `TODO.md` 重复，且没有记录本次 P0 问题 |
| `index.md` | P2 | 导航本身可用；`tech-vibe-coding-guide.md` 未被任何导航引用，形成孤立长文 |
| `TODO.md` | P1 | 方向正确，但需要加入本报告列出的已确认错误，而不只是“待实测”项目 |
| `CONTEXT.md` | OK | 分类定义仍适用；`ehall.ysu.edu.cn` 当前有效 |
| `contributing.md` | P2 | “时效内容注明核实时间或来源”的规则合理，但多个现有页面没有执行 |
| `campus-mail-index.md` | P1 | 邮箱入口有效；第三方教育优惠和固定申请界面不能保证 |
| `campus-ms-index.md` | P0 | 入口有效，但仍推荐多款已停止支持的 Windows、Office 和 Mac Office |
| `campus-network-connect.md` | P0 | 认证地址显示与链接不一致；运营商办理建议和固定 UI 需要校内复核 |
| `campus-network-index.md` | P0 | 免费流量、免流、设备数和运营商套餐均缺公开官方依据 |
| `campus-network-qa.md` | 待补 | 正文只有 TODO，无法提供新生排障帮助 |
| `campus-network-vpn.md` | P2 | 入口有效；应改称学校 WebVPN/校外访问系统，避免与通用翻墙 VPN 混淆 |
| `campus-service-index.md` | P0 | 入口有效，但成绩、预约处罚和劳动学时等规则没有现行依据 |
| `tech-cc-switch.md` | P2 | 桌面版安装方式有效；功能描述需跟随版本更新，且“官网”一栏为空 |
| `tech-cloudflare.md` | P1 | 多数服务仍存在；“不限流量”“任何域名”等表述过满，大陆免费网络无境内节点 |
| `tech-domain.md` | P0 | Namecheap 权益已移除，`.com` 价格过时，备案解释不准确 |
| `tech-free-ai.md` | P0 | 多项额度和模型写死，部分说法错误；海外平台不适合作为大陆默认方案 |
| `tech-free-cloud.md` | P0 | Oracle、Netlify、DigitalOcean、AWS、GCP 等计费和免费政策已有变化 |
| `tech-git-github.md` | P0 | 回退命令和暂存流程对新生不安全；第三方 GitHub 镜像建议风险较大 |
| `tech-index.md` | P2 | 导航有效；应增加海外服务地区限制总提示 |
| `tech-llm-glossary.md` | P1 | 概念整体准确；A2A 规范版与仓库发行版应区分，官方资料在大陆可能无法直连 |
| `tech-mooc.md` | P0 | Coursera 旁听和助学金固定规则无法确认，B 站“搬运版本”不应推荐 |
| `tech-oss-alternatives.md` | P1 | 内容混合开源与免费专有软件；部分教育优惠和远控建议需更新 |
| `tech-relay.md` | P1 | 已提示基础风险，但缺少运营主体、日志、个人信息和数据出境检查 |
| `tech-research-tools.md` | P0 | Overleaf 时限过时，Zotero 附件描述不准，Google Scholar 镜像建议不安全 |
| `tech-self-hosting.md` | P1 | 方案方向可用；Oracle、Tailscale 配额和公开服务安全/备案需要补充 |
| `tech-student-pack.md` | P0 | 多项权益已经变化或无法从当前 Pack 核验 |
| `tech-vibe-coding-guide.md` | P0 | 存在不可用命令、特定中转商痕迹、危险 Git 操作和大量未固定版本的远程执行命令 |
| `tech-vibecoding.md` | P1 | 产品概览大体正确，但没有说明三家海外服务均不正式支持中国大陆 |

## 校园类文档详细问题

### 校园邮箱

- `campus-mail-index.md:13-14`：校园邮箱只能作为申请教育优惠的材料之一，不能保证 Microsoft 365、GitHub Education 或 JetBrains 一定通过。
- `campus-mail-index.md:20-25`：“随便填”“随机分配”“等待几天”无法从未登录页面核实。应改成按页面要求填写，以审批结果为准。
- `campus-mail-index.md:36-41`：Microsoft 365 A1 取决于学校租户和管理员分配，不是拥有学校邮箱就能自动获得。
- `campus-mail-index.md:52-66`：GitHub Education 的定位、证件类型和按钮会动态变化。“必须在燕大校内”没有官方普遍依据。
- `campus-mail-index.md:77-82`：JetBrains 学生资格通常需要定期续期，但具体表单字段不应写死。

当前可访问入口：

- [燕山大学校园邮箱](https://stumail.ysu.edu.cn/)
- [燕山大学一网通办](https://ehall.ysu.edu.cn/default/index.html#/)
- [GitHub Education 申请说明](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student)
- [JetBrains 学生授权](https://www.jetbrains.com/community/education/#students)

### 正版化软件

- `campus-ms-index.md:23`：Windows 8、8.1 已结束支持，Windows 10 Home/Pro 常规支持也已于 2025 年 10 月 14 日结束。平台仍可下载不代表适合新装。
- `campus-ms-index.md:35`：Office 2013、2016、2019 及多个 Mac 版本已停止支持。Office 2021 也将在 2026 年 10 月 13 日结束支持。
- `campus-ms-index.md:31,43`：Windows 和 Office 激活都指向同一帮助页，需要登录后人工确认是否确为统一 KMS 指南。
- 建议只把仍受安全支持的版本列为默认选择，旧版本单独放入“兼容旧软件”说明。

来源：

- [燕山大学正版化平台](https://software.ysu.edu.cn/)
- [Windows 10 生命周期](https://learn.microsoft.com/en-us/lifecycle/products/windows-10-home-and-pro)
- [Office 2016 生命周期](https://learn.microsoft.com/en-us/lifecycle/products/microsoft-office-2016)
- [Office 2019 生命周期](https://learn.microsoft.com/en-us/lifecycle/products/microsoft-office-2019)
- [Office 2021 生命周期](https://learn.microsoft.com/en-us/lifecycle/products/office-2021)

### 校园网

- `campus-network-connect.md:14`：显示文字是 `auth.ysu.edu.cn`，实际链接却是 `auth1.ysu.edu.cn`。`10.11.0.1` 是校内私网地址，应明确只能连接校园网后访问。
- `campus-network-connect.md:19,24,38-45`：首次服务选择和“六项自助服务”未找到公开规则，应改成“以当前页面为准”。
- `campus-network-connect.md:56`：账号、密码和套餐问题应联系运营商官方客服或营业厅，不应联系个人推销者。
- `campus-network-index.md:34`：60GB、B 站和魔搭免流、三台设备、不可结转等均需校方公告或自助服务截图佐证。
- `campus-network-index.md:36`：25GB 国内流量、280GB 河北省内流量和一台设备不能代表所有运营商、年份和入网批次。
- `campus-network-index.md:40`：“办卡本身免费”不够准确，仍可能存在预存、首月费、合约和违约金。

这些内容应统一改为“登录自助服务查看本人套餐”，并单独收集 2026 级新生实测。

### 一网通办与 WebVPN

- 一网通办、WebVPN、本科教务、座位预约、可信数据和劳动教育平台当前均可访问。
- `campus-service-index.md:34`：未评教不能查成绩、过期不能补评，需要当学期教务通知支持。
- `campus-service-index.md:35`：教务系统显示的平均绩点不能直接等同于转专业、推免等所有评定规则。
- `campus-service-index.md:59-64`：预约时间、300 积分、扣 100 分、禁约 4 天、15 分钟签到等没有从公开规则页核实。
- `campus-service-index.md:76-79`：劳动教育“毕业前必须完成 80 小时”需要按年级、专业培养方案和学院通知核对。
- `campus-network-vpn.md` 应改称“学校 WebVPN”或“校外访问系统”。它用于访问校内资源，不是通用互联网代理。

来源：

- [一网通办](https://ehall.ysu.edu.cn/default/index.html#/)
- [学校 WebVPN](https://vpn.ysu.edu.cn/portal/#!/service)
- [本科教务系统](https://jwxt.ysu.edu.cn/)
- [燕山大学图书馆](https://library.ysu.edu.cn/)
- [燕山大学教务处](https://jwc.ysu.edu.cn/)

## 学生权益与免费资源详细问题

### GitHub 学生包

- `tech-student-pack.md:22`：当前 Pack 页面标注 Copilot 新计划注册暂时暂停，原文所写日期和权益层级没有官方依据。
- `tech-student-pack.md:25`：DigitalOcean 当前优惠写有明确截止日期和排除服务，不能继续概括为“200 美元、有效 1 年”。
- `tech-student-pack.md:26`、`tech-domain.md:19`：当前 Pack 页面已找不到 Namecheap `.me`；仍能确认 `.TECH` 和 Name.com 的部分权益。
- `tech-student-pack.md:27`：Termius 当前是学生身份期间免费，不是固定两年。
- `tech-student-pack.md:31-34`：审核时间、固定两年有效期、必须校园网和固定姓名格式均不是 GitHub 官方 SLA。
- `tech-student-pack.md:41-42`：Figma 是独立教育计划；Zed 当前无法从 Pack 页面核验，不应放在“仍然有效”表中。
- `tech-student-pack.md:43`：Microsoft 365 A1 由学校租户决定。
- `tech-student-pack.md:44`：Azure for Students 指全球 Azure，不是世纪互联运营的 Azure 中国。

来源：

- [GitHub Student Developer Pack](https://education.github.com/pack)
- [GitHub Education 学生说明](https://docs.github.com/en/education/about-github-education/github-education-for-students/about-github-education-for-students)
- [Figma Education](https://help.figma.com/hc/en-us/articles/360041061214-Apply-for-the-Figma-for-Education-plan)
- [Azure for Students](https://azure.microsoft.com/en-us/free/students)
- [Azure 中国](https://www.azure.cn/)

### Cloudflare 与域名

- `tech-cloudflare.md:19`：“不限流量”应改为“没有按 GB 收费，但受缓存限制、合理使用和服务条款约束”。
- `tech-cloudflare.md:22,47`：R2 的 10GB 免费存储和 Internet egress 免费仍有依据，但操作请求、存储类型和账单资料仍可能产生限制或费用。
- `tech-cloudflare.md:25,51`：Tunnel 能绕过公网 IP 限制，但没有鉴权时仍是公开互联网服务，且可能违反校园网规定。
- `tech-cloudflare.md:56`：不是“任何域名”都能无条件托管，仍取决于 TLD、注册商和是否可更改 NS。
- Cloudflare China Network 是 Enterprise 单独订阅，普通 Free/Pro 用户不会获得中国大陆节点；接入还要求 ICP 等合规条件。
- `tech-domain.md:31`：`.com` 约 8 美元已经过时，应链接实时价格，不写死数字。
- `tech-domain.md:41`：Email Routing 只是收件转发，不提供以该域名发信。
- `tech-domain.md:50`：任何部署在中国大陆服务器并向公众提供网站的域名都可能需要 ICP 备案，不只 `.cn`。境外注册商也可能不满足备案接入要求。

来源：

- [Cloudflare China Network](https://developers.cloudflare.com/china-network/)
- [Cloudflare R2 定价](https://developers.cloudflare.com/r2/pricing/)
- [Cloudflare Registrar](https://developers.cloudflare.com/registrar/)
- [Cloudflare Email Routing](https://developers.cloudflare.com/email-routing/)
- [工信部备案系统](https://beian.miit.gov.cn/)

### 免费云平台

- `tech-free-cloud.md:28`：不能把 Cloudflare Pages、GitHub Pages、Netlify、Vercel 一概说成无需信用卡且长期规则不变。
- Vercel Hobby 主要面向个人、非商业用途；Netlify 新账户已采用 credit-based Free plan。
- `tech-free-cloud.md:41-43`：Oracle A1 是账户总配额，受 home region 容量影响，不保证能创建一台 4 核 24GB 实例。中国大陆没有普通 OCI 公有云区域。
- Oracle 未升级的 Free Tier tenancy 不会按正常用量收费，但信用卡预授权、主动升级和付费资源仍需区分，不能写“不会产生扣费”。
- `tech-free-cloud.md:35`：Heroku 普通免费层已取消，但当前学生包存在学生额度例外。
- `tech-free-cloud.md:48`：Supabase 配额和暂停规则需要实时定价页支持。
- `tech-free-cloud.md:54`：DigitalOcean 的学生额度已经出现截止日期和排除项。
- `tech-free-cloud.md:59`：GCP Free Trial 未手动升级不会自动收费；AWS 新 Free account plan 到期或额度用完也不会自动转成付费计划。两者不能合并描述。
- 面向中国大陆用户的公开网站，应优先评估境内合规云、备案和真实访问速度；Cloudflare 免费 CDN 不能自动解决这些问题。

来源：

- [Oracle Cloud Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm)
- [Vercel Hobby](https://vercel.com/docs/plans/hobby)
- [Netlify credit-based pricing](https://docs.netlify.com/manage/accounts-and-billing/billing/billing-for-credit-based-pricing/)
- [Google Cloud Free Program](https://cloud.google.com/free/docs/free-cloud-features)
- [AWS Free Tier](https://aws.amazon.com/free/)

## 学习与科研文档详细问题

### MOOC

- `tech-mooc.md:16`：中国大学 MOOC 的免费学习范围取决于当期开课设置。
- `tech-mooc.md:18,46`：不应引导新生查找 B 站“搬运版本”。只推荐高校、教师和课程官方账号。
- `tech-mooc.md:22`：Coursera 不是所有课程都支持免费旁听。
- `tech-mooc.md:31-35`：入口、两篇 150 词、15 天审核、180 天完成、最多 10 个申请和固定减免比例都可能变化，当前无法作为稳定规则。
- `tech-mooc.md:46`：校园网不等于国际专线，不能保证解决海外视频加载问题。
- 燕大是否认可 MOOC 学分仍需教务处按当前培养方案确认。

### 文献与排版

- `tech-research-tools.md:20`：占 Zotero 存储的是同步附件，不只 PDF；图片、EPUB 和网页快照也会占用空间。
- 坚果云 WebDAV 适合个人库附件，不支持 Zotero group library 附件同步。
- `tech-research-tools.md:27`：“官方 Zotero 插件”应明确是坚果云提供的第三方插件，或者删除无法确认的版本描述。
- `tech-research-tools.md:28`：邮箱下划线导致失败属于未复现个案，不应当成通用规则。
- `tech-research-tools.md:36`：Overleaf Free 当前编译超时为 10 秒，不是文中的 20 秒；免费计划仍通常只允许 1 位协作者。
- `tech-research-tools.md:47`：Google Scholar 在中国大陆不能作为稳定入口，也不应推荐来源不明的镜像。优先使用图书馆、知网、万方、Web of Science（若学校订购）、Semantic Scholar、Crossref 或 OpenAlex。
- `tech-research-tools.md:50`：知网和 Web of Science 能否校内访问取决于燕大当年采购范围。

来源：

- [Zotero 同步说明](https://www.zotero.org/support/sync)
- [Zotero Storage](https://www.zotero.org/storage)
- [Overleaf 免费版限制](https://docs.overleaf.com/getting-started/free-and-premium-plans/plan-limits)
- [燕山大学图书馆](https://library.ysu.edu.cn/)

### Git 与开源软件

- `tech-git-github.md:29`：不要笼统推荐“镜像加速”。第三方镜像可能不同步、篡改内容或诱导用户输入凭据。
- `tech-git-github.md:35-39`：`git checkout <提交号>`会进入 detached HEAD，不是适合新生的安全回滚方法。
- `tech-git-github.md:37`：直接 `git add .`可能把 `.env`、密钥和大文件一起提交。应先教 `.gitignore`、`git status` 和 `git diff --staged`。
- `tech-git-github.md:47`：2FA 是强烈建议且部分用户已被强制，但不应概括成所有新账号统一即时强制。大陆手机号可能收不到短信，优先使用 TOTP 或 passkey 并保存恢复码。
- `tech-git-github.md:48`：应补充 HTTPS 使用 PAT/Credential Manager，以及 SSH 443 端口的官方方案。
- `tech-oss-alternatives.md` 实际混合“开源”和“免费专有”软件，建议改名为“免费与开源替代软件”。
- PDFgear、Obsidian、Photopea、DaVinci Resolve 和 Everything 等并非开源软件。
- 在线 PDF 和图片工具不适合处理身份证、成绩单和未发表论文。
- RustDesk 自建中继及其他远程访问服务需要遵守校园网络规定。

来源：

- [Git switch](https://git-scm.com/docs/git-switch)
- [Git restore](https://git-scm.com/docs/git-restore)
- [Git revert](https://git-scm.com/docs/git-revert)
- [GitHub 强制 2FA 说明](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-mandatory-two-factor-authentication)
- [GitHub SSH over HTTPS](https://docs.github.com/en/authentication/troubleshooting-ssh/using-ssh-over-the-https-port)

## AI 与开发工具详细问题

### 海外服务地区限制

以下服务不能按“中国大陆新生注册后即可使用”来介绍：

- OpenAI API、ChatGPT 与 Codex；
- Anthropic API、Claude 订阅与 Claude Code；
- Google AI Studio、Gemini API 与 Gemini CLI 的官方云端模型服务。

官方支持地区列表不包含中国大陆。从非支持地区访问可能触发账号限制。中转站和配置切换工具只能改变连接方式，不能改变服务条款、账号归属、个人信息处理和数据跨境责任。

来源：

- [OpenAI 支持地区](https://help.openai.com/en/articles/5347006-openai-api-supported-countries-and-territories)
- [Anthropic 支持地区](https://www.anthropic.com/supported-countries)
- [Gemini API 支持地区](https://ai.google.dev/gemini-api/docs/available-regions)

### 免费 AI API

- `tech-free-ai.md:19-21`：Gemini 免费层存在，但模型和限额会调整，中国大陆不在支持地区。
- `tech-free-ai.md:26`：OpenRouter 免费模型数量和名称会变化，不应写成固定 24 至 28 个。
- `tech-free-ai.md:28`：`HTTP-Referer` 和 `X-OpenRouter-Title` 用于应用归属，不是免费模型调用的必需请求头，缺少它们不会因此 402。
- `tech-free-ai.md:32`：Groq“首字 200ms 内”缺少模型、输入和地区条件。
- `tech-free-ai.md:37-38`：Cerebras 的限制按模型计算，原文遗漏每小时限制。
- `tech-free-ai.md:44-54`：智谱、硅基流动、Kimi、火山和百度的赠送额度及“永久免费”说法都应删除，改成官方价格页和核验日期。
- Kimi 网页产品和开放平台 API 不是一回事，不能把“不限 Token”写成 API 规则。
- 三个参考链接均为第三方汇总，不足以支撑当前额度，应换成各平台官方定价页。

来源：

- [OpenRouter 限额](https://openrouter.ai/docs/api-reference/limits)
- [OpenRouter App Attribution](https://openrouter.ai/docs/app-attribution)
- [Gemini API 定价](https://ai.google.dev/gemini-api/docs/pricing)
- [Groq 限额](https://console.groq.com/docs/rate-limits)
- [Cerebras 限额](https://inference-docs.cerebras.ai/support/rate-limits)

### Vibe Coding 长篇指南

`tech-vibe-coding-guide.md` 是当前风险最高的单篇文档。

已确认问题：

- `53-58、68-99、128-153`：CC-Switch npm 包和 CLI 命令不存在。官方是 Tauri 桌面应用。
- `49`：Claude Code 的 npm 安装方式已被官方标为 deprecated，应改用原生安装、Homebrew 或 WinGet。
- `60-76、169-189`：“服务分组”“折扣倍率”“随想 AI”明显来自特定中转商，不应混在通用教程里。
- `159、209、279`：“只改 base_url”“一份 Key 多客户端复用”过度简化，第三方网关未必实现完整的 Responses API、工具调用、缓存和流式事件。
- `222、241、259、274`：具体模型名会变化，不应作为长期可复制默认值。
- `240`：OpenAI 示例仍用 Chat Completions，而前文 Codex 配置使用 Responses API，教程内部不一致。
- `310`：nvm-windows 下载地址为空。
- `315-316`：固定安装 Node 20 已过时，应使用当前 LTS。
- `377`：nvm `v0.39.7` 已过时。
- `322、367`：npmmirror 是第三方镜像，需要说明同步和供应链风险，并给出恢复官方 registry 的命令。
- 多处 `curl | bash`、`npx -y @latest` 和 `uvx --from git+...` 会直接执行远程代码，应提醒核验发布者并固定版本。
- 多数命令按 Bash 编写，不能让 Windows PowerShell 用户直接复制。
- `590-594`：`git restore .`会丢弃未提交修改。
- `580-583`：`git add -A`可能误提交密钥和无关文件。
- MCP、Plugin、Skill 的字段和目录相似，但不能保证 Claude Code 与 Codex 完全兼容。
- Context7、Serena、Playwright、Exa、DeepWiki、CodeGraph 及社区插件会读取代码或向第三方发送内容，需要单独说明权限和数据流。
- Task Master 要求把 Key 写入 `.env`，却没有提醒加入 `.gitignore`。
- Trellis、GSD、Task Master、Open Design 等社区项目没有标最后核验日期、许可证和成熟度，不应与官方工具放在同一可信度层级。

建议在完成逐节重写前，将这篇长文标成“实验性、未经完整验证”，并从新生导航中继续隐藏。

来源：

- [CC Switch 官方中文说明](https://github.com/farion1231/cc-switch/blob/main/README_ZH.md)
- [Claude Code 安装](https://docs.anthropic.com/en/docs/claude-code/setup)
- [OpenAI Codex 配置参考](https://developers.openai.com/codex/config-reference)
- [npm Registry 说明](https://docs.npmjs.com/cli/using-npm/registry)

### 中转站与自托管

- `tech-relay.md` 的基础风险提醒方向正确，但还需检查运营主体、隐私政策、请求日志、数据删除、上游来源、发票退款和安全事件处理。
- 不建议增加具体中转站推荐。站点预置在 cc-switch 中也不代表经过知识库背书。
- 学生不应上传身份证、成绩、健康信息、未公开论文、实验数据、实习代码和学校内部系统资料。
- `tech-self-hosting.md:19`：Oracle 免费机不能作为稳定可获得前提。
- `tech-self-hosting.md:29-31`：Tunnel、Tailscale 和 frp 在校园网的连接质量与合规性必须实测。
- Cloudflare Tunnel 不等于私网；未配置 Access 或应用认证时，服务仍可能公开在互联网。
- `tech-self-hosting.md:46`：不是每个项目都有可直接使用的 `docker-compose.yml`。
- 公开网站若部署在中国大陆服务器，需要评估 ICP 备案；宿舍设备公开提供服务还需遵守学校网络规定。

相关法规与说明：

- [生成式人工智能服务管理暂行办法](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm)
- [个人信息保护法](https://www.gov.cn/xinwen/2021-08/20/content_5632486.htm)
- [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/)
- [Tailscale 定价](https://tailscale.com/pricing)

### LLM 术语表

`tech-llm-glossary.md` 本轮未发现主要概念错误：

- MCP 当前稳定协议版本 `2025-11-25` 正确。
- A2A 官方规范页仍标 Latest Released Version 1.0.0；项目仓库最新发行标签为 v1.0.1。建议分别写“规范版本”和“实现发行版”。
- System、Developer、User 的表格是入门简化，应补一句完整指令层级和不同厂商实现可能不同。
- 官方参考资料在中国大陆可能无法直连，但不应换成来源不明的镜像。
- 可再补充个人信息和未公开资料的跨境处理提醒。

来源：

- [MCP Versioning](https://modelcontextprotocol.io/specification/versioning)
- [A2A 规范](https://a2a-protocol.org/latest/specification/)
- [A2A Releases](https://github.com/a2aproject/A2A/releases/latest)

## 文档维护层面的问题

1. `README.md` 目前是按分类整理的 TODO，与 `TODO.md` 重复。建议让 README 回到项目介绍、访问入口、贡献方式和维护状态。
2. `tech-vibe-coding-guide.md` 没有出现在 `index.md`、`tech-index.md` 或 README 中。考虑到当前风险，暂时不接入新生导航是合理的，但应明确标为草稿。
3. `contributing.md` 要求时效内容注明核实时间或来源，但 `tech-free-ai.md`、`tech-free-cloud.md`、`tech-cloudflare.md`、`tech-vibecoding.md`、校园网和校园邮箱等页面没有统一核验日期。
4. 免费额度、价格、模型列表和学生优惠不适合长期写死。建议采用“最后核验日期 + 官方链接 + 可自动检查字段”的格式。
5. 校园规则需要区分三种证据：公开校方文件、登录后截图、学生经验。学生经验不能写成学校统一政策。
6. 外部链接检查中，`10.11.0.1` 属于预期的校内私网；MCP 接口返回 406 也不代表服务失效。链接检测结果需要结合协议和网络位置解释。

## 建议修订顺序

### 第一批：避免直接误导

1. 删除长篇指南的虚假 CC-Switch CLI 命令和危险 Git 命令。
2. 修正学生包、免费域名、DigitalOcean、Oracle、AWS/GCP 和 Overleaf 信息。
3. 删除 Kimi“不限 Token”、OpenRouter 请求头、固定 Coursera 助学金数字。
4. 删除无来源校园套餐、绩点用途、预约处罚和劳动教育 80 小时。
5. 给所有海外 AI 服务加中国大陆官方地区限制。

### 第二批：补中国大陆使用前提

1. 域名和自托管补充 ICP、境外注册商和校园网络规定。
2. Cloudflare 补充大陆无免费境内节点、R2 账单和 Tunnel 鉴权。
3. 中转站补充个人信息、日志、数据出境、运营主体和上游来源检查。
4. 科研工具删除不明镜像，补校图书馆和国内正规检索入口。

### 第三批：建立长期维护机制

1. 所有价格、额度和模型表增加“最后核验日期”。
2. 把官方事实、校内实测和个人经验分栏记录。
3. 每月自动检查外链，每学期人工复核校园入口和套餐。
4. 每次新生入学前，重点复核校园网、邮箱、正版化、学生权益和 Git 入门五篇文档。
