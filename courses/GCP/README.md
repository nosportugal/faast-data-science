# FAAST Advance Data Science - GCP

![FAAST logo](/images/FAAST_preto.png)

---

## Welcome to the GCP for Data Scientists Learning Path ☁️🎉

Welcome to the official repository for the "GCP for Data Scientists: From Foundations to MLOps" learning path.

This course offers a pragmatic, hands-on introduction to the Google Cloud Platform, designed specifically for data scientists, machine learning engineers, and data analysts looking to scale their workflows in the cloud. We'll start with the fundamentals of cloud data management and infrastructure, and progressively build towards advanced MLOps and machine learning services on GCP.

### Course Philosophy

### Course Philosophy

This course follows the **Ken Thompson philosophy**: simple, direct, each topic teaches one thing well. We focus on foundational concepts that work on any cloud, then show practical implementation with GCP.

**Our Principles:**

-   **Cloud-Agnostic Fundamentals**: Learn universal patterns and principles first (databases, distributed systems, infrastructure as code, MLOps). These concepts apply to AWS, Azure, or any cloud.
-   **One Concept, One Topic**: Each section teaches one thing thoroughly. Master the fundamentals before moving to advanced topics.
-   **GCP Implementation**: After learning concepts, see how they're implemented in Google Cloud. Understand both the "why" and the "how".
-   **Industry-Standard Resources**: Learn from the best - Martin Kleppmann, Chip Huyen, Google SRE books, MIT/CMU courses, and proven GitHub repositories.
-   **Production-Ready**: This isn't just theory. Learn operational practices for cost, security, reliability, and scale.

### Methodology

This is a self-paced learning path with 4 modules. Each module:
1. **Teaches core concepts** (cloud-agnostic)
2. **Shows GCP implementation** (vendor-specific)
3. **Includes hands-on practice** (real projects)
4. **References top resources** (books, courses, GitHub repos)

Estimated time: **8-12 hours** total, but take as long as you need to practice and internalize concepts.

---

### Curriculum

Here is the breakdown of the topics covered in each module:

#### 1. Cloud Databases & Storage: The Foundation ~ 3 hours

Learn database fundamentals that apply to any cloud, then implement them with GCP services. Master the difference between transactional and analytical databases, understand data classification, and choose the right storage solution.

**Core Concepts (Cloud-Agnostic):**
-   Database types: Relational, columnar, document, key-value
-   OLTP vs OLAP workloads
-   Object storage patterns
-   Data governance principles

**GCP Implementation:**
-   Cloud Storage (buckets, lifecycle policies)
-   BigQuery (columnar data warehouse)
-   Cloud SQL, Spanner, Firestore, Bigtable
-   Dataplex (data governance)

**Key Resources**: CMU Database Systems course, "Designing Data-Intensive Applications", GCP documentation

---

#### 2. Infrastructure & Core Services ~ 2-3 hours

Understand compute models, container orchestration, and event-driven architecture. These patterns work on any cloud - learn the concepts, then see GCP's implementation.

**Core Concepts (Cloud-Agnostic):**
-   VMs vs Containers vs Serverless
-   Kubernetes fundamentals
-   Data pipeline patterns (batch & streaming)
-   Apache Airflow for orchestration
-   Pub/Sub messaging patterns

**GCP Implementation:**
-   Compute Engine, GKE, Cloud Run
-   Dataflow (Apache Beam), Dataproc (Spark)
-   Cloud Composer (managed Airflow)
-   Pub/Sub, Artifact Registry

**Key Resources**: Kubernetes: Up & Running (Kelsey Hightower), System Design Primer, Google SRE book

---

#### 3. Managing Costs, Security & Infrastructure as Code ~ 2-3 hours

Learn operational excellence: automate everything, secure by default, measure everything. These SRE and DevOps practices are cloud-universal.

**Core Concepts (Cloud-Agnostic):**
-   Infrastructure as Code with Terraform
-   IAM and least privilege security
-   Cost optimization patterns
-   Site Reliability Engineering (SRE) principles
-   Observability (logs, metrics, traces)

