# Renxian Tang — GitHub 上传完整操作指南

> 🎯 **你的任务**：在 Bowei 和 Wang Xu 上传后端代码之后，上传前端核心架构代码。
> ⏱ **预计耗时**：40-60 分钟
> ⚠️ **前置条件**：Bowei（Stage 1）和 Wang Xu（Stage 2a）必须已经完成并合并到 develop！

---

## 📋 操作步骤总览

| 步骤 | 做什么 | 大概时间 |
|:--:|--------|:--:|
| **Step 0** | 准备工作 | 10 分钟（你应该已经配好 Git） |
| **Step 1** | 确认前置依赖 + 创建分支 | 5 分钟 |
| **Step 2** | 复制前端核心文件（29 个文件） | 15 分钟 |
| **Step 3** | 创建 `.env.example` + 确认 `.gitignore` | 5 分钟 |
| **Step 4** | 提交、推送、创建 PR | 10 分钟 |
| **Step 5** | 等 Jiahai + 1 人 Review、合并 | 5 分钟 |

---

## Step 0：准备工作

### 0.1 确认你的 Git 已配置

打开**命令提示符**（`Win + R` → `cmd`），检查配置：

```cmd
git --version
git config --global user.name
git config --global user.email
```

如果 user.name 不是 "Renxian Tang" 或 user.email 不是你 GitHub 的邮箱，重新配置：

```cmd
git config --global user.name "Renxian Tang"
git config --global user.email "你的GitHub邮箱@example.com"
```

### 0.2 导航到仓库

```cmd
cd %USERPROFILE%\Desktop\SG_CampusSwap
```

如果还没有克隆：

```cmd
cd %USERPROFILE%\Desktop
git clone https://github.com/LuoX11a/SG_CampusSwap.git
cd SG_CampusSwap
```

---

## Step 1：确认前置依赖 + 创建分支

### 1.1 确认 Bowei 和 Wang Xu 的代码已在 develop 上

```cmd
git fetch origin
git branch -a
```

确认能看到：
```
remotes/origin/develop
```

### 1.2 检查 develop 上已有后端文件

```cmd
git checkout -b temp-check origin/develop
dir backend\app\models
dir backend\app\api\v1
git checkout master
git branch -d temp-check
```

