## Module 3: Managing Costs, Security & Infrastructure 🏗️

### Operating Production Systems

Building systems is one thing. Operating them reliably, securely, and cost-effectively is another. This module teaches operational excellence through infrastructure as code, security principles, and reliability engineering practices that work on any cloud.

**Philosophy**: Automate everything. Measure everything. Secure by default. These principles transcend any specific cloud provider.

### Learning Objectives

By the end of this module, you will be able to:

-   **Automate** infrastructure provisioning with Terraform (works on AWS, Azure, GCP)
-   **Implement** security best practices using IAM and least privilege principles
-   **Monitor** costs and optimize spending across cloud services
-   **Design** resilient systems following SRE principles
-   **Manage** secrets and encryption keys properly
-   **Observe** system behavior with logging and monitoring

---

### Learning Resources

#### 1. Infrastructure as Code with Terraform

**Topic**: Automate infrastructure - one language for all clouds

**[HashiCorp Learn - Terraform](https://developer.hashicorp.com/terraform/tutorials)** (Official tutorials - best place to start)

**[Terraform Learning Journey](https://github.com/siliney/terraform-learning-journey)** (GitHub) - Hands-on examples

**[![Terraform Explained](https://img.youtube.com/vi/l5k1ai_GBDE/0.jpg)](https://www.youtube.com/watch?v=l5k1ai_GBDE)**

**Core Concepts** (Cloud-Agnostic):
*   Declarative configuration (describe desired state)
*   State management (tracking infrastructure)
*   Providers for any platform (AWS, Azure, GCP, Kubernetes)
*   Modules for reusable infrastructure components
*   Plan, apply, destroy lifecycle

**Why Terraform:**
- Write once, deploy to any cloud
- Version control your infrastructure
- Reproducible environments (dev, staging, prod)
- Review changes before applying (terraform plan)

**Best Practices:**
- Store state remotely (GCS, S3, Azure Blob)
- Use modules for common patterns
- Never commit secrets to git
- Use workspaces for environments

**[Terraform Best Practices](https://github.com/antonbabenko/terraform-best-practices)**

**GCP-Specific:**
- [Google Provider Documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
- [GCP Terraform Examples](https://github.com/terraform-google-modules)

---

#### 2. Security: Identity and Access Management (IAM)

**Topic**: Least privilege access control (universal security principle)

**[![Cloud IAM](https://img.youtube.com/vi/xQClVtAECdg/0.jpg)](http://youtube.com/watch?v=xQClVtAECdg)**

**IAM Principles** (Apply to any cloud):
*   **Identity**: Who (users, service accounts, groups)
*   **Roles**: What permissions (read, write, admin)
*   **Resources**: Where (projects, buckets, databases)
*   **Least Privilege**: Give minimum necessary access

**Best Practices:**
1. Use service accounts for applications (not user accounts)
2. Create custom roles for specific needs
3. Regularly audit permissions
4. Use groups to manage access at scale
5. Enable MFA for human users

**Security Model:**
```
Identity + Role + Resource = Permission
```

**GCP IAM:**
- Predefined roles (Viewer, Editor, Owner)
- Custom roles for fine-grained control
- Resource hierarchy (Organization > Folder > Project)

**[GCP IAM Best Practices](https://cloud.google.com/iam/docs/best-practices)**

---

#### 3. Cost Management and Optimization

**Topic**: Understanding and controlling cloud spending

**[![Billing Analysis](https://img.youtube.com/vi/XR_d8u5AGyM/0.jpg)](https://www.youtube.com/watch?v=XR_d8u5AGyM)**

**[![Cost Optimization](https://img.youtube.com/vi/jRb8piwa2GI/0.jpg)](https://www.youtube.com/watch?v=jRb8piwa2GI)**

**Universal Cost Patterns:**
*   Compute: Right-size instances, use spot/preemptible VMs
*   Storage: Lifecycle policies, tiered storage classes
*   Data Transfer: Minimize cross-region traffic
*   Idle Resources: Auto-shutdown dev/test environments

**Cost Management Strategy:**
1. **Visibility**: Export billing to BigQuery for analysis
2. **Budgets**: Set alerts before overspending
3. **Quotas**: Prevent runaway costs
4. **Tagging**: Track spending by project/team
5. **Reserved Capacity**: Commit for discounts (when stable)

**GCP Tools:**
- Billing reports and dashboard
- Committed Use Discounts (CUDs)
- Sustained Use Discounts (automatic)
- Cost allocation with labels

**[FinOps Foundation](https://www.finops.org/)** - Cloud financial management best practices

---

#### 4. Site Reliability Engineering (SRE)

**Topic**: Building reliable systems at scale

**[Site Reliability Engineering Book](https://sre.google/sre-book/table-of-contents/)** by Google (Free online - industry bible)

**[Site Reliability Workbook](https://sre.google/workbook/table-of-contents/)** (Practical implementation guide)

**Core SRE Principles:**
*   **Service Level Objectives (SLOs)**: Target reliability (e.g., 99.9% uptime)
*   **Service Level Indicators (SLIs)**: Measurements (latency, error rate, throughput)
*   **Error Budgets**: Acceptable failure rate (1 - SLO)
*   **Toil Reduction**: Automate repetitive work
*   **Blameless Postmortems**: Learn from failures

**Key Practices:**
- Monitoring and alerting on SLIs
- Incident response procedures
- Capacity planning
- Release engineering (gradual rollouts, rollbacks)

**Applied to Data Science:**
- Monitor model performance drift
- Track pipeline success rates
- Alert on data quality issues
- Automate model retraining

---

#### 5. Encryption and Key Management

**Topic**: Protecting data at rest and in transit

**[![Cloud KMS](https://img.youtube.com/vi/WKZC93y-aWI/0.jpg)](https://www.youtube.com/watch?v=WKZC93y-aWI)**

**Encryption Basics** (Cloud-Agnostic):
*   **At Rest**: Data stored on disk
*   **In Transit**: Data moving across networks
*   **Key Management**: Controlling encryption keys

**Encryption Layers:**
1. **Default**: Cloud provider encryption (automatic)
2. **Customer-Managed**: You control keys (KMS, Key Vault, HSM)
3. **Client-Side**: Encrypt before uploading

**When to Use Customer-Managed Keys:**
- Compliance requirements (HIPAA, GDPR)
- Key rotation policies
- Audit trail for key usage
- Cross-cloud portability

**GCP Implementation:**
- Cloud KMS for key management
- Customer-Managed Encryption Keys (CMEK)
- Encryption by default for all storage

**Security Best Practice**: Separate key management from data storage

---

#### 6. Observability: Logging and Monitoring

**Topic**: Understanding system behavior

**[![Cloud Logging](https://img.youtube.com/vi/gyDp-Cl_MdA/0.jpg)](https://www.youtube.com/watch?v=gyDp-Cl_MdA)**

**Observability Pillars** (Universal):
1. **Metrics**: Time-series data (CPU, memory, latency)
2. **Logs**: Event records (errors, transactions)
3. **Traces**: Request flows through distributed systems

**Logging Best Practices:**
*   Structured logging (JSON format)
*   Include correlation IDs for tracing
*   Log at appropriate levels (DEBUG, INFO, WARN, ERROR)
*   Aggregate logs centrally
*   Set up alerts on error rates

**GCP Stack:**
- Cloud Logging (formerly Stackdriver)
- Cloud Monitoring for metrics
- Cloud Trace for distributed tracing
- Export logs to BigQuery for analysis

**Open Standards:**
- OpenTelemetry for instrumentation (works everywhere)
- Prometheus for metrics (Kubernetes standard)
- Grafana for visualization

**[Google Cloud Observability](https://cloud.google.com/products/operations)**

---

### Hands-On Practice

**Project: Deploy Infrastructure with Terraform**

1. Write Terraform config for:
   - Storage bucket
   - BigQuery dataset
   - Cloud Function
2. Plan and apply changes
3. Add IAM permissions
4. Set up monitoring and alerts
5. Destroy resources

**Labs:**
- [Terraform on GCP Qwiklab](https://www.cloudskillsboost.google/focuses/1208)
- [IAM Custom Roles](https://www.cloudskillsboost.google/focuses/1035)
- [Cost Optimization](https://www.cloudskillsboost.google/focuses/1846)

**Time**: 3-4 hours

### Further Reading

- **Book**: "Site Reliability Engineering" - Google ([Free](https://sre.google/books/))
- **Book**: "Infrastructure as Code" by Kief Morris
- **GitHub**: [Terraform Best Practices](https://github.com/antonbabenko/terraform-best-practices)
- **GitHub**: [GCP Architecture Guides](https://github.com/GCP-Architecture-Guides)
- **FinOps**: [Cloud Cost Optimization](https://www.finops.org/framework/)
- **Security**: [OWASP Cloud Security](https://owasp.org/www-project-cloud-security/)
