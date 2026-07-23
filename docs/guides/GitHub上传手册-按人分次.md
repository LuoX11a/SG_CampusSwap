# SG CampusSwap — GitHub 上传手册

> 每个人有 3 次上传，对应 3 个文件夹：1-5 → week7 → week8（必须按顺序）
> 文件夹位置：`C:\Users\92183\Desktop\1-5` / `week7` / `week8`
> GitHub 仓库：`LuoX11a/SG_CampusSwap`

---

## ⚠️ 核心规则

```
每个人的 1-5 上传完成后 → 才能上传 week7
每个人的 week7 上传完成后 → 才能上传 week8

Bowei 的 1-5 必须先上传（后端基础代码）→ 其他人才能上传依赖后端的部分
```

---

# 一、Bowei（Backend Lead）的 3 次上传

---

## Bowei 第 1 次：上传 1-5 文件夹（后端基础）

**来源文件夹**：`Desktop\1-5\Wang Bowei\`
**PR 分支名**：`feature/bowei-w1to5-backend-scaffold`

```
要复制的文件：

Desktop\1-5\Wang Bowei\.github\workflows\deploy.yml    → .github\workflows\deploy.yml
Desktop\1-5\Wang Bowei\backend\requirements.txt         → backend\requirements.txt
Desktop\1-5\Wang Bowei\backend\app\config.py             → backend\app\config.py
Desktop\1-5\Wang Bowei\backend\app\database.py           → backend\app\database.py
Desktop\1-5\Wang Bowei\backend\app\main.py               → backend\app\main.py
Desktop\1-5\Wang Bowei\backend\app\models\user.py        → backend\app\models\user.py
Desktop\1-5\Wang Bowei\backend\app\models\item.py        → backend\app\models\item.py
Desktop\1-5\Wang Bowei\backend\app\models\review.py      → backend\app\models\review.py
Desktop\1-5\Wang Bowei\backend\app\schemas\user.py       → backend\app\schemas\user.py
Desktop\1-5\Wang Bowei\backend\app\schemas\item.py       → backend\app\schemas\item.py
Desktop\1-5\Wang Bowei\backend\app\schemas\review.py     → backend\app\schemas\review.py
Desktop\1-5\Wang Bowei\backend\app\services\auth_service.py → backend\app\services\auth_service.py
```

**额外操作**：
- 创建 `backend\app\__init__.py`（空文件）
- 创建 `backend\app\models\__init__.py`（导入所有模型）
- 创建 `backend\app\schemas\__init__.py`（空文件）
- 创建 `backend\app\services\__init__.py`（空文件）
- 创建 `backend\app\utils\__init__.py`（空文件）
- 创建 `backend\app\api\__init__.py`（空文件）
- 创建 `backend\app\api\v1\__init__.py`（空文件）
- 创建项目根目录 `.gitignore`

**Commit 信息**：`feat: add FastAPI backend scaffold — models, schemas, auth service, CI/CD`

**完成后**：Push → 创建 PR → 等 Review → 合并到 `develop`

---

## Bowei 第 2 次：上传 week7 文件夹（后端 W7 文档）

**来源文件夹**：`Desktop\week7\Wang Bowei\`
**PR 分支名**：`feature/bowei-week7-docs`

```
要复制的文件：

Desktop\week7\Wang Bowei\backend-lead-deliverables-w7.md → docs\week7\Wang Bowei\backend-lead-deliverables-w7.md
```

**额外操作**：无（纯文档，1 个文件）

**Commit 信息**：`docs: add backend lead week 7 deliverables summary`

---

## Bowei 第 3 次：上传 week8 文件夹（后端 W8 API 路由）

**来源文件夹**：`Desktop\week8\Wang Bowei\`
**PR 分支名**：`feature/bowei-week8-auth-and-deploy`

```
要复制的文件：

