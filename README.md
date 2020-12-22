短网址服务，是一个能够将冗长的网址转换缩短为更简短、方便的短网址的工具。

经过短网址服务缩短的网址很短很容易使用和传播。

例如我们经常会在营销短信中会看到短网址。

本项目使用 Serverless 创建一个简单的短网址服务。

## 使用的技术
### 使用的产品与服务：
* Serverless Framework：一个免费开源的 Serverless 框架。
* Tencent SCF：腾讯云云函数服务。
* Lambda Store：全球第一个 Serverless Redis 服务。

### 语言及框架：
* Python 3.6
* Flask：一个微型的 Python 开发的 Web 框架。

## 部署
通过 npm 全局安装 Serverless 命令行工具：
```bash
$ npm install -g serverless
```

部署到腾讯云 SCF：
```bash
$ serverless deploy
```

## 参考
* https://registry.serverless.com/package/flask-starter
* https://github.com/serverless-components/tencent-flask
* https://github.com/LordGhostX/fauna-url-shortener
