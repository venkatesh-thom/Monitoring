# Episode 4 – Interview Answers

1. **Alert lifecycle:** Prometheus evaluates rules, transitions alert states (pending→firing), pushes notifications to Alertmanager, which deduplicates, groups, silences, and sends them to receivers like Slack or PagerDuty.
2. **Preventing alert storms:** Group alerts by service, use inhibition rules, deduplicate via Alertmanager, and design dependency-aware alerts so a shared outage pages once instead of per-instance.
3. **Evaluation vs `for` duration:** Evaluation frequency defines how often expressions run; `for` requires a condition to stay true for a period, filtering flaps but increasing detection latency—tune both based on SLOs and risk tolerance.
4. **Routing strategies:** Match on labels such as `team`, `service`, `severity`, or `region` to send notifications to the right channels, and chain routes so warnings notify dev chat while critical pages reach on-call phones.
5. **Testing alerts:** Use unit tests (promtool), run synthetic metric pushes in staging, leverage temporary recording rules, or fire controlled chaos experiments to verify rules before production paging.
