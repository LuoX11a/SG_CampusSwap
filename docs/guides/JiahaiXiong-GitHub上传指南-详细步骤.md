# Jiahai Xiong — GitHub 上传完整操作指南

> 🎯 **你的任务**：在 Renxian 上传前端核心架构之后，上传你开发的扩展页面和组件。
> ⏱ **预计耗时**：30-45 分钟
> ⚠️ **前置条件**：Renxian（Stage 3）必须已经完成并合并到 develop！你的代码依赖他的组件和 stores。

---

## 📋 操作步骤总览

| 步骤 | 做什么 | 大概时间 |
|:--:|--------|:--:|
| **Step 0** | 装 Git、配置 GitHub、克隆仓库 | 20 分钟（如已做过可跳过） |
| **Step 1** | 确认 Renxian 已完成 + 创建分支 | 5 分钟 |
| **Step 2** | 复制你的前端扩展文件（10 个文件） | 10 分钟 |
| **Step 3** | 提交、推送、创建 PR | 10 分钟 |
| **Step 4** | 等 Renxian Review、合并 | 5 分钟 |

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
git config --global user.name "Jiahai Xiong"
git config --global user.email "jiahai.xiong@example.com"
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

## Step 1：确认 Renxian 已完成 + 创建分支

### 1.1 确认 Renxian 的前端代码已在 develop 上

```cmd
git fetch origin
git branch -a
```

确认能看到 `remotes/origin/develop`。

### 1.2 检查 develop 上已有前端基础文件

```cmd
git checkout -b temp-check origin/develop
dir web\src\components
dir web\src\stores
git checkout master
git branch -d temp-check
```

你应该看到：
- Sidebar.tsx, ItemCard.tsx, SearchBar.tsx, CategoryChips.tsx, SkeletonCard.tsx ← Renxian 的组件
- auth-store.ts, item-store.ts, filter-store.ts, chat-store.ts ← Renxian 的 stores

> ❌ 如果看不到这些文件，说明 Renxian 还没完成！等他做完再进行。

### 1.3 创建你的功能分支

```cmd
git checkout -b feature/frontend-pages origin/develop
```

预期输出：`Switched to a new branch 'feature/frontend-pages'`

---

## Step 2：复制你的文件

### 2.1 你要上传的文件清单

| 来源文件夹 | 文件 | 放到仓库的哪里 |
|-----------|------|---------------|
| `Desktop\week7\Jiahai Xiong\` | `frontend-dev-deliverables-w7.md` | `docs\week7\Jiahai Xiong\` |
| `Desktop\week8\Jiahai Xiong\` | `web\src\app\messages\page.tsx` | `web\src\app\messages\` |
| | `web\src\app\messages\[id]\page.tsx` | `web\src\app\messages\[id]\` |
| | `web\src\app\profile\page.tsx` | `web\src\app\profile\` |
| | `web\src\app\profile\edit\page.tsx` | `web\src\app\profile\edit\` |
| | `web\src\app\profile\[id]\page.tsx` | `web\src\app\profile\[id]\` |
| | `web\src\app\settings\page.tsx` | `web\src\app\settings\` |
| | `web\src\app\reviews\page.tsx` | `web\src\app\reviews\` |
| | `web\src\app\my-listings\page.tsx` | `web\src\app\my-listings\` |
| | `web\src\components\FilterModal.tsx` | `web\src\components\` |
| | `frontend-dev-w8-summary.md` | `docs\week8\Jiahai Xiong\` |

共 **11 个文件**（9 个代码 + 2 个文档）。

### 2.2 创建需要的文件夹

```cmd
mkdir docs\week7\Jiahai Xiong
mkdir docs\week8\Jiahai Xiong
mkdir web\src\app\messages\[id]
mkdir web\src\app\profile\edit
mkdir web\src\app\profile\[id]
mkdir web\src\app\settings
mkdir web\src\app\reviews
mkdir web\src\app\my-listings
```

> 如果提示"子目录或文件已存在"，忽略即可。

### 2.3 复制文件

依次执行以下命令：

```cmd
REM === W7 文档 ===
copy "C:\Users\92183\Desktop\week7\Jiahai Xiong\frontend-dev-deliverables-w7.md" "docs\week7\Jiahai Xiong\frontend-dev-deliverables-w7.md"

REM === W8 文档 ===
copy "C:\Users\92183\Desktop\week8\Jiahai Xiong\frontend-dev-w8-summary.md" "docs\week8\Jiahai Xiong\frontend-dev-w8-summary.md"

REM === Chat 模块（2 个页面）===
copy "C:\Users\92183\Desktop\week8\Jiahai Xiong\web\src\app\messages\page.tsx"      "web\src\app\messages\page.tsx"
copy "C:\Users\92183\Desktop\week8\Jiahai Xiong\web\src\app\messages\[id]\page.tsx"  "web\src\app\messages\[id]\page.tsx"

REM === Profile 模块（3 个页面）===
copy "C:\Users\92183\Desktop\week8\Jiahai Xiong\web\src\app\profile\page.tsx"       "web\src\app\profile\page.tsx"
copy "C:\Users\92183\Desktop\week8\Jiahai Xiong\web\src\app\profile\edit\page.tsx"   "web\src\app\profile\edit\page.tsx"
copy "C:\Users\92183\Desktop\week8\Jiahai Xiong\web\src\app\profile\[id]\page.tsx"   "web\src\app\profile\[id]\page.tsx"