**GCP Implementation:**
-   Terraform with Google Provider
-   Cloud IAM
-   Cost management tools
-   Cloud KMS for encryption
-   Cloud Logging and Monitoring

**Key Resources**: HashiCorp Learn, Google SRE Book, Terraform best practices, FinOps Foundation

---

#### 4. Data Science & MLOps in GCP ~ 4-6 hours

Production ML is software engineering. Learn MLOps principles that apply everywhere, then use GCP's ML platform. Build systems, not just notebooks.

**Core Concepts (Cloud-Agnostic):**
-   MLOps lifecycle and best practices
-   Model versioning and experiment tracking
-   CI/CD for ML
-   Model monitoring and drift detection
-   ML deployment patterns

**GCP Implementation:**
-   BigQuery ML (SQL-based ML)
-   Vertex AI (unified ML platform)
-   Pre-trained ML APIs
-   Model deployment options
-   Looker Studio for visualization

**Key Resources**: Chip Huyen's "Designing ML Systems", Full Stack Deep Learning, Stanford CS 329S


---

### Key Skills You'll Acquire

Upon completing this course, you will have a comprehensive understanding of:

**Foundational Skills (Any Cloud):**
-   Database design patterns and when to use each type
-   Distributed systems concepts (scalability, reliability, consistency)
-   Container orchestration with Kubernetes
-   Infrastructure automation with Terraform
-   Security best practices and IAM patterns
-   Cost optimization strategies
-   Site Reliability Engineering (SRE) principles
-   MLOps best practices and production ML systems

**GCP-Specific Skills:**
-   Implementing solutions with BigQuery, Cloud Storage, and GCP databases
-   Building data pipelines with Dataflow and Dataproc
-   Deploying applications on GKE and Cloud Run
-   Managing infrastructure with Terraform on GCP
-   Training and deploying ML models with Vertex AI
-   Monitoring and observability with Cloud Operations

**Most Importantly:** You'll learn principles and patterns that work on any cloud provider. The GCP implementations are examples - you'll be able to adapt these concepts to AWS, Azure, or any other platform.

---

### Recommended Learning Path

**For Complete Beginners:**
1. Start with Module 1 (Databases)
2. Work through modules sequentially
3. Complete hands-on labs after each module
4. Build a capstone project combining all concepts

**For Experienced Engineers:**
1. Review module objectives to identify gaps
2. Focus on cloud-agnostic concepts first
3. Skim GCP-specific implementation sections
4. Jump to hands-on practice quickly

**For ML Engineers/Data Scientists:**
1. Modules 1-3 provide essential context
2. Module 4 is the main focus
3. But don't skip operations and infrastructure!
4. Production ML requires all these skills

---

### Additional Resources

**Essential Reading:**
- "Designing Data-Intensive Applications" by Martin Kleppmann
- "Site Reliability Engineering" by Google (free online)
- "Designing Machine Learning Systems" by Chip Huyen
- "Kubernetes: Up & Running" by Kelsey Hightower et al.

**Top GitHub Repositories:**
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Awesome Database Learning](https://github.com/pingcap/awesome-database-learning)
- [Awesome MLOps](https://github.com/visenger/awesome-mlops)
- [Learning Cloud](https://github.com/lynnlangit/learning-cloud)
- [Terraform Best Practices](https://github.com/antonbabenko/terraform-best-practices)

**Free Courses:**
- MIT 6.5840: Distributed Systems
- CMU 15-445: Database Systems (Andy Pavlo)
- Stanford CS 329S: ML Systems Design
- Full Stack Deep Learning

**GCP Resources:**
- [GCP Architecture Center](https://cloud.google.com/architecture)
- [GCP Best Practices](https://cloud.google.com/architecture/framework)
- [Qwiklabs Hands-On Labs](https://www.cloudskillsboost.google/)

---

We are excited to have you on this journey to mastering cloud architecture, infrastructure, and machine learning operations. Remember: learn the fundamentals, practice relentlessly, build real projects, and never stop learning.

**Start with Module 1** and begin your transformation into a cloud-native data scientist!
