# Bowei — GitHub 上传完整操作指南

> 🎯 **你的任务**：作为 Backend Lead，你需要第一个上传代码，为整个团队建立基础。
> ⏱ **预计耗时**：1-2 小时（大部分是第一次配置的时间）
> 📅 **必须第一个完成**：所有人都等你这一步做完才能开始

---

## 📋 你需要做的三件事（按顺序）

| 步骤 | 做什么 | 大概时间 |
|:--:|--------|:--:|
| **Step 0** | 装 Git、配置 GitHub、克隆仓库 | 20 分钟 |
| **Step 1** | 创建 `develop` 分支并推送到 GitHub | 10 分钟 |
| **Step 2** | 上传你的后端代码（19 个文件） | 30 分钟 |
| **Step 3** | 创建 Pull Request、等 Review、合并 | 15 分钟 |

---

## Step 0：准备工作（只做一次）

### 0.1 检查电脑有没有装 Git

打开 **命令提示符**（按 `Win + R`，输入 `cmd`，回车），输入：

```cmd
git --version
```

如果显示类似 `git version 2.45.0` — ✅ 已安装，跳到 0.3

如果显示 `'git' 不是内部或外部命令` — ❌ 没装，继续 0.2

### 0.2 安装 Git（如果没装的话）

1. 打开浏览器，访问：**https://git-scm.com/download/win**
2. 下载会自动开始，下载完成后双击运行
3. 安装过程中，**所有选项用默认值**，一路点 "Next" → "Install"
4. 装完后，**关掉命令提示符，重新打开**
5. 再次输入 `git --version` 确认安装成功

### 0.3 配置你的 Git 用户名和邮箱

在命令提示符中输入（**替换成你自己的名字和邮箱**）：

```cmd
git config --global user.name "Wang Bowei"
git config --global user.email "bowei.wang@example.com"
```

> ⚠️ 这个邮箱要和你的 GitHub 账号邮箱一致！不然提交记录不会关联到你的 GitHub 头像。

检查是否配置成功：

```cmd
git config --global user.name
git config --global user.email
```

### 0.4 确认你能登录 GitHub

1. 打开浏览器，访问：**https://github.com/login**
2. 用你的账号密码登录
3. 确认你能看到团队仓库：**https://github.com/LuoX11a/SG_CampusSwap**

> 如果你看不到这个仓库，让 Renxian（仓库 owner）在 GitHub 上把你的账号加为 Collaborator：
> 仓库页面 → Settings → Collaborators → Add people → 输入你的 GitHub 用户名

### 0.5 克隆仓库到你的电脑

在命令提示符中输入：

```cmd
cd %USERPROFILE%\Desktop
git clone https://github.com/LuoX11a/SG_CampusSwap.git
cd SG_CampusSwap
dir
```

你应该只看到一个 `README.md` 文件。

### 0.6 检查三个源文件夹

你的文件分散在三个文件夹里，确保它们都在：

```cmd
dir "C:\Users\92183\Desktop\1-5\Wang Bowei"
dir "C:\Users\92183\Desktop\week7\Wang Bowei"
dir "C:\Users\92183\Desktop\week8\Wang Bowei"
```

每条命令都应该列出一堆文件。如果有哪个文件夹不存在或为空，**马上告诉 Renxian**。

---

## Step 1：创建 develop 分支

> 🎯 **目的**：`develop` 是团队的开发主分支，所有人从它拉出自己的功能分支，最后合并回来。

### 1.1 确保你在最新状态

```cmd
cd %USERPROFILE%\Desktop\SG_CampusSwap
git checkout master
git pull origin master
```

预期输出：`Already up to date.`

### 1.2 创建 develop 分支

```cmd
git checkout -b develop
```

预期输出：`Switched to a new branch 'develop'`

你现在在 `develop` 分支上。

### 1.3 推送 develop 到 GitHub

```cmd
git push -u origin develop
```

