# SG CampusSwap — GitHub 上传时间轴与操作手册

> 当前状态：GitHub 仅有 `master` 分支 + README.md
> 目标：按依赖顺序上传 1-5、week7、week8 三个文件夹，建立完整协作流
> 分支策略：`master` ← `develop` ← `feature/xxx`

---

## 一、上传依赖关系

```
Bowei (Backend Lead)
  ├── 必须先上：后端基础代码 (models/schemas/services/config)
  │      ↓ 依赖
  ├── Wang Xu (Backend Dev)：API 路由依赖 Bowei 的 models
  │      ↓ 参考
  ├── Renxian (Frontend Lead)：API Client 依赖后端 API 结构
  │      ↓ 依赖
  └── Jiahai (Frontend Dev)：页面组件依赖 Renxian 的 scaffold

Junliang (UI/UX & QA) ──→ 独立，但 GitHub Labels 应尽早
Hongrui (PM)         ──→ 完全独立
```

---

## 二、分阶段详细操作

---

### 🚀 阶段 0：Bowei 创建 develop 分支（所有人等待）

**执行者**：Wang Bowei  
**时间**：Day 1 上午（所有人都等这一步）  
**作用**：建立基础分支架构，所有后续工作从 `develop` 拉分支

```bash
# 1. 克隆仓库
git clone https://github.com/LuoX11a/SG_CampusSwap.git
cd SG_CampusSwap

# 2. 创建 develop 分支并推送
git checkout -b develop
git push -u origin develop

# 3. 在 GitHub 上设置分支保护：
#    Settings → Branches → Add rule
#    - master: 禁止直接推送，必须通过 PR
#    - develop: 禁止直接推送，必须通过 PR
```

**上传文件**：无（纯操作）

**产出**：`develop` 分支存在，团队可以开始工作

---

### 🚀 阶段 1：Bowei 上传后端基础（Day 1 下午）

**执行者**：Wang Bowei  
**分支**：`feature/backend-scaffold`（从 `develop` 拉出）

**操作步骤**：

```bash
git checkout develop
git pull origin develop
git checkout -b feature/backend-scaffold
```

**上传的文件夹内容**：

```
📁 从 Desktop\1-5\Wang Bowei\ 复制：
  .github\workflows\deploy.yml          → .github\workflows\deploy.yml
  backend\app\config.py                 → backend\app\config.py
  backend\app\database.py               → backend\app\database.py
  backend\app\main.py                   → backend\app\main.py
  backend\app\models\user.py            → backend\app\models\user.py
  backend\app\models\item.py            → backend\app\models\item.py
  backend\app\models\review.py          → backend\app\models\review.py
  backend\app\schemas\user.py           → backend\app\schemas\user.py
  backend\app\schemas\item.py           → backend\app\schemas\item.py
  backend\app\schemas\review.py         → backend\app\schemas\review.py
  backend\app\services\auth_service.py  → backend\app\services\auth_service.py
  backend\requirements.txt              → backend\requirements.txt

📁 从 Desktop\week7\Wang Bowei\ 复制：
  backend-lead-deliverables-w7.md       → docs\week7\Wang Bowei\backend-lead-deliverables-w7.md

📁 从 Desktop\week8\Wang Bowei\ 复制：
  backend\app\api\v1\__init__.py        → backend\app\api\v1\__init__.py
  backend\app\api\v1\auth.py            → backend\app\api\v1\auth.py
  backend\Dockerfile                    → backend\Dockerfile
  backend\.env.example                  → backend\.env.example
  backend-lead-w8-summary.md            → docs\week8\Wang Bowei\backend-lead-w8-summary.md
  docker-compose.yml                    → docker-compose.yml
```

**同时还要做的事**：
- [ ] 在 `backend/` 下创建所有缺失的 `__init__.py`
- [ ] 创建 `backend\app\models\__init__.py`（导出所有模型）
- [ ] 验证 `python -c "from app.main import app"` 不报错
- [ ] 添加 `.gitignore`（Python/Node/IDE/OS/.env）
- [ ] 提交时写 Conventional Commit：`feat: add FastAPI backend scaffold with auth and 22 API endpoints`
- [ ] Push → 创建 PR → `feature/backend-scaffold` → `develop`
- [ ] **等待至少 1 人 Review 通过后合并**

