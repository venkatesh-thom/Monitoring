# Episode 10 – Interview Answers

1. **Layer-specific alerts:** Tag metrics by service/tier, create alerts per job (`web`, `api`, `db`), and include dependency hints so responders immediately know which layer is faltering.
2. **Monitoring stateful services:** Track replication, WAL, disk I/O, connection pools, and long-running transactions; combine exporter metrics with query-level logging to capture slow queries and blocking chains.
3. **Sizing Prometheus:** Calculate target count × metrics × scrape frequency, ensure adequate CPU/RAM/SSD for TSDB, shard or use federation/remote-write when one instance cannot keep up.
4. **Rolling out routing changes:** Treat alertmanager config as code, stage updates in lower environments, use feature flags or canaries for new receivers, and monitor notification delivery before promoting globally.
5. **Keeping assets in sync:** Store dashboards, alerts, and runbooks in the same repo, tie updates to change requests, and automate CI checks that verify references (e.g., dashboards link to existing alerts/runbooks).
