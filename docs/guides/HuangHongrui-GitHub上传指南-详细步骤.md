# Huang Hongrui — GitHub 上传完整操作指南

> 🎯 **你的任务**：上传项目管理文档。你的工作**不依赖任何人**，可以和 Jiahai 同一天做。
> ⏱ **预计耗时**：40-60 分钟（含 GitHub Projects Kanban 设置）
> ⚠️ **无需等待**：你是完全独立的，Bowei 创建 develop 后你就可以开始

---

## 📋 操作步骤总览

| 步骤 | 做什么 | 大概时间 |
|:--:|--------|:--:|
| **Step 0** | 装 Git、配置 GitHub、克隆仓库 | 20 分钟（如已做过可跳过） |
| **Step 1** | 从 develop 创建功能分支 | 5 分钟 |
| **Step 2** | 复制 PM 文档（12 个文件） | 10 分钟 |
| **Step 3** | 提交、推送、创建 PR | 10 分钟 |
| **Step 4** | 在 GitHub Projects 创建 Kanban Board | 15 分钟 |
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
git config --global user.name "Huang Hongrui"
git config --global user.email "hongrui.huang@example.com"
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

### 1.2 创建你的功能分支

```cmd
git fetch origin
git checkout -b feature/pm-docs origin/develop
```

预期输出：`Switched to a new branch 'feature/pm-docs'`

---

## Step 2：复制你的 PM 文档

### 2.1 你要上传的 12 个文件

| 来源文件夹 | 文件 | 放到仓库的哪里 |
|-----------|------|---------------|
| `Desktop\1-5\Huang Hongrui\` | `blockers-issues-log.md` | `docs\week7\Huang Hongrui\` |
| | `final-report-framework.md` | `docs\week7\Huang Hongrui\` |
| | `gantt-update-w7.md` | `docs\week7\Huang Hongrui\` |
| | `risk-register.md` | `docs\week7\Huang Hongrui\` |
| | `sprint-backlog.md` | `docs\week7\Huang Hongrui\` |
| | `week7-meeting-agenda.md` | `docs\week7\Huang Hongrui\` |
| | `meeting-minutes\phase1-progress-summary-w1-w5.md` | `docs\week7\Huang Hongrui\meeting-minutes\` |
| | `meeting-minutes\weekly-meetings-w1-w5.md` | `docs\week7\Huang Hongrui\meeting-minutes\` |
| `Desktop\week8\Huang Hongrui\` | `sprint-backlog-w8-update.md` | `docs\week8\Huang Hongrui\` |
| | `week8-meeting-agenda.md` | `docs\week8\Huang Hongrui\` |
| | `week8-progress-report.md` | `docs\week8\Huang Hongrui\` |
| | `risk-register-w8-update.md` | `docs\week8\Huang Hongrui\` |

> 📝 注意：W7 文档用的是 `1-5\Huang Hongrui\` 文件夹，不是 `week7\Huang Hongrui\`。

### 2.2 创建需要的文件夹

```cmd
mkdir docs\week7\Huang Hongrui\meeting-minutes
mkdir docs\week8\Huang Hongrui
```

> 如果提示"子目录或文件已存在"，忽略即可。

### 2.3 复制文件

依次执行以下命令：

```cmd
REM === W7 PM 文档（6 个主文档）===
copy "C:\Users\92183\Desktop\1-5\Huang Hongrui\blockers-issues-log.md"  "docs\week7\Huang Hongrui\blockers-issues-log.md"
copy "C:\Users\92183\Desktop\1-5\Huang Hongrui\final-report-framework.md" "docs\week7\Huang Hongrui\final-report-framework.md"
copy "C:\Users\92183\Desktop\1-5\Huang Hongrui\gantt-update-w7.md"        "docs\week7\Huang Hongrui\gantt-update-w7.md"
copy "C:\Users\92183\Desktop\1-5\Huang Hongrui\risk-register.md"          "docs\week7\Huang Hongrui\risk-register.md"
copy "C:\Users\92183\Desktop\1-5\Huang Hongrui\sprint-backlog.md"         "docs\week7\Huang Hongrui\sprint-backlog.md"
copy "C:\Users\92183\Desktop\1-5\Huang Hongrui\week7-meeting-agenda.md"   "docs\week7\Huang Hongrui\week7-meeting-agenda.md"

