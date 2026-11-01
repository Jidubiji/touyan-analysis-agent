# 投研分析 Agent · 季度笔记

![投研分析 Agent 图标](plugins/touyan-analysis-agent/assets/logo.png)

面向美股上市公司的中文估值与产业链研究插件。版本 **0.1.3**。

这是通过 GitHub 分发的纯 skill 插件，供其他人安装到自己的 **Codex 桌面版／CLI**。
使用者用自己的 ChatGPT 账号登录 Codex，消耗自己的账号／工作区额度。作者不提供模型 API、MCP 后台、服务器或付费行情订阅，作者电脑不需要在线。

## 最简单的安装方法

把下面这句话发给你自己的 Codex：

> 请从 https://github.com/hongyuning/touyan-analysis-agent 安装投研分析插件，按 README 注册插件市场并安装 touyan-analysis-agent@jidubiji-research。保留我现有的插件和配置，使用我自己的 ChatGPT/Codex 登录运行，不新建 API Key 或服务器。完成后告诉我如何在新聊天调用。

Codex 会在你的本机执行安装，可能根据本机权限要求确认。

## 命令行安装

已安装当前 Codex CLI 的用户可以执行：

```sh
codex plugin marketplace add https://github.com/hongyuning/touyan-analysis-agent
codex plugin add touyan-analysis-agent@jidubiji-research
```

然后在桌面应用的插件页确认“投研分析 Agent”已安装、启用，并打开新聊天使用；如果客户端要求刷新，重启桌面应用。

若提示命令不存在，请更新 Codex 或让自己的 Codex 按官方本地插件市场流程安装。企业／学校账号还受管理员的插件和来源策略限制。

[官方插件市场文档](https://developers.openai.com/plugins/build/plugins) · [CLI 命令文档](https://learn.chatgpt.com/docs/developer-commands)

## 使用示例

安装后在新聊天中选择“投研分析 Agent”，再发送：

- **公司估值**：分析 MSFT 的投资价值，按完整估值框架输出，并给出下一步研究方向。
- **产业链研究**：研究 AI 半导体产业链的瓶颈、利润池、核心受益路径和证伪指标。
- **分部估值**：对 AMZN 做 SOTP，列清分部价值、净现金调节及敏感性。

仅输入股票代码时，默认进入完整公司估值；包含产业链关键词时，进入产业链模式。完整报告包含下一步研究方向，署名“季度笔记”。

## 包含的研究框架

- 估值 SOP v2.0：根据商业模式选择估值方法，核验资料时效，区分独立假设与管理层执行情景。
- 适用的相对估值、现金流估值、SOTP、反向估值和敏感性分析。
- 产业链供需、瓶颈、议价权、利润池、受益路径与反证研究。
- 重大信息后的重新估值，以及按优先级排列的下一步研究问题。
- 六份原始知识文件完整保留在 `plugins/touyan-analysis-agent/skills/touyan-research/references/`。

## 额度、数据与使用范围

- 以自己的 ChatGPT 账号登录 Codex时，使用自己的账号／工作区额度；如果自行使用 API Key 登录，则由该 Key 对应账号计费。
- 插件不包含作者的模型 API Key，也不调用作者的后台或服务器。
- 最新市场数据依赖使用者自己的检索能力或已授权工具；无法核验的新数据须明确披露，不能编造。
- 研究输出不保证收益，不执行交易。
- 这是 GitHub 仓库分发，尚未上架 OpenAI 公共插件目录。安装不会自动使插件在 ChatGPT 网页或手机端可用。
- 包内指令和知识文件可由安装者查看。

## 下载与更新

[下载整个仓库 ZIP](https://github.com/hongyuning/touyan-analysis-agent/archive/refs/heads/main.zip)

更新插件市场后，按客户端的更新／重新安装提示处理：

```sh
codex plugin marketplace upgrade jidubiji-research
```

## 验证范围

发布前已核对插件市场结构、资源路径、15 个插件文件与现行候选版逐字节一致，以及 6 份原始知识文件 SHA256。
本机 Codex CLI 0.164.0 已能识别该市场中的 0.1.3 插件。文件校验值见 `source-sha256.json`。
尚未在所有接收者环境实装，也未完成实时股票研究效果验收。
