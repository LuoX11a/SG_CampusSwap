# SG CampusSwap — GitHub 上传指南索引

> 6 份操作手册，每人一份。比新手教程还详细，从安装 Git 到合并 PR 全覆盖。

---

## 📊 总体时间线

```
           Day 1              Day 2              Day 3              Day 4              Day 5
      ────────────────  ────────────────  ────────────────  ────────────────  ────────────────
      
      🔴 Bowei           🟡 Wang Xu           🟢 Renxian          🔵 Jiahai           ⚪ 收尾
      必须第一个！        🟡 Junliang          依赖 Wang Xu        依赖 Renxian        所有人合并完
      创建 develop       两个可并行            上传前端核心        上传前端扩展        develop→master
      上传后端基础        依赖 Bowei                               依赖 Renxian        Tag v1.0.0
                                              🟣 Hongrui
                                              完全独立
                                              上传 PM 文档
```

## 📁 六份指南文件

| 成员 | 系统 | 文件 | 依赖 | 文件数 | 分支名 |
|------|:--:|------|:--:|:--:|------|
| 🔴 **Wang Bowei** | 🪟 | `Bowei-GitHub上传指南-详细步骤.md` | 无 | 19 | `feature/backend-scaffold` |
| 🟡 **Wang Xu** | 🪟 | `WangXu-GitHub上传指南-详细步骤.md` | Bowei | 10 | `feature/backend-api-routes` |
| 🟡 **Junliang Li** | 🍎 | `JunliangLi-GitHub上传指南-Mac版.md` | 无 | 11 | `feature/github-templates-and-design` |
| 🟢 **Renxian Tang** | 🪟 | `RenxianTang-GitHub上传指南-详细步骤.md` | Bowei + Wang Xu | 29 | `feature/frontend-core` |
| 🔵 **Jiahai Xiong** | 🪟 | `JiahaiXiong-GitHub上传指南-详细步骤.md` | Renxian | 11 | `feature/frontend-pages` |
| 🟣 **Huang Hongrui** | 🪟 | `HuangHongrui-GitHub上传指南-详细步骤.md` | 无 | 12 | `feature/pm-docs` |

## 🔀 分支策略

```
master ───────────────────────────────────────────── 🔒 最终合并 + Tag
  │
  └── develop ──────────────────────────────────── 🔒 开发主分支
        │
        ├── feature/backend-scaffold        ← Bowei（Day 1）
        ├── feature/backend-api-routes      ← Wang Xu（Day 2）
        ├── feature/github-templates-and-design ← Junliang（Day 2）
        ├── feature/frontend-core           ← Renxian（Day 3）
        ├── feature/frontend-pages          ← Jiahai（Day 4）
        └── feature/pm-docs                 ← Hongrui（Day 4）
```

## 📊 最终仓库结构

```
SG_CampusSwap/
├── .github/
│   ├── workflows/deploy.yml               ← Bowei
│   └── ISSUE_TEMPLATE/
│       ├── bug-report.md                  ← Junliang
│       └── feature-request.md             ← Junliang
├── backend/
│   ├── app/
│   │   ├── main.py                        ← Bowei
│   │   ├── config.py                      ← Bowei
│   │   ├── database.py                    ← Bowei
│   │   ├── models/                        ← Bowei（user, item, review）
│   │   ├── schemas/                       ← Bowei（user, item, review）
│   │   ├── api/v1/
│   │   │   ├── auth.py                    ← Bowei
│   │   │   ├── items.py                   ← Wang Xu
│   │   │   ├── search.py                  ← Wang Xu
│   │   │   ├── users.py                   ← Wang Xu
│   │   │   ├── upload.py                  ← Wang Xu
│   │   │   └── reviews.py                 ← Wang Xu
│   │   └── services/
│   │       ├── auth_service.py            ← Bowei
│   │       ├── item_service.py            ← Wang Xu
│   │       ├── upload_service.py          ← Wang Xu
│   │       └── chat_service.py            ← Wang Xu
│   ├── requirements.txt                   ← Bowei
│   ├── Dockerfile                         ← Bowei
│   └── .env.example                       ← Bowei
├── web/
│   ├── src/
│   │   ├── app/
│   │   │   ├── (auth)/                    ← Renxian（login, register, verify）
│   │   │   ├── browse/                    ← Renxian
│   │   │   ├── item/[id]/                 ← Renxian
│   │   │   ├── sell/                      ← Renxian
│   │   │   ├── messages/                  ← Jiahai
│   │   │   ├── profile/                   ← Jiahai
│   │   │   ├── settings/                  ← Jiahai
│   │   │   ├── reviews/                   ← Jiahai
│   │   │   └── my-listings/               ← Jiahai
│   │   ├── components/                    ← Renxian (5) + Jiahai (1)
│   │   ├── lib/                           ← Renxian（api-client, types, format）
│   │   └── stores/                        ← Renxian（auth, items, filter, chat）
│   ├── package.json                       ← Renxian
│   └── .env.example                       ← Renxian
├── docs/
│   ├── week7/                             ← 全部 6 人
│   └── week8/                             ← 全部 6 人
├── docker-compose.yml                     ← Bowei
├── .gitignore                             ← Bowei
└── README.md
```

## 👀 Review 责任分配

| PR 提交者 | Reviewer | 审查重点 |
|-----------|----------|----------|
| Bowei | 任意 1 人 | 代码架构、安全性 |
| **Wang Xu** | **Bowei** | 后端代码质量、API 设计 |
| Junliang | 任意 1 人 | 纯文档（无需代码背景） |
| **Renxian** | **Jiahai + Bowei** | 前端架构 + 代码审查 |
| **Jiahai** | **Renxian** | 前端代码质量、组件一致性 |
| Hongrui | 任意 1 人 | 纯文档（无需代码背景） |

## 📋 每份指南包含的内容

每份指南统一结构：
- **Step 0**：安装 Git、配置用户名邮箱、克隆仓库、确认 GitHub 权限
- **Step 1**：确认前置依赖已完成、创建功能分支
- **Step 2**：逐条 copy 命令、创建所需文件夹
- **Step 3**：git add → commit → push
- **Step 4**：创建 PR（含完整标题和描述模板，直接复制粘贴）
- **Step 5**：等待 Review + 合并
- **常见问题**：Token 认证、权限错误、冲突解决等

## 🚀 开始顺序

1. **先把这些指南发给对应的人**
2. **Bowei 先开始**（其他人等他完成 develop 和基础后端）
3. **Bowei 完成后** → Wang Xu + Junliang 并行（Day 2）
4. **Wang Xu 完成后** → Renxian（Day 3）
5. **Renxian 完成后** → Jiahai（Day 4）+ Hongrui 并行
6. **全部合并后** → Bowei 更新 README + develop → master + Tag v1.0.0

---

## 📞 所有指南都在这个文件夹

```
C:\Users\92183\Desktop\cp3102\
├── Bowei-GitHub上传指南-详细步骤.md
├── WangXu-GitHub上传指南-详细步骤.md
├── JunliangLi-GitHub上传指南-详细步骤.md
├── RenxianTang-GitHub上传指南-详细步骤.md
├── JiahaiXiong-GitHub上传指南-详细步骤.md
├── HuangHongrui-GitHub上传指南-详细步骤.md
└── GitHub上传指南-索引.md              ← 你正在看的文件
```