预期输出：
```
remote: Create a pull request for 'develop' on GitHub by visiting:
remote:      https://github.com/LuoX11a/SG_CampusSwap/pull/new/develop
...
To https://github.com/LuoX11a/SG_CampusSwap.git
 * [new branch]      develop -> develop
branch 'develop' set up to track 'origin/develop'.
```

### 1.4 去 GitHub 网页上设置分支保护

1. 打开浏览器，访问：**https://github.com/LuoX11a/SG_CampusSwap/settings/branches**
2. 点击 **"Add branch protection rule"** 按钮
3. 在 "Branch name pattern" 输入框中输入：`develop`
4. 勾选以下选项：
   - ☑️ **Require a pull request before merging**（禁止直接推送，必须通过 PR）
   - ☑️ **Require approvals**（需要至少 1 人批准），默认是 1，保持不变
5. 点击页面底部的绿色 **"Create"** 按钮
6. 重复以上步骤，但把分支名改成 `master`（同样禁止直接推送）

> 📸 做好后**截图发到团队群里**，告诉大家 "develop 分支已创建，可以开始工作了"

✅ **Step 1 完成！** 告诉团队可以开始了。

---

## Step 2：上传你的后端基础代码

> 🎯 **目的**：把你的后端代码（models、schemas、services、config 等）上传到 `feature/backend-scaffold` 分支，然后通过 PR 合并到 `develop`。

### 2.1 从 develop 创建你的功能分支

```cmd
cd %USERPROFILE%\Desktop\SG_CampusSwap
git checkout develop
git pull origin develop
git checkout -b feature/backend-scaffold
```

预期：`Switched to a new branch 'feature/backend-scaffold'`

### 2.2 创建目标文件夹结构

你需要在仓库里创建这些文件夹（如果还不存在的话）：

```cmd
mkdir backend\app\models
mkdir backend\app\schemas
mkdir backend\app\services
mkdir backend\app\api\v1
mkdir docs\week7\Wang Bowei
mkdir docs\week8\Wang Bowei
mkdir .github\workflows
```

> 如果提示"子目录或文件已存在"，忽略即可，不影响。

### 2.3 从三个源文件夹复制文件

#### 📁 第一组：从 1-5\Wang Bowei 复制（12 个代码文件）

依次执行以下命令：

```cmd
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\backend\app\config.py"          "backend\app\config.py"
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\backend\app\database.py"        "backend\app\database.py"
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\backend\app\main.py"            "backend\app\main.py"
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\backend\app\models\user.py"     "backend\app\models\user.py"
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\backend\app\models\item.py"     "backend\app\models\item.py"
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\backend\app\models\review.py"   "backend\app\models\review.py"
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\backend\app\schemas\user.py"    "backend\app\schemas\user.py"
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\backend\app\schemas\item.py"    "backend\app\schemas\item.py"
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\backend\app\schemas\review.py"  "backend\app\schemas\review.py"
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\backend\app\services\auth_service.py" "backend\app\services\auth_service.py"
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\backend\requirements.txt"       "backend\requirements.txt"
copy "C:\Users\92183\Desktop\1-5\Wang Bowei\.github\workflows\deploy.yml"   ".github\workflows\deploy.yml"
```

#### 📁 第二组：从 week7\Wang Bowei 复制（1 个文档）

```cmd
copy "C:\Users\92183\Desktop\week7\Wang Bowei\backend-lead-deliverables-w7.md" "docs\week7\Wang Bowei\backend-lead-deliverables-w7.md"
```

#### 📁 第三组：从 week8\Wang Bowei 复制（6 个文件）

