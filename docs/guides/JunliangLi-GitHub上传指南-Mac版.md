# Junliang Li — GitHub 上传完整操作指南（Mac 版）

> 🎯 **你的任务**：上传设计文档 + GitHub Issue 模板 + 创建 28 个 Labels。你的工作**不依赖任何人**，可以和 Wang Xu 同一天做。
> ⏱ **预计耗时**：1-1.5 小时（大部分时间在手动创建 28 个 Labels）
> 💻 **你是 Mac**：本指南专门针对 macOS 编写，所有命令是 Mac 终端用的
> ⚠️ **无需等待**：你是唯一完全独立的人，Bowei 创建 develop 后你就可以开始

---

## 📋 操作步骤总览

| 步骤 | 做什么 | 大概时间 |
|:--:|--------|:--:|
| **Step 0** | 获取源文件 + 装 Git + 克隆仓库 | 20 分钟 |
| **Step 1** | 从 develop 创建功能分支 | 5 分钟 |
| **Step 2** | 复制文档和模板文件（11 个文件） | 10 分钟 |
| **Step 3** | 提交、推送、创建 PR | 10 分钟 |
| **Step 4** | 在 GitHub 网页上手动创建 28 个 Labels | 20 分钟 |
| **Step 5** | 等 Review、合并 | 5 分钟 |

---

## Step 0：准备工作

### 0.1 先从 Renxian 那里拿到源文件

> ⚠️ **重要**：源文件在 Renxian 的 Windows 电脑上，你需要先把它们弄到你的 Mac 上。

**方式一：微信/网盘传输（推荐）**
让 Renxian 把以下两个文件夹打包发给你：
- `1-5\Junliang Li\` 整个文件夹
- `week8\Junliang Li\` 整个文件夹

收到后，解压放到你的桌面（`~/Desktop/`），确保结构是：
```
~/Desktop/Junliang Li/
├── 1-5/
│   ├── figma-screen-specifications.md
│   ├── github-labels-taxonomy.md
│   ├── github-templates/
│   │   ├── bug-report.md
│   │   └── feature-request.md
│   ├── literature-review-uux-qa.md
│   ├── test-plan-and-cases.md
│   └── usability-testing-recruitment-plan.md
└── week8/
    ├── component-design-system-web.md
    ├── design-tokens-web.json
    ├── test-plan-update-w8.md
    └── web-design-specifications.md
```

**方式二：U 盘**
让 Renxian 把文件拷到 U 盘，你再从 U 盘拷到桌面。

**方式三：Renxian 直接在你的 Mac 上操作**
如果你们在一起，让 Renxian 登录 GitHub 直接帮你传。（但你还是得学会 Git）

### 0.2 检查 Git 是否安装

打开 **终端**（Terminal）：
- 按 `Command + 空格`，输入 `Terminal`，回车
- 或者在 Launchpad → 其他 → 终端

输入：

```bash
git --version
```

如果显示类似 `git version 2.39.x` → ✅ 已安装，跳到 0.4

如果显示 `command not found: git` → ❌ 没装，继续 0.3

### 0.3 安装 Git（Mac）

Mac 上最简单的方式是通过 Homebrew。先检查有没有 Homebrew：

```bash
brew --version
```

如果显示 `Homebrew 4.x.x` → ✅ 已有 Homebrew，直接装 Git：

```bash
brew install git
```

如果显示 `command not found: brew` → ❌ 需要先装 Homebrew：

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

安装过程中会要求输入你的 Mac 登录密码（输入时不显示字符，正常现象），然后按回车。装完后再装 Git：

```bash
brew install git
```

验证安装：

```bash
git --version
```

### 0.4 配置 Git 用户名和邮箱

```bash
git config --global user.name "Junliang Li"
git config --global user.email "junliang.li@example.com"
```

> ⚠️ **把邮箱换成你 GitHub 账号的实际邮箱！** 不然提交记录不会关联到你的 GitHub 头像。

验证配置：

```bash
git config --global user.name
git config --global user.email
```

### 0.5 确认能登录 GitHub

1. 打开浏览器（Safari / Chrome），访问：**https://github.com/login**
2. 登录你的 GitHub 账号
3. 确认你能看到团队仓库：**https://github.com/LuoX11a/SG_CampusSwap**
4. 如果显示 404（页面不存在），说明你没有权限。让 Renxian 在仓库 Settings → Collaborators → Add people 加你

### 0.6 克隆仓库到 Mac

```bash
cd ~/Desktop
git clone https://github.com/LuoX11a/SG_CampusSwap.git
cd SG_CampusSwap
ls
```

你应该只看到一个 `README.md` 文件。

---

## Step 1：确认 develop 存在 + 创建分支

### 1.1 确认 develop 分支存在

```bash
git branch -a
```

你应该看到：
```
* master
  remotes/origin/master
  remotes/origin/develop