REM === Settings + Reviews + MyListings（3 个页面）===
copy "C:\Users\92183\Desktop\week8\Jiahai Xiong\web\src\app\settings\page.tsx"      "web\src\app\settings\page.tsx"
copy "C:\Users\92183\Desktop\week8\Jiahai Xiong\web\src\app\reviews\page.tsx"       "web\src\app\reviews\page.tsx"
copy "C:\Users\92183\Desktop\week8\Jiahai Xiong\web\src\app\my-listings\page.tsx"   "web\src\app\my-listings\page.tsx"

REM === 组件（1 个）===
copy "C:\Users\92183\Desktop\week8\Jiahai Xiong\web\src\components\FilterModal.tsx" "web\src\components\FilterModal.tsx"
```

### 2.4 检查文件结构

```cmd
dir /s /b web\src\app\messages web\src\app\profile web\src\app\settings web\src\app\reviews web\src\app\my-listings docs\week7\Jiahai Xiong docs\week8\Jiahai Xiong
```

你应该看到：
```
web\src\app\messages\page.tsx
web\src\app\messages\[id]\page.tsx
web\src\app\profile\page.tsx
web\src\app\profile\edit\page.tsx
web\src\app\profile\[id]\page.tsx
web\src\app\settings\page.tsx
web\src\app\reviews\page.tsx
web\src\app\my-listings\page.tsx
web\src\components\FilterModal.tsx
docs\week7\Jiahai Xiong\frontend-dev-deliverables-w7.md
docs\week8\Jiahai Xiong\frontend-dev-w8-summary.md
```

---

## Step 3：提交并推送

### 3.1 查看状态 → 暂存 → 提交

```cmd
git status
git add .
git status
```

确认所有文件变绿。

```cmd
git commit -m "feat: add Chat, Profile, Settings, Reviews, MyListings pages and FilterModal"
```

### 3.2 推送到 GitHub

```cmd
git push -u origin feature/frontend-pages
```

---

## Step 4：创建 Pull Request

### 4.1 打开 PR 页面

1. 浏览器访问：**https://github.com/LuoX11a/SG_CampusSwap**
2. 点击黄色提示条的 **"Compare & pull request"**
3. 如果没有提示条：Pull requests → New pull request → `base: develop` ← `compare: feature/frontend-pages`

### 4.2 填写 PR 信息

**标题**：
```
feat: add Chat, Profile, Settings, Reviews, MyListings pages and FilterModal
```

**描述**：
```markdown
## Description
基于 Renxian 的前端核心架构，上传扩展页面和组件：
- Chat 模块（消息列表 + 聊天对话页）
- Profile 模块（个人资料 + 编辑 + 查看他人资料）
- Settings 页面
- Reviews 页面
- My Listings 页面
- FilterModal 组件

所有页面依赖 Renxian 的共享组件（Sidebar, ItemCard, SearchBar）和 Zustand stores。

## Files Changed

### Chat 模块
- `web/src/app/messages/page.tsx` — 消息列表页
- `web/src/app/messages/[id]/page.tsx` — 聊天对话页

### Profile 模块
- `web/src/app/profile/page.tsx` — 个人资料主页
- `web/src/app/profile/edit/page.tsx` — 编辑个人资料
- `web/src/app/profile/[id]/page.tsx` — 查看他人资料

### 其他页面
- `web/src/app/settings/page.tsx` — 设置页面
- `web/src/app/reviews/page.tsx` — 评价页面
- `web/src/app/my-listings/page.tsx` — 我的商品列表

### 组件
- `web/src/components/FilterModal.tsx` — 筛选弹窗组件

### 文档
- `docs/week7/Jiahai Xiong/frontend-dev-deliverables-w7.md` — W7 交付文档
- `docs/week8/Jiahai Xiong/frontend-dev-w8-summary.md` — W8 总结文档

## Checklist
- [x] 代码已本地测试通过
- [x] 遵循 Conventional Commits
- [x] 无 merge conflict
- [x] 依赖 Renxian 的组件和 stores 已就位

## Reviewer
@RenxianTang — 请 Review 前端代码
```

### 4.3 设置 Reviewer

PR 页面右侧 → **Reviewers** → 齿轮 → 选择 **Renxian 的 GitHub 用户名**

### 4.4 点击 **"Create pull request"**

---

## Step 5：等待 Review 并合并

1. 把 PR 链接发到团队群
2. **Renxian 是主要 Reviewer**（你的代码依赖他的架构）
3. 如果有人提修改意见，本地修改后：
   ```cmd
   git add .
   git commit -m "fix: address review feedback"
   git push
   ```
4. 获得批准后，点击 **"Merge pull request"** → **"Confirm merge"**
5. 合并后更新本地：

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
用文件资源管理器手动打开 `C:\Users\92183\Desktop\week8\Jiahai Xiong\web\src\app\` 确认文件存在。如果不存在，找 Renxian 要文件。

### Q4: PR 有 merge conflict（常见！因为你依赖 Renxian 的文件）
```cmd
git checkout feature/frontend-pages
git fetch origin
git merge origin/develop
# 手动解决冲突 → 用记事本打开冲突文件，搜索 <<<<<<< 和 >>>>>>>
git add .
git commit -m "fix: resolve merge conflicts"
git push
```

### Q5: 文件夹名带空格怎么办（Jiahai Xiong）
Windows 命令提示符里，路径带空格需要用双引号包裹。上面所有命令已经加了双引号，直接复制粘贴即可。

### Q6: 你的文件里 import 了 Renxian 的组件但路径不对
因为你们两人的文件现在在同一个仓库里，import 路径不需要改动。如果之前 import 路径是相对路径，合并后应该没问题。如果发现路径有问题，在本地改完再 push 一次。
