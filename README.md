# Cloud-Native Microservices Task Manager

## Project Overview
This project presents a **Cloud-Native Microservices Task Manager**, designed to showcase proficiency in modern cloud development practices. It demonstrates a robust understanding of containerization, Infrastructure as Code (IaC), microservices architecture, and continuous integration/continuous deployment (CI/CD) pipelines. This project is ideal for developers looking to highlight their skills to recruiters in the cloud and DevOps domains.

## Features
- **Task Management**: A core API for creating, retrieving, and managing tasks.
- **Decoupled Services**: Utilizes a microservices architecture with separate services for task management and future notifications.
- **Local Cloud Simulation**: Leverages LocalStack to simulate AWS services (DynamoDB, S3, SQS) locally, enabling full-stack development without cloud provider accounts.
- **Infrastructure as Code (IaC)**: Terraform scripts define and provision cloud resources, ensuring repeatable and consistent environments.
- **Containerization**: All services are containerized using Docker, providing isolated and portable execution environments.
- **CI/CD Pipeline**: Automated workflows with GitHub Actions for linting, building, and validating code changes.

## Technologies Used
- **Backend**: Python (Flask) for API services.
- **Containerization**: Docker, Docker Compose.
- **Cloud Simulation**: LocalStack (for DynamoDB, S3, SQS).
- **Infrastructure as Code**: Terraform.
- **CI/CD**: GitHub Actions.
- **Version Control**: Git, GitHub.

## Architecture Overview
The project follows a microservices pattern, with a clear separation of concerns:

1.  **Task API**: A Python Flask application responsible for handling CRUD operations for tasks. It interacts with DynamoDB for persistence.
2.  **Notification Service (Planned)**: A separate service (currently a placeholder) that would consume messages from an SQS queue to process notifications or background tasks.
3.  **LocalStack**: Provides local mock AWS services, allowing for development and testing against cloud-like environments without incurring costs or requiring actual AWS credentials.
4.  **Terraform**: Defines the DynamoDB table, S3 bucket for attachments, and SQS queue within the LocalStack environment.

```mermaid
graph TD
    User -->|HTTP/REST| TaskAPI(Task API Service)
    TaskAPI -->|DynamoDB API| LocalStack(LocalStack - AWS Services)
    LocalStack --> DynamoDB[DynamoDB (Tasks)]
    TaskAPI -->|SQS API| LocalStack
    LocalStack --> SQS[SQS (Notifications)]
    NotificationService(Notification Service) -->|SQS API| LocalStack
    LocalStack --> S3[S3 (Attachments)]
    Terraform -->|Provision Resources| LocalStack
    GitHubActions(GitHub Actions) -->|Build & Validate| Docker(Docker Images)
```

## Setup and Local Development

### Prerequisites
- Docker and Docker Compose
- Terraform
- Python 3.9+

### Steps
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/YOUR_USERNAME/cloud-task-manager.git
    cd cloud-task-manager
    ```

2.  **Start LocalStack and Services**:
    ```bash
    docker-compose up -d
    ```
    This will bring up LocalStack and the `task-api` service.

3.  **Initialize and Apply Terraform**: Provision the necessary AWS resources (DynamoDB table, S3 bucket, SQS queue) within LocalStack.
    ```bash
    cd terraform
    terraform init
    terraform apply --auto-approve
    cd ..
    ```

4.  **Interact with the Task API**:
    The Task API will be running on `http://localhost:5000`.

    -   **Create a Task**:
        ```bash
        curl -X POST -H "Content-Type: application/json" -d '{"id": "task123", "title": "Learn Cloud Native"}' http://localhost:5000/tasks
        ```

    -   **Get a Task**:
        ```bash
        curl http://localhost:5000/tasks/task123
        ```

## CI/CD with GitHub Actions
The `.github/workflows/ci.yml` file defines a GitHub Actions workflow that automatically runs on every push and pull request to the `main` branch. This workflow performs:
-   **Code Linting**: Ensures code quality and adherence to standards.
-   **Terraform Validation**: Checks Terraform configuration for syntax errors and best practices.
-   **Docker Image Build**: Verifies that Docker images can be successfully built.

## How to Demonstrate to Recruiters
This project effectively showcases the following skills:

-   **Cloud-Native Principles**: Understanding of microservices, decoupling, and resilience.
-   **Infrastructure as Code (Terraform)**: Ability to define, provision, and manage cloud infrastructure programmatically.
-   **Containerization (Docker)**: Experience in packaging applications for consistent deployment.
-   **CI/CD (GitHub Actions)**: Knowledge of automating development workflows and ensuring code quality.
-   **AWS Services (LocalStack)**: Familiarity with core AWS services like DynamoDB, S3, and SQS, even in a local development environment.
-   **Problem Solving**: Designing and implementing a functional system from scratch.

When presenting this project, emphasize the architectural decisions, the benefits of using IaC and containerization, and how the CI/CD pipeline ensures reliable deployments.

## Future Enhancements
-   Implement the Notification Service to process SQS messages.
-   Add a simple frontend application to interact with the Task API.
-   Integrate unit and integration tests for the Python services.
-   Expand Terraform to include more complex resource configurations.
-   Implement authentication and authorization for the API.

---
*Authored by Manus AI*