```

> ❌ 如果看不到 `remotes/origin/develop`，说明 Bowei 还没完成！在群里问他进度，等他做完再进行。

### 1.2 拉取最新代码并创建你的分支

```bash
git fetch origin
git checkout -b feature/github-templates-and-design origin/develop
```

预期输出：`Switched to a new branch 'feature/github-templates-and-design'`

---

## Step 2：复制文件到仓库

### 2.1 你的文件清单（11 个）

| 来源（你桌面的文件夹） | 文件 | 放到仓库的哪里 |
|-----------|------|---------------|
| `~/Desktop/Junliang Li/1-5/` | `figma-screen-specifications.md` | `docs/week7/Junliang Li/` |
| | `github-labels-taxonomy.md` | `docs/week7/Junliang Li/` |
| | `literature-review-uux-qa.md` | `docs/week7/Junliang Li/` |
| | `test-plan-and-cases.md` | `docs/week7/Junliang Li/` |
| | `usability-testing-recruitment-plan.md` | `docs/week7/Junliang Li/` |
| | `github-templates/bug-report.md` | `.github/ISSUE_TEMPLATE/` |
| | `github-templates/feature-request.md` | `.github/ISSUE_TEMPLATE/` |
| `~/Desktop/Junliang Li/week8/` | `web-design-specifications.md` | `docs/week8/Junliang Li/` |
| | `component-design-system-web.md` | `docs/week8/Junliang Li/` |
| | `design-tokens-web.json` | `docs/week8/Junliang Li/` |
| | `test-plan-update-w8.md` | `docs/week8/Junliang Li/` |

### 2.2 创建需要的文件夹

```bash
mkdir -p "docs/week7/Junliang Li"
mkdir -p "docs/week8/Junliang Li"
mkdir -p ".github/ISSUE_TEMPLATE"
```

> Mac 上用 `mkdir -p`（和 Windows 的 `mkdir` 不同）。`-p` 表示如果父文件夹不存在就自动创建。如果提示 "File exists"，忽略即可。

### 2.3 复制文件

逐条执行以下命令（Mac 用 `cp`，不是 Windows 的 `copy`）：

```bash
# === W7 设计文档（5 个）===
cp ~/Desktop/Junliang\ Li/1-5/figma-screen-specifications.md "docs/week7/Junliang Li/figma-screen-specifications.md"
cp ~/Desktop/Junliang\ Li/1-5/github-labels-taxonomy.md "docs/week7/Junliang Li/github-labels-taxonomy.md"
cp ~/Desktop/Junliang\ Li/1-5/literature-review-uux-qa.md "docs/week7/Junliang Li/literature-review-uux-qa.md"
cp ~/Desktop/Junliang\ Li/1-5/test-plan-and-cases.md "docs/week7/Junliang Li/test-plan-and-cases.md"
cp ~/Desktop/Junliang\ Li/1-5/usability-testing-recruitment-plan.md "docs/week7/Junliang Li/usability-testing-recruitment-plan.md"

# === W7 GitHub 模板（2 个）===
cp ~/Desktop/Junliang\ Li/1-5/github-templates/bug-report.md ".github/ISSUE_TEMPLATE/bug-report.md"
cp ~/Desktop/Junliang\ Li/1-5/github-templates/feature-request.md ".github/ISSUE_TEMPLATE/feature-request.md"

