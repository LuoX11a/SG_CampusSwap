# Junliang Li — GitHub 上传完整操作指南

> 🎯 **你的任务**：上传设计文档 + GitHub Issue 模板 + 创建 28 个 Labels。你的工作**不依赖任何人**，可以和 Wang Xu 同一天做。
> ⏱ **预计耗时**：1-1.5 小时（大部分时间在手动创建 28 个 Labels）
> ⚠️ **无需等待**：你是唯一完全独立的人，Bowei 创建 develop 后你就可以开始

---

## 📋 操作步骤总览

| 步骤 | 做什么 | 大概时间 |
|:--:|--------|:--:|
| **Step 0** | 装 Git、配置 GitHub、克隆仓库 | 20 分钟（如已做过可跳过） |
| **Step 1** | 从 develop 创建功能分支 | 5 分钟 |
| **Step 2** | 复制文档和模板文件（10 个文件） | 10 分钟 |
| **Step 3** | 提交、推送、创建 PR | 10 分钟 |
| **Step 4** | 在 GitHub 网页上手动创建 28 个 Labels | 20 分钟 |
| **Step 5** | 等 Review、合并 | 5 分钟 |

---

## Step 0：准备工作（只做一次）

### 0.1 检查 Git 是否安装

打开**命令提示符**（按 `Win + R`，输入 `cmd`，回车），输入：

```cmd
git --version
```

如果显示 `git version 2.xx.x` → ✅ 已安装，跳到 0.3
如果显示 `'git' 不是内部或外部命令` → ❌ 没装，继续 0.2

### 0.2 安装 Git

1. 打开浏览器访问：**https://git-scm.com/download/win**
2. 下载后双击安装，所有选项用默认值，一路 "Next" → "Install"
3. 装完后关掉命令提示符，重新打开
4. 再次输入 `git --version` 确认

### 0.3 配置 Git 用户名和邮箱

```cmd
git config --global user.name "Junliang Li"
git config --global user.email "junliang.li@example.com"
```

> ⚠️ 邮箱必须和你的 GitHub 账号邮箱一致！

验证配置：

```cmd
git config --global user.name
git config --global user.email
```

### 0.4 确认能登录 GitHub

1. 浏览器访问：**https://github.com/login**，登录你的账号
2. 确认能看到：**https://github.com/LuoX11a/SG_CampusSwap**
3. 如果看不到，让 Renxian 在 Settings → Collaborators 里加你

### 0.5 克隆仓库

```cmd
cd %USERPROFILE%\Desktop
git clone https://github.com/LuoX11a/SG_CampusSwap.git
cd SG_CampusSwap
```

> 如果提示文件夹已存在：
> ```cmd
> rmdir /s /q SG_CampusSwap
> git clone https://github.com/LuoX11a/SG_CampusSwap.git
> cd SG_CampusSwap
> ```

---

## Step 1：确认 develop 存在 + 创建分支

### 1.1 确认 develop 分支存在

```cmd
git branch -a
```

你应该看到：
```
* master
  remotes/origin/master
  remotes/origin/develop
```

> ❌ 如果看不到 `remotes/origin/develop`，说明 Bowei 还没完成！等他做完再进行。

### 1.2 拉取最新代码并创建你的分支

```cmd
git fetch origin
git checkout -b feature/github-templates-and-design origin/develop
```

预期输出：`Switched to a new branch 'feature/github-templates-and-design'`

---

## Step 2：复制你的文件

### 2.1 你要上传的文件清单

| 来源文件夹 | 文件 | 放到仓库的哪里 |
|-----------|------|---------------|
| `Desktop\1-5\Junliang Li\` | `figma-screen-specifications.md` | `docs\week7\Junliang Li\` |
| | `github-labels-taxonomy.md` | `docs\week7\Junliang Li\` |
| | `literature-review-uux-qa.md` | `docs\week7\Junliang Li\` |
| | `test-plan-and-cases.md` | `docs\week7\Junliang Li\` |
| | `usability-testing-recruitment-plan.md` | `docs\week7\Junliang Li\` |
| | `github-templates\bug-report.md` | `.github\ISSUE_TEMPLATE\` |
| | `github-templates\feature-request.md` | `.github\ISSUE_TEMPLATE\` |
| `Desktop\week8\Junliang Li\` | `web-design-specifications.md` | `docs\week8\Junliang Li\` |
| | `component-design-system-web.md` | `docs\week8\Junliang Li\` |
| | `design-tokens-web.json` | `docs\week8\Junliang Li\` |
| | `test-plan-update-w8.md` | `docs\week8\Junliang Li\` |

共 **11 个文件**（7 个 W7 文档与模板 + 4 个 W8 文档）。

> 📝 注意：W7 文档用的是 `1-5\Junliang Li\` 文件夹，不是 `week7\Junliang Li\`。

### 2.2 创建需要的文件夹

```cmd
mkdir docs\week7\Junliang Li
mkdir docs\week8\Junliang Li
mkdir .github\ISSUE_TEMPLATE
```

> 如果提示"子目录或文件已存在"，忽略即可。

### 2.3 复制文件

依次执行以下命令：

```cmd
REM === W7 设计文档（5 个）===
copy "C:\Users\92183\Desktop\1-5\Junliang Li\figma-screen-specifications.md"        "docs\week7\Junliang Li\figma-screen-specifications.md"
copy "C:\Users\92183\Desktop\1-5\Junliang Li\github-labels-taxonomy.md"             "docs\week7\Junliang Li\github-labels-taxonomy.md"
copy "C:\Users\92183\Desktop\1-5\Junliang Li\literature-review-uux-qa.md"           "docs\week7\Junliang Li\literature-review-uux-qa.md"
copy "C:\Users\92183\Desktop\1-5\Junliang Li\test-plan-and-cases.md"                "docs\week7\Junliang Li\test-plan-and-cases.md"
copy "C:\Users\92183\Desktop\1-5\Junliang Li\usability-testing-recruitment-plan.md" "docs\week7\Junliang Li\usability-testing-recruitment-plan.md"