Desktop\week8\Wang Bowei\backend\app\api\v1\__init__.py  → backend\app\api\v1\__init__.py
Desktop\week8\Wang Bowei\backend\app\api\v1\auth.py       → backend\app\api\v1\auth.py
Desktop\week8\Wang Bowei\backend\Dockerfile               → backend\Dockerfile
Desktop\week8\Wang Bowei\backend\.env.example             → backend\.env.example
Desktop\week8\Wang Bowei\docker-compose.yml               → docker-compose.yml
Desktop\week8\Wang Bowei\backend-lead-w8-summary.md       → docs\week8\Wang Bowei\backend-lead-w8-summary.md
```

**额外操作**：
- 更新 `backend\app\main.py`，把 `api_router` 注册进去（如果之前没写）

**Commit 信息**：`feat: add Auth API routes, Docker config, and API router registry`

---

# 二、Wang Xu（Backend Dev）的 3 次上传

---

## Wang Xu 第 1 次：上传 1-5 文件夹（⚠️ 1-5 没有 Wang Xu 的代码，只有文档）

**来源文件夹**：`Desktop\1-5\Wang Xu\`
**PR 分支名**：`feature/wangxu-week7-docs`

> 注意：1-5 和 week7 的 Wang Xu 内容都是文档，没有代码。
> 可以合并成一次上传，但仍算 week7 的内容。

```
要复制的文件：

Desktop\week7\Wang Xu\backend-dev-deliverables-w7.md → docs\week7\Wang Xu\backend-dev-deliverables-w7.md
```

**额外操作**：无

**Commit 信息**：`docs: add backend developer week 7 deliverables`

---

## Wang Xu 第 2 次：上传 week7 文件夹（同第 1 次，week7 就是这份文档）

> Wang Xu 的 1-5 文件夹和 week7 文件夹内容相同（都是 `backend-dev-deliverables-w7.md`），合并处理即可。

---

## Wang Xu 第 3 次：上传 week8 文件夹（后端 W8 API 路由 + Service）

**来源文件夹**：`Desktop\week8\Wang Xu\`
**前置条件**：Bowei 的第 1 次上传已完成（models/schemas 已合入 develop）
**PR 分支名**：`feature/wangxu-week8-api-routes`

```
要复制的文件：

Desktop\week8\Wang Xu\backend\app\api\v1\items.py         → backend\app\api\v1\items.py
Desktop\week8\Wang Xu\backend\app\api\v1\search.py        → backend\app\api\v1\search.py
Desktop\week8\Wang Xu\backend\app\api\v1\users.py         → backend\app\api\v1\users.py
Desktop\week8\Wang Xu\backend\app\api\v1\upload.py        → backend\app\api\v1\upload.py
Desktop\week8\Wang Xu\backend\app\api\v1\reviews.py       → backend\app\api\v1\reviews.py
Desktop\week8\Wang Xu\backend\app\services\item_service.py    → backend\app\services\item_service.py
Desktop\week8\Wang Xu\backend\app\services\upload_service.py  → backend\app\services\upload_service.py
Desktop\week8\Wang Xu\backend\app\services\chat_service.py    → backend\app\services\chat_service.py
Desktop\week8\Wang Xu\backend-dev-w8-summary.md            → docs\week8\Wang Xu\backend-dev-w8-summary.md
```

**额外操作**：无

**Commit 信息**：`feat: add Item CRUD, Search, Upload, Users, Reviews API routes and services`

---

# 三、Renxian（Frontend Lead）的 3 次上传

---

## Renxian 第 1 次：上传 1-5 文件夹（前端 W7 设计文档）

**来源文件夹**：`Desktop\1-5\Renxian Tang\`
**PR 分支名**：`feature/renxian-week7-docs`

```
要复制的文件：

Desktop\1-5\Renxian Tang\frontend-lead-deliverables-w7.md → docs\week7\Renxian Tang\frontend-lead-deliverables-w7.md
```

**额外操作**：无

**Commit 信息**：`docs: add frontend lead week 7 deliverables`

---

## Renxian 第 2 次：上传 week7 文件夹（同 1-5，合并处理）

> Renxian 的 week7 和 1-5 文件夹内容相同，已在第 1 次上传中处理。

---

## Renxian 第 3 次：上传 week8 文件夹（前端 Web 项目核心）

**来源文件夹**：`Desktop\week8\Renxian Tang\`
**前置条件**：Bowei 第 1+3 次 + Wang Xu 第 3 次已完成（后端 API 结构已确定）
**PR 分支名**：`feature/renxian-week8-frontend-core`

```
要复制的文件：

