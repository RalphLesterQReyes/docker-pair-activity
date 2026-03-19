# 🐳 Docker Data Analysis: Pair Activity

This repository demonstrates the **portability** of Docker by containerizing two different Python-based data analysis projects. 

## 👥 Authors
* **Student A:** Ralph Lester Reyes - Topic: Sales Performance Analysis
* **Student B:** Christian Licuanan - Topic: [Partner's Topic Name]

---

## 🛠 Prerequisites
Before running these projects, ensure you have:
1 **Docker Desktop** installed and running.
2. **WSL 2** enabled
3. **VS Code** (recommended).

---
## Github
1. Before you start coding make sure to create new branch.
---

## 🚀 How to Run the Projects

### 📂 Running Student A (Sales Analysis)
1. Open your terminal and navigate to the folder:
   ```bash
   cd student-a-sales
2. Build the Docker Image: This command creates the image named `student-a-app` based on our Dockerfile.
    ```bash
    docker build -t student-a-app .
3. Run the Container: This command runs the container and links your current folder `(${PWD})` to the container's `/app` folder so the generated graphs are saved to your laptop.
    ```bash
    docker run -v "${PWD}:/app" student-a-apps