你应该看到：
- `backend\app\models\` 下有三个文件（user.py, item.py, review.py）← Bowei 的
- `backend\app\api\v1\` 下有 items.py, search.py, users.py 等 ← Wang Xu 的

> ❌ 如果看不到这些文件，说明前置依赖还没完成！等 Bowei 和 Wang Xu 合并后再进行。

### 1.3 创建你的功能分支

```cmd
git checkout -b feature/frontend-core origin/develop
```

预期输出：`Switched to a new branch 'feature/frontend-core'`

---

## Step 2：复制前端核心文件

### 2.1 你要上传的 29 个文件

| 来源 | 文件 | 目标位置 |
|------|------|----------|
| `week7\Renxian Tang\` | `frontend-lead-deliverables-w7.md` | `docs\week7\Renxian Tang\` |
| `week8\Renxian Tang\` | `web\package.json` | `web\` |
| | `web\next.config.js` | `web\` |
| | `web\tsconfig.json` | `web\` |
| | `web\tailwind.config.ts` | `web\` |
| | `web\postcss.config.js` | `web\` |
| | `web\src\app\globals.css` | `web\src\app\` |
| | `web\src\app\layout.tsx` | `web\src\app\` |
| | `web\src\app\page.tsx` | `web\src\app\` |
| | `web\src\app\browse\page.tsx` | `web\src\app\browse\` |
| | `web\src\app\item\[id]\page.tsx` | `web\src\app\item\[id]\` |
| | `web\src\app\sell\page.tsx` | `web\src\app\sell\` |
| | `web\src\app\(auth)\login\page.tsx` | `web\src\app\(auth)\login\` |
| | `web\src\app\(auth)\register\page.tsx` | `web\src\app\(auth)\register\` |
| | `web\src\app\(auth)\verify-email\page.tsx` | `web\src\app\(auth)\verify-email\` |
| | `web\src\components\Sidebar.tsx` | `web\src\components\` |
| | `web\src\components\ItemCard.tsx` | `web\src\components\` |
| | `web\src\components\SearchBar.tsx` | `web\src\components\` |
| | `web\src\components\CategoryChips.tsx` | `web\src\components\` |
| | `web\src\components\SkeletonCard.tsx` | `web\src\components\` |
| | `web\src\lib\api-client.ts` | `web\src\lib\` |
| | `web\src\lib\types.ts` | `web\src\lib\` |
| | `web\src\lib\format.ts` | `web\src\lib\` |
| | `web\src\stores\auth-store.ts` | `web\src\stores\` |
| | `web\src\stores\item-store.ts` | `web\src\stores\` |
| | `web\src\stores\filter-store.ts` | `web\src\stores\` |
| | `web\src\stores\chat-store.ts` | `web\src\stores\` |
| | `frontend-lead-w8-summary.md` | `docs\week8\Renxian Tang\` |

### 2.2 创建需要的文件夹

```cmd
mkdir docs\week7\Renxian Tang
mkdir docs\week8\Renxian Tang
mkdir web\src\app\(auth)\login
mkdir web\src\app\(auth)\register
mkdir web\src\app\(auth)\verify-email
mkdir web\src\app\browse
mkdir web\src\app\item\[id]
mkdir web\src\app\sell
mkdir web\src\components
mkdir web\src\lib
mkdir web\src\stores
```

> 如果提示"子目录或文件已存在"，忽略即可。
> 注意：PowerShell 里括号需要特殊处理，建议用命令提示符（cmd）执行这些命令。

### 2.3 复制文件（用命令提示符 cmd）

```cmd
REM === W7 文档 ===
copy "C:\Users\92183\Desktop\week7\Renxian Tang\frontend-lead-deliverables-w7.md" "docs\week7\Renxian Tang\frontend-lead-deliverables-w7.md"

REM === W8 文档 ===
copy "C:\Users\92183\Desktop\week8\Renxian Tang\frontend-lead-w8-summary.md" "docs\week8\Renxian Tang\frontend-lead-w8-summary.md"

REM === Web 配置文件（5 个）===
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\package.json"      "web\package.json"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\next.config.js"    "web\next.config.js"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\tsconfig.json"     "web\tsconfig.json"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\tailwind.config.ts" "web\tailwind.config.ts"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\postcss.config.js" "web\postcss.config.js"

REM === App 核心（3 个文件）===
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\app\globals.css" "web\src\app\globals.css"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\app\layout.tsx"  "web\src\app\layout.tsx"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\app\page.tsx"    "web\src\app\page.tsx"

REM === 路由页面（6 个）===
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\app\browse\page.tsx"       "web\src\app\browse\page.tsx"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\app\item\[id]\page.tsx"     "web\src\app\item\[id]\page.tsx"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\app\sell\page.tsx"          "web\src\app\sell\page.tsx"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\app\(auth)\login\page.tsx"        "web\src\app\(auth)\login\page.tsx"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\app\(auth)\register\page.tsx"     "web\src\app\(auth)\register\page.tsx"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\app\(auth)\verify-email\page.tsx" "web\src\app\(auth)\verify-email\page.tsx"

REM === 组件（5 个）===
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\components\Sidebar.tsx"      "web\src\components\Sidebar.tsx"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\components\ItemCard.tsx"     "web\src\components\ItemCard.tsx"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\components\SearchBar.tsx"    "web\src\components\SearchBar.tsx"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\components\CategoryChips.tsx" "web\src\components\CategoryChips.tsx"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\components\SkeletonCard.tsx"  "web\src\components\SkeletonCard.tsx"

