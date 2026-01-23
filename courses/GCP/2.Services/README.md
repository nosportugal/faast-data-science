## Module 2: Infrastructure and Services ⚙️

### Powering Your Data Workflows

With a solid understanding of data storage, it's time to explore the core services that will process, manage, and serve your data. This module dives into the engine room of Google Cloud, covering everything from fundamental compute options to sophisticated tools for data orchestration and serverless computing.

You will learn how to build scalable data pipelines with Dataflow, orchestrate complex workflows with Cloud Composer, and deploy containerized applications with Cloud Run. These services are the building blocks for creating robust, automated, and efficient data science solutions on GCP.

### Learning Objectives

By the end of this module, you will be able to:

-   **Select** the appropriate Virtual Machine (VM) type for different computational needs.
-   **Understand** the use cases for both batch and streaming data processing with Dataflow.
-   **Orchestrate** complex data pipelines using Cloud Composer.
-   **Manage and deploy** containerized applications using Artifact Registry and Cloud Run.
-   **Decouple** system components effectively with the Pub/Sub messaging service.
-   **Grasp** the fundamentals of API management and cloud cost analysis.
-   **Reinforce** your practical skills in querying large datasets with BigQuery.
-   **Automate** the creation and management of cloud resources using Terraform (Infrastructure as Code).
-   **Understand** the fundamentals of container orchestration with Kubernetes.

---

### Learning Resources

#### 1. What are the VM types in GCP? And how to choose between them?

These videos explains the various types and families of virtual machines (VMs) in Google Compute Engine (GCE) and provides guidelines for selecting the right one for your workloads.