# 项目配置 (6 个)
Desktop\week8\Renxian Tang\web\package.json           → web\package.json
Desktop\week8\Renxian Tang\web\next.config.js          → web\next.config.js
Desktop\week8\Renxian Tang\web\tsconfig.json           → web\tsconfig.json
Desktop\week8\Renxian Tang\web\tailwind.config.ts      → web\tailwind.config.ts
Desktop\week8\Renxian Tang\web\postcss.config.js       → web\postcss.config.js

# 核心布局 (2 个)
Desktop\week8\Renxian Tang\web\src\app\globals.css     → web\src\app\globals.css
Desktop\week8\Renxian Tang\web\src\app\layout.tsx      → web\src\app\layout.tsx

# 页面 — 主页 (1 个)
Desktop\week8\Renxian Tang\web\src\app\page.tsx        → web\src\app\page.tsx

# 页面 — Auth (3 个)
Desktop\week8\Renxian Tang\web\src\app\(auth)\login\page.tsx         → web\src\app\(auth)\login\page.tsx
Desktop\week8\Renxian Tang\web\src\app\(auth)\register\page.tsx      → web\src\app\(auth)\register\page.tsx
Desktop\week8\Renxian Tang\web\src\app\(auth)\verify-email\page.tsx  → web\src\app\(auth)\verify-email\page.tsx

# 页面 — 功能页 (3 个)
Desktop\week8\Renxian Tang\web\src\app\browse\page.tsx     → web\src\app\browse\page.tsx
Desktop\week8\Renxian Tang\web\src\app\item\[id]\page.tsx  → web\src\app\item\[id]\page.tsx
Desktop\week8\Renxian Tang\web\src\app\sell\page.tsx       → web\src\app\sell\page.tsx

# 核心组件 (5 个)
Desktop\week8\Renxian Tang\web\src\components\Sidebar.tsx       → web\src\components\Sidebar.tsx
Desktop\week8\Renxian Tang\web\src\components\ItemCard.tsx      → web\src\components\ItemCard.tsx
Desktop\week8\Renxian Tang\web\src\components\SearchBar.tsx     → web\src\components\SearchBar.tsx
Desktop\week8\Renxian Tang\web\src\components\CategoryChips.tsx → web\src\components\CategoryChips.tsx
Desktop\week8\Renxian Tang\web\src\components\SkeletonCard.tsx  → web\src\components\SkeletonCard.tsx

# 工具库 (3 个)
Desktop\week8\Renxian Tang\web\src\lib\api-client.ts     → web\src\lib\api-client.ts
Desktop\week8\Renxian Tang\web\src\lib\types.ts          → web\src\lib\types.ts
Desktop\week8\Renxian Tang\web\src\lib\format.ts         → web\src\lib\format.ts

# 状态管理 (4 个)
Desktop\week8\Renxian Tang\web\src\stores\auth-store.ts   → web\src\stores\auth-store.ts
Desktop\week8\Renxian Tang\web\src\stores\item-store.ts   → web\src\stores\item-store.ts
Desktop\week8\Renxian Tang\web\src\stores\filter-store.ts  → web\src\stores\filter-store.ts
Desktop\week8\Renxian Tang\web\src\stores\chat-store.ts    → web\src\stores\chat-store.ts

# W8 总结文档 (1 个)
Desktop\week8\Renxian Tang\frontend-lead-w8-summary.md   → docs\week8\Renxian Tang\frontend-lead-w8-summary.md
```

**额外操作**：
- 创建 `web\.env.example`：`NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1`
- 确保 `.gitignore` 排除 `node_modules/`、`.next/`、`.env.local`

**Commit 信息**：`feat: add Next.js 14 web scaffold with sidebar, auth, item grid, and API client`

---

# 四、Jiahai（Frontend Dev）的 3 次上传

---

## Jiahai 第 1 次：上传 1-5 文件夹（前端 W7 设计文档）

**来源文件夹**：`Desktop\1-5\Jiahai Xiong\`
**PR 分支名**：`feature/jiahai-week7-docs`

```
要复制的文件：

