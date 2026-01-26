#  2 – Interview Answers

1. **Why Node Exporter first:** It gives instant host visibility (CPU, memory, disk) with almost zero engineering effort, but it still misses app-level metrics and black-box availability, so you must layer additional telemetry later.
2. **Target up/down semantics:** Prometheus marks a target `up` when a scrape succeeds before the timeout; shorter `scrape_interval` improves detection speed but increases resource usage and can create more alert noise if thresholds are too tight.
3. **Static vs discovery:** Static configs are simple and deterministic for labs, while service discovery scales automatically but needs tagging conventions, ACLs, and extra infrastructure (Consul, Kubernetes, etc.).
4. **Sizing storage:** Estimate samples per second (`targets × metrics × scrape interval`) and multiply by retention goals; keep head-room for spikes and consider remote storage if retention exceeds what a single Prometheus can hold.
5. **Validating metrics:** Compare values against OS tools (`top`, `free`, `df`), run load experiments, and enforce metric review checklists so you trust the data before wiring dashboards or alerts.
