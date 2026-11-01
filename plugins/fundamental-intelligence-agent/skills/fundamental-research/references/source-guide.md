# V1.3.1 来源导航

`source-bundle/`保存用户提供的全部10个文件，逐字节保留。SHA256见插件根目录`source-sha256.json`。

| 文件 | 用途 |
|---|---|
| [AGENTS.md](source-bundle/AGENTS.md) | 现行规范：§0–1问题/输入，§2来源，§2.1 S阶段，§2.2 B证据/合同，§2.3 G增长/KPI，§2.4 C资本/每股现金，§2.5 V估值，§2.6 Q审计，§3阶段，§3.0–3.4 A/M/X/P/R，§4证据格式，§5输出，§6行业，§8闸门，§11协议，§12配置。 |
| [signal_rules.yaml](source-bundle/signal_rules.yaml) | 现行1.3.1初筛及闸门，需由研究流程解释执行。 |
| [QA_TESTS.md](source-bundle/QA_TESTS.md) | T01–T89合成案例定义，未附实测日志。 |
| [README_V1.3.1.md](source-bundle/README_V1.3.1.md) | 原始交付说明。 |
| [V1.3.1_CHANGELOG.md](source-bundle/V1.3.1_CHANGELOG.md) | 现行估值补丁及未测试状态。 |
| [check_bundle.py](source-bundle/check_bundle.py) | 原始静态检查器；直接运行会因寻找未提供的V1.2备份而失败。 |
| [AGENTS_V1.3_backup.md](source-bundle/AGENTS_V1.3_backup.md) | 历史规范，仅版本比较/回滚时读取。 |
| [signal_rules_V1.3_backup.yaml](source-bundle/signal_rules_V1.3_backup.yaml) | 历史1.3.0规则。 |
| [QA_TESTS_V1.3_backup.md](source-bundle/QA_TESTS_V1.3_backup.md) | 历史73个案例定义。 |
| [V1.3_CHANGELOG.md](source-bundle/V1.3_CHANGELOG.md) | 历史说明，其中V1.2清单不代表本次实际文件清单。 |

打包适配不修改原件：

- `scripts/validate_bundle.py`由原校验器适配，资源根指向`references/source-bundle/`，将3个遗留V1.2备份名换为实际提供的V1.3备份名，其它原检查逻辑保留。
- 原规范§12的1.3.0及YAML标题V1.3为遗留文字；现行规范标题、补丁和实际`ruleset_version: '1.3.1'`一致，旧版本不覆盖补丁。
- 数据库、模型执行器、持续监控为实现建议，本插件未部署。案例实测与历史样本外验证仍未完成。