Desktop\1-5\Jiahai Xiong\frontend-dev-deliverables-w7.md → docs\week7\Jiahai Xiong\frontend-dev-deliverables-w7.md
```

**额外操作**：无

**Commit 信息**：`docs: add frontend developer week 7 deliverables`

---

## Jiahai 第 2 次：上传 week7 文件夹（同 1-5，合并处理）

---

## Jiahai 第 3 次：上传 week8 文件夹（前端扩展页面）

**来源文件夹**：`Desktop\week8\Jiahai Xiong\`
**前置条件**：Renxian 第 3 次上传已完成（Next.js 脚手架 + 组件 + stores 已合入）
**PR 分支名**：`feature/jiahai-week8-pages`

```
要复制的文件：

# 聊天 (2 个)
Desktop\week8\Jiahai Xiong\web\src\app\messages\page.tsx       → web\src\app\messages\page.tsx
Desktop\week8\Jiahai Xiong\web\src\app\messages\[id]\page.tsx  → web\src\app\messages\[id]\page.tsx

# 个人中心 (3 个)
Desktop\week8\Jiahai Xiong\web\src\app\profile\page.tsx        → web\src\app\profile\page.tsx
Desktop\week8\Jiahai Xiong\web\src\app\profile\edit\page.tsx   → web\src\app\profile\edit\page.tsx
Desktop\week8\Jiahai Xiong\web\src\app\profile\[id]\page.tsx   → web\src\app\profile\[id]\page.tsx

# 设置/评价/我的商品 (3 个)
Desktop\week8\Jiahai Xiong\web\src\app\settings\page.tsx       → web\src\app\settings\page.tsx
Desktop\week8\Jiahai Xiong\web\src\app\reviews\page.tsx        → web\src\app\reviews\page.tsx
Desktop\week8\Jiahai Xiong\web\src\app\my-listings\page.tsx    → web\src\app\my-listings\page.tsx

# 筛选组件 (1 个)
Desktop\week8\Jiahai Xiong\web\src\components\FilterModal.tsx  → web\src\components\FilterModal.tsx

# W8 总结文档 (1 个)
Desktop\week8\Jiahai Xiong\frontend-dev-w8-summary.md → docs\week8\Jiahai Xiong\frontend-dev-w8-summary.md
```

**额外操作**：无

**Commit 信息**：`feat: add Chat, Profile, Settings, Reviews, MyListings pages and FilterModal`

---

# 五、Junliang（UI/UX & QA）的 3 次上传

---

## Junliang 第 1 次：上传 1-5 文件夹（设计规范 + 测试计划 + 文献综述）

**来源文件夹**：`Desktop\1-5\Junliang Li\`
**PR 分支名**：`feature/junliang-week7-design-and-templates`

```
要复制的文件：

Desktop\1-5\Junliang Li\figma-screen-specifications.md          → docs\week7\Junliang Li\figma-screen-specifications.md
Desktop\1-5\Junliang Li\github-labels-taxonomy.md               → docs\week7\Junliang Li\github-labels-taxonomy.md
Desktop\1-5\Junliang Li\literature-review-uux-qa.md             → docs\week7\Junliang Li\literature-review-uux-qa.md
Desktop\1-5\Junliang Li\test-plan-and-cases.md                  → docs\week7\Junliang Li\test-plan-and-cases.md
Desktop\1-5\Junliang Li\usability-testing-recruitment-plan.md   → docs\week7\Junliang Li\usability-testing-recruitment-plan.md
```

**额外操作**：无

**Commit 信息**：`docs: add UI/UX design specs, test plan, literature review, and labels taxonomy`

---

## Junliang 第 2 次：上传 week7 文件夹（GitHub Issue 模板）

**来源文件夹**：`Desktop\week7\Junliang Li\`
**PR 分支名**：`feature/junliang-week7-templates`

```
要复制的文件：

