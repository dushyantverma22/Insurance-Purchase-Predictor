# 🚗 Vehicle Insurance Purchase Prediction — End-to-End MLOps Project

> **Production-grade ML system built with Random Forest + FastAPI + Docker + AWS + CI/CD**

This project predicts whether a customer will purchase vehicle insurance based on demographic, policy & vehicle attributes.
Demonstrates real-world **MLOps, ML Engineering, Deployment & Cloud skills** end-to-end.

---

## 🎯 Objective

Build & deploy a **Vehicle Insurance Purchase Prediction System** with:

✅ Modular ML Pipeline
✅ Automated CI/CD
✅ Cloud Deployment (AWS EC2 + ECR + S3)
✅ Model Registry & Versioning
✅ Real-time inference API (FastAPI)
✅ MongoDB as Data Source

---

## 📊 Feature Engineering & ML Model

### 🎯 Target Variable

`Response` → **1 = Customer will purchase**, **0 = No purchase**

### 🧠 Model Used

```text
Random Forest Classifier
```

### 🧾 Input Features

| Feature              | Description                                 |
| -------------------- | ------------------------------------------- |
| id                   | Unique customer ID                          |
| Gender               | Male / Female                               |
| Age                  | Age of customer                             |
| Driving_License      | Has driving license (0/1)                   |
| Region_Code          | Customer region                             |
| Previously_Insured   | Customer already insured (0/1)              |
| Vehicle_Age          | "< 1 Year", "1-2 Years", "> 2 Years"        |
| Vehicle_Damage       | Whether vehicle was damaged previously      |
| Annual_Premium       | Annual premium amount                       |
| Policy_Sales_Channel | Sales channel code                          |
| Vintage              | Days since customer associated with company |

---

## 🏗️ System Architecture

```
User → FastAPI UI → ML Model API → AWS EC2 (Docker Container)
            ↑
   GitHub Actions CI/CD
            ↑
Docker Image ← AWS ECR
            ↑
Model Registry ← AWS S3
            ↑
Trained Model ← Sklearn (Random Forest)
            ↑
MongoDB Atlas ← Raw Vehicle Insurance Data
```

---

## 🧠 ML Pipeline Components

| Stage               | Description                                               |
| ------------------- | --------------------------------------------------------- |
| Data Ingestion      | Load data from MongoDB Atlas                              |
| Data Validation     | Schema check, missing values, dtype validation            |
| Data Transformation | Encoding, scaling, feature store & artifacts              |
| Model Training      | Random Forest Classifier                                  |
| Model Evaluation    | Compare latest vs previous model (threshold change check) |
| Model Registry      | Store best model in AWS S3                                |
| Prediction Pipeline | FastAPI endpoint for prediction                           |

---

## 🛠️ Tech Stack

### 🧠 ML

* Python 3.10
* Scikit-Learn, Pandas, NumPy

### 🧱 MLOps

* ML Modular Pipeline
* Model registry in S3
* Artifact tracking
* Logging & Exception framework

### ☁️ Cloud & DevOps

| Category           | Tool                          |
| ------------------ | ----------------------------- |
| Cloud              | AWS                           |
| Compute            | EC2                           |
| Container Registry | ECR                           |
| Storage            | S3                            |
| CI/CD              | GitHub Actions                |
| Runner             | Self-hosted EC2 GitHub Runner |
| Web Framework      | FastAPI                       |
| Containerization   | Docker                        |
| Database           | MongoDB Atlas                 |

---

## 📂 Directory Structure

```
src/
 ┣ components/
 ┣ entity/
 ┣ pipelines/
 ┣ configuration/
 ┣ aws_storage/
 ┣ utils/
 ┣ logger/
 ┣ exception/
notebooks/
templates/
static/
.github/workflows/aws.yaml
Dockerfile
app.py
requirements.txt
setup.py / pyproject.toml
```

---

## 🚀 CI/CD Pipeline

| Stage    | Action                                        |
| -------- | --------------------------------------------- |
| CI       | Code checkout & dependency setup              |
| Build    | Docker image build                            |
| Security | Secret-based credential flow                  |
| Push     | Push image to Amazon ECR                      |
| Deploy   | EC2 self-hosted runner pulls & runs container |

Trigger:

```
git push origin main
```

---

## 🌐 API Endpoints

| Route      | Description                               |
| ---------- | ----------------------------------------- |
| `/`        | Web UI                                    |
| `/predict` | Make prediction                           |
| `/train`   | Train pipeline & push updated model to S3 |

---

## ♻️ Deployment Flow

```
Push Code → GitHub Actions → Build Docker Image → Push to ECR →
EC2 Self-Hosted Runner → Pull Image → Run Container → FastAPI Live
```

EC2 exposes app on port:

```
http://23.22.207.115:5000/
```

---

## 🔐 Secrets Used

| Key                   | Purpose                |
| --------------------- | ---------------------- |
| MONGODB_URL           | MongoDB Cluster Access |
| AWS_ACCESS_KEY_ID     | AWS Credentials        |
| AWS_SECRET_ACCESS_KEY | AWS Credentials        |
| AWS_REGION            | Deployment Region      |
| ECR_REPO              | AWS ECR Repo Name      |

---

## ✨ Key Highlights

✅ Real-world ML pipeline
✅ Random Forest model deployment
✅ FastAPI production-ready API
✅ Dockerized microservice architecture
✅ GitHub Actions CI/CD
✅ AWS ECR + EC2 + S3
✅ MongoDB Atlas integration
✅ Logging & exception framework
✅ Model version comparison & registry


---

## 🏁 Conclusion

This project demonstrates practical skills in:

* Machine Learning Engineering
* Cloud DevOps (AWS)
* CI/CD Automation
* Production Deployment & API serving
* Data Engineering & Pipeline Orchestration


