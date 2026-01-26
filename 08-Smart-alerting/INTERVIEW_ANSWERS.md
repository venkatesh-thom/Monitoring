# Episode 8 – Interview Answers

1. **Reducing alert fatigue:** Prioritize SLO-based alerts, add deduplication/grouping, route informational events to chat, and continually prune alerts that never trigger or never drive action.
2. **Multi-burn-rate design:** Evaluate fast windows (e.g., 5m) for early detection and slow windows (1h/6h) for accuracy, combining them with different thresholds to page only when both indicate SLO burn.
3. **Routing warnings vs critical:** Chat notifications keep teams informed without paging, while critical alerts escalate via PagerDuty/on-call; ensure documentation so engineers know how to promote/demote severities responsibly.
4. **Histograms vs summaries:** Histograms aggregate well across instances and feed heatmaps, making them ideal for backend latency; summaries provide client-side quantiles but cannot be aggregated across replicas.
5. **Managing labeled metrics:** Limit enumerations (`warning`, `critical`), avoid per-user labels, and monitor `cardinality` via Prometheus tooling so that added dimensions stay bounded.