---

### 🚀 阶段 2：Wang Xu 上传后端 API + Junliang 上传模板（Day 2）

**两件事可并行**

---

#### 2a. Wang Xu — 上传后端 API 路由

**执行者**：Wang Xu  
**分支**：`feature/backend-api-routes`（从最新的 `develop` 拉出）

**前置依赖**：阶段 1 完成（Bowei 的 models 已合入 develop）

```bash
git checkout develop
git pull origin develop
git checkout -b feature/backend-api-routes
```

**上传的文件**：

```
📁 从 Desktop\week7\Wang Xu\ 复制：
  backend-dev-deliverables-w7.md     → docs\week7\Wang Xu\backend-dev-deliverables-w7.md

📁 从 Desktop\week8\Wang Xu\ 复制：
  backend\app\api\v1\items.py        → backend\app\api\v1\items.py
  backend\app\api\v1\search.py       → backend\app\api\v1\search.py
  backend\app\api\v1\users.py        → backend\app\api\v1\users.py
  backend\app\api\v1\upload.py       → backend\app\api\v1\upload.py
  backend\app\api\v1\reviews.py      → backend\app\api\v1\reviews.py
  backend\app\services\item_service.py   → backend\app\services\item_service.py
  backend\app\services\upload_service.py → backend\app\services\upload_service.py
  backend\app\services\chat_service.py   → backend\app\services\chat_service.py
```

**同时还要做的事**：
- [ ] 创建 `backend\app\services\__init__.py`
- [ ] 创建 `backend\app\utils\__init__.py`（如不存在）
- [ ] 验证新增的 18 个 API 端点可正常导入
- [ ] 提交：`feat: add Item CRUD, Search, Upload, Users, and Reviews API routes`
- [ ] Push → 创建 PR → `feature/backend-api-routes` → `develop`
- [ ] **等待 Bowei Review 通过后合并**

---

#### 2b. Junliang — 上传 GitHub 模板和设计文档

**执行者**：Junliang Li  
**分支**：`feature/github-templates-and-design`（从 `develop` 拉出）

**无前置依赖**（模板和设计文档独立）

```bash
git checkout develop
git pull origin develop
git checkout -b feature/github-templates-and-design
```

**上传的文件**：

```
📁 从 Desktop\1-5\Junliang Li\ 复制：
  figma-screen-specifications.md         → docs\week7\Junliang Li\figma-screen-specifications.md
  github-labels-taxonomy.md              → docs\week7\Junliang Li\github-labels-taxonomy.md
  literature-review-uux-qa.md            → docs\week7\Junliang Li\literature-review-uux-qa.md
  test-plan-and-cases.md                 → docs\week7\Junliang Li\test-plan-and-cases.md
  usability-testing-recruitment-plan.md  → docs\week7\Junliang Li\usability-testing-recruitment-plan.md

📁 从 Desktop\week7\Junliang Li\ 复制：
  github-templates\bug-report.md         → .github\ISSUE_TEMPLATE\bug-report.md
  github-templates\feature-request.md    → .github\ISSUE_TEMPLATE\feature-request.md

📁 从 Desktop\week8\Junliang Li\ 复制：
  web-design-specifications.md           → docs\week8\Junliang Li\web-design-specifications.md
  component-design-system-web.md         → docs\week8\Junliang Li\component-design-system-web.md
  design-tokens-web.json                 → docs\week8\Junliang Li\design-tokens-web.json
  test-plan-update-w8.md                 → docs\week8\Junliang Li\test-plan-update-w8.md
```

**同时还要做的事**：
- [ ] 在 GitHub Issues 网页 → Labels → 根据 `github-labels-taxonomy.md` 手动创建 28 个标签
- [ ] 提交：`docs: add GitHub issue templates, labels taxonomy, and design specifications`
- [ ] Push → 创建 PR → `feature/github-templates-and-design` → `develop`
- [ ] **任何人可 Review**

