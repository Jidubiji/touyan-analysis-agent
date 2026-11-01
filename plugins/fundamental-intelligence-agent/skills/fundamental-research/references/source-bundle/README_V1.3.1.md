# Fundamental Intelligence Agent V1.3.1 — 使用说明

**主文件**：`AGENTS.md`（最新完整指令）。

**配套**：`signal_rules.yaml`（研究闸门，须由实现代码解释执行），`QA_TESTS.md`（T01–T89测试定义）、`V1.3.1_CHANGELOG.md`（本次更新）、`check_bundle.py`（静态检查）。

此补丁仅更新估值模块：对于盈利为正、可合理预测盈利的公司，以正常化FY1 Forward P/E作为主要观察值，列FY2及GAAP比较，尽可能评估过去3–5年同口径历史分位并在≥85%时提醒；交叉验证FCF、ROIC、CapEx及每股稀释。

使用真实数据前：配置已授权的公司披露、历史时点分析师一致预期和证券价格。不得把当前预测回填为历史时点预测。没有真实预测或跨阶段不可比则保留缺口，不应编造估值分位与目标价。

运行`python check_bundle.py`仅验证文件结构和规则参数，不代表Agent已跑通或估值判断正确。`AGENTS_V1.3_backup.md`、`signal_rules_V1.3_backup.yaml`与`QA_TESTS_V1.3_backup.md`可回滚到修改前的V1.3。
