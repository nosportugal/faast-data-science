## Module 1: Cloud Databases & Storage 💾

### The Foundation of Data

Every data science project begins with data. This module teaches you how to store, manage, and access data in the cloud. We start with foundational database concepts that apply to any cloud provider, then focus on practical implementation with Google Cloud services.

**Philosophy**: Each section teaches one core concept. Master the fundamentals before moving to vendor-specific implementations.

### Learning Objectives

By the end of this module, you will be able to:

-   **Understand** fundamental database types and when to use each (concepts apply to any cloud)
-   **Classify** data types and choose appropriate storage solutions
-   **Design** scalable storage architectures using cloud-agnostic patterns
-   **Implement** these patterns using GCP services (Cloud Storage, BigQuery, Cloud SQL)
-   **Apply** data governance principles for production systems

---

### Learning Resources

#### 1. Database Fundamentals (Cloud-Agnostic)

**Topic**: Understanding database types and when to use each

**[CMU Database Systems Course - Andy Pavlo (YouTube Playlist)](https://www.youtube.com/playlist?list=PLSE8ODhjZXjbj8BMuIrRcacnQh20hmY9g)**

One of the best database courses in the world. Start with lectures 1-3 for fundamentals: relational model, SQL, and storage concepts. These principles apply to any cloud database system.

**Key Concepts:**
*   Relational, document, columnar, and key-value databases
*   ACID properties and transaction management
*   When to use OLTP vs OLAP databases
*   Trade-offs in database design (consistency, availability, partition tolerance)

**Supplementary Reading:**  
[Designing Data-Intensive Applications](https://dataintensive.net/) by Martin Kleppmann (Chapter 1-3) - Industry standard for understanding database systems at scale.

---

#### 2. Types of Data: Structured, Semi-structured, Unstructured

**Topic**: One concept - classifying data to choose the right storage

**[![Source: YouTube](https://img.youtube.com/vi/bcvt22A_G9Y/0.jpg)](https://www.youtube.com/watch?v=bcvt22A_G9Y)**

**Key Takeaways:**
*   Structured: Fixed schema (SQL databases, Spanner)
*   Semi-structured: Flexible schema (JSON in Firestore, MongoDB)
*   Unstructured: No schema (files in object storage)
*   Match data type to storage system for optimal performance

---

#### 3. Object Storage: The Foundation

**Topic**: Understanding cloud object storage (applies to S3, Azure Blob, GCS)

**[![Storage Classes](https://img.youtube.com/vi/wNOs3LlsH6k/0.jpg)](https://www.youtube.com/watch?v=wNOs3LlsH6k)**

**[Google Cloud Storage Documentation](https://cloud.google.com/storage/docs)**

**Key Concepts:**
*   Object storage vs block storage vs file storage
*   Storage classes: Hot (Standard), Cool (Nearline), Cold (Coldline), Archive
*   Cost optimization through lifecycle policies
*   Multi-regional vs regional storage for availability

**Practical Exercise**: [GCP Cloud Storage Quick Start](https://cloud.google.com/storage/docs/quickstart-console)

---

#### 4. Analytical Databases: BigQuery

**Topic**: Columnar databases for analytics (one thing: fast aggregation queries)

**[![BigQuery Intro](https://img.youtube.com/vi/BH_7_zVk5oM/0.jpg)](https://cloud.google.com/bigquery/docs/introduction#bigquery-video-tutorials)**

**Why Columnar Databases:**
*   Store data by column, not row
*   Excellent for aggregations (SUM, AVG, COUNT)
*   Poor for transactional updates
*   Examples: BigQuery (GCP), Redshift (AWS), Synapse (Azure)

**[BigQuery Best Practices](https://cloud.google.com/bigquery/docs/best-practices)**

**Key Takeaways:**
*   Partitioning and clustering for performance
*   Query optimization techniques
*   Cost management with slots and reservations
*   Integration with data science tools (Python, notebooks)

**Architecture Pattern**: [GCP Data Analytics Reference Architecture](https://cloud.google.com/architecture/reference-patterns)

---

#### 5. Choosing the Right GCP Database

**Topic**: Decision framework for database selection

**[![Database Decision Tree](https://cloud.google.com/static/architecture/images/hybrid-multicloud-patterns/architectures.svg)](https://cloud.google.com/products/databases)**

**Decision Framework:**
1. **Transactional (OLTP)**: Cloud SQL (PostgreSQL/MySQL), Cloud Spanner (global scale)
2. **Analytical (OLAP)**: BigQuery (data warehouse)
3. **Document/NoSQL**: Firestore (documents), Bigtable (wide-column, time-series)
4. **In-Memory/Cache**: Memorystore (Redis, Memcached)

**[GCP Database Decision Tool](https://cloud.google.com/architecture/database-decision)**

**Read**: [Comparing GCP database services](https://bluexp.netapp.com/blog/gcp-cvo-blg-google-cloud-database-the-right-service-for-your-workloads)

---

#### 6. Data Governance with Dataplex

**Topic**: Managing data across distributed systems

**[![Dataplex Overview](https://img.youtube.com/vi/bbFeAt7cw1g/0.jpg)](https://www.youtube.com/watch?v=bbFeAt7cw1g)**

**Key Concepts:**
*   Data catalog and metadata management
*   Data quality monitoring
*   Access controls and compliance
*   Unified view of data lakes and warehouses

**When to use**: Multi-zone data infrastructure, regulatory compliance requirements, large data teams

---

### Hands-On Practice

**Start Here**: [GCP Data Analytics Codelab](https://codelabs.developers.google.com/codelabs/cloud-bigquery-python)

1. Create a Cloud Storage bucket
2. Load CSV data into BigQuery
3. Run analytical queries
4. Export results

**Time**: 30-45 minutes

### Further Reading

- **Book**: "Designing Data-Intensive Applications" - Martin Kleppmann (Chapters 1-4)
- **GitHub**: [Awesome Database Learning](https://github.com/pingcap/awesome-database-learning)
- **GCP**: [Architecture Center - Data Lifecycle](https://cloud.google.com/architecture/data-lifecycle-cloud-platform)
