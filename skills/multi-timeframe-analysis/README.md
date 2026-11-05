# 多周期分析

用于 Codex 的中文 skill，结合周线背景、日线主结构与 60 分钟辅助确认，研究股票和 ETF 的波段机会。默认按新做多、持有 1—3 个月分析，可按用户目标调整。

## 安装

把下面这句话发给你自己的 Codex。

> 请使用 skill-installer 从 https://github.com/Jidubiji/touyan-analysis-agent/tree/main/skills/multi-timeframe-analysis 安装 multi-timeframe-analysis。安装后告诉我如何调用。如果已有同名技能，先比较内容并说明更新范围。

使用默认 Codex 配置目录、且已具备系统 skill-installer 时，也可以执行以下命令。

```sh
python3 "$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo Jidubiji/touyan-analysis-agent \
  --path skills/multi-timeframe-analysis
```

使用自定义 `CODEX_HOME` 时，将安装器路径中的 `$HOME/.codex` 替换为实际配置目录。安装器会在已有同名目录时停止，请先比较本地改动再更新。安装完成后可在下一轮对话调用。

## 调用示例

```text
使用 $multi-timeframe-analysis 完整分析 KO，计划持有 1—3 个月。
请展示周线、日线、60 分钟图，在价格与 MACD 上标注日期、价位、
交叉和前后动量峰谷，并说明当前状态、关键区域与转强或转弱条件。
```

也可以提供已有仓位、成本、计划持仓时间和具体问题，调整观察尺度与条件。

## MACD 标注内容

- 三个周期默认都带 MACD 面板，标明参数、零轴、DIF、DEA、柱体定义及最新数值。
- 用同时间轴或竖虚线连接价格与动量，区分价格极值和指标极值的实际发生时间。
- 比较相应价格波段的动量峰谷，标出与判断有关的交叉和中间变化。
- 对接近零的微小交叉、未完成 K 线、最新拐点和背离线索说明确认状态。
- 近期事件密集时，增加价格与 MACD 配对放大图。

## 数据与运行条件

行情来自安装者自己可调用的授权工具或提供的 OHLCV 文件。获取日线、小时线及指标预热历史后，核验复权、时段、交易日和跨周期聚合。缺少某个周期时，输出会说明可用范围及限制。

绘图需要安装者环境中的量化绘图库、中文字体和可用计算工具。可使用 pandas、Matplotlib、TA-Lib，或已核对口径的同类实现。MACD 默认采用收盘价和 DIF−DEA 柱体。

该技能用于行情研究与图表输出。研究结论采用可观察的条件，实际交易与持续监控需要用户明确指令。市场数据服务由安装者自行取得。

## 文件

- [SKILL.md](SKILL.md) 为技能入口。
- [MACD 研判与标注](references/macd-annotations.md) 说明对应关系、微小交叉、峰谷比较与检查方法。
- [数据与来源核验](references/data-and-sources.md) 说明行情口径、聚合与计算约定。
- [图表与交付规范](references/charts-and-delivery.md) 说明默认图组、视觉检查和完整输出。

## 验证范围

本次发布检查技能结构、引用路径、界面元数据及安装目录布局。KO 图表迭代用于明确标注要求，跨标的研究效果与策略表现仍需进一步验证。