REM === W7 GitHub 模板（2 个）===
copy "C:\Users\92183\Desktop\1-5\Junliang Li\github-templates\bug-report.md"      ".github\ISSUE_TEMPLATE\bug-report.md"
copy "C:\Users\92183\Desktop\1-5\Junliang Li\github-templates\feature-request.md" ".github\ISSUE_TEMPLATE\feature-request.md"

REM === W8 设计文档（4 个）===
copy "C:\Users\92183\Desktop\week8\Junliang Li\web-design-specifications.md"      "docs\week8\Junliang Li\web-design-specifications.md"
copy "C:\Users\92183\Desktop\week8\Junliang Li\component-design-system-web.md"    "docs\week8\Junliang Li\component-design-system-web.md"
copy "C:\Users\92183\Desktop\week8\Junliang Li\design-tokens-web.json"            "docs\week8\Junliang Li\design-tokens-web.json"
copy "C:\Users\92183\Desktop\week8\Junliang Li\test-plan-update-w8.md"            "docs\week8\Junliang Li\test-plan-update-w8.md"
```

### 2.4 检查文件结构

```cmd
dir /s /b docs\week7\Junliang Li docs\week8\Junliang Li .github\ISSUE_TEMPLATE
```

你应该看到：
```
docs\week7\Junliang Li\figma-screen-specifications.md
docs\week7\Junliang Li\github-labels-taxonomy.md
docs\week7\Junliang Li\literature-review-uux-qa.md
docs\week7\Junliang Li\test-plan-and-cases.md
docs\week7\Junliang Li\usability-testing-recruitment-plan.md
docs\week8\Junliang Li\web-design-specifications.md
docs\week8\Junliang Li\component-design-system-web.md
docs\week8\Junliang Li\design-tokens-web.json
docs\week8\Junliang Li\test-plan-update-w8.md
.github\ISSUE_TEMPLATE\bug-report.md
.github\ISSUE_TEMPLATE\feature-request.md
```

---

## Step 3：提交、推送、创建 PR

### 3.1 查看状态 → 暂存 → 提交

```cmd
git status
git add .
git status
git commit -m "docs: add GitHub issue templates, labels taxonomy, and design specifications"
```

### 3.2 推送到 GitHub

```cmd
git push -u origin feature/github-templates-and-design
```

### 3.3 创建 PR

1. 浏览器访问：**https://github.com/LuoX11a/SG_CampusSwap**
2. 点击黄色提示条的 **"Compare & pull request"**
3. 如果没有提示条：Pull requests → New pull request → `base: develop` ← `compare: feature/github-templates-and-design`

**标题**：
```
docs: add GitHub issue templates, labels taxonomy, and design specifications
```

**描述**：
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

**Reviewer**：选任何一位团队成员即可（你的是纯文档，不需要代码审查）。

点击 **"Create pull request"**。

---

## Step 4：手动创建 28 个 GitHub Labels（重要！）

> ⚠️ 这一步**必须在 PR 合并之后**做，或者至少等 develop 上有你的 `github-labels-taxonomy.md`。

### 4.1 打开 Labels 管理页面

1. 浏览器访问：**https://github.com/LuoX11a/SG_CampusSwap/labels**
2. 先把 GitHub 默认的 9 个标签全部删掉（点击每个标签右边的 "Delete"）

### 4.2 对照标签分类文档逐一创建

打开你的标签分类文档查看完整列表：**`docs\week7\Junliang Li\github-labels-taxonomy.md`**

创建步骤（每个标签重复）：
1. 点击 **"New label"** 按钮
2. 填入 Label name（标签名）
3. 填入 Description（描述，可选）
4. 选择颜色（Color），填入十六进制颜色码，如 `#FF6B6B`
5. 点击 **"Create label"**