Desktop\week7\Junliang Li\github-templates\bug-report.md      → .github\ISSUE_TEMPLATE\bug-report.md
Desktop\week7\Junliang Li\github-templates\feature-request.md → .github\ISSUE_TEMPLATE\feature-request.md
```

**额外操作**：
- 去 GitHub Issues 网页 → Labels → 按照 `github-labels-taxonomy.md` 中的 28 个标签，一个个手动创建
- 每个 Label 需要：名称、颜色、描述

**Commit 信息**：`docs: add GitHub issue templates for bug report and feature request`

---

## Junliang 第 3 次：上传 week8 文件夹（Web 设计规范 + 更新测试计划）

**来源文件夹**：`Desktop\week8\Junliang Li\`
**PR 分支名**：`feature/junliang-week8-design`

```
要复制的文件：

Desktop\week8\Junliang Li\web-design-specifications.md       → docs\week8\Junliang Li\web-design-specifications.md
Desktop\week8\Junliang Li\component-design-system-web.md     → docs\week8\Junliang Li\component-design-system-web.md
Desktop\week8\Junliang Li\design-tokens-web.json             → docs\week8\Junliang Li\design-tokens-web.json
Desktop\week8\Junliang Li\test-plan-update-w8.md             → docs\week8\Junliang Li\test-plan-update-w8.md
```

**额外操作**：无

**Commit 信息**：`docs: add web design specifications, component system, and updated test plan`

---

# 六、Hongrui（PM）的 3 次上传

---

## Hongrui 第 1 次：上传 1-5 文件夹（PM 全部文档）

**来源文件夹**：`Desktop\1-5\Huang Hongrui\`
**PR 分支名**：`feature/hongrui-week7-pm-docs`

```
要复制的文件：

Desktop\1-5\Huang Hongrui\blockers-issues-log.md                         → docs\week7\Huang Hongrui\blockers-issues-log.md
Desktop\1-5\Huang Hongrui\final-report-framework.md                      → docs\week7\Huang Hongrui\final-report-framework.md
Desktop\1-5\Huang Hongrui\gantt-update-w7.md                             → docs\week7\Huang Hongrui\gantt-update-w7.md
Desktop\1-5\Huang Hongrui\risk-register.md                               → docs\week7\Huang Hongrui\risk-register.md
Desktop\1-5\Huang Hongrui\sprint-backlog.md                              → docs\week7\Huang Hongrui\sprint-backlog.md
Desktop\1-5\Huang Hongrui\week7-meeting-agenda.md                        → docs\week7\Huang Hongrui\week7-meeting-agenda.md
Desktop\1-5\Huang Hongrui\meeting-minutes\phase1-progress-summary-w1-w5.md → docs\week7\Huang Hongrui\meeting-minutes\phase1-progress-summary-w1-w5.md
Desktop\1-5\Huang Hongrui\meeting-minutes\weekly-meetings-w1-w5.md       → docs\week7\Huang Hongrui\meeting-minutes\weekly-meetings-w1-w5.md
```

**额外操作**：无

**Commit 信息**：`docs: add PM documents — sprint backlog, risk register, meeting minutes, gantt`

---

## Hongrui 第 2 次：上传 week7 文件夹（同 1-5，合并处理）

> Hongrui 的 week7 内容已在 Desktop\1-5 中全部覆盖。第 2 次上传可以跳过，或补传遗漏文件。

---

## Hongrui 第 3 次：上传 week8 文件夹（W8 PM 更新文档）

**来源文件夹**：`Desktop\week8\Huang Hongrui\`
**PR 分支名**：`feature/hongrui-week8-pm-update`

```
要复制的文件：

