#!/usr/bin/env python3
"""V1.3.1 static artifact checks. NOT an agent runtime or empirical performance test."""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
try:
    import yaml
except ImportError:
    print('ERROR: Requires PyYAML (pip install pyyaml)', file=sys.stderr)
    sys.exit(2)

errors = []

def test(condition, message):
    if not condition:
        errors.append(message)

required = ['AGENTS.md', 'signal_rules.yaml', 'QA_TESTS.md', 'V1.3_CHANGELOG.md', 'V1.3.1_CHANGELOG.md',
            'AGENTS_V1.2_backup.md', 'signal_rules_V1.2_backup.yaml', 'QA_TESTS_V1.2_backup.md']
for name in required:
    test((ROOT/name).is_file(), f'missing file: {name}')

agent = (ROOT/'AGENTS.md').read_text(encoding='utf-8')
qa = (ROOT/'QA_TESTS.md').read_text(encoding='utf-8')
config = yaml.safe_load((ROOT/'signal_rules.yaml').read_text(encoding='utf-8'))

test(agent.startswith('# Fundamental Intelligence Agent V1.3.1'), 'incorrect agent version')
test(config.get('ruleset_version') == '1.3.1', 'incorrect ruleset_version')
test('V1.3' in qa.splitlines()[0], 'incorrect QA version')
test(agent.count('```') % 2 == 0, 'unmatched markdown code fences')

modules = {
    'Module S': 'Business Regime Detection Engine',
    'Module B': 'Balanced Evidence & Backlog Integrity',
    'Module G': 'Organic Growth & Metric Definition Engine',
    'Module C': 'Capital Allocation & Shareholder Return',
    'Module V': 'Expectations & Valuation',
    'Module Q': 'Independent Evidence QA',
    'Module A': 'Anomaly & Inflection Engine',
    'Module M': 'Management Accountability Ledger',
    'Module X': 'Cross-Company Contradiction Engine',
    'Module P': 'Expectation Gap Engine',
    'Module R': 'Research Evolution Loop',
}
for module, label in modules.items():
    test(module in agent and label in agent, f'missing module or label: {module} {label}')

required_sections = ['research_mandate', 'regime_detection', 'history',
                     'evidence_balance', 'contract_quality', 'growth_quality',
                     'cash_and_capital', 'valuation_integrity', 'independent_qa',
                     'anomaly_detection', 'management_audit', 'cross_company',
                     'expectation_gap', 'signal_lifecycle', 'quality_gates']
for key in required_sections:
    test(key in config, f'missing YAML block: {key}')

test(config.get('evidence_balance',{}).get('require_best_support_best_counter_and_null') is True, 'missing opposing evidence gate')
test(config.get('contract_quality',{}).get('never_net_rpo_against_purchase_commitments') is True, 'missing RPO/commitment netting protection')
test(config.get('growth_quality',{}).get('key_metric_definition_check_always_even_if_no_regime_break') is True, 'missing KPI definition gate')
test(config.get('cash_and_capital',{}).get('require_gaap_net_income_to_ocf_indirect_bridge') is True, 'missing indirect cash flow bridge')
test(config.get('valuation_integrity',{}).get('enterprise_equity_denominator_mismatch', False) is not True, 'ambiguous valuation flag')
test('enterprise_equity_denominator_mismatch' in config.get('valuation_integrity',{}).get('blocked_if',[]), 'missing EV/equity mismatch blocker')
test(config.get('independent_qa',{}).get('default_agent_performance') == 'not_tested', 'incorrect default performance state')

ids = re.findall(r'^\| (T\d\d) \|', qa, flags=re.MULTILINE)
unique = set(ids)
expected = {f'T{i:02d}' for i in range(1,90)}
test(len(ids)==len(unique), 'duplicate test IDs')
test(unique==expected, f'test IDs mismatch: missing={sorted(expected-unique)}, extra={sorted(unique-expected)}')
test('T38–T73' in qa, 'missing V1.3 test group')
test('T74–T89' in qa, 'missing V1.3.1 test group')
test(config['valuation_integrity']['historical_forward_pe']['extreme_high_percentile_threshold'] == 85,'missing 85th percentile alert')
test(config['valuation_integrity']['profitable_company_primary_valuation']=='normalized_forward_fy1','missing normalized forward pe priority')
test('normalized_forward_PE_FY1' in agent and '历史同口径Forward P/E分位' in agent,'missing forward P/E methodology')
test('not_tested' in qa or '未执行' in qa, 'QA does not disclose unexecuted status')

print('Artifact structural checks:', 'PASS' if not errors else 'FAIL')
print(f'Modules listed: {len(modules)}; QA case definitions: {len(ids)}; Ruleset: {config.get("ruleset_version", "missing")}')
print('Scope: files/config/sections/test IDs only; no live data, model execution, blind backtest or agent accuracy validation.')
if errors:
    for e in errors:
        print(' -',e)
    sys.exit(1)
