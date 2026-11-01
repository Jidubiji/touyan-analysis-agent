# 季度笔记 · 投研插件

在自己的 Codex 中安装、使用的中文投研插件，共用一个 GitHub 插件市场 **jidubiji-research**。

| 插件 | 当前版本 | 适用任务 | 安装名称 |
|---|---|---|---|
| [投研分析 Agent](plugins/touyan-analysis-agent/) | 0.1.3 | 美股完整估值、DCF/SOTP、产业链利润池与下一步研究方向。 | `touyan-analysis-agent@jidubiji-research` |
| [基本面研究 Agent](plugins/fundamental-intelligence-agent/) | 1.3.1 | 财报/电话会复盘、管理层承诺、增长质量、经营拐点、产业链反证及前瞻估值。 | `fundamental-intelligence-agent@jidubiji-research` |

两个插件独立安装，原估值插件内容保持原样。新插件基于 **Fundamental Intelligence Agent V1.3.1**，完整保留用户提供的10个文件。

## 最简单的安装方法

把对应句子发给自己的 Codex：

**安装新版基本面研究插件：**

> 请从 https://github.com/Jidubiji/touyan-analysis-agent 安装基本面研究 Agent：注册或更新 jidubiji-research 插件市场，再安装 fundamental-intelligence-agent@jidubiji-research。保留已有插件和配置，使用我自己的 ChatGPT/Codex 账号，不创建 API Key 或服务器。安装后告诉我如何在新聊天调用。

**安装原估值插件：**

> 请从 https://github.com/Jidubiji/touyan-analysis-agent 安装投研分析插件：注册或更新 jidubiji-research 插件市场，再安装 touyan-analysis-agent@jidubiji-research。保留已有插件和配置，使用我自己的 ChatGPT/Codex 登录，不新建 API Key 或服务器。完成后告诉我如何在新聊天调用。

Codex会按接收者本机权限完成安装；企业/学校账号还受管理员策略限制。

## 命令行安装

首次使用此市场：

```sh
codex plugin marketplace add https://github.com/Jidubiji/touyan-analysis-agent
```

已经添加过此市场，先更新目录：

```sh
codex plugin marketplace upgrade jidubiji-research
```

按需要安装一个或两个插件：

```sh
codex plugin add fundamental-intelligence-agent@jidubiji-research
codex plugin add touyan-analysis-agent@jidubiji-research
```

在桌面应用插件页确认已启用，打开新聊天使用；如客户端提示刷新，重启应用。若没有相关命令，请更新Codex或让自己的Codex按[官方插件市场流程](https://developers.openai.com/plugins/build/plugins)处理。

## 使用示例

- **新版财报研究**：使用 `$fundamental-research` 复盘 GOOGL 最新财报，核验增长质量、历史承诺、产业链反证和每股现金流，并说明证据缺口。
- **新版经营阶段研究**：使用 `$fundamental-research` 研究 INTC 的经营阶段变化，核对分部抵销、旧资本负担与每股价值。
- **原公司估值**：使用 `$touyan-research` 分析 MSFT 的投资价值，输出完整估值报告和下一步研究方向。
- **原产业链研究**：使用 `$touyan-research` 研究 AI 半导体产业链的瓶颈、利润池、受益路径和证伪指标。

原插件仅输入股票代码默认公司估值，完整报告包含下一步研究方向、署名“季度笔记”。明确技能名可以指定使用哪一套流程。

## 额度与数据

- ChatGPT登录Codex使用自己的账号/工作区额度；自行选择API Key登录则按该Key账号计费。
- 两个插件均为纯skill包，没有作者模型API、MCP后台或服务器，作者电脑无需在线。
- 数据依赖使用者提供的文件、检索能力或自己的授权工具；不附带付费行情、逐字稿或一致预期订阅。无法核验的数据须披露缺口。
- 研究不保证收益，不执行交易；安装者可查看包内指令及知识文件。
- 这是GitHub仓库分发，尚未上架OpenAI公共目录，不自动在ChatGPT网页或手机端可用。

## 下载、更新与验证

[下载整个仓库 ZIP](https://github.com/Jidubiji/touyan-analysis-agent/archive/refs/heads/main.zip)

使用 `codex plugin marketplace upgrade jidubiji-research` 更新目录，再按客户端提示更新或重新安装所需插件。

原估值插件15个文件保持原样，其6份原始知识文件校验值见根目录 `source-sha256.json`。新版10份原件校验值见 `plugins/fundamental-intelligence-agent/source-sha256.json`。

新版提供静态文档/配置校验器；89个合成案例仅为定义，未完成真实财报研究效果、逐例Agent实测或历史样本外验收，`agent_performance`保持 `not_tested`。具体范围和源文件遗留项见[新版说明](plugins/fundamental-intelligence-agent/README.md)。