# === W8 设计文档（4 个）===
cp ~/Desktop/Junliang\ Li/week8/web-design-specifications.md "docs/week8/Junliang Li/web-design-specifications.md"
cp ~/Desktop/Junliang\ Li/week8/component-design-system-web.md "docs/week8/Junliang Li/component-design-system-web.md"
cp ~/Desktop/Junliang\ Li/week8/design-tokens-web.json "docs/week8/Junliang Li/design-tokens-web.json"
cp ~/Desktop/Junliang\ Li/week8/test-plan-update-w8.md "docs/week8/Junliang Li/test-plan-update-w8.md"
```

> 💡 **注意**：路径中的 `Junliang\ Li` 中间有个 `\ `（反斜杠+空格），这是 Mac/Linux 终端里对空格的处理方式。你也可以直接把文件夹名改成没有空格的 `JunliangLi`，就不用加反斜杠了。

### 2.4 验证文件都复制到位了

```bash
ls -R "docs/week7/Junliang Li" "docs/week8/Junliang Li" ".github/ISSUE_TEMPLATE"
```

你应该看到完整的 11 个文件。

---

## Step 3：提交、推送、创建 PR

### 3.1 查看 Git 状态

```bash
git status
```

你会看到新增的文件显示为红色（Untracked files）。

### 3.2 添加到暂存区

```bash
git add .
git status
```

现在文件应该变成绿色（Changes to be committed）。

### 3.3 提交

```bash
git commit -m "docs: add GitHub issue templates, labels taxonomy, and design specifications"
```

### 3.4 推送到 GitHub

```bash
git push -u origin feature/github-templates-and-design
```

如果是第一次 push，可能会弹出一个对话框要求你登录 GitHub。选择 **"Sign in with your browser"**（用浏览器登录）最方便。

如果终端里直接要求输入密码：
- **Username**：你的 GitHub 用户名
- **Password**：**不要输入你的 GitHub 密码！** 需要 Personal Access Token（见下方 FAQ Q1）

### 3.5 创建 Pull Request

1. 浏览器访问：**https://github.com/LuoX11a/SG_CampusSwap**
2. 页面顶部应该会出现一个黄色提示条：`feature/github-templates-and-design has recent pushes`
3. 点击 **"Compare & pull request"** 绿色按钮
4. 如果没有黄色提示条：
   - 点击顶部 **"Pull requests"** 标签
   - 点击 **"New pull request"** 绿色按钮
   - `base` 选择 `develop`，`compare` 选择 `feature/github-templates-and-design`
   - 点击 **"Create pull request"**

**标题**（复制填入）：
```
docs: add GitHub issue templates, labels taxonomy, and design specifications
```

**描述**（复制以下全部内容填入）：
```markdown
## Description
上传 UI/UX 设计文档、GitHub Issue 模板和标签体系：
- 15 屏幕 Figma 完整规格文档
- GitHub Issue 模板（Bug Report + Feature Request）
- 28 个标签分类体系
- Web 端设计规范 + 设计 Token
- 测试计划（80 条用例）+ W8 更新
- 可用性测试招募计划
- 文献综述

## Files Changed

### Design Specs
- `docs/week7/Junliang Li/figma-screen-specifications.md` — 15 个屏幕的完整 ASCII 规范 + 设计系统
- `docs/week8/Junliang Li/web-design-specifications.md` — Web 端设计规范
- `docs/week8/Junliang Li/component-design-system-web.md` — Web 组件设计系统
- `docs/week8/Junliang Li/design-tokens-web.json` — 设计 Token（JSON）

### GitHub Templates
- `.github/ISSUE_TEMPLATE/bug-report.md` — Bug 报告模板
- `.github/ISSUE_TEMPLATE/feature-request.md` — 功能请求模板

### QA & Testing
- `docs/week7/Junliang Li/test-plan-and-cases.md` — 80 条测试用例
- `docs/week8/Junliang Li/test-plan-update-w8.md` — W8 测试计划更新
- `docs/week7/Junliang Li/usability-testing-recruitment-plan.md` — 可用性测试招募

### Labels & Research
- `docs/week7/Junliang Li/github-labels-taxonomy.md` — 28 个标签分类
- `docs/week7/Junliang Li/literature-review-uux-qa.md` — 8 篇文献综述

## Checklist
- [x] 所有文档已上传
- [x] Issue 模板格式正确
- [x] 遵循 Conventional Commits
- [x] 无 merge conflict

## 后续操作
PR 合并后，我会在 GitHub Issues → Labels 页面手动创建 28 个标签

## Reviewer
任何一位团队成员都可以 Review（纯文档，无代码依赖）
```

**Reviewer**（PR 页面右侧 → Reviewers → 齿轮图标）：选任意成员即可。

点击 **"Create pull request"**。

---

## Step 4：手动创建 28 个 GitHub Labels

> ⚠️ 这一步**在 PR 合并前后做都可以**。在 GitHub 网页上操作，不需要终端。

### 4.1 打开 Labels 页面

1. 浏览器访问：**https://github.com/LuoX11a/SG_CampusSwap/labels**
2. 你会看到 GitHub 默认的 9 个标签。先把它们全删掉：
   - 点击每个标签右边的 **"Delete"** 按钮
   - 重复 9 次

### 4.2 逐个创建标签

创建步骤（每个标签重复）：
1. 点击 **"New label"** 绿色按钮
2. 填入 **Label name**（标签名）
3. 可选的 **Description**（描述）
4. 在 **Color** 输入框中输入 **6 位颜色码**（不要带 `#`，GitHub 自动添加）
5. 点击 **"Create label"**