### 4.3 28 个标签完整列表（按分类）

#### 🐛 Type — Bug 相关（红色系）

| 标签名 | 颜色码 | 描述 |
|--------|:-----:|------|
| `type: bug` | `#D73A4A` | Something isn't working |
| `type: blocker` | `#B60205` | Blocks development or deployment |
| `type: hotfix` | `#FF4444` | Urgent fix needed in production |

#### ✨ Type — 功能相关（绿色系）

| 标签名 | 颜色码 | 描述 |
|--------|:-----:|------|
| `type: feature` | `#0E8A16` | New feature or functionality |
| `type: enhancement` | `#A2EEEF` | Improvement to existing feature |
| `type: refactor` | `#1D76DB` | Code restructuring, no behavior change |

#### 📚 Type — 文档相关（蓝色系）

| 标签名 | 颜色码 | 描述 |
|--------|:-----:|------|
| `type: documentation` | `#0075CA` | Documentation additions or updates |
| `type: research` | `#5319E7` | Research and investigation tasks |

#### 🔧 Type — 技术相关（灰色系）

| 标签名 | 颜色码 | 描述 |
|--------|:-----:|------|
| `type: testing` | `#C5DEF5` | Testing tasks and test coverage |
| `type: ci/cd` | `#BFDADC` | CI/CD pipeline and deployment |
| `type: dependencies` | `#F9D0C4` | Dependency updates |
| `type: chore` | `#EEEEEE` | Maintenance and housekeeping |

#### 🎯 Priority（优先级）

| 标签名 | 颜色码 | 描述 |
|--------|:-----:|------|
| `priority: critical` | `#FF0000` | Must fix immediately |
| `priority: high` | `#FF6B6B` | Should fix in current sprint |
| `priority: medium` | `#FFA500` | Fix when possible |
| `priority: low` | `#0E8A16` | Nice to have |

#### 📐 Effort（工作量）

| 标签名 | 颜色码 | 描述 |
|--------|:-----:|------|
| `effort: xl` | `#8B0000` | 5+ days |
| `effort: l` | `#FF6347` | 2-3 days |
| `effort: m` | `#FFD700` | 1 day |
| `effort: s` | `#90EE90` | Few hours |
| `effort: xs` | `#F0FFF0` | Under 1 hour |

#### 👤 Component（功能模块）

| 标签名 | 颜色码 | 描述 |
|--------|:-----:|------|
| `component: auth` | `#FFE4B5` | Authentication & user management |
| `component: listings` | `#DA70D6` | Item listing and browsing |
| `component: chat` | `#87CEEB` | Messaging and chat |
| `component: search` | `#98FB98` | Search and filtering |
| `component: reviews` | `#DDA0DD` | Review and rating system |
| `component: profile` | `#F0E68C` | User profile and settings |
| `component: ui/ux` | `#FFB6C1` | Interface and user experience |
| `component: deployment` | `#B0C4DE` | Deployment and infrastructure |

---

创建完 28 个标签后，你的 Labels 页面应该五彩缤纷。**截图发到团队群**，告诉大家 Labels 已就位。

---

## Step 5：等待 Review 并合并

1. 把 PR 链接发到团队群
2. 任何人可以 Review（你是纯文档，不需要代码背景）
3. 获得批准后，点击 **"Merge pull request"** → **"Confirm merge"**
4. 合并后更新本地：

```cmd
git checkout develop
git pull origin develop
```

---

## ❓ 常见问题

### Q1: push 时弹密码框
GitHub 不支持密码登录。需要 Personal Access Token：
1. 打开 https://github.com/settings/tokens
2. "Generate new token (classic)" → 勾选 `repo` → 生成 → 复制 token
3. 密码框粘贴 token（不会显示字符，正常）

### Q2: `Permission denied`
你没有仓库写权限。让 Renxian 在仓库 Settings → Collaborators 里加你。

### Q3: 创建 Labels 时颜色码不生效
确保你输入的是 6 位十六进制颜色码，**不带 `#` 号**（GitHub 会自动加上）。例如输入 `D73A4A`，不是 `#D73A4A`。

### Q4: 忘记删除默认标签就创建了新的
没关系。在 Labels 页面，默认的 9 个标签（bug, documentation, duplicate, enhancement, good first issue, help wanted, invalid, question, wontfix）一个个删除即可。

### Q5: 你的电脑上没有 `1-5\Junliang Li\` 文件夹
源文件在 Renxian 的电脑上。让他把整个 `1-5\Junliang Li\` 文件夹通过微信/网盘发给你，放到你的桌面上。或者直接让 Renxian 帮忙复制文件。
