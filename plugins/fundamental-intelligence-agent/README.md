# 基本面研究 Agent · Fundamental Intelligence Agent V1.3.1

面向上市公司财报深度复盘、电话会与分析师问答核验、管理层承诺、增长质量、产业链矛盾和有条件的前瞻估值。原始10份文件完整保留。

## 安装

把下面这句话发给自己的 Codex：

> 请从 https://github.com/Jidubiji/touyan-analysis-agent 安装基本面研究 Agent：注册或更新 jidubiji-research 插件市场，再安装 fundamental-intelligence-agent@jidubiji-research。保留已有插件和配置，使用我自己的 ChatGPT/Codex 账号，不创建 API Key 或服务器。

命令行首次安装：

```sh
codex plugin marketplace add https://github.com/Jidubiji/touyan-analysis-agent
codex plugin add fundamental-intelligence-agent@jidubiji-research
```

已添加市场的用户，先用 `codex plugin marketplace upgrade jidubiji-research` 更新，再安装新插件。完成后确认启用并打开新聊天，必要时刷新或重启桌面应用。客户端及组织的来源权限仍适用。

## 调用示例

- 使用 `$fundamental-research` 复盘 GOOGL 最新财报，核验有机增长、Cloud共享成本、合同需求及每股现金流，列出最强反证。
- 使用 `$fundamental-research` 研究 INTC 的经营阶段变化，保留旧厂折旧、债务和稀释，核对历史承诺及代工业务抵销。
- 使用 `$fundamental-research` 检验云厂商CapEx与上游订单是否矛盾，按产品、财季和时滞对齐，保留至少两种解释。

本插件独立于原“投研分析 Agent”，用明确技能名可指定新版流程；原插件内容保持原样。

## 数据、费用与验证范围

纯skill插件，在安装者自己的Codex运行。ChatGPT登录使用安装者账号/工作区额度；API Key登录按其自己的API账号计费。没有作者模型接口、MCP后台或服务器，作者电脑可以关机。财报、逐字稿、历史共识和行情依赖使用者提供的材料或授权工具，不附送付费数据订阅。

本版默认 `agent_performance: not_tested`。T01–T89是合成案例定义，尚未逐例运行；静态检查与安装成功不证明研究准确率。没有正常化EPS、可比历史快照或股权价值桥时，按原规范降级。

原始文件位于 `skills/fundamental-research/references/source-bundle/`，完整性清单为 `source-sha256.json`。在此插件目录执行打包静态检查：

```sh
python3 skills/fundamental-research/scripts/validate_bundle.py
```

需Python 3与PyYAML。该入口修正原检查器遗留的V1.2备份文件名，使用实际提供的V1.3备份；原始脚本未改动，直接运行仍会报告缺少旧备份。其它源文件遗留文字见[来源导航](skills/fundamental-research/references/source-guide.md)。

GitHub安装者能查看包内指令和知识文件。仓库分发不等于已上架OpenAI公共目录，不自动适用于ChatGPT网页/手机端。
