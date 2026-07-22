# SG CampusSwap — Week 10 最终项目报告

> 项目: SG CampusSwap — 新加坡大学校园二手交易平台
> 日期: 2026-07-22
> 演示日期: 2026-08-07

---

## 项目概述

SG CampusSwap 是一个面向新加坡大学学生的校园二手物品交易平台。学生可以使用大学邮箱注册，在校园内发布、浏览和交易二手物品。

## 技术架构

| 层级 | 技术 | 部署平台 |
|------|------|------|
| 前端 | Next.js 14 + TypeScript + Tailwind CSS | Vercel |
| 后端 | FastAPI + Python 3.11 | Render |
| 数据库 | PostgreSQL | Neon |
| 实时通信 | Firebase Firestore | Google Cloud |
| 图片存储 | Cloudinary | Cloudinary |
| 邮件 | SendGrid | SendGrid |

## 功能清单

### 已完成 ✅
- 大学邮箱注册/验证/登录 (JWT Token)
- 物品发布/编辑/删除/状态管理
- 物品浏览（分页/筛选/排序/搜索）
- 用户资料查看/编辑
- 交易评价系统
- 图片上传 (Cloudinary)
- 实时聊天 (Firebase)
- **移动端响应式适配** (PWA + 底部导航)
- Docker 容器化
- CI/CD Pipeline

### 待完成 ⚠️
- 前端 Jest 组件测试
- AWS EC2 部署（备选方案）
- 可用性测试 (10-15 名学生)
- 数据库 Alembic 迁移生成

## 移动端适配

- 响应式布局: 桌面侧栏 / 手机底部 Tab Bar
- PWA: 可添加到手机主屏幕
- Service Worker: 离线缓存
- iOS 安全区适配
- 触控友好: 44px 最小触摸区

## 部署方案

采用 Vercel (前端) + Render (后端) + Neon (数据库) 免费方案:
- 前端: https://sg-campusswap.vercel.app
- 后端: https://sg-campusswap-api.onrender.com
- API 文档: https://sg-campusswap-api.onrender.com/docs

详见 `DEPLOY_GUIDE.md`

## 代码统计

| 模块 | 文件数 | 代码行数 |
|------|:---:|:---:|
| 后端 API 路由 | 7 | ~1400 |
| 后端 Service | 4 | ~600 |
| 后端 Models | 3 | ~150 |
| 后端 Schemas | 3 | ~130 |
| 后端测试 | 9 | ~1000 |
| 前端页面 | 15 | ~2500 |
| 前端组件 | 7 | ~800 |
| 前端 Stores | 4 | ~400 |
| Docker 配置 | 3 | ~50 |
| **总计** | **~60** | **~7000** |

## 成员贡献

| 成员 | 角色 | 主要贡献 |
|------|------|------|
| Huang Hongrui | PM | 项目管理/风险登记/Sprint规划/会议记录 |
| Wang Bowei | Backend Lead | API路由/Docker/CI-CD/部署 |
| Wang Xu | Backend Dev | Service层/测试/Firebase聊天 |
| Renxian Tang | Frontend Lead | Next.js框架/核心页面/状态管理/移动端改造 |
| Jiahai Xiong | Frontend Dev | 扩展页面/Chat/Profile/FilterModal |
| Junliang Li | QA/UX | 设计系统/测试计划/可用性测试设计 |

## 演示准备清单

- [ ] 部署后端到 Render
- [ ] 部署前端到 Vercel
- [ ] 配置 Neon 数据库
- [ ] 运行数据库迁移
- [ ] 测试用户注册/登录流程
- [ ] 测试物品发布/浏览流程
- [ ] 测试聊天功能
- [ ] 手机端 UI 检查
- [ ] PWA "添加到主屏幕"测试
- [ ] 准备演示账号
- [ ] 准备演示物品数据

## 已知限制

1. Render 免费版 15 分钟无请求休眠（首次访问慢 30-50 秒）
2. Firebase 聊天需要配置 Service Account
3. Cloudinary 上传需要配置 API Key
4. SendGrid 邮件验证需要配置 API Key
