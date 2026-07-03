# Git 与 GitHub 入门

> 本板块的很多内容（学生包、Pages 建站、开源软件）都默认你有 GitHub 账号、会基本的 Git 操作。如果你还不会，这篇是最短路径入门。

## 为什么要学

- 课程大作业 / 毕设的代码需要版本管理，避免 "最终版_v2_真最终版.zip"
- 申请 [GitHub 学生包](./student-pack.md)的前提是有 GitHub 账号
- 求职时 GitHub 主页就是你的作品集
- 用 [Cloudflare Pages](./cloudflare.md) / GitHub Pages 部署网站都从 Git 仓库开始

## 安装与初始配置

Windows 用户直接安装 [Git for Windows](https://git-scm.com/download/win)（自带 Git Bash）。装完先配置身份：

```bash
git config --global user.name "你的名字"
git config --global user.email "你的邮箱"
```

> 💡 国内访问 GitHub 时慢时快属于正常现象。克隆大仓库可以用镜像加速或浅克隆（`git clone --depth 1`）。
> <!-- TODO: 待补充校园网环境下访问 GitHub 的实测情况与推荐加速方案 -->

## 五个够用一学期的命令

```bash
git init                 # 把当前文件夹变成 Git 仓库
git add .                # 暂存所有改动
git commit -m "说明"     # 提交一次快照
git log --oneline        # 查看提交历史
git checkout <提交号>    # 回到任意历史版本
```

日常循环就是 `改代码 → git add . → git commit`。commit 信息写清楚这次改了什么，两个月后的你会感谢现在的你。

## 连接 GitHub

1. 注册 [GitHub](https://github.com/) 账号（建议用户名取得正式一点，以后简历要写）
2. 开启两步验证（2FA）——GitHub 已强制要求，也是申请学生包的前提
3. 配置 SSH 密钥或使用 [GitHub Desktop](https://desktop.github.com/)（图形界面，新手友好）
4. 推送代码：

```bash
git remote add origin git@github.com:用户名/仓库名.git
git push -u origin main
```

## 进阶路线

- **分支与合并**：`git branch` / `git merge`，多人协作或试验性改动时用
- **Pull Request**：参与开源项目（包括给本知识库[投稿](../contributing.md)）的标准流程
- **GitHub Pages**：仓库设置里开启，免费托管个人主页
- **GitHub Actions**：自动跑测试、自动部署

## 推荐学习资源

- [Pro Git 中文版](https://git-scm.com/book/zh/v2)：官方书，免费在线阅读
- [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN)：可视化交互练习，分支概念一玩就懂
- [GitHub Skills](https://skills.github.com/)：官方互动教程