---

### 🚀 阶段 3：Renxian 上传前端核心 (Day 3)

**执行者**：Renxian Tang  
**分支**：`feature/frontend-core`（从最新 `develop` 拉出）

**前置依赖**：阶段 1+2 完成（后端 API 结构已确定，可以据此写 API Client）

```bash
git checkout develop
git pull origin develop
git checkout -b feature/frontend-core
```

**上传的文件**：

```
📁 从 Desktop\week7\Renxian Tang\ 复制：
  frontend-lead-deliverables-w7.md   → docs\week7\Renxian Tang\frontend-lead-deliverables-w7.md

📁 从 Desktop\week8\Renxian Tang\ 复制：
  web\package.json                   → web\package.json
  web\next.config.js                 → web\next.config.js
  web\tsconfig.json                  → web\tsconfig.json
  web\tailwind.config.ts             → web\tailwind.config.ts
  web\postcss.config.js              → web\postcss.config.js
  web\src\app\globals.css            → web\src\app\globals.css
  web\src\app\layout.tsx             → web\src\app\layout.tsx
  web\src\app\page.tsx               → web\src\app\page.tsx
  web\src\app\browse\page.tsx        → web\src\app\browse\page.tsx
  web\src\app\item\[id]\page.tsx     → web\src\app\item\[id]\page.tsx
  web\src\app\sell\page.tsx          → web\src\app\sell\page.tsx
  web\src\app\(auth)\login\page.tsx        → web\src\app\(auth)\login\page.tsx
  web\src\app\(auth)\register\page.tsx     → web\src\app\(auth)\register\page.tsx
  web\src\app\(auth)\verify-email\page.tsx → web\src\app\(auth)\verify-email\page.tsx
  web\src\components\Sidebar.tsx     → web\src\components\Sidebar.tsx
  web\src\components\ItemCard.tsx    → web\src\components\ItemCard.tsx
  web\src\components\SearchBar.tsx   → web\src\components\SearchBar.tsx
  web\src\components\CategoryChips.tsx → web\src\components\CategoryChips.tsx
  web\src\components\SkeletonCard.tsx→ web\src\components\SkeletonCard.tsx
  web\src\lib\api-client.ts          → web\src\lib\api-client.ts
  web\src\lib\types.ts               → web\src\lib\types.ts
  web\src\lib\format.ts              → web\src\lib\format.ts
  web\src\stores\auth-store.ts       → web\src\stores\auth-store.ts
  web\src\stores\item-store.ts       → web\src\stores\item-store.ts
  web\src\stores\filter-store.ts     → web\src\stores\filter-store.ts
  web\src\stores\chat-store.ts       → web\src\stores\chat-store.ts
  web\.env.local                     → web\.env.local           (手动创建，不提交)
  frontend-lead-w8-summary.md        → docs\week8\Renxian Tang\frontend-lead-w8-summary.md
```

**同时还要做的事**：
- [ ] 确保 `web\.env.local` 被 `.gitignore` 排除（只上传 `.env.example`）
- [ ] 创建 `web\.env.example`：`NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1`
- [ ] 提交：`feat: add Next.js 14 web scaffold with sidebar navigation, auth pages, item grid, and API client`
- [ ] Push → 创建 PR → `feature/frontend-core` → `develop`
- [ ] **等待 Jiahai + 1 人 Review**

---

### 🚀 阶段 4：Jiahai 上传前端页面 + Hongrui 上传 PM 文档 (Day 4)

**两件事可并行**

---

#### 4a. Jiahai — 上传前端扩展页面

**执行者**：Jiahai Xiong  
**分支**：`feature/frontend-pages`（从最新 `develop` 拉出）

**前置依赖**：阶段 3 完成（依赖 Renxian 的组件和 stores）

```bash
git checkout develop
git pull origin develop
git checkout -b feature/frontend-pages
```

