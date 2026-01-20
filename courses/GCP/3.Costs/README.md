## Module 3: Managing Costs, Security & Infrastructure 🏗️

### Building Robust and Responsible Solutions

Now that you're familiar with GCP's core data and infrastructure services, it's time to learn how to manage them responsibly and efficiently. Building powerful solutions is only half the battle; ensuring they are secure, cost-effective, and reproducible is what separates a good data scientist from a great one in a cloud environment.

This module focuses on the operational aspects of working with GCP. You will learn how to monitor your spending, secure your projects with Identity and Access Management (IAM), automate your infrastructure with Terraform, and ensure your data is protected with encryption. These are essential skills for building professional-grade, production-ready systems.

### Learning Objectives

By the end of this module, you will be able to:

-   **Analyze** cloud spending using GCP's billing reports and export billing data for deeper analysis.
-   **Implement** the principle of least privilege by configuring roles and permissions with Cloud IAM.
-   **Automate** the creation and management of cloud resources using Terraform (Infrastructure as Code).
-   **Understand** the fundamentals of container orchestration with Kubernetes.
-   **Secure** your data at rest by creating and managing encryption keys with Cloud KMS.
-   **Monitor** and debug your applications effectively using Cloud Logging.

---


### Learning Resources

#### 1. Analyze Billing Data and Cost Trends with Reports

This video explores how to use billing reports in Google Cloud to analyze costs and identify spending trends.

**[![Source: YouTube 1](https://img.youtube.com/vi/XR_d8u5AGyM/0.jpg)](https://www.youtube.com/watch?v=XR_d8u5AGyM)**

**[![Source: YouTube 2](https://img.youtube.com/vi/jRb8piwa2GI/0.jpg)](https://www.youtube.com/watch?v=jRb8piwa2GI)**

**[![Source: YouTube 3](https://img.youtube.com/vi/ZyMO9XabUUM/0.jpg)](https://www.youtube.com/watch?v=ZyMO9XabUUM)**

**Key Takeaways:**
*   How to access detailed cost reports in Google Cloud.
*   Identifying services that generate the highest costs.
*   Comparing daily costs and optimizing spending.
*   Best practices for exporting billing data to BigQuery for advanced analysis.

#### 2. What is Cloud IAM?

This video explains Identity and Access Management (IAM) in Google Cloud, the cornerstone of securing your resources.

**[![Source: YouTube](https://img.youtube.com/vi/xQClVtAECdg/0.jpg)](http://youtube.com/watch?v=xQClVtAECdg)**

**Key Takeaways:**
*   The difference between basic and predefined roles.
*   How to configure roles and service accounts for fine-grained security.
*   Best practices for organizing permissions in projects.

#### 3. Terraform Explained in 15 Mins

An introductory tutorial on Terraform and its application as infrastructure as code, allowing you to define and provision infrastructure declaratively.

**[![Source: YouTube](https://img.youtube.com/vi/l5k1ai_GBDE/0.jpg)](https://www.youtube.com/watch?v=l5k1ai_GBDE)**

**Key Takeaways:**
*   What Terraform is and how it works.
*   The difference between Terraform and other tools like Ansible.
*   Basic commands and architecture of Terraform.

#### 4. Kubernetes Explained in 15 Minutes

A practical overview of Kubernetes, the industry-standard system for automating the deployment, scaling, and management of containerized applications.

**[![Source: YouTube](https://img.youtube.com/vi/r2zuL9MW6wc/0.jpg)](https://www.youtube.com/watch?v=r2zuL9MW6wc)**

**Key Takeaways:**
*   An explanation of containerization and orchestration.
*   A practical demonstration of a basic configuration in Kubernetes.
*   Recommended resources for deeper learning.

#### 5. Astro vs. Apache Airflow OSS

A comparison between Astro (a managed Airflow service) and open-source Apache Airflow for data orchestration, highlighting key differences.

**[![Source: Article](https://www.astronomer.io/images/vs-oss/astro-airflow-logos.svg?_cchid=5f1b974eadca9cef8d91d61c4ed99db2)](https://www.astronomer.io/astro-vs-apache-airflow-oss/)**

**Key Takeaways:**
*   Differences in functionality and architecture between Astro and Airflow.
*   Benefits of Astro for simplifying data pipeline operations.
*   Additional resources for exploring Astro.

#### 6. Encryption with Cloud KMS Keys

This video demonstrates how to use the Cloud Key Management Service (KMS) to manage your own cryptographic keys for encrypting data in GCP.

**[![Source: YouTube](https://img.youtube.com/vi/WKZC93y-aWI/0.jpg)](https://www.youtube.com/watch?v=WKZC93y-aWI)**

**Key Takeaways:**
*   How to create encryption keys in Google Cloud.
*   The benefits of using customer-managed encryption keys for data security.
*   A practical demonstration of key configuration.

#### 7. Cloud Logging

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
