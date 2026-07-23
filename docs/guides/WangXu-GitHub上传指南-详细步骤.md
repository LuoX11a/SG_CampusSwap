# Wang Xu — GitHub 上传完整操作指南

> 🎯 **你的任务**：在 Bowei 上传后端基础代码之后，上传你的 API 路由和服务层代码。
> ⏱ **预计耗时**：40-60 分钟
> ⚠️ **前置条件**：Bowei 必须已经完成他的上传并合并到 develop！

---

## 📋 操作步骤总览

| 步骤 | 做什么 | 大概时间 |
|:--:|--------|:--:|
| **Step 0** | 装 Git、配置 GitHub、克隆仓库 | 20 分钟（如已做过可跳过） |
| **Step 1** | 从 develop 创建功能分支 | 5 分钟 |
| **Step 2** | 复制你的 9 个文件到仓库 | 15 分钟 |
| **Step 3** | 提交、推送、创建 PR | 10 分钟 |
| **Step 4** | 等 Bowei Review、合并 | 5 分钟 |

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
git config --global user.name "Wang Xu"
git config --global user.email "wang.xu@example.com"
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

> 如果提示文件夹已存在（因为之前克隆过），先删掉旧的：
> ```cmd
> rmdir /s /q SG_CampusSwap
> git clone https://github.com/LuoX11a/SG_CampusSwap.git
> cd SG_CampusSwap
> ```

---

## Step 1：确认 Bowei 已完成 + 创建功能分支

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
git checkout -b feature/backend-api-routes origin/develop
```

预期输出：`Switched to a new branch 'feature/backend-api-routes'`

> 这条命令做了两件事：基于远程最新的 develop 创建本地 develop 的引用，然后从它拉出你的功能分支。

---

## Step 2：复制你的文件

### 2.1 你要上传的文件清单

| 来源文件夹 | 文件 | 放到仓库的哪里 |
|-----------|------|---------------|
| `Desktop\week7\Wang Xu\` | `backend-dev-deliverables-w7.md` | `docs\week7\Wang Xu\` |
| `Desktop\week8\Wang Xu\` | `backend\app\api\v1\items.py` | `backend\app\api\v1\` |
| | `backend\app\api\v1\search.py` | `backend\app\api\v1\` |
| | `backend\app\api\v1\users.py` | `backend\app\api\v1\` |
| | `backend\app\api\v1\upload.py` | `backend\app\api\v1\` |
| | `backend\app\api\v1\reviews.py` | `backend\app\api\v1\` |
| | `backend\app\services\item_service.py` | `backend\app\services\` |
| | `backend\app\services\upload_service.py` | `backend\app\services\` |
| | `backend\app\services\chat_service.py` | `backend\app\services\` |
| | `backend-dev-w8-summary.md` | `docs\week8\Wang Xu\` |

共 **10 个文件**（8 个代码 + 2 个文档）。

### 2.2 创建需要的文件夹

```cmd
mkdir docs\week7\Wang Xu
mkdir docs\week8\Wang Xu
```

> 其他文件夹（如 `backend\app\api\v1\`、`backend\app\services\`）Bowei 已经创建好了。如果提示"已存在"，忽略即可。

### 2.3 复制文件

依次执行以下命令：

```cmd
REM === W7 文档 ===
copy "C:\Users\92183\Desktop\week7\Wang Xu\backend-dev-deliverables-w7.md" "docs\week7\Wang Xu\backend-dev-deliverables-w7.md"

REM === W8 文档 ===
copy "C:\Users\92183\Desktop\week8\Wang Xu\backend-dev-w8-summary.md" "docs\week8\Wang Xu\backend-dev-w8-summary.md"

REM === API 路由（5 个文件）===
copy "C:\Users\92183\Desktop\week8\Wang Xu\backend\app\api\v1\items.py"   "backend\app\api\v1\items.py"
copy "C:\Users\92183\Desktop\week8\Wang Xu\backend\app\api\v1\search.py"  "backend\app\api\v1\search.py"
copy "C:\Users\92183\Desktop\week8\Wang Xu\backend\app\api\v1\users.py"   "backend\app\api\v1\users.py"
copy "C:\Users\92183\Desktop\week8\Wang Xu\backend\app\api\v1\upload.py"  "backend\app\api\v1\upload.py"
copy "C:\Users\92183\Desktop\week8\Wang Xu\backend\app\api\v1\reviews.py" "backend\app\api\v1\reviews.py"

