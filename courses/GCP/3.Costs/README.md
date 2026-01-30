## Module 3: Managing Costs, Security & Infrastructure 🏗️

### Building Robust and Responsible Solutions

Now that you're familiar with GCP's core data and infrastructure services, it's time to learn how to manage them responsibly and efficiently. Building powerful solutions is only half the battle; ensuring they are secure, cost-effective, and reproducible is what separates a good data scientist from a great one in a cloud environment.

This module focuses on the operational aspects of working with GCP. You will learn how to monitor your spending, secure your projects with Identity and Access Management (IAM), automate your infrastructure with Terraform, and ensure your data is protected with encryption. These are essential skills for building professional-grade, production-ready systems.

### Learning Objectives

By the end of this module, you will be able to:

-   **Analyze** cloud spending using GCP's billing reports and export billing data for deeper analysis.
-   **Implement** the principle of least privilege by configuring roles and permissions with Cloud IAM.
-   **Secure** your data at rest by creating and managing encryption keys with Cloud KMS.
-   **Monitor** and debug your applications effectively using Cloud Logging.

---

### Learning Resources

#### 1. Optimizing Costs in BigQuery

This module covers BigQuery cost optimization through query efficiency, data scan reduction, and table design techniques.

**[![Source: YouTube 1](https://img.youtube.com/vi/y0ZTg2Ckjz4/0.jpg)] (https://www.youtube.com/watch?v=y0ZTg2Ckjz4)**

**[![Source: YouTube 2](https://img.youtube.com/vi/iz6lxi9BczA/0.jpg)] (https://www.youtube.com/watch?v=iz6lxi9BczA)**
Article: cloud.google.com/blog/topics/developers-practitioners/bigquery-admin-reference-guide-query-optimization

**[![Source: YouTube 3](https://img.youtube.com/vi/cZgTavxWO2k/0.jpg)] (https://www.youtube.com/live/cZgTavxWO2k?si=NMk57zwDnflYsIjp&t=792)**
Note: Watch the video from 13 to 42 minutes.

**Key Takeaways:**
*   Difference between returned data vs processed data
*   Partitioned tables – concept and impact on cost
*   Clustering — when it helps and when it doesn't
*   BigQuery pricing overview
*   On-demand vs capacity pricing (slots)
*   Good organizational practices

#### 2. Optimizing Costs in Cloud Run and Compute Engine

This module covers compute cost optimization using Cloud Run and Compute Engine configuration and resource tuning strategies.

**[![Source: YouTube 4](https://img.youtube.com/vi/Oywj7ammIaw/0.jpg)] (https://www.youtube.com/watch?v=Oywj7ammIaw)**

**[![Source: YouTube 5](https://img.youtube.com/vi/oBH7fBkqMfk/0.jpg)] (https://www.youtube.com/watch?v=oBH7fBkqMfk)**

**[![Source: YouTube 6](https://img.youtube.com/vi/1FPkXkZ1D5E/0.jpg)] (https://www.youtube.com/watch?v=1FPkXkZ1D5E)**
Note: Watch the video until 32 minutes.

**Key Takeaways:**
*   How Cloud Run works
*   Price components (CPU, RAM, time, requests)
*   VM cost model

#### 3. Analyze Billing Data and Cost Trends with Reports

This video explores how to use billing reports in Google Cloud to analyze costs and identify spending trends.

**[![Source: YouTube 1](https://img.youtube.com/vi/XR_d8u5AGyM/0.jpg)](https://www.youtube.com/watch?v=XR_d8u5AGyM)**

**[![Source: YouTube 2](https://img.youtube.com/vi/jRb8piwa2GI/0.jpg)](https://www.youtube.com/watch?v=jRb8piwa2GI)**

**[![Source: YouTube 3](https://img.youtube.com/vi/ZyMO9XabUUM/0.jpg)](https://www.youtube.com/watch?v=ZyMO9XabUUM)**

**Key Takeaways:**
*   How to access detailed cost reports in Google Cloud.
*   Identifying services that generate the highest costs.
*   Comparing daily costs and optimizing spending.
*   Best practices for exporting billing data to BigQuery for advanced analysis.

#### 4. What is Cloud IAM?

This video explains Identity and Access Management (IAM) in Google Cloud, the cornerstone of securing your resources.

**[![Source: YouTube](https://img.youtube.com/vi/xQClVtAECdg/0.jpg)](http://youtube.com/watch?v=xQClVtAECdg)**

**Key Takeaways:**
*   The difference between basic and predefined roles.
*   How to configure roles and service accounts for fine-grained security.
*   Best practices for organizing permissions in projects.

#### 5. Encryption with Cloud KMS Keys

This video demonstrates how to use the Cloud Key Management Service (KMS) to manage your own cryptographic keys for encrypting data in GCP.

**[![Source: YouTube](https://img.youtube.com/vi/WKZC93y-aWI/0.jpg)](https://www.youtube.com/watch?v=WKZC93y-aWI)**

**Key Takeaways:**
*   How to create encryption keys in Google Cloud.
*   The benefits of using customer-managed encryption keys for data security.
*   A practical demonstration of key configuration.

#### 6. Cloud Logging

Explains how to use Cloud Logging to monitor, troubleshoot, and manage logs from all your applications and services running on Google Cloud.

**[![Source: YouTube](https://img.youtube.com/vi/gyDp-Cl_MdA/0.jpg)](https://www.youtube.com/watch?v=gyDp-Cl_MdA)**

**Key Takeaways:**
*   How to configure basic and advanced log queries.
*   Using the Logs Router to sink logs to different destinations.
*   Best practices for monitoring and alerting on errors.

#### Further Reading
*   [GCP Billing & Cost Analysis Videos](https://www.youtube.com/watch?v=XR_d8u5AGyM) – Track usage, read reports, spot high-cost services.
*   [FinOps Foundation - Cloud Financial Management](https://www.finops.org/framework/) – Principles for cost control and cloud finance.
*   [Terraform Tutorials for Cost-Aware Infrastructure](https://developer.hashicorp.com/terraform/tutorials) – Build IaC while monitoring cost impact.
*   [Terraform Best Practices GitHub](https://github.com/antonbabenko/terraform-best-practices) – Efficient, versioned IaC patterns.
*   [GCP Architecture Guides GitHub](https://github.com/GCP-Architecture-Guides) – Cost-conscious reference cloud architectures.