REM === W7 会议纪要（2 个）===
copy "C:\Users\92183\Desktop\1-5\Huang Hongrui\meeting-minutes\phase1-progress-summary-w1-w5.md" "docs\week7\Huang Hongrui\meeting-minutes\phase1-progress-summary-w1-w5.md"
copy "C:\Users\92183\Desktop\1-5\Huang Hongrui\meeting-minutes\weekly-meetings-w1-w5.md"       "docs\week7\Huang Hongrui\meeting-minutes\weekly-meetings-w1-w5.md"

REM === W8 PM 文档（4 个）===
copy "C:\Users\92183\Desktop\week8\Huang Hongrui\sprint-backlog-w8-update.md"  "docs\week8\Huang Hongrui\sprint-backlog-w8-update.md"
copy "C:\Users\92183\Desktop\week8\Huang Hongrui\week8-meeting-agenda.md"      "docs\week8\Huang Hongrui\week8-meeting-agenda.md"
copy "C:\Users\92183\Desktop\week8\Huang Hongrui\week8-progress-report.md"     "docs\week8\Huang Hongrui\week8-progress-report.md"
copy "C:\Users\92183\Desktop\week8\Huang Hongrui\risk-register-w8-update.md"   "docs\week8\Huang Hongrui\risk-register-w8-update.md"
```

### 2.4 检查文件结构

```cmd
dir /s /b "docs\week7\Huang Hongrui" "docs\week8\Huang Hongrui"
```

你应该看到：
```
docs\week7\Huang Hongrui\blockers-issues-log.md
docs\week7\Huang Hongrui\final-report-framework.md
docs\week7\Huang Hongrui\gantt-update-w7.md
docs\week7\Huang Hongrui\risk-register.md
docs\week7\Huang Hongrui\sprint-backlog.md
docs\week7\Huang Hongrui\week7-meeting-agenda.md
docs\week7\Huang Hongrui\meeting-minutes\phase1-progress-summary-w1-w5.md
docs\week7\Huang Hongrui\meeting-minutes\weekly-meetings-w1-w5.md
docs\week8\Huang Hongrui\sprint-backlog-w8-update.md
docs\week8\Huang Hongrui\week8-meeting-agenda.md
docs\week8\Huang Hongrui\week8-progress-report.md
docs\week8\Huang Hongrui\risk-register-w8-update.md
```

---

## Step 3：提交、推送、创建 PR

### 3.1 查看状态 → 暂存 → 提交

```cmd
git status
git add .
git status
```

确认所有 12 个文件变绿。

```cmd
git commit -m "docs: add PM documents — sprint backlog, risk register, meeting minutes, and progress reports"
```

### 3.2 推送到 GitHub

```cmd
git push -u origin feature/pm-docs
```

### 3.3 创建 PR

1. 浏览器访问：**https://github.com/LuoX11a/SG_CampusSwap**
2. 点击黄色提示条的 **"Compare & pull request"**
3. 如果没有提示条：Pull requests → New pull request → `base: develop` ← `compare: feature/pm-docs`

**标题**：
```
docs: add PM documents — sprint backlog, risk register, meeting minutes, and progress reports
```

**描述**：
```markdown
## Description
上传项目管理全套文档（W1-W8），包括：
- Sprint Backlog（5 个 Sprint / 57 任务项）+ W8 更新
- Risk Register（1 CRITICAL + 3 HIGH 风险）+ W8 更新
- Blockers & Issues Log（3 BLOCKER + 6 issues）
- Gantt 更新（实际 vs 计划对比 + 3 条恢复路径）
- Final Report 框架（11 章结构 + 写作计划）
- W7 Meeting Agenda + W8 Meeting Agenda
- W1-W5 会议纪要 + Phase 1 进度总结
- W8 进度报告

## Files Changed

### W7 — Sprint & Planning（4 files）
- `docs/week7/Huang Hongrui/sprint-backlog.md` — 5 Sprints, 57 任务项
- `docs/week7/Huang Hongrui/risk-register.md` — 1 CRITICAL + 3 HIGH 风险
- `docs/week7/Huang Hongrui/gantt-update-w7.md` — 实际 vs 计划 + 恢复路径
- `docs/week7/Huang Hongrui/blockers-issues-log.md` — 3 BLOCKER + 6 issues