**上传的文件**：

```
📁 从 Desktop\week7\Jiahai Xiong\ 复制：
  frontend-dev-deliverables-w7.md   → docs\week7\Jiahai Xiong\frontend-dev-deliverables-w7.md

📁 从 Desktop\week8\Jiahai Xiong\ 复制：
  web\src\app\messages\page.tsx           → web\src\app\messages\page.tsx
  web\src\app\messages\[id]\page.tsx      → web\src\app\messages\[id]\page.tsx
  web\src\app\profile\page.tsx            → web\src\app\profile\page.tsx
  web\src\app\profile\edit\page.tsx       → web\src\app\profile\edit\page.tsx
  web\src\app\profile\[id]\page.tsx       → web\src\app\profile\[id]\page.tsx
  web\src\app\settings\page.tsx           → web\src\app\settings\page.tsx
  web\src\app\reviews\page.tsx            → web\src\app\reviews\page.tsx
  web\src\app\my-listings\page.tsx        → web\src\app\my-listings\page.tsx
  web\src\components\FilterModal.tsx      → web\src\components\FilterModal.tsx
  frontend-dev-w8-summary.md             → docs\week8\Jiahai Xiong\frontend-dev-w8-summary.md
```

**同时还要做的事**：
- [ ] 验证所有页面可以编译：`cd web && npm run build`（或 `npx next build`）
- [ ] 提交：`feat: add Chat, Profile, Settings, Reviews, MyListings pages and FilterModal`
- [ ] Push → 创建 PR → `feature/frontend-pages` → `develop`
- [ ] **等待 Renxian Review 通过后合并**

---

#### 4b. Hongrui — 上传 PM 文档

**执行者**：Huang Hongrui  
**分支**：`feature/pm-docs`（从 `develop` 拉出）

**无前置依赖**

```bash
git checkout develop
git pull origin develop
git checkout -b feature/pm-docs
```

**上传的文件**：

```
📁 从 Desktop\1-5\Huang Hongrui\ 复制（全部到 docs\week7\Huang Hongrui\）：
  blockers-issues-log.md                   → docs\week7\Huang Hongrui\blockers-issues-log.md
  final-report-framework.md                → docs\week7\Huang Hongrui\final-report-framework.md
  gantt-update-w7.md                       → docs\week7\Huang Hongrui\gantt-update-w7.md
  risk-register.md                         → docs\week7\Huang Hongrui\risk-register.md
  sprint-backlog.md                        → docs\week7\Huang Hongrui\sprint-backlog.md
  week7-meeting-agenda.md                  → docs\week7\Huang Hongrui\week7-meeting-agenda.md
  meeting-minutes\phase1-progress-summary-w1-w5.md → docs\week7\Huang Hongrui\meeting-minutes\
  meeting-minutes\weekly-meetings-w1-w5.md → docs\week7\Huang Hongrui\meeting-minutes\

📁 从 Desktop\week8\Huang Hongrui\ 复制（全部到 docs\week8\Huang Hongrui\）：
  sprint-backlog-w8-update.md              → docs\week8\Huang Hongrui\sprint-backlog-w8-update.md
  week8-meeting-agenda.md                  → docs\week8\Huang Hongrui\week8-meeting-agenda.md
  week8-progress-report.md                 → docs\week8\Huang Hongrui\week8-progress-report.md
  risk-register-w8-update.md               → docs\week8\Huang Hongrui\risk-register-w8-update.md
```

**同时还要做的事**：
- [ ] 在 GitHub Projects 中创建 Kanban Board，导入 Sprint Backlog 任务
- [ ] 提交：`docs: add PM documents — sprint backlog, risk register, meeting minutes, progress reports`
- [ ] Push → 创建 PR → `feature/pm-docs` → `develop`
- [ ] **任何人可 Review**

---

### 🚀 阶段 5：收尾 — 更新 README + 最终合并 (Day 5)

**执行者**：Bowei + Hongrui

#### 5a. 更新 README.md

```bash
git checkout -b docs/readme-update
```

