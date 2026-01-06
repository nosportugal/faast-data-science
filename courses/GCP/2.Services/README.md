## Module 2: Infrastructure and Services ⚙️

### Building Scalable Systems

This module teaches core infrastructure concepts that apply to any cloud, then shows practical implementation with GCP. Learn to think about compute, containers, orchestration, and messaging as universal patterns.

**Philosophy**: Master one concept at a time. Understand the "why" before the "how". Learn patterns that work on any cloud, then apply them to GCP.

### Learning Objectives

By the end of this module, you will be able to:

-   **Understand** fundamental compute models: VMs, containers, serverless (cloud-agnostic concepts)
-   **Design** scalable architectures using industry-standard patterns
-   **Implement** data pipelines for batch and streaming processing
-   **Orchestrate** workflows using Apache Airflow principles (Cloud Composer on GCP)
-   **Deploy** containerized applications following 12-factor app principles
-   **Architect** event-driven systems with pub/sub messaging patterns

---

### Learning Resources

#### 1. Compute Fundamentals: VMs, Containers, Serverless

**Topic**: Three compute models - understanding trade-offs

**[System Design Primer - Scalability](https://github.com/donnemartin/system-design-primer#scalability)**

**Core Concepts (Cloud-Agnostic):**
*   **Virtual Machines**: Full OS control, persistent, stateful (EC2, Compute Engine, Azure VMs)
*   **Containers**: Portable, lightweight, consistent environments (Docker everywhere)
*   **Serverless**: Zero infrastructure management, pay-per-use (Lambda, Cloud Functions, Azure Functions)

**Decision Framework:**
- VMs: Legacy apps, full OS control, long-running processes
- Containers: Microservices, consistent environments, Kubernetes orchestration
- Serverless: Event-driven, short-lived tasks, extreme scale

**GCP Implementation:**

**[![Compute Engine Basics](https://img.youtube.com/vi/_5tqGhu7V-4/0.jpg)](https://www.youtube.com/watch?v=_5tqGhu7V-4)**

**Key Takeaways:**
*   Machine families: General-purpose, compute-optimized, memory-optimized
*   Right-sizing for cost optimization
*   Preemptible VMs for batch processing

**Read**: [GCP Compute Documentation](https://cloud.google.com/compute/docs)

---

#### 2. Containers and Kubernetes Fundamentals

**Topic**: Understanding container orchestration (one concept: managing containers at scale)

**[Kubernetes: Up & Running](https://www.oreilly.com/library/view/kubernetes-up-and/9781098110192/)** by Kelsey Hightower (Industry standard book)

**[Kubernetes the Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way)** (GitHub) - Learn by building from scratch

**[![Kubernetes Explained](https://img.youtube.com/vi/r2zuL9MW6wc/0.jpg)](https://www.youtube.com/watch?v=r2zuL9MW6wc)**

**Core Concepts:**
*   Pods, Services, Deployments (universal to any Kubernetes)
*   Declarative configuration (desired state)
*   Self-healing and auto-scaling
*   Works on GKE, EKS, AKS - same principles

**GCP: Google Kubernetes Engine (GKE)**
- Managed Kubernetes with Google SRE practices
- Autopilot mode for hands-off operations
- Integration with GCP services

**GitHub Resources:**
- [Kubernetes Examples](https://github.com/kubernetes/examples)
- [Awesome Kubernetes](https://github.com/ramitsurana/awesome-kubernetes)

---

#### 3. Serverless: Cloud Run and Cloud Functions

**Topic**: Deploying containers and functions without managing infrastructure

**[![Serverless on GCP](https://img.youtube.com/vi/PBw9vD_BO5A/0.jpg)](https://www.youtube.com/watch?v=PBw9vD_BO5A)**

**[![Cloud Run](https://img.youtube.com/vi/AL2rAmWFZjM/0.jpg)](https://www.youtube.com/watch?v=AL2rAmWFZjM)**

**Serverless Spectrum (Universal Pattern):**
1. **Functions-as-a-Service**: Single-purpose functions (Cloud Functions, Lambda, Azure Functions)
2. **Containers-as-a-Service**: Full apps in containers (Cloud Run, AWS Fargate, Azure Container Instances)
3. **Platform-as-a-Service**: Complete frameworks (App Engine, Heroku, Azure App Service)

**When to Use:**
- Event-driven workloads (file uploads, API requests)
- Variable traffic (scale-to-zero capability)
- Reduced operational complexity

**[Cloud Run Documentation](https://cloud.google.com/run/docs)**

---

#### 4. Data Processing: Batch and Streaming

**Topic**: Processing data at scale (one pattern: unified batch and streaming)

**Apache Beam Concepts** (Cloud-agnostic framework):
- Write once, run anywhere (Dataflow, Spark, Flink)
- Unified programming model
- Windows, triggers, watermarks for streaming

**[![Dataflow Overview](https://img.youtube.com/vi/XdsuDOQ9nkU/0.jpg)](https://www.youtube.com/watch?v=XdsuDOQ9nkU)**

**GCP Implementations:**
- **Dataflow**: Managed Apache Beam (serverless)
- **Dataproc**: Managed Spark/Hadoop (VM-based)

**[![Dataproc](https://img.youtube.com/vi/lHYHXzFCF10/0.jpg)](https://www.youtube.com/watch?v=lHYHXzFCF10)**

**Decision Guide:**
- Dataflow: New projects, unified batch/streaming, auto-scaling
- Dataproc: Existing Spark/Hadoop code, granular control

**[GCP Data Processing Reference Architectures](https://cloud.google.com/architecture/reference-patterns/overview)**

---

#### 5. Workflow Orchestration with Apache Airflow

**Topic**: Scheduling and monitoring data pipelines (one tool: Airflow everywhere)

**[![Cloud Composer](https://img.youtube.com/vi/3UfYwR3Uwgw/0.jpg)](https://www.youtube.com/watch?v=3UfYwR3Uwgw)**

**Apache Airflow Fundamentals** (Cloud-Agnostic):
- Directed Acyclic Graphs (DAGs) for workflow definition
- Operators for different tasks (Python, SQL, sensors)
- Extensible with custom operators
- Runs on GCP (Composer), AWS (MWAA), Azure (Data Factory), self-hosted

**Cloud Composer = Managed Airflow on GCP**

**Best Practices:**
- Idempotent tasks (rerunnable)
- Separate configuration from code
- Monitor task duration and failures

**Resources:**
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [Awesome Apache Airflow](https://github.com/jghoman/awesome-apache-airflow)

---

#### 6. Messaging and Event-Driven Architecture

**Topic**: Decoupling systems with async messaging (universal pattern)

**[![Cloud Pub/Sub](https://img.youtube.com/vi/jLI-84UjZLE/0.jpg)](https://www.youtube.com/watch?v=jLI-84UjZLE)**

**Pub/Sub Pattern** (Works everywhere):
- Publishers send messages to topics
- Subscribers consume from subscriptions
- Decouples producers and consumers
- Examples: Pub/Sub (GCP), SNS/SQS (AWS), Service Bus (Azure), Kafka (self-hosted)

**Key Concepts:**
*   At-least-once delivery semantics
*   Message ordering (when needed)
*   Dead-letter topics for failures
*   Fan-out patterns for multiple consumers

**Use Cases:**
- Stream processing pipelines
- Microservices communication
- Event-driven serverless
- Log aggregation

**[Event-Driven Architecture Patterns](https://cloud.google.com/architecture/event-driven-architectures)**

---

#### 7. Container Registry and Artifact Management

**Topic**: Managing build artifacts (one practice: version control for binaries)

**[![Artifact Registry](https://img.youtube.com/vi/712Y0KpeHok/0.jpg)](https://www.youtube.com/watch?v=712Y0KpeHok)**

**Universal Concepts:**
*   Container image registries (Docker Hub, ECR, ACR, Artifact Registry)
*   Versioning and tagging strategies
*   Vulnerability scanning
*   Integration with CI/CD

**GCP Artifact Registry:**
- Supports Docker, Maven, npm, Python packages
- Regional and multi-regional repositories
- IAM integration for access control

---

### Hands-On Practice

**System Design Exercise**: Design a scalable data processing pipeline
1. Data ingestion (Pub/Sub)
2. Processing (Dataflow)
3. Storage (BigQuery)
4. Orchestration (Composer)

**Practical Labs:**
- [GCP Qwiklabs - Cloud Run](https://www.cloudskillsboost.google/focuses/5161)
- [Kubernetes Basics Tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Dataflow Templates](https://cloud.google.com/dataflow/docs/guides/templates/provided-templates)

**Time**: 2-3 hours

### Further Reading

- **Book**: "Site Reliability Engineering" by Google - [Free Online](https://sre.google/sre-book/table-of-contents/)
- **Book**: "System Design Interview" by Alex Xu - Chapter 1-4
- **GitHub**: [System Design Primer](https://github.com/donnemartin/system-design-primer)
- **GitHub**: [Learning Cloud](https://github.com/lynnlangit/learning-cloud)
- **GCP**: [Architecture Framework](https://cloud.google.com/architecture/framework)