### 4.3 28 个标签完整列表

#### 🐛 Type — Bug 相关（红色系）

| 标签名 | 颜色码（不带 #） | 描述 |
|--------|:-----:|------|
| `type: bug` | `D73A4A` | Something isn't working |
| `type: blocker` | `B60205` | Blocks development or deployment |
| `type: hotfix` | `FF4444` | Urgent fix needed in production |

#### ✨ Type — 功能相关（绿色/蓝色系）

| 标签名 | 颜色码（不带 #） | 描述 |
|--------|:-----:|------|
| `type: feature` | `0E8A16` | New feature or functionality |
| `type: enhancement` | `A2EEEF` | Improvement to existing feature |
| `type: refactor` | `1D76DB` | Code restructuring, no behavior change |

#### 📚 Type — 文档相关

| 标签名 | 颜色码（不带 #） | 描述 |
|--------|:-----:|------|
| `type: documentation` | `0075CA` | Documentation additions or updates |
| `type: research` | `5319E7` | Research and investigation tasks |

#### 🔧 Type — 技术相关（灰色系）

| 标签名 | 颜色码（不带 #） | 描述 |
|--------|:-----:|------|
| `type: testing` | `C5DEF5` | Testing tasks and test coverage |
| `type: ci/cd` | `BFDADC` | CI/CD pipeline and deployment |
| `type: dependencies` | `F9D0C4` | Dependency updates |
| `type: chore` | `EEEEEE` | Maintenance and housekeeping |

#### 🎯 Priority（优先级）

| 标签名 | 颜色码（不带 #） | 描述 |
|--------|:-----:|------|
| `priority: critical` | `FF0000` | Must fix immediately |
| `priority: high` | `FF6B6B` | Should fix in current sprint |
| `priority: medium` | `FFA500` | Fix when possible |
| `priority: low` | `0E8A16` | Nice to have |

#### 📐 Effort（工作量）

| 标签名 | 颜色码（不带 #） | 描述 |
|--------|:-----:|------|
| `effort: xl` | `8B0000` | 5+ days |
| `effort: l` | `FF6347` | 2-3 days |
| `effort: m` | `FFD700` | 1 day |
| `effort: s` | `90EE90` | Few hours |
| `effort: xs` | `F0FFF0` | Under 1 hour |

#### 👤 Component（功能模块）

| 标签名 | 颜色码（不带 #） | 描述 |
|--------|:-----:|------|
| `component: auth` | `FFE4B5` | Authentication & user management |
| `component: listings` | `DA70D6` | Item listing and browsing |
| `component: chat` | `87CEEB` | Messaging and chat |
| `component: search` | `98FB98` | Search and filtering |
| `component: reviews` | `DDA0DD` | Review and rating system |
| `component: profile` | `F0E68C` | User profile and settings |
| `component: ui/ux` | `FFB6C1` | Interface and user experience |
| `component: deployment` | `B0C4DE` | Deployment and infrastructure |

---

创建完 28 个标签后，**截图发到团队群**，告诉大家 Labels 已就位。

---

## Step 5：等待 Review 并合并

1. 把 PR 链接发到团队微信群
2. 任何人可以 Review（你是纯文档，不需要代码背景）
3. 如果有人提修改意见（Request changes），在你的 Mac 上改好文件，然后：
   ```bash
   git add .
   git commit -m "fix: address review feedback"
   git push
   ```
4. 获得批准（Approve）后，在 PR 页面点击 **"Merge pull request"** → **"Confirm merge"**
5. 合并后，可以点击 **"Delete branch"** 删除远程分支（可选，保持仓库整洁）
6. 更新你本地的 develop：
   ```bash
   git checkout develop
   git pull origin develop
   ```

---

## 🎉 完成！

你做完后，队友可以开始用你创建的 Labels 给 Issue 打标签了。

---

## ❓ Mac 专属常见问题

### Q1: git push 时要求输入密码怎么办？

GitHub 从 2021 年起不再支持密码登录 Git，需要用 **Personal Access Token**（个人访问令牌）。

