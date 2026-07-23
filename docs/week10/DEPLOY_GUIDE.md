# SG CampusSwap — 部署指南（阶段一）

> 目标: 手机浏览器通过公网访问，8月7日演示可用

## 架构

```
用户手机浏览器
    │
    ├── https://sg-campusswap.vercel.app (前端)
    │       └── Vercel (免费, 自动 HTTPS, 全球 CDN)
    │
    └── https://sg-campusswap-api.onrender.com (后端)
            └── Render (免费, 自动 HTTPS)
                    └── Neon PostgreSQL (免费 0.5GB)
```

## 第一步: Neon PostgreSQL 数据库

1. 打开 https://console.neon.tech (已有账号)
2. 复制连接字符串，格式: `postgresql+asyncpg://user:pass@ep-xxx.us-east-2.aws.neon.tech/db?sslmode=require`
3. 在 Neon SQL Editor 中执行 Alembic 迁移（或直接创建表）

## 第二步: Render 部署后端

1. 打开 https://dashboard.render.com → New → Web Service
2. 连接 GitHub 仓库 (LuoX11a/SG_CampusSwap)
3. 配置:
   - **Name**: sg-campusswap-api
   - **Root Directory**: backend
   - **Runtime**: Python 3.11
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Health Check Path**: `/health`
4. 添加 Environment Variables（参考 .env.example）
5. 点击 Deploy

## 第三步: Vercel 部署前端

1. 打开 https://vercel.com → New Project
2. 导入 GitHub 仓库
3. 配置:
   - **Root Directory**: project/web
   - **Framework**: Next.js
   - **Build Command**: `npm run build`
4. 添加 Environment Variable:
   - `NEXT_PUBLIC_API_URL` = `https://sg-campusswap-api.onrender.com/api/v1`
5. 点击 Deploy → 获得域名 `https://sg-campusswap.vercel.app`

## 第四步: 配置 CORS

1. 去 Render Dashboard → sg-campusswap-api → Environment
2. 更新 `CORS_ORIGINS` = `http://localhost:3000,https://sg-campusswap.vercel.app`
3. 重新部署

## 第五步: 生成数据库表

```bash
# 本地操作（或通过 Render Shell）
cd backend
alembic revision --autogenerate -m "init"
alembic upgrade head
```

## 验证

```bash
# 1. 后端健康检查
curl https://sg-campusswap-api.onrender.com/health
# → {"status":"healthy","database":"connected"}

# 2. 前端访问
# 手机浏览器打开 https://sg-campusswap.vercel.app
# 应看到首页物品列表

# 3. API 文档
# 浏览器打开 https://sg-campusswap-api.onrender.com/docs
```

## Render 免费版注意事项

- 15 分钟无请求自动休眠，下次访问需等待 30-50 秒
- 每月 750 小时免费运行时间（够用）
- 如需避免休眠：用 https://cron-job.org 每 10 分钟 ping `/health`