```cmd
copy "C:\Users\92183\Desktop\week8\Wang Bowei\backend\app\api\v1\__init__.py" "backend\app\api\v1\__init__.py"
copy "C:\Users\92183\Desktop\week8\Wang Bowei\backend\app\api\v1\auth.py"      "backend\app\api\v1\auth.py"
copy "C:\Users\92183\Desktop\week8\Wang Bowei\backend\Dockerfile"              "backend\Dockerfile"
copy "C:\Users\92183\Desktop\week8\Wang Bowei\backend\.env.example"            "backend\.env.example"
copy "C:\Users\92183\Desktop\week8\Wang Bowei\backend-lead-w8-summary.md"      "docs\week8\Wang Bowei\backend-lead-w8-summary.md"
copy "C:\Users\92183\Desktop\week8\Wang Bowei\docker-compose.yml"              "docker-compose.yml"
```

### 2.4 创建缺失的 `__init__.py` 文件

Python 包需要 `__init__.py` 文件（可以是空文件）。创建以下文件：

```cmd
type nul > backend\app\__init__.py
type nul > backend\app\api\__init__.py
type nul > backend\app\models\__init__.py
type nul > backend\app\schemas\__init__.py
type nul > backend\app\services\__init__.py
```

### 2.5 创建 `.gitignore` 文件

在仓库根目录创建 `.gitignore`，防止把不该传的文件上传到 GitHub：

```cmd
echo # Python > .gitignore
echo __pycache__/ >> .gitignore
echo *.py[cod] >> .gitignore
echo *.egg-info/ >> .gitignore
echo venv/ >> .gitignore
echo .venv/ >> .gitignore
echo # Node >> .gitignore
echo node_modules/ >> .gitignore
echo .next/ >> .gitignore
echo # Environment >> .gitignore
echo .env >> .gitignore
echo .env.local >> .gitignore
echo # IDE >> .gitignore
echo .vscode/ >> .gitignore
echo .idea/ >> .gitignore
echo # OS >> .gitignore
echo Thumbs.db >> .gitignore
echo .DS_Store >> .gitignore
```

### 2.6 检查你的文件结构

确认所有文件都在正确位置：

```cmd
dir /s /b
```

你应该看到类似这样的结构（只列出你上传的文件）：

```
C:\Users\你的用户名\Desktop\SG_CampusSwap\
├── .gitignore                              ← 新建
├── docker-compose.yml                      ← 从 week8 复制
├── .github\workflows\deploy.yml            ← 从 1-5 复制
├── backend\
│   ├── .env.example                        ← 从 week8 复制
│   ├── Dockerfile                          ← 从 week8 复制
│   ├── requirements.txt                    ← 从 1-5 复制
│   └── app\
│       ├── __init__.py                     ← 新建（空文件）
│       ├── config.py                       ← 从 1-5 复制
│       ├── database.py                     ← 从 1-5 复制
│       ├── main.py                         ← 从 1-5 复制
│       ├── api\
│       │   ├── __init__.py                 ← 新建（空文件）
│       │   └── v1\
│       │       ├── __init__.py             ← 从 week8 复制
│       │       └── auth.py                 ← 从 week8 复制
│       ├── models\
│       │   ├── __init__.py                 ← 新建（空文件）
│       │   ├── item.py                     ← 从 1-5 复制
│       │   ├── review.py                   ← 从 1-5 复制
│       │   └── user.py                     ← 从 1-5 复制
│       ├── schemas\
│       │   ├── __init__.py                 ← 新建（空文件）
│       │   ├── item.py                     ← 从 1-5 复制
│       │   ├── review.py                   ← 从 1-5 复制
│       │   └── user.py                     ← 从 1-5 复制
│       └── services\
│           ├── __init__.py                 ← 新建（空文件）
│           └── auth_service.py             ← 从 1-5 复制
└── docs\
    ├── week7\Wang Bowei\
    │   └── backend-lead-deliverables-w7.md  ← 从 week7 复制
    └── week8\Wang Bowei\
        └── backend-lead-w8-summary.md      ← 从 week8 复制
```

### 2.7 查看 Git 检测到的变化

```cmd
git status
```

你会看到红色的新文件列表 — 这些是 Git 检测到的新文件，但还没被追踪。

---

