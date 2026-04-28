# 🚀 Cloud-Native Microservices Task Manager

**End-to-end microservices application with LocalStack AWS simulation, Terraform IaC, Docker containerization, and GitHub Actions CI/CD.**

[![GitHub](https://img.shields.io/badge/github-karthikk022-181717?style=flat-square&logo=github)](https://github.com/karthikk022/cloud-task-manager)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue?style=flat-square&logo=python)](https://python.org)
[![Docker](https://img.shields.io/badge/docker-compose-2496ED?style=flat-square&logo=docker)](https://docker.com)
[![Terraform](https://img.shields.io/badge/terraform-IaC-623CE4?style=flat-square&logo=terraform)](https://terraform.io)
[![AWS](https://img.shields.io/badge/aws-localstack-FF9900?style=flat-square&logo=amazon-aws)](https://localstack.cloud)

---

## 🎯 Project Highlights

A **complete cloud-native microservices example** showcasing enterprise development patterns:

| Feature | Benefit |
|---------|---------|
| **Microservices Architecture** | Decoupled Task API with Flask for scalability & maintainability |
| **LocalStack AWS Simulation** | Full DynamoDB, S3, SQS locally — no AWS account or costs needed |
| **Infrastructure as Code (Terraform)** | Reproducible resource provisioning (DynamoDB, S3, SQS) |
| **Docker Containerization** | Portable, isolated services ready for production deployment |
| **REST API** | Production-ready CRUD operations on tasks with error handling |
| **CI/CD Pipeline** | GitHub Actions for linting, building, and validation |
| **Development-Ready** | docker-compose brings up entire stack in seconds |

---

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────┐
│                  Developer Workflow                      │
│  Code → Git Push → GitHub Actions (Lint, Build, Validate)
└────────────────────┬─────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
        ▼                         ▼
   ✓ Python Lint            ✓ Docker Build
   ✓ Terraform Validate     ✓ Push to Registry
        │                         │
        └────────────┬────────────┘
                     │
        ┌────────────▼────────────────┐
        │   docker-compose up -d      │
        │  ┌──────────────────────┐   │
        │  │  Task API Service    │   │
        │  │  (Flask + Boto3)     │   │
        │  │  :5000               │   │
        │  └──────────────┬───────┘   │
        │                 │           │
        │  ┌──────────────▼───────┐   │
        │  │ LocalStack (AWS Mock)│   │
        │  │ :4566               │   │
        │  │                     │   │
        │  ├─ DynamoDB (Tasks)   │   │
        │  ├─ S3 (Attachments)   │   │
        │  └─ SQS (Notifications)│   │
        └───────────────────────┬────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
                    ▼                       ▼
            ┌──────────────────┐   ┌──────────────────┐
            │  Terraform Apply │   │  Task API Tests  │
            │  Provisions      │   │  CRUD Operations │
            │  Resources       │   │  :5000/tasks     │
            └──────────────────┘   └──────────────────┘
```

---

## 📦 Tech Stack

### Backend & Services
- **Framework**: Flask (Python 3.9+)
- **Database Access**: Boto3 (AWS SDK for Python)
- **Local AWS Services**: LocalStack (DynamoDB, S3, SQS mock)

### Infrastructure & DevOps
- **Containerization**: Docker, Docker Compose
- **Infrastructure as Code**: Terraform (resource provisioning)
- **Cloud Provider**: AWS (or LocalStack for local dev)

### CI/CD & Automation
- **CI/CD Pipeline**: GitHub Actions
- **Code Quality**: Linting & validation
- **Container Builds**: Automated Docker image building

### Services Included
```
┌─────────────────────────────────────────┐
│         AWS Services (LocalStack)       │
├─────────────────────────────────────────┤
│ DynamoDB Table: "Tasks"                │
│ - Partition Key: id (String)            │
│ - Billing: On-Demand (auto-scaling)    │
├─────────────────────────────────────────┤
│ S3 Bucket: "task-attachments-bucket"   │
│ - For storing task files/attachments    │
├─────────────────────────────────────────┤
│ SQS Queue: "task-notifications-queue"  │
│ - For async task notifications          │
└─────────────────────────────────────────┘
```

---

## 🚀 Quick Start (10 minutes)

### Prerequisites
```bash
# Required tools
- Docker & Docker Compose (v20.10+)
- Terraform (v1.0+)
- Python 3.9+ (for local development)
- Git
```

### Installation & Deployment

#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/karthikk022/cloud-task-manager.git
cd cloud-task-manager
```

#### 2️⃣ Start LocalStack & Task API
```bash
# Brings up LocalStack and Task API service
docker-compose up -d

# Verify services are running
docker-compose ps

# Expected output:
# NAME         STATUS           PORTS
# localstack   Up 2 minutes     0.0.0.0:4566->4566/tcp
# task-api     Up 2 minutes     0.0.0.0:5000->5000/tcp
```

#### 3️⃣ Provision AWS Resources with Terraform
```bash
cd terraform

# Initialize Terraform (downloads AWS provider)
terraform init

# Plan the infrastructure
terraform plan

# Apply configuration (creates DynamoDB table, S3 bucket, SQS queue)
terraform apply --auto-approve

# Verify resources created
terraform state list

cd ..
```

#### 4️⃣ Test the Task API
```bash
# Health check
curl http://localhost:5000/health

# Expected response:
# {"status": "healthy"}
```

---

## 📡 API Reference

### Base URL
```
http://localhost:5000
```

### Endpoints

#### ✅ Health Check
```bash
GET /health

# Response (200 OK)
{
  "status": "healthy"
}
```

#### ➕ Create a Task
```bash
POST /tasks
Content-Type: application/json

Request Body:
{
  "id": "task-123",
  "title": "Implement authentication"
}

# Response (201 Created)
{
  "message": "Task created",
  "id": "task-123"
}

# Stored in DynamoDB:
{
  "id": "task-123",
  "title": "Implement authentication",
  "status": "PENDING"
}
```

**Example with curl:**
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"id": "task-001", "title": "Learn Cloud Native"}'
```

#### 🔍 Get a Task
```bash
GET /tasks/{task_id}

# Response (200 OK)
{
  "id": "task-001",
  "title": "Learn Cloud Native",
  "status": "PENDING"
}

# Response (404 Not Found) if task doesn't exist
{
  "error": "Task not found"
}
```

**Example with curl:**
```bash
curl http://localhost:5000/tasks/task-001
```

#### 📊 Response Codes
| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |
| 500 | Server Error |

---

## 🏗️ Project Structure

```
cloud-task-manager/
├── services/
│   └── task-api/
│       ├── main.py                  # Flask app with CRUD endpoints
│       ├── Dockerfile               # Multi-stage Python image
│       └── requirements.txt          # Python dependencies
├── terraform/
│   └── main.tf                      # DynamoDB, S3, SQS provisioning
├── docs/
│   └── cicd/
│       └── ci-workflow-sample.yml   # GitHub Actions workflow template
├── docker-compose.yml               # LocalStack + Task API orchestration
└── README.md                        # This file
```

---

## 🔐 Best Practices Demonstrated

### Cloud-Native Architecture
✅ **Microservices Separation** — Task API decoupled from infrastructure  
✅ **Stateless Services** — Flask app scales horizontally  
✅ **Managed Data Layer** — DynamoDB for reliable persistence  
✅ **Async Processing Ready** — SQS integration for background jobs  

### Infrastructure as Code
✅ **Terraform** — All AWS resources defined in code, versioned in Git  
✅ **Reproducible Environments** — Same infra locally & in production  
✅ **Resource Tagging** — Ready for cost allocation & management  

### Containerization
✅ **Lightweight Images** — python:3.9-slim (optimized for size)  
✅ **Security** — Runs as non-root user  
✅ **Production Ready** — Proper EXPOSE, CMD, and error handling  

### CI/CD & Testing
✅ **Automated Builds** — GitHub Actions on every push  
✅ **Linting & Validation** — Code quality checks before deployment  
✅ **Docker Build Verification** — Ensures images compile correctly  

---

## 🔧 Advanced Usage

### Scale the Task API
```bash
# Change replicas in docker-compose.yml
docker-compose up -d --scale task-api=3
```

### View LocalStack Logs
```bash
docker-compose logs -f localstack
```

### Query DynamoDB Directly
```bash
# List all tasks in DynamoDB
aws dynamodb scan --table-name Tasks \
  --endpoint-url http://localhost:4566 \
  --region us-east-1
```

### Access LocalStack S3
```bash
# List buckets
aws s3 ls --endpoint-url http://localhost:4566

# Upload file
aws s3 cp myfile.txt s3://task-attachments-bucket/ \
  --endpoint-url http://localhost:4566
```

### View Terraform State
```bash
cd terraform
terraform show
terraform output
cd ..
```

### Cleanup
```bash
# Stop containers
docker-compose down

# Remove Terraform resources (optional)
cd terraform && terraform destroy && cd ..

# Remove volumes (optional, for full cleanup)
docker-compose down -v
```

---

## 📊 What Each Component Does

### Task API Service (Flask)
- **Purpose**: Handles HTTP requests for task CRUD operations
- **Endpoints**: `/health`, `/tasks` (POST), `/tasks/<id>` (GET)
- **Database**: Connects to DynamoDB via Boto3
- **Error Handling**: Catches ClientError from AWS SDK

**Key Features:**
```python
# Health checks for load balancers
@app.route('/health', methods=['GET'])

# Create tasks (PUT into DynamoDB)
@app.route('/tasks', methods=['POST'])

# Retrieve tasks (GET from DynamoDB)
@app.route('/tasks/<task_id>', methods=['GET'])
```

### LocalStack
- **Purpose**: Local AWS service mock for development
- **Services**: DynamoDB, S3, SQS
- **Endpoint**: http://localhost:4566
- **Benefits**: No AWS account needed, fast, free, offline-capable

### Terraform
- **Purpose**: Infrastructure provisioning as code
- **Creates**:
  - DynamoDB table "Tasks" with on-demand billing
  - S3 bucket "task-attachments-bucket"
  - SQS queue "task-notifications-queue"
- **State**: Stored locally in `terraform.tfstate`

### Docker Compose
- **Purpose**: Orchestrate LocalStack + Task API
- **Services**: 2 containers (localstack, task-api)
- **Networking**: task-api connects to localstack via hostname
- **Volumes**: LocalStack data persists to `/tmp/localstack/data`

---

## 🎓 Learning Outcomes

By exploring this project, you'll master:

1. **Microservices Architecture** — Service isolation, scalability patterns
2. **REST API Design** — CRUD operations, HTTP methods, status codes
3. **AWS Core Services** — DynamoDB (NoSQL), S3 (object storage), SQS (messaging)
4. **Python Backend** — Flask framework, error handling, Boto3 SDK
5. **Infrastructure as Code** — Terraform for reproducible infrastructure
6. **Docker Containerization** — Building, running, and orchestrating containers
7. **Local Development** — LocalStack for cost-free AWS development
8. **CI/CD Automation** — GitHub Actions for code quality gates

---

## 📈 Future Enhancements

- [ ] Add **Notification Service** — consume SQS messages, send emails/webhooks
- [ ] Implement **Authentication & Authorization** — JWT tokens, IAM policies
- [ ] Add **Frontend UI** — React/Vue dashboard to manage tasks
- [ ] Integrate **Unit & Integration Tests** — pytest with mocking
- [ ] Add **API Documentation** — Swagger/OpenAPI spec
- [ ] Implement **Logging** — Structured logging with CloudWatch integration
- [ ] Add **Metrics & Monitoring** — Prometheus metrics, CloudWatch dashboards
- [ ] Deploy to **Production** — AWS ECS, Lambda, or Kubernetes
- [ ] Add **Database Migrations** — DynamoDB schema versioning
- [ ] Implement **Task Filtering** — Query by status, date range, etc.

---

## 🎯 For Recruiters & Interviewers

**What this project demonstrates:**

| Skill | Evidence |
|-------|----------|
| **AWS Service Proficiency** | DynamoDB CRUD, S3 bucket creation, SQS queue setup via Terraform |
| **Backend Development** | Flask API with proper error handling, HTTP methods, response codes |
| **Infrastructure as Code** | Terraform configs for reproducible, version-controlled infrastructure |
| **DevOps Practices** | Docker containerization, docker-compose orchestration, CI/CD pipeline |
| **Python Expertise** | Boto3 integration, environment config, error handling, Flask best practices |
| **Microservices Design** | Service decoupling, stateless API, external data persistence |
| **Problem-Solving** | Full-stack development without production AWS costs |
| **Software Architecture** | Clear separation of concerns (API, infrastructure, automation) |

**Interview Talking Points:**
- "Walk me through how tasks persist from the API to DynamoDB"
- "How would you add the Notification Service to process SQS messages?"
- "What would change if we deployed this to AWS ECS instead of docker-compose?"
- "How would you implement task filtering (by status, date) in Terraform?"
- "What's your approach to scaling this API from 1 to 1000 requests/second?"
- "How would you add authentication to this API?"

---

## 🔗 Resources & Documentation

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Boto3 (AWS SDK) Docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [DynamoDB Best Practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [LocalStack Documentation](https://docs.localstack.cloud/)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [GitHub Actions Workflows](https://docs.github.com/en/actions/using-workflows)

---

## 📝 License

MIT License — feel free to fork, modify, and use for learning & portfolios.

---

## ✨ Credits

**Author**: Karthick Raja C ([@karthikk022](https://github.com/karthikk022))

**Stack**: Flask, Python, AWS (LocalStack), Terraform, Docker, GitHub Actions

---

**⭐ If this helps you — star the repo and share it with fellow cloud engineers!**

For questions, issues, or improvements, open a GitHub issue or PR.