Desktop\week8\Huang Hongrui\sprint-backlog-w8-update.md   → docs\week8\Huang Hongrui\sprint-backlog-w8-update.md
Desktop\week8\Huang Hongrui\week8-meeting-agenda.md       → docs\week8\Huang Hongrui\week8-meeting-agenda.md
Desktop\week8\Huang Hongrui\week8-progress-report.md      → docs\week8\Huang Hongrui\week8-progress-report.md
Desktop\week8\Huang Hongrui\risk-register-w8-update.md    → docs\week8\Huang Hongrui\risk-register-w8-update.md
```

**额外操作**：无

**Commit 信息**：`docs: add week 8 PM update — sprint backlog, meeting agenda, progress report, risk register`

---

# 七、完整时间轴

```
         第 1 轮                   第 2 轮                  第 3 轮
      (上传 1-5)              (上传 week7)             (上传 week8)
  ────────────────────    ────────────────────    ────────────────────

  Bowei                    Bowei                   Bowei
  │ 上传后端基础代码       │ 上传W7总结文档        │ 上传Auth+Docker
  │ (models/schemas/       │ (1个文档)             │ (5个文件+文档)
  │  services/CI/CD)       │                       │
  │ 12个文件               │  额外：无              │  额外：更新main.py
  ▼                        ▼                       ▼
  
  Wang Xu                  Wang Xu                 Wang Xu
  │ (1-5无代码，跳过)      │ 上传W7文档            │ 上传API路由+Service
  │                        │ (1个文档)             │ (9个文件)
  │                        │                       │
  │                        │  额外：无              │  额外：无
  ▼                        ▼                       ▼
  
  Renxian                  Renxian                 Renxian
  │ 上传W7设计文档         │ (同1-5，合并)          │ 上传前端核心项目
  │ (1个文档)              │                       │ (28个文件)
  │                        │                       │
  │  额外：无               │                       │  额外：创建.env.example
  ▼                        ▼                       ▼
  
  Jiahai                   Jiahai                  Jiahai
  │ 上传W7设计文档         │ (同1-5，合并)          │ 上传前端扩展页面
  │ (1个文档)              │                       │ (10个文件)
  │                        │                       │
  │  额外：无               │                       │  额外：无
  ▼                        ▼                       ▼
  
  Junliang                 Junliang                Junliang
  │ 上传设计+测试+文献     │ 上传Issue模板         │ 上传Web设计规范
  │ (5个文档)              │ (2个模板)             │ (4个文档)
  │                        │                       │
  │  额外：无               │  额外：GitHub网页      │  额外：无
  │                        │  手动创建28个Labels    │
  ▼                        ▼                       ▼
  
  Hongrui                  Hongrui                 Hongrui
  │ 上传全部PM文档         │ (同1-5，合并)          │ 上传W8 PM更新
  │ (8个文档)              │                       │ (4个文档)
  │                        │                       │
  │  额外：无               │                       │  额外：无
  ▼                        ▼                       ▼
```

## 八、依赖关系简图

```
第 1 轮（1-5）：
  Bowei ═══ 必须先做（后端基础代码）
  其他人 ── 可并行（都是纯文档）

第 2 轮（week7）：
  所有人 ── 可并行（都是纯文档）
  Junliang ── 额外步骤：GitHub 手动创建 Labels

第 3 轮（week8）：
  Bowei ═══ 先做（Auth API + Docker）
          ↓
  Wang Xu ── 依赖 Bowei（API 路由引用 models）
          ↓
  Renxian ── 依赖 Bowei+Wang Xu（API Client 需要知道 API 结构）
          ↓
  Jiahai  ── 依赖 Renxian（页面引用 components + stores）
  
  Junliang ── 独立（设计文档）
  Hongrui  ── 独立（PM 文档）
```

## 九、操作清单（每人每轮 Check List）

```
第 1 轮操作清单：
□ git checkout develop && git pull
□ git checkout -b feature/[名字]-w1to5-[描述]
□ 复制文件到对应位置
□ git add .
□ git commit -m "feat/docs: ..."
□ git push -u origin feature/[名字]-w1to5-[描述]
□ 在 GitHub 创建 PR → develop
□ 等待 Review → Merge

第 2 轮操作清单：
□ git checkout develop && git pull （拉取最新合并）
□ git checkout -b feature/[名字]-week7-[描述]
□ 复制文件
□ git add . && git commit && git push
□ 创建 PR → 等待 Review → Merge

第 3 轮操作清单：
□ git checkout develop && git pull
□ git checkout -b feature/[名字]-week8-[描述]
□ 复制文件
□ git add . && git commit && git push
□ 创建 PR → 等待 Review → Merge
```