在 README 中补充：
- 项目简介
- 技术栈
- 本地运行指南（Backend + Frontend）
- 团队 6 人名单 + 角色
- 分支策略说明

提交：`docs: update README with project overview, tech stack, and setup guide`

#### 5b. 所有分支合并到 develop 后

```bash
git checkout develop
git pull origin develop
# 运行最终验证
cd backend && pytest           # 或手动验证
cd web && npm run build        # 确认前端可编译
```

#### 5c. develop → master 合并

```bash
git checkout master
git merge develop
git tag v1.0.0
git push origin master --tags
```

---

## 三、时间轴可视化

```
         Day 1              Day 2              Day 3              Day 4              Day 5
    ────────────────  ────────────────  ────────────────  ────────────────  ────────────────
    
    Bowei             Bowei (继续)                                             Bowei + Hongrui
    │                 │                                                        │
    ├─ 创建 develop   ├─ 合并 PR ✅                                           ├─ 更新 README
    ├─ 创建分支       │                                                        ├─ 最终验证
    ├─ 上传后端基础   Wang Xu                 Renxian           Jiahai         ├─ develop→master
    ├─ 创建 PR        │                       │                 │              ├─ Tag v1.0.0
    │                 ├─ 创建分支             ├─ 创建分支       ├─ 创建分支    │
    │  所有人等待     ├─ 上传 18 个 API       ├─ 上传 Next.js   ├─ 上传 8 页面  │
    │                 ├─ 创建 PR              ├─ 上传 6 组件    ├─ 创建 PR      │
    │                 │                       ├─ 上传 4 Store   │               │
    │                 Junliang               ├─ 创建 PR        Hongrui         │
    │                 │                       │                 │               │
    │                 ├─ 创建分支             │  等待 Review    ├─ 创建分支     │
    │                 ├─ 上传设计文档         │                 ├─ 上传 PM 文档 │
    │                 ├─ 上传 Issue 模板      │                 ├─ 创建 PR      │
    │                 ├─ 创建 28 Labels       │                 │               │
    │                 ├─ 创建 PR              │                 │               │
    │                 │                       │                 │               │
    ▼                 ▼                       ▼                 ▼               ▼
    Bowei合并 ✅       Wang Xu + Junliang ✅    Renxian ✅         Jiahai +       全部合并 ✅
                     (可并行)                                 Hongrui ✅
                                                             (可并行)


Review 责任分配：
  Bowei     → Review Wang Xu 的 PR（后端代码）
  Renxian   → Review Jiahai 的 PR（前端页面）
  Bowei     → Review Renxian 的 PR（前端架构审查）
  任意成员  → Review Junliang + Hongrui 的 PR（文档）
```

---

## 四、总文件上传清单

### Bowei — 19 个文件

| 来源 | 目标 | 文件数 |
|------|------|:--:|
| 1-5/Wang Bowei | 项目根目录 (`backend/`, `.github/`) | 12 |
| week7/Wang Bowei | `docs/week7/Wang Bowei/` | 1 |
| week8/Wang Bowei | 项目根目录 + `docs/week8/` | 6 |

### Wang Xu — 9 个文件

| 来源 | 目标 | 文件数 |
|------|------|:--:|
| week7/Wang Xu | `docs/week7/Wang Xu/` | 1 |
| week8/Wang Xu | `backend/app/api/v1/` + `backend/app/services/` | 8 |

### Renxian — 28 个文件

| 来源 | 目标 | 文件数 |
|------|------|:--:|
| week7/Renxian Tang | `docs/week7/Renxian Tang/` | 1 |
| week8/Renxian Tang | `web/` + `docs/week8/` | 27 |

### Jiahai — 10 个文件

| 来源 | 目标 | 文件数 |
|------|------|:--:|
| week7/Jiahai Xiong | `docs/week7/Jiahai Xiong/` | 1 |
| week8/Jiahai Xiong | `web/src/app/` + `web/src/components/` + `docs/week8/` | 9 |

### Junliang — 13 个文件