## Step 3：提交并推送到 GitHub

### 3.1 添加所有文件到暂存区

```cmd
git add .
```

没有任何输出是正常的。

### 3.2 再次检查状态

```cmd
git status
```

现在文件名应该都是绿色的，表示已暂存。

### 3.3 提交（commit）

```cmd
git commit -m "feat: add FastAPI backend scaffold with auth, models, schemas, and CI/CD"
```

> 💡 **Commit 信息格式**：`feat:` 表示新功能。团队统一使用 [Conventional Commits](https://www.conventionalcommits.org/)：
> - `feat:` — 新功能
> - `fix:` — Bug 修复
> - `docs:` — 文档
> - `chore:` — 杂项（配置、依赖等）

### 3.4 推送到 GitHub

```cmd
git push -u origin feature/backend-scaffold
```

预期输出：
```
remote: Create a pull request for 'feature/backend-scaffold' on GitHub by visiting:
remote:      https://github.com/LuoX11a/SG_CampusSwap/pull/new/feature/backend-scaffold
...
To https://github.com/LuoX11a/SG_CampusSwap.git
 * [new branch]      feature/backend-scaffold -> feature/backend-scaffold
```

---

## Step 4：创建 Pull Request（PR）

### 4.1 打开 GitHub 创建 PR

1. 打开浏览器，访问：**https://github.com/LuoX11a/SG_CampusSwap**
2. 你应该会看到页面顶部有一个黄色提示条：
   > `feature/backend-scaffold has recent pushes. Compare & pull request`
3. 点击绿色的 **"Compare & pull request"** 按钮
4. 如果没有看到这个提示条：
   - 点击 **"Pull requests"** 标签页
   - 点击绿色的 **"New pull request"** 按钮
   - `base` 选择 `develop`，`compare` 选择 `feature/backend-scaffold`
   - 点击 **"Create pull request"**

### 4.2 填写 PR 信息

**标题**：
```
feat: add FastAPI backend scaffold with auth, models, schemas, and CI/CD
```

**描述**（复制以下内容填入）：
```markdown
## Description
后端基础架构代码上传，包括：
- FastAPI 入口（main.py）+ 配置（config.py）+ 数据库（database.py）
- 三个数据模型：User、Item、Review
- 三个 Pydantic Schema：User、Item、Review
- JWT 认证服务（auth_service.py）
- 22 所大学邮箱白名单验证
- API v1 auth 路由
- Dockerfile + docker-compose.yml
- CI/CD workflow（GitHub Actions）
- W7 + W8 交付物文档

## Files Changed
- `backend/app/config.py` — 应用配置（JWT、数据库、CORS、大学域名白名单）
- `backend/app/database.py` — 异步 SQLAlchemy 引擎
- `backend/app/main.py` — FastAPI 入口（lifespan、CORS、health check）
- `backend/app/models/user.py` — User 模型
- `backend/app/models/item.py` — Item 模型（+ 5个枚举）
- `backend/app/models/review.py` — Review + ItemImage + Transaction + EmailVerification 模型
- `backend/app/schemas/user.py` — Register/Login/Verify/Token/Profile schema
- `backend/app/schemas/item.py` — Create/Update/List/Detail schema
- `backend/app/schemas/review.py` — Review schema
- `backend/app/services/auth_service.py` — JWT + bcrypt + 邮箱域名白名单
- `backend/app/api/v1/auth.py` — 认证 API 路由
- `backend/requirements.txt` — Python 依赖（19 个包）
- `backend/Dockerfile` — 后端容器化
- `backend/.env.example` — 环境变量模板
- `docker-compose.yml` — 服务编排
- `.github/workflows/deploy.yml` — CI/CD（lint → test → deploy）
- `.gitignore` — 忽略规则
- `docs/week7/Wang Bowei/backend-lead-deliverables-w7.md` — W7 交付文档
- `docs/week8/Wang Bowei/backend-lead-w8-summary.md` — W8 总结文档

## Checklist
- [x] 代码已在本地测试通过
- [x] 遵循 Conventional Commits
- [x] 无 merge conflict
- [x] 包含 `.gitignore`

## Reviewer
@LuoX11a — 请 Review
```

### 4.3 选择 Reviewer

在 PR 页面右侧找到 **"Reviewers"**，点击齿轮图标，选择 **LuoX11a**（Renxian）。

### 4.4 创建 PR

点击页面底部的绿色 **"Create pull request"** 按钮。

✅ **PR 创建完成！**

---

## Step 5：等待 Review 并合并

### 5.1 等别人 Review

- 把 PR 链接发到团队微信群
- 至少需要 **1 个人 Approve** 才能合并
- 如果有人提了修改意见（Request changes），修改后在本地改好，再 `git add` → `git commit` → `git push`，PR 会自动更新

### 5.2 合并 PR

当 PR 获得批准后：

1. 打开你的 PR 页面
2. 点击绿色的 **"Merge pull request"** 按钮
3. 合并方式选择 **"Create a merge commit"**（默认选项）
4. 点击 **"Confirm merge"**
5. 合并完成后，可以点击 **"Delete branch"** 删除远程的 `feature/backend-scaffold` 分支

### 5.3 更新你本地的 develop

合并后，你的本地 `develop` 就过时了，更新一下：

```cmd
cd %USERPROFILE%\Desktop\SG_CampusSwap
git checkout develop
git pull origin develop
```

---

## 🎉 你完成了！

做完以上所有步骤后，你的任务就完成了。后续你需要：

- **Review Wang Xu 的 PR**（后端 API 路由，他依赖你的 models）
- **Review Renxian 的 PR**（前端架构审查）

---

## ❓ 常见问题 / 排错指南

### Q1: `git push` 时要求输入密码
**原因**：GitHub 不再支持密码登录，需要用 Personal Access Token。
**解决**：
1. 打开 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. Note 填 "SG_CampusSwap"，过期时间选 "No expiration"
4. 勾选 `repo`（全部）、`workflow`
5. 点击 "Generate token"，**复制生成的 token**（只显示一次！）
6. 回到命令行，当要求密码时，粘贴 token（不会显示字符，这是正常的）

### Q2: `git push` 报 `Permission denied`
**原因**：你没有仓库的写权限。
**解决**：让 Renxian 去 https://github.com/LuoX11a/SG_CampusSwap/settings/access 添加你为 Collaborator。

### Q3: `git commit` 报 `nothing to commit`
**原因**：文件没有被成功添加。
**解决**：先用 `git status` 检查文件是否在暂存区（绿色）。如果是红色的，先执行 `git add .`

### Q4: 复制文件时提示"系统找不到指定的路径"
**原因**：源文件夹路径不对。
**解决**：用文件资源管理器手动打开 `C:\Users\92183\Desktop\1-5\Wang Bowei\`，确认文件夹存在。如果不在这台电脑上，找 Renxian 要文件。

### Q5: PR 有 merge conflict
**原因**：`develop` 分支上有新的提交和你的修改冲突了。
**解决**：
```cmd
git checkout develop
git pull origin develop
git checkout feature/backend-scaffold
git merge develop
# 此时会提示哪些文件有冲突
# 用记事本打开冲突文件，找到 <<<<<<< 和 >>>>>>> 标记
# 手动修改、保存
git add .
git commit -m "fix: resolve merge conflicts"
git push
```

### Q6: 不小心提交了不该提交的文件
**解决**：
```cmd
git reset HEAD~1          # 撤销最近一次 commit，保留文件修改
# 修改 .gitignore 排除那些文件
git add .gitignore
git commit -m "chore: update .gitignore"
git push -f                # 强制推送（小心使用）
```

---

## 📞 遇到问题？

1. 先在团队群里问
2. 截全屏发到群里（包含命令行和错误信息）
3. 或直接私聊 Renxian