REM === 服务层（3 个文件）===
copy "C:\Users\92183\Desktop\week8\Wang Xu\backend\app\services\item_service.py"   "backend\app\services\item_service.py"
copy "C:\Users\92183\Desktop\week8\Wang Xu\backend\app\services\upload_service.py" "backend\app\services\upload_service.py"
copy "C:\Users\92183\Desktop\week8\Wang Xu\backend\app\services\chat_service.py"   "backend\app\services\chat_service.py"
```

### 2.4 检查有没有遗漏的 `__init__.py`

```cmd
dir backend\app\utils /b 2>nul
```

如果显示"找不到文件"，说明 `utils` 文件夹不存在，创建它：

```cmd
mkdir backend\app\utils
type nul > backend\app\utils\__init__.py
```

### 2.5 检查文件结构

```cmd
dir /s /b backend\app\api backend\app\services docs\week7\Wang Xu docs\week8\Wang Xu
```

你应该看到：
```
backend\app\api\v1\items.py
backend\app\api\v1\search.py
backend\app\api\v1\users.py
backend\app\api\v1\upload.py
backend\app\api\v1\reviews.py
backend\app\services\item_service.py
backend\app\services\upload_service.py
backend\app\services\chat_service.py
docs\week7\Wang Xu\backend-dev-deliverables-w7.md
docs\week8\Wang Xu\backend-dev-w8-summary.md
```

---

## Step 3：提交并推送

### 3.1 查看 Git 状态

```cmd
git status
```

确认所有文件都显示为红色（新文件，尚未追踪）。

### 3.2 添加到暂存区

```cmd
git add .
git status
```

现在文件应该变成绿色。

### 3.3 提交

```cmd
git commit -m "feat: add Item CRUD, Search, Upload, Users, and Reviews API routes"
```

### 3.4 推送到 GitHub

```cmd
git push -u origin feature/backend-api-routes
```

---

## Step 4：创建 Pull Request

### 4.1 打开 PR 页面

1. 浏览器访问：**https://github.com/LuoX11a/SG_CampusSwap**
2. 页面顶部会出现黄色提示条：`feature/backend-api-routes has recent pushes`
3. 点击 **"Compare & pull request"**
4. 如果没有提示条：点击 "Pull requests" → "New pull request" → `base` 选 `develop`，`compare` 选 `feature/backend-api-routes`

### 4.2 填写 PR 信息

**标题**：
```
feat: add Item CRUD, Search, Upload, Users, and Reviews API routes
```

**描述**（复制以下内容填入）：
```markdown
## Description
基于 Bowei 的后端基础架构，上传后端 API 路由和服务层代码：
- 5 个 API 路由模块（items, search, users, upload, reviews）
- 3 个服务模块（item_service, upload_service, chat_service）
- W7 + W8 交付文档

## Files Changed

### API Routes（`backend/app/api/v1/`）
- `items.py` — 商品 CRUD（创建/查询/更新/删除）
- `search.py` — 商品搜索（关键词 + 分类 + 价格筛选）
- `users.py` — 用户资料（查看/更新个人信息）
- `upload.py` — 图片上传（Cloudinary 集成）
- `reviews.py` — 评价系统（创建/查看评价）

### Services（`backend/app/services/`）
- `item_service.py` — 商品业务逻辑
- `upload_service.py` — 图片上传业务逻辑
- `chat_service.py` — Firebase 聊天服务

### Docs
- `docs/week7/Wang Xu/backend-dev-deliverables-w7.md` — W7 交付文档
- `docs/week8/Wang Xu/backend-dev-w8-summary.md` — W8 总结文档

## Checklist
- [x] 代码已在本地测试通过
- [x] 遵循 Conventional Commits
- [x] 无 merge conflict
- [x] 依赖 Bowei 的 models 已就位

## Reviewer
@Bowei 的 GitHub 用户名 — 请 Review 后端代码
```

### 4.3 设置 Reviewer

PR 页面右侧 → **Reviewers** → 齿轮图标 → 选择 **Bowei 的 GitHub 用户名**

### 4.4 创建 PR

点击 **"Create pull request"**

---

## Step 5：等待 Review 并合并

1. 把 PR 链接发到团队群
2. 等 Bowei Review 通过（Approve）
3. 如果有人提修改意见，在本地改好 → `git add .` → `git commit -m "fix: address review feedback"` → `git push`
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
用文件资源管理器手动打开 `C:\Users\92183\Desktop\week8\Wang Xu\backend\` 确认文件存在。如果不存在，找 Renxian。

### Q4: PR 有 merge conflict
```cmd
git checkout feature/backend-api-routes
git fetch origin
git merge origin/develop
# 手动解决冲突文件（搜索 <<<<<<< 和 >>>>>>>）
git add .
git commit -m "fix: resolve merge conflicts"
git push
```

### Q5: 发现 Bowei 的代码里有问题
不要在你的 PR 里改 Bowei 的文件。单独告诉他，或者另开一个 fix PR。