| 来源 | 目标 | 文件数 |
|------|------|:--:|
| 1-5/Junliang Li | `docs/week7/Junliang Li/` | 6 |
| week7/Junliang Li | `.github/ISSUE_TEMPLATE/` | 2 |
| week8/Junliang Li | `docs/week8/Junliang Li/` | 4 |
| — | GitHub Labels（网页手动创建 28 个） | — |

### Hongrui — 12 个文件

| 来源 | 目标 | 文件数 |
|------|------|:--:|
| 1-5/Huang Hongrui | `docs/week7/Huang Hongrui/` | 8 |
| week8/Huang Hongrui | `docs/week8/Huang Hongrui/` | 4 |

---

## 五、Commit 规范

所有成员必须遵循 Conventional Commits：

```
feat:    新功能          feat: add Item CRUD API routes
fix:     Bug 修复        fix: correct ItemStatus enum casing
docs:    文档            docs: add meeting minutes W1-W5
refactor: 重构           refactor: switch database to lazy loading
test:    测试            test: add auth service unit tests
chore:   杂项            chore: update .gitignore
```

## 六、PR 模板

每个 PR 必须包含：

```markdown
## Description
简要描述做了什么

## Files Changed
- backend/app/api/v1/items.py — Item CRUD routes
- ...

## Checklist
- [ ] 代码已在本地测试通过
- [ ] 遵循 Conventional Commits
- [ ] 无 merge conflict
- [ ] 已关联相关 Issue（如有）

## Reviewer
@reviewer-name
```

---

## 七、最终仓库结构（完成后）

```
SG_CampusSwap/
├── .github/
│   ├── workflows/deploy.yml               (Bowei: CI/CD)
│   └── ISSUE_TEMPLATE/
│       ├── bug-report.md                  (Junliang)
│       └── feature-request.md             (Junliang)
├── backend/
│   ├── app/
│   │   ├── main.py                        (Bowei)
│   │   ├── config.py                      (Bowei)
│   │   ├── database.py                    (Bowei)
│   │   ├── models/                        (Bowei: User, Item, Review)
│   │   ├── schemas/                       (Bowei: User, Item, Review)
│   │   ├── api/v1/
│   │   │   ├── auth.py                    (Bowei)
│   │   │   ├── items.py                   (Wang Xu)
│   │   │   ├── search.py                  (Wang Xu)
│   │   │   ├── users.py                   (Wang Xu)
│   │   │   ├── upload.py                  (Wang Xu)
│   │   │   └── reviews.py                 (Wang Xu)
│   │   └── services/
│   │       ├── auth_service.py            (Bowei)
│   │       ├── item_service.py            (Wang Xu)
│   │       ├── upload_service.py          (Wang Xu)
│   │       └── chat_service.py            (Wang Xu)
│   ├── requirements.txt                   (Bowei)
│   ├── Dockerfile                         (Bowei)
│   └── .env.example                       (Bowei)
├── web/
│   ├── src/
│   │   ├── app/                           (Renxian: core pages)
│   │   │   ├── (auth)/                    (Renxian: login, register, verify)
│   │   │   ├── browse/                    (Renxian)
│   │   │   ├── item/[id]/                 (Renxian)
│   │   │   ├── sell/                      (Renxian)
│   │   │   ├── messages/                  (Jiahai)
│   │   │   ├── profile/                   (Jiahai)
│   │   │   ├── settings/                  (Jiahai)
│   │   │   ├── reviews/                   (Jiahai)
│   │   │   └── my-listings/               (Jiahai)
│   │   ├── components/                    (Renxian + Jiahai)
│   │   ├── lib/                           (Renxian: api-client, types, format)
│   │   └── stores/                        (Renxian: auth, items, filter, chat)
│   ├── package.json                       (Renxian)
│   └── tailwind.config.ts                 (Renxian)
├── docs/
│   ├── week7/                             (所有 6 人)
│   └── week8/                             (所有 6 人)
├── docker-compose.yml                     (Bowei)
└── README.md                              (更新: Bowei + Hongrui)
```