### W7 — Meetings & Reports（4 files）
- `docs/week7/Huang Hongrui/week7-meeting-agenda.md` — W7 会议议程
- `docs/week7/Huang Hongrui/final-report-framework.md` — 11 章报告框架
- `docs/week7/Huang Hongrui/meeting-minutes/phase1-progress-summary-w1-w5.md`
- `docs/week7/Huang Hongrui/meeting-minutes/weekly-meetings-w1-w5.md` — W1-W5 详细纪要

### W8 — Updates（4 files）
- `docs/week8/Huang Hongrui/sprint-backlog-w8-update.md`
- `docs/week8/Huang Hongrui/risk-register-w8-update.md`
- `docs/week8/Huang Hongrui/week8-meeting-agenda.md`
- `docs/week8/Huang Hongrui/week8-progress-report.md`

## Checklist
- [x] 所有 12 份文档已上传
- [x] 遵循 Conventional Commits
- [x] 无 merge conflict

## 后续操作
PR 合并后，我会在 GitHub Projects 中创建 Kanban Board，导入 Sprint Backlog 任务

## Reviewer
任何团队成员都可以 Review（纯文档，无代码依赖）
```

**Reviewer**：选任意成员即可（你是纯文档）。

点击 **"Create pull request"**。

---

## Step 4：在 GitHub Projects 创建 Kanban Board

> ⚠️ 这一步在 PR 合并前后做都可以。

### 4.1 创建 Project

1. 浏览器访问：**https://github.com/LuoX11a/SG_CampusSwap/projects**
2. 点击 **"New project"**
3. 选择 **"Board"** 布局（Kanban 视图）
4. Project name：`SG CampusSwap — Sprint Board`
5. 点击 **"Create project"**

### 4.2 设置列（Columns）

默认有三列（Todo / In Progress / Done）。根据你的 Sprint Backlog 结构调整：

1. 点击列标题旁边的 `...` → **"Edit name"**
2. 建议的列结构：

| 列名 | 用途 |
|------|------|
| 🔴 **Backlog** | 未排期的任务 |
| 🟡 **Sprint To Do** | 当前 Sprint 待做 |
| 🟠 **In Progress** | 正在做 |
| 🔵 **In Review** | 等待 Review |
| 🟢 **Done** | 已完成 |

添加新列：点击最右侧的 **"+"** 按钮 → 输入列名。

### 4.3 导入 Sprint Backlog 任务

1. 打开你的 Sprint Backlog 文档（`docs\week7\Huang Hongrui\sprint-backlog.md`）
2. 在 Kanban Board 中，点击 **"Add item"**（在 Backlog 列底部）
3. 将任务逐条输入，格式：
   - 标题：`[FE] Login page UI implementation` 或 `[BE] JWT authentication middleware`
   - 可以用 `[FE]` / `[BE]` / `[DOC]` / `[QA]` 前缀区分类型
4. 如果任务需要更多描述，点击任务卡片 → 在右侧面板补充描述、Assignee、Labels 等
5. 高优先级任务（Sprint Backlog 中的 P0/P1）加上 `priority: critical` 或 `priority: high` 标签

### 4.4 关联已有 Issues/PRs

- 在任务卡片描述中输入 `#123` 即可自动关联 Issue #123 或 PR #123
- 后续可以在每个 PR 的右侧面板 → Projects → 选择这个 Board → 设置状态列

---

## Step 5：等待 Review 并合并

1. 把 PR 链接发到团队群
2. 任何人可以 Review（你是纯文档）
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

### Q3: 复制文件提示"找不到路径"
用文件资源管理器手动打开 `C:\Users\92183\Desktop\1-5\Huang Hongrui\` 确认文件存在。如果不存在，找 Renxian 要文件。

### Q4: 你的电脑上没有 `1-5\Huang Hongrui\` 文件夹
源文件在 Renxian 的电脑上。让他把整个 `1-5\Huang Hongrui\` 文件夹通过微信/网盘发给你，放到你的桌面上。或者直接让 Renxian 帮忙复制文件。

### Q5: Kanban Board 不知道怎么设置
这是可选的加分项，不是必须的。如果你觉得太复杂，可以跳过 Step 4，以后再做。

### Q6: 路径中的空格问题
`Huang Hongrui` 有空格，上面所有命令已经用双引号包裹，直接复制粘贴即可。