**创建 Token：**
1. 浏览器打开：https://github.com/settings/tokens
2. 点击 **"Generate new token"** → **"Generate new token (classic)"**
3. Note 填 `SG_CampusSwap_Mac`（随便，提醒你这是哪台机器的）
4. Expiration 选 **"No expiration"**（不过期）
5. 勾选 `repo`（全部勾上）、`workflow`
6. 拉到页面底部，点击绿色 **"Generate token"**
7. ⚠️ **立刻复制生成的 token**（以 `ghp_` 开头的一串字符）— 页面关了就再也看不到了

**在终端使用 Token：**
- 当 `git push` 弹出 `Username` 时 → 输入你的 GitHub 用户名
- 当弹出 `Password` 时 → **粘贴 token**（不是你的 GitHub 密码！）
- 粘贴时终端不会显示任何字符，这是正常的（安全设计）

**让 Mac 记住 Token（下次不用再输）：**
```bash
git config --global credential.helper osxkeychain
```

这样第一次输入后，Mac 钥匙串会记住，以后自动使用。

### Q2: GitHub 弹出了浏览器登录页面

这是 GitHub 的新登录方式（Git Credential Manager）。选择 **"Sign in with your browser"**，浏览器会自动打开 GitHub 授权页面，点击 **"Authorize"** 即可。这是最方便的方式。

### Q3: Permission denied（权限被拒绝）

你没有被加入仓库的 Collaborator。让 Renxian 去：
https://github.com/LuoX11a/SG_CampusSwap/settings/access
→ **Collaborators** → **Add people** → 输入你的 GitHub 用户名 → 发送邀请。

你会在 GitHub 绑定的邮箱里收到邀请邮件，点 **"Accept invitation"**。

### Q4: 桌面上没有 `Junliang Li` 文件夹

说明你还没从 Renxian 那里拿到源文件。回到 Step 0.1，先找 Renxian 要文件。

如果你把文件夹放在了别的位置（比如下载文件夹 `~/Downloads/`），把命令里的 `~/Desktop/Junliang\ Li` 换成你实际的位置。例如：
```bash
cp ~/Downloads/Junliang\ Li/1-5/figma-screen-specifications.md "docs/week7/Junliang Li/figma-screen-specifications.md"
```

### Q5: 路径里有空格 — `Junliang Li`

Mac/Linux 终端里，路径有空格需要加反斜杠转义：`Junliang\ Li`

或者用双引号把整个路径包起来：`"~/Desktop/Junliang Li/1-5/"`

**最省事的办法**：把桌面上的文件夹重命名为 `JunliangLi`（去掉空格），所有命令里就不需要反斜杠了。

### Q6: `cp` 命令说 "No such file or directory"

先手动确认文件是否存在：
```bash
ls ~/Desktop/Junliang\ Li/1-5/
```

如果能看到文件列表，说明路径对但复制命令里的路径写法有问题。检查空格处有没有加 `\ `。

### Q7: `git commit` 后想修改 commit 信息

```bash
git commit --amend -m "新的 commit 信息"
git push -f
```

⚠️ `-f` 是强制推送，只有在你确定没有别人基于你这个分支工作时才能用。你是一个人用这个分支，所以安全。

### Q8: PR 有 merge conflict

```bash
git checkout feature/github-templates-and-design
git fetch origin
git merge origin/develop
# 终端会提示哪些文件有冲突（CONFLICT 字样）
# 用 Mac 自带的文本编辑器打开冲突文件
# 搜索 <<<<<<< 标记，手动删除冲突标记，保留正确的内容
git add .
git commit -m "fix: resolve merge conflicts"
git push
```

---

## 📝 Mac vs Windows 命令对照表

| 操作 | Windows (cmd) | Mac (终端) |
|------|---------------|------------|
| 列出文件 | `dir` | `ls` |
| 列出文件（含子文件夹） | `dir /s /b` | `ls -R` |
| 当前目录 | `cd` | `pwd` |
| 桌面路径 | `%USERPROFILE%\Desktop` | `~/Desktop` |
| 创建文件夹 | `mkdir x` | `mkdir -p x` |
| 复制文件 | `copy A B` | `cp A B` |
| 移动文件 | `move A B` | `mv A B` |
| 删除文件 | `del x` | `rm x` |
| 删除文件夹 | `rmdir /s /q x` | `rm -rf x` |
| 创建空文件 | `type nul > x` | `touch x` |
| 查看文件内容 | `type x` | `cat x` |
| 路径分隔符 | `\` | `/` |
| 路径有空格 | `"C:\path\name\"` | `path/name\ ` 或 `"path/name"` |
| 注释 | `REM` | `#` |
