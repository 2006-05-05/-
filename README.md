# 码上爬 - 爬虫实战练习项目
本项目为个人爬虫学习实战案例，所有案例均提供 **Python + Node.js 双版本代码**。
涵盖网页请求、数据解析、JS逆向、CryptoJS 加密解密等常见爬虫基础知识点，仅用于编程学习研究。

## 项目结构
├── cases/                # 所有爬虫练习代码（.py/.js）
├── .gitignore            # Git 忽略文件配置
├── package.json          # Node.js 依赖管理
├── requirements.txt      # Python 依赖管理
└── README.md             # 项目说明文档

## 环境依赖安装

### 1. Python 环境
安装 Python 所需依赖：
pip install -r requirements.txt
依赖包含：`requests`、`execjs`

运行 JS 脚本**必须先安装依赖**：
npm install
依赖包含：`crypto-js`

## 运行方式

### 运行 Python 爬虫
cd cases

python 对应脚本名.py

### 运行 Node.js 爬虫
cd cases

node 对应脚本名.js

## 项目内容说明

项目包含多套完整爬虫练习案例：

- 基础网页数据抓取
- 接口数据解析
- JS 逆向加密分析
- CryptoJS 加密模拟
- Python 与 JS 代码对照实现

## 免责声明

本仓库所有代码**仅用于学习交流**。
禁止用于商业用途、违规爬取、批量采集等违法行为，使用本代码产生的一切后果由使用者自行承担。
请严格遵守目标网站 `robots` 协议及国家网络安全法律法规。
