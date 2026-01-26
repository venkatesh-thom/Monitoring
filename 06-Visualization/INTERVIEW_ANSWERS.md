#  6 – Interview Answers

1. **Actionable dashboards:** They surface key signals (golden metrics), include thresholds or alert overlays, and provide context/runsbooks so responders know what to do instead of just seeing pretty charts.
2. **Many vs single dashboards:** Use smaller, role-specific dashboards when audiences differ, but maintain an executive/overview board for shared situational awareness; avoid monolithic boards that become slow or cluttered.
3. **Handling cardinality visually:** Aggregate with PromQL (`sum by`, `topk`), use heatmaps or histograms, and offer filters/templating so viewers can scope down without rendering thousands of lines.
4. **Source control for dashboards:** Store JSON/YAML in Git to enable code review, change tracking, and CI validation—especially vital when multiple teams collaborate or compliance requires audit trails.
5. **Annotations and links:** Automatic annotations from Alertmanager plus panel links to runbooks or logs shorten MTTR by guiding responders straight from symptoms to diagnostics.
