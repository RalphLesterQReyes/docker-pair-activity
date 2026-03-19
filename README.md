# 🐳 Docker Data Analysis: Pair Activity

This repository demonstrates the **portability** of Docker by containerizing two different Python-based data analysis projects. 

## 👥 Authors
* **Student A:** Ralph Lester Reyes - Topic: Sales Performance Analysis
* **Student B:** Christian Licuanan - Topic: [Partner's Topic Name]

---

## 🛠 Prerequisites
Before running these projects, ensure you have:
1. **Docker Desktop** installed and running.
2. **WSL 2** enabled
3. **VS Code** (recommended).

---
## 🛠 Instructions for Student B (Christian)

### 1. Clone the Repository
* Open **GitHub Desktop**.
* Go to `File > Clone Repository` and select `docker-pair-activity`.
* Choose a local path on your laptop to save the files.

### 2. Create Your Feature Branch
*In GitHub Desktop, before adding any code:*
* Click the **Current Branch** button (top center).
* Click **New Branch** and name it `feature-student-b`.
* Click **Publish Branch** to sync it with GitHub.

### 3. Run Student A's Analysis (Portability Test)
*To prove Docker works, run my code on your machine:*
1. Open the project in **VS Code**.
2. Open the terminal (Ctrl + `) and run:
   ```bash
   cd student-a-sales
   docker build -t student-a-app .
   docker run -v "${PWD}:/app" student-a-app
---