REM === 工具库（3 个）===
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\lib\api-client.ts" "web\src\lib\api-client.ts"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\lib\types.ts"      "web\src\lib\types.ts"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\lib\format.ts"     "web\src\lib\format.ts"

REM === 状态管理（4 个 Store）===
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\stores\auth-store.ts"   "web\src\stores\auth-store.ts"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\stores\item-store.ts"   "web\src\stores\item-store.ts"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\stores\filter-store.ts" "web\src\stores\filter-store.ts"
copy "C:\Users\92183\Desktop\week8\Renxian Tang\web\src\stores\chat-store.ts"   "web\src\stores\chat-store.ts"
```

### 2.4 检查文件结构

```cmd
dir /s /b web docs\week7\Renxian Tang docs\week8\Renxian Tang
```

你应该看到完整的 29 个文件。

---

## Step 3：创建环境变量文件 + 检查 .gitignore

### 3.1 创建 `.env.example`（提交到 GitHub）

```cmd
echo NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1 > web\.env.example
```

### 3.2 创建 `.env.local`（不提交，本地开发用）

```cmd
echo NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1 > web\.env.local
```

### 3.3 确认 `.env.local` 不会被提交

```cmd
type .gitignore | findstr ".env"
```

应该看到 `.env` 和 `.env.local` 在列表中（Bowei 创建的 `.gitignore` 里应该有）。

如果没有，追加：

```cmd
echo .env.local >> .gitignore
```

---

## Step 4：提交、推送、创建 PR

### 4.1 查看状态 → 暂存 → 提交

```cmd
git status
git add .
git status
```

确认所有文件变绿，且 `.env.local` **不在列表中**（因为被 `.gitignore` 排除了）。

```cmd
git commit -m "feat: add Next.js 14 web scaffold with sidebar navigation, auth pages, item grid, and API client"
```

### 4.2 推送到 GitHub

```cmd
git push -u origin feature/frontend-core
```

### 4.3 创建 PR

1. 浏览器访问：**https://github.com/LuoX11a/SG_CampusSwap**
2. 点击 **"Compare & pull request"**
3. `base: develop` ← `compare: feature/frontend-core`

**标题**：
```
feat: add Next.js 14 web scaffold with sidebar navigation, auth pages, item grid, and API client
```

**描述**：
```markdown
## Description
上传 Next.js 14 前端核心架构代码，包括：
- 项目配置（Next.js / TypeScript / Tailwind / PostCSS）
- 应用入口（layout + homepage）
- 6 个路由页面（Browse, Item Detail, Sell, Login, Register, Verify Email）
- 5 个共享组件（Sidebar, ItemCard, SearchBar, CategoryChips, SkeletonCard）
- API 客户端（axios + JWT 拦截器 + Next.js 代理）
- TypeScript 类型定义（11 个 interface）
- 4 个 Zustand Store（auth, items, filter, chat）
- 格式化工具函数

## Files Changed

### Config（5 files）
- `web/package.json` — 依赖声明
- `web/next.config.js` — Next.js 配置（含 API 代理）
- `web/tsconfig.json` — TypeScript 配置
- `web/tailwind.config.ts` — Tailwind CSS 配置
- `web/postcss.config.js` — PostCSS 配置

### App Core（3 files）
- `web/src/app/globals.css` — 全局样式
- `web/src/app/layout.tsx` — 根布局（Sidebar + 内容区）
- `web/src/app/page.tsx` — 首页

### Route Pages（6 files）
- `web/src/app/browse/page.tsx` — 商品浏览页
- `web/src/app/item/[id]/page.tsx` — 商品详情页
- `web/src/app/sell/page.tsx` — 发布商品页
- `web/src/app/(auth)/login/page.tsx` — 登录页
- `web/src/app/(auth)/register/page.tsx` — 注册页
- `web/src/app/(auth)/verify-email/page.tsx` — 邮箱验证页

