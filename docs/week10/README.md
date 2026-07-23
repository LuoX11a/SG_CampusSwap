# SG CampusSwap — Week 10 最终交付包

> 📅 2026-07-22 | 六成员 | 📱 手机端可用 | 🚀 Vercel + Render 部署

---

## 🏗️ 部署架构

```
手机浏览器 ──→ Vercel (前端) ──→ Render (后端) ──→ Neon PostgreSQL
   📱           免费 CDN          免费 Web Service     免费 0.5GB
```

详细部署步骤见 `DEPLOY_GUIDE.md`

---

## 👥 成员文件清单

| 成员 | 角色 | 文件夹 | 新增/修改 |
|------|------|--------|------|
| **Wang Bowei** | Backend Lead | `Wang-Bowei/` | API路由(8含chat) + main.py + Docker + .env.example |
| **Wang Xu** | Backend Dev | `Wang-Xu/` | Service层(3) + 测试(10) |
| **Renxian Tang** | Frontend Lead | `Renxian-Tang/` | 🔥 **移动端改造**: 响应式布局 + 底部导航 + PWA |
| **Jiahai Xiong** | Frontend Dev | `Jiahai-Xiong/` | 扩展页面(8) + FilterModal |
| **Junliang Li** | QA/UX | `Junliang-Li/` | 设计系统 + 测试计划 |
| **Huang Hongrui** | PM | `Huang-Hongrui/` | W8/W9/W10 PM文档 + 部署指南 |

---

## 📱 移动端适配（本周新增）

| 改动 | 文件 | 说明 |
|------|------|------|
| 响应式布局 | `layout.tsx` | 桌面侧栏 / 手机底部Tab |
| 底部导航栏 | `MobileBottomNav.tsx` | 5个Tab: Home/Browse/Chat/Sell/Profile |
| PWA 支持 | `manifest.json` + `sw.js` | 可添加到主屏幕，离线缓存 |
| 触控优化 | `globals.css` | 44px最小触摸区，iOS安全区适配 |
| 离线回退 | `sw.js` | API离线时返回提示 |

---

## 🚀 上传顺序

```
1. Wang-Bowei   → backend/app/api/v1/* + main.py + Docker + .env.example
2. Wang-Xu      → backend/app/services/* + backend/tests/*
3. Renxian-Tang → project/web/* (全部覆盖，含移动端改造)
4. Jiahai-Xiong → project/web/src/app/* + components/* (合并)
5. Junliang-Li  → docs/week8/* + docs/week9/*
6. Huang-Hongrui→ docs/week8/* + docs/week9/* + docs/week10/*
```

---

## ✅ 上传后本地验证

```bash
# 后端
cd backend && pip install -r requirements.txt
uvicorn app.main:app --reload
# → http://localhost:8000/docs

# 测试
pytest tests/ -v

# 前端
cd project/web && npm install && npm run dev
# → http://localhost:3000 (手机可用局域网IP访问)
```

---

## ⚠️ 上线前必须做

- [ ] `.env` 配置真实数据库URL + JWT密钥
- [ ] `alembic revision --autogenerate -m "init"` 生成迁移
- [ ] `alembic upgrade head` 创建数据库表
- [ ] Vercel 部署前端 → 获得域名
- [ ] Render 部署后端 → 设置 CORS_ORIGINS
- [ ] `project/backend/.env` 中的数据库密码轮换（已泄露）

---

## 📊 改动记录 (对比上一版 week10)

| 改动 | 说明 |
|------|------|
| 🔥 `layout.tsx` | Sidebar → 响应式: 桌面侧栏 / 手机底部Tab |
| 🆕 `MobileBottomNav.tsx` | 5Tab 底部导航栏 |
| 🆕 `manifest.json` | PWA 清单文件 |
| 🆕 `sw.js` | Service Worker 离线缓存 |
| 🆕 `icons/` | PWA 图标 (192 + 512) |
| 🔧 `globals.css` | 安全区 + 触控 + 底部导航偏移 |
| 🔧 `main.py` | Render 健康检查 + DB 连接测试 |
| 🔧 `.env.example` | Render 部署说明 + Vercel CORS |
| 🆕 `DEPLOY_GUIDE.md` | 完整部署步骤 |
