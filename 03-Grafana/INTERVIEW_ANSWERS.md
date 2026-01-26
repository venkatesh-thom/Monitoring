#  3 – Interview Answers

1. **Self-service Grafana:** It empowers product teams to explore data, reduces reporting backlog, and encourages ownership, whereas raw PromQL is steep for non-SRE stakeholders.
2. **Dashboard variables:** `label_values` fetches label values from a metric quickly, while `query` lets you run arbitrary PromQL; choose based on whether you need filtered label sets or advanced logic (e.g., regex or aggregations).
3. **Storage approaches:** In-DB dashboards are easy but harder to version control; provisioning from Git enables reviews, reproducible environments, and drift detection at the cost of a slightly steeper workflow.
4. **Securing Grafana:** Integrate SSO, enforce role-based access, segment data sources per tenant, rotate secrets, and use network controls (VPN, TLS) to keep dashboards from leaking sensitive metrics.
5. **Diagnosing cardinality:** Use panels that query `count_values`/`topk` on `__name__` or labels to reveal explosion, then adjust instrumentation or relabeling based on what Grafana visualizes.
