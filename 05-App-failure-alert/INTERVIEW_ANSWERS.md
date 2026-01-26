#  5 – Interview Answers

1. **White-box benefits:** They expose internal states (queues, code paths) so you can detect issues before they manifest externally, while black-box checks only see symptoms and may miss root-cause data.
2. **Metric type selection:** Counters for monotonically increasing events, Gauges for values that go up/down (memory), Histograms for latency distributions, and Summaries for client-side quantiles when aggregation isn’t required.
3. **Distinguishing blips vs failures:** Combine rate/ratio metrics with `for` durations and multi-window checks so the alert fires only when both a percentage and absolute count stay elevated.
4. **Controlling cardinality:** Limit unbounded labels (user ids, request ids), prefer enumerable enums, and enforce instrumentation reviews so labels reflect stable dimensions like service or region.
5. **Validating alerts:** Replay known failure scenarios, run load scripts, or temporarily manipulate metrics (via `fail_mode` or test endpoints) to confirm alerts fire and resolve with the expected timeline and messaging.