### Components（5 files）
- `web/src/components/Sidebar.tsx` — 侧边导航栏
- `web/src/components/ItemCard.tsx` — 商品卡片
- `web/src/components/SearchBar.tsx` — 搜索栏
- `web/src/components/CategoryChips.tsx` — 分类筛选
- `web/src/components/SkeletonCard.tsx` — 加载骨架屏

### Lib + Stores（7 files）
- `web/src/lib/api-client.ts` — Axios 实例 + JWT 拦截器
- `web/src/lib/types.ts` — TypeScript 类型（User, Item, Review 等 11 个 interface）
- `web/src/lib/format.ts` — 价格/日期格式化
- `web/src/stores/auth-store.ts` — 认证状态（Zustand + 持久化）
- `web/src/stores/item-store.ts` — 商品列表状态
- `web/src/stores/filter-store.ts` — 筛选条件状态
- `web/src/stores/chat-store.ts` — 聊天状态

### Docs（2 files）
- `docs/week7/Renxian Tang/frontend-lead-deliverables-w7.md` — W7 交付文档
- `docs/week8/Renxian Tang/frontend-lead-w8-summary.md` — W8 总结文档

### Other
- `web/.env.example` — 环境变量模板

## Checklist
- [x] 代码已在本地测试通过（16 个页面全部 200）
- [x] 遵循 Conventional Commits
- [x] 无 merge conflict
- [x] `.env.local` 已通过 `.gitignore` 排除
- [x] 依赖 Bowei + Wang Xu 的后端 API 结构已就位

## Reviewer
@JiahaiXiong — 请 Review 前端代码
@Bowei — 请 Review 架构
```

### 4.4 设置 Reviewer

- **Jiahai**（前端开发者，主要 Reviewer）
- **Bowei**（Backend Lead，架构审查）

### 4.5 点击 **"Create pull request"**

---

## Step 5：等待 Review 并合并

1. 把 PR 链接发到团队群
2. Jiahai 是主要 Reviewer，Bowei 做架构审查
3. 如果有人提修改意见，本地修改后 `git add .` → `git commit -m "fix: address review feedback"` → `git push`
4. 获得足够 Approve 后，点击 **"Merge pull request"** → **"Confirm merge"**
5. 合并后更新本地：

```cmd
git checkout develop
git pull origin develop
```

---

## ⚠️ 特别注意

### 关于 `.env.local`
- ✅ `web\.env.example` — 提交到 Git，里面是示例值
- ❌ `web\.env.local` — **绝对不能提交**，里面有真实的 API 密钥
- 每次 `git add .` 之后，用 `git status` 确认 `.env.local` 不在暂存区

### 关于包含括号的文件夹名
`(auth)` 文件夹在 PowerShell 里需要特殊处理。如果你用 PowerShell：
```powershell
mkdir "web\src\app\(auth)\login"
```
或者在文件资源管理器里手动创建这些文件夹。

**建议直接用命令提示符（cmd.exe）操作**，括号不会有问题。

---

## ❓ 常见问题

### Q1: push 时弹密码框
用 Personal Access Token 代替密码：
1. 打开 https://github.com/settings/tokens
2. "Generate new token (classic)" → 勾选 `repo` + `workflow`
3. 复制 token，在密码框粘贴

### Q2: `git commit` 报 `nothing to commit`
先用 `git status` 确认文件已复制到正确位置。如果文件是红色（未追踪），执行 `git add .`

### Q3: 复制时提示"系统找不到指定的路径"
确认源文件夹 `C:\Users\92183\Desktop\week8\Renxian Tang\` 存在。你的文件在 Renxian（你自己）的电脑上，这些源路径应该都正确。

### Q4: PR 有 merge conflict
```cmd
git checkout feature/frontend-core
git fetch origin
git merge origin/develop
# 手动解决冲突 → 搜索 <<<<<<< 和 >>>>>>>
git add .
git commit -m "fix: resolve merge conflicts"
git push
```
