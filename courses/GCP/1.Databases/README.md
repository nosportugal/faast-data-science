## Module 1: Cloud Databases & Storage 💾

### The Foundation of Data

Welcome to the first module! Every data science project begins with data, and understanding how to effectively store, manage, and access it in the cloud is a fundamental skill. This foundational module covers the most critical aspect of any data science project: data storage and management.

Here, you will explore the landscape of database technologies available on Google Cloud. You'll learn to distinguish between different data structures and select the optimal service for your specific needs, from handling unstructured files in Cloud Storage to running massive analytical queries in BigQuery.

### Learning Objectives

By the end of this module, you will be able to:

-   **Differentiate** between various database types (Relational, Columnar, Document) and their primary use cases.
-   **Classify** data as structured, semi-structured, or unstructured and map them to the appropriate GCP service.
-   **Configure** Google Cloud Storage buckets, including setting locations and storage classes for cost and performance optimization.
-   **Choose** the most suitable Google Cloud database service for different workloads.
-   **Perform** large-scale data analysis using the core features of BigQuery.
-   **Understand** the role of Dataplex in unifying and governing distributed data.

---

### Learning Resources

#### 1. Types of Databases: Relational, Columnar, Document, and More

This video explores various types of databases, such as relational, columnar, document, and graph, highlighting their core features and ideal use cases.

**[![Source: YouTube](https://img.youtube.com/vi/VfcRxtBKI54/0.jpg)](https://www.youtube.com/watch?v=VfcRxtBKI54)**

**Key Takeaways:**
*   Differences between database types.
*   Use cases for each type of database.
*   How to choose the right database for your needs.

#### 2. Structured, Semi-structured, and Unstructured Data

Learn to differentiate between types of data and discover which Google Cloud products are best suited for storing and managing each of them.

**[![Source: YouTube](https://img.youtube.com/vi/bcvt22A_G9Y/0.jpg)](https://www.youtube.com/watch?v=bcvt22A_G9Y)**

**Key Takeaways:**
*   Definitions of structured, semi-structured, and unstructured data.
*   Google Cloud products for each data type.
*   Practical examples of data storage solutions.

#### 3. Bucket Options in Cloud Storage

Learn how to configure buckets in Google Cloud Storage, including critical settings like location options and storage classes, to optimize for performance, cost, and compliance.

**[![Source: YouTube 1](https://img.youtube.com/vi/wNOs3LlsH6k/0.jpg)](https://www.youtube.com/watch?v=wNOs3LlsH6k)**

**[![Source: YouTube 2](https://img.youtube.com/vi/8DMOJ6Lgm7s/0.jpg)](https://www.youtube.com/watch?v=8DMOJ6Lgm7s)**

**Key Takeaways:**
*   Bucket configuration options.
*   Types of locations (Regional, Multi-regional) and storage classes (Standard, Nearline, etc.).
*   Best practices for managing sensitive data in buckets.

#### 4. Choosing the Right Database

This video explains the key differences between structured and unstructured storage and provides guidance on how to choose the best cloud solution for your data.

**[![Source: YouTube](https://img.youtube.com/vi/CIW8baJqBes/0.jpg)](https://www.youtube.com/watch?v=CIW8baJqBes)**

**Key Takeaways:**
*   Comparison of structured vs. unstructured storage.
*   Cloud storage solutions in Google Cloud.

#### 5. Google Cloud Database: Choosing the Right Service

This article provides a detailed overview of the main database services offered by Google Cloud and a framework for choosing the best one for your workloads.

**[![Source: Article](https://cloud.google.com/static/architecture/images/hybrid-multicloud-patterns/architectures.svg)](https://bluexp.netapp.com/blog/gcp-cvo-blg-google-cloud-database-the-right-service-for-your-workloads)**

**Key Takeaways:**
*   Comparison of key database services in Google Cloud (e.g., Cloud SQL, Spanner, Bigtable).
*   Features and benefits of each service.
*   How to optimize database selection for different scenarios (transactional, analytical).

#### 6. Introduction to BigQuery

Learn about BigQuery, Google's fully-managed, petabyte-scale analytical data warehouse, and how to use it for querying massive datasets with incredible speed.

**[![Source: YouTube](https://img.youtube.com/vi/q9npE47O2UI/0.jpg)](https://www.youtube.com/watch?v=q9npE47O2UI)**

**[![Source: Google Cloud](https://img.youtube.com/vi/BH_7_zVk5oM/0.jpg)](https://cloud.google.com/bigquery/docs/introduction#bigquery-video-tutorials)**

**Key Takeaways:**
*   Setting up and using the BigQuery interface.
*   Examples of SQL queries and integration with other tools.
*   The core benefits of BigQuery for large-scale data analysis.

#### 7. Google BigQuery vs. SQL Server

This article provides a technical comparison between Google BigQuery and a traditional data warehouse like SQL Server, highlighting their architectural differences and use cases.

**[![Source: Article](https://res.cloudinary.com/hevo/images/c_scale,w_648,h_345/f_webp,q_auto:best/v1685950115/hevo-learn-1/Google-BigQuery-Vs-SQL-Server-FI/Google-BigQuery-Vs-SQL-Server-FI.png?_i=AA)](https://hevodata.com/learn/bigquery-vs-sql-server/)**

**Key Takeaways:**
*   Differences in performance, architecture, and scalability.
*   A look at analytical features and native machine learning support.
*   When to choose BigQuery over SQL Server, and vice-versa.

#### 8. What is Dataplex?

Discover how Dataplex can help you unify distributed data, automate data management and governance, and power analytics at scale in a secure and unified way.

**[![Source: YouTube](https://img.youtube.com/vi/bbFeAt7cw1g/0.jpg)](https://www.youtube.com/watch?v=bbFeAt7cw1g)**

**Key Takeaways:**
*   Unifying metadata and enabling data discovery across lakes and warehouses.
*   Automating data management processes like quality checks and lifecycle policies.
*   Integrating with analytics tools for scalable, governed insights.

#### Further Reading
*   [CMU Database Systems Course](https://www.youtube.com/playlist?list=PLSE8ODhjZXjbj8BMuIrRcacnQh20hmY9g) - Andy Pavlo – Core database concepts.
*   [BigQuery Intro](https://cloud.google.com/bigquery/docs/introduction#bigquery-video-tutorials) – SQL-based analytics & ML.
*   [Comparing GCP Database Services](https://bluexp.netapp.com/blog/gcp-cvo-blg-google-cloud-database-the-right-service-for-your-workloads) – Pick the right service.
*   [Designing Data-Intensive Applications](https://dataintensive.net/) - Martin Kleppmann – Fundamentals for reliable data systems.
*   [Awesome Database Learning GitHub](https://github.com/pingcap/awesome-database-learning) – Curated DB resources.
*   [GCP Architecture Center - Data Lifecycle](https://cloud.google.com/architecture/data-lifecycle-cloud-platform) – Reference best practices.