**[![Source: YouTube](https://img.youtube.com/vi/A2zZ86aYcmI/0.jpg)](https://www.youtube.com/watch?v=A2zZ86aYcmI)**

**[![Source: YouTube](https://img.youtube.com/vi/QZ8PmZjF9vw/0.jpg)](https://www.youtube.com/watch?v=QZ8PmZjF9vw)**


**Key Takeaways:**
*   Understand the different VM types and families in GCP.
*   Learn how to choose the appropriate VM for specific workloads.
*   Explore the role of GCE in hosting applications and workloads.

#### 2. Dataflow in a Minute

A quick overview of Google Cloud Dataflow, a fully managed streaming analytics service that minimizes latency and processing time for large-scale data tasks.

**[![Source: YouTube](https://img.youtube.com/vi/XdsuDOQ9nkU/0.jpg)](https://www.youtube.com/watch?v=XdsuDOQ9nkU)**

**Key Takeaways:**
*   Dataflow supports both batch and streaming data processing.
*   It offers autoscaling and cost optimization features.
*   Ideal for real-time analytics and data transformation.

#### 3. How to Use Cloud Composer for Data Orchestration

This video demonstrates how Cloud Composer, a managed Apache Airflow service, can be used to create, schedule, and monitor complex data workflows in Google Cloud.

**[![Source: YouTube](https://img.youtube.com/vi/3UfYwR3Uwgw/0.jpg)](https://www.youtube.com/watch?v=3UfYwR3Uwgw)**

**Key Takeaways:**
*   Cloud Composer simplifies data orchestration and workflow management.
*   Learn about its use cases and advantages for data processing.
*   Explore an example of how Cloud Composer can be applied in real-world scenarios.

#### 4. Intro to Dataproc

Learn about Dataproc and how you can leverage it to build your datapipelines.

**[![Source: YouTube 1](https://img.youtube.com/vi/lHYHXzFCF10/0.jpg)](https://www.youtube.com/watch?v=lHYHXzFCF10)**

**[![Source: YouTube 2](https://img.youtube.com/vi/HEQvXxTBuH4/0.jpg)](https://www.youtube.com/watch?v=HEQvXxTBuH4)**

**Key Takeaways:**
*   Understand the features of Cloud Dataproc as a managed service for running Spark and Hadoop clusters.
*   Learn how to quickly provision clusters and migrate existing Spark/Hadoop workloads.
*   Explore integrations with other GCP services and the key differences between Dataproc and Dataflow.

#### 5. Intro to Artifact Registry

Learn about Artifact Registry, the evolution of Container Registry, and its capabilities for managing container images and language packages, integrating seamlessly with CI/CD systems.

**[![Source: YouTube](https://img.youtube.com/vi/712Y0KpeHok/0.jpg)](https://www.youtube.com/watch?v=712Y0KpeHok)**

**Key Takeaways:**
*   Understand the features of Artifact Registry for managing artifacts.
*   Learn how to create and configure repositories.
*   Explore identity access controls and integration with CI/CD systems.

#### 6. Serverless

This video explores how serverless can be used to build powerful data pipelines.

**[![Source: YouTube](https://img.youtube.com/vi/PBw9vD_BO5A/0.jpg)](https://www.youtube.com/watch?v=PBw9vD_BO5A)**

**Key Takeaways:**
*   Understand the features of GCP's serverless options for running code, containers, or full applications without managing servers.
*   Learn to differentiate between Cloud Functions, Cloud Run, and App Engine to choose the correct service for a workload.
*   Explore event-driven triggers and patterns for integrating services using tools like Cloud Pub/Sub and Cloud Tasks.

#### 7. Cloud Run in a Minute

A concise overview of Cloud Run, a fully managed compute service for deploying and scaling containerized applications quickly and securely.

**[![Source: YouTube](https://img.youtube.com/vi/AL2rAmWFZjM/0.jpg)](https://www.youtube.com/watch?v=AL2rAmWFZjM)**

**Key Takeaways:**
*   Cloud Run simplifies running containerized workloads.
*   It automatically scales containers up and down based on demand.
*   You only pay for the resources used while your code is running.

#### 8. Intro to Apigee API Management

Discover how Apigee, Google Cloud's API management platform, helps organizations design, secure, deploy, and monitor APIs effectively.

**[![Source: YouTube](https://img.youtube.com/vi/vGe38icp0n4/0.jpg)](https://www.youtube.com/watch?v=vGe38icp0n4)**

**Key Takeaways:**
*   Learn the benefits of Apigee for API management.
*   Understand how Apigee supports both modern microservices and older backend services.
*   Explore the three key pillars of API management with Apigee.

#### 9. Cloud Pub/Sub in a Minute

A brief explanation of Cloud Pub/Sub, an asynchronous, scalable messaging service designed to decouple services that produce and consume events.

**[![Source: YouTube](https://img.youtube.com/vi/jLI-84UjZLE/0.jpg)](https://www.youtube.com/watch?v=jLI-84UjZLE)**

**Key Takeaways:**
*   Understand the concept of Pub/Sub and its primary use cases.
*   Learn how Pub/Sub enables real-time, reliable message delivery.
*   Explore its scalability and high availability features.

#### 10. Networking in a Minute

Discover how Virtual Private Cloud (VPC) provides the networking foundation for your resources, enabling you to connect them globally and secure them with firewall rules.

**[![Source: Video](https://docs.cloud.google.com/static/vpc-service-controls/images/service_perimeter_private.png)](https://www.cloudskillsboost.google/focuses/1229?catalog_rank=%7B%22rank%22%3A2%2C%22num_filters%22%3A0%2C%22has_search%22%3Atrue%7D&parent=catalog&search_id=42028897)**

**Key Takeaways:**
*   Explore the default VPC network
*   Create an auto mode network with firewall rules
*   Create VM instances using Compute Engine
*   Explore the connectivity for VM instances

#### 11. Terraform Explained in 15 Mins

An introductory tutorial on Terraform and its application as infrastructure as code, allowing you to define and provision infrastructure declaratively.

**[![Source: YouTube](https://img.youtube.com/vi/l5k1ai_GBDE/0.jpg)](https://www.youtube.com/watch?v=l5k1ai_GBDE)**

**Key Takeaways:**
*   What Terraform is and how it works.
*   The difference between Terraform and other tools like Ansible.
*   Basic commands and architecture of Terraform.

#### 12. Kubernetes Explained in 15 Minutes

A practical overview of Kubernetes, the industry-standard system for automating the deployment, scaling, and management of containerized applications.

**[![Source: YouTube](https://img.youtube.com/vi/r2zuL9MW6wc/0.jpg)](https://www.youtube.com/watch?v=r2zuL9MW6wc)**

**Key Takeaways:**
*   An explanation of containerization and orchestration.
*   A practical demonstration of a basic configuration in Kubernetes.
*   Recommended resources for deeper learning.

#### 13. Astro vs. Apache Airflow OSS

A comparison between Astro (a managed Airflow service) and open-source Apache Airflow for data orchestration, highlighting key differences.

**[![Source: Article](https://www.astronomer.io/images/vs-oss/astro-airflow-logos.svg?_cchid=5f1b974eadca9cef8d91d61c4ed99db2)](https://www.astronomer.io/astro-vs-apache-airflow-oss/)**

**Key Takeaways:**
*   Differences in functionality and architecture between Astro and Airflow.
*   Benefits of Astro for simplifying data pipeline operations.
*   Additional resources for exploring Astro.


#### Further reading
*   [System Design Primer - Scalability](https://github.com/donnemartin/system-design-primer#scalability) – High-level architecture thinking.
*   [GCP Compute Docs](https://cloud.google.com/compute/docs) – VMs, serverless, containers.
*   [Apache Beam Concepts](https://beam.apache.org/) – Dataflow pipelines.
*   [Cloud Composer / Airflow Docs](https://airflow.apache.org/docs/) – Orchestrate workflows.
*   [Kubernetes: Up & Running](https://www.oreilly.com/library/view/kubernetes-up-and/9781098110192/) – Core orchestration concepts.
*   [Cloud Run Docs](https://cloud.google.com/run/docs) – Containerized services.
*   [Event-Driven Architecture Patterns](https://cloud.google.com/architecture/event-driven-architectures) – Pub/Sub & serverless patterns.
*   [GCP Architecture Framework](https://cloud.google.com/architecture/framework) – Reference best practices.
*   [Site Reliability Engineering Book](https://sre.google/sre-book/table-of-contents/) - Google – Reliability & operations.
