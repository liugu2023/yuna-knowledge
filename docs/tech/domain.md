# 域名白嫖与管理指南

> 想要一个自己的域名做个人主页、博客、邮箱后缀？学生身份可以第一年免费，之后每年成本价续费，总花费极低。
>
> 信息核实时间：2026 年 7 月。

## 第一年：学生包免费域名

通过 [GitHub 学生包](./student-pack.md)认证后，可以免费领取一年域名：

- **Namecheap**：免费一年 **.me** 域名 + SSL 证书
- **.TECH Domains**：免费一年标准 **.tech** 域名
- **Name.com** 等其他合作商也有免费后缀，以[学生包页面](https://education.github.com/pack)实时列表为准

领取流程（以 Namecheap 为例）：学生包页面进入 Namecheap 专属链接 → 搜索想要的域名 → 加入订单 → 用注册学生包的邮箱完成免费下单。

> ⚠️ 域名只免费**一年**，到期后按原价续费（.me / .tech 续费不便宜）。要么第一年结束前转出，要么一开始就想好这个域名是玩玩还是长期用。

## 长期使用：Cloudflare Registrar 成本价

打算长期持有的域名，推荐注册 / 转入 [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/)：

- **完全不加价**：只收注册局 + ICANN 的成本费。例如 .com 约 $8/年，且续费同价，没有"首年特价、续费翻倍"的套路
- 自带免费 DNS、CDN、SSL、DNSSEC、域名锁
- 支持 390+ 后缀
- 限制：域名必须使用 Cloudflare 的 DNS（对大多数人反而是优点，配合 [Cloudflare 白嫖指南](./cloudflare.md)里的 Pages / Workers 无缝衔接）

**省钱组合**：第一年学生包白嫖 .me → 觉得会长期用 → 到期前转入 Cloudflare 按成本价续费；或者跳过白嫖，直接在 Cloudflare 注册一个 .com（一年一顿饭钱）。

## 域名能拿来干什么

- **个人主页 / 博客**：配合 Cloudflare Pages 或 GitHub Pages，全套免费
- **自定义邮箱**：Cloudflare Email Routing 免费把 `me@你的域名` 转发到 QQ 邮箱
- **给自托管服务一个门牌**：见[自托管入门](./self-hosting.md)
- **简历加分**：邮箱和主页用自己的域名，观感完全不同

## 避坑提醒

1. **不要用来路不明的"永久免费域名"**（如某些免费二级域分发站）：随时可能被回收，做正经站点不可靠。
2. 域名注册信息启用 WHOIS 隐私保护（Cloudflare / Namecheap 都免费提供）。
3. 域名续费记得设自动续费或日历提醒，过期被抢注就很难拿回来了。
4. `.cn` 域名及国内备案是另一套流程（需实名 + 备案才能解析到国内服务器），个人玩海外服务托管一般用不到。

<!-- TODO: 待补充实际领取 Namecheap .me 的截图教程，以及 .me/.tech 在 Cloudflare 的当前续费价格（价格随汇率和注册局调价浮动，写死数字容易过时） -->

## 参考链接

- [GitHub 学生包官方页面](https://education.github.com/pack)
- [Cloudflare Registrar 官方介绍](https://www.cloudflare.com/products/registrar/)
