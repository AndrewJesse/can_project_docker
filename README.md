# CAN_PROJECT
This guide will help you set up and run the project using Docker. This project is hosted on Vercel, and the updated link will be sent to the contributor of a main branch merge. 

## Overview
This project consists of the following components:
- **Backend**: Python FastAPI
- **Frontend**: Vue.js
- **Database**: SQLite

**DevOps**:
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Hosting**: Vercel

## Prerequisites
- **Windows & Mac users**: [Download Docker Desktop](https://docs.docker.com/get-docker/)
- **Linux users**: [Download Docker Compose](https://docs.docker.com/compose/install/)

## Getting started and building the dev environment
1. **Run Docker Desktop**
   - Ensure Docker Desktop is running on your machine.

2. **Clone the Repository & Start a New Branch**
   ```bash
   git clone https://github.com/AndrewJesse/can_project_docker
   cd can_project_docker
   git checkout -b <new_branch_name>
   ```

3. **Navigate to the Root Folder and Run Docker Compose**
   ```bash
   docker-compose up
   ```

4. **Open Your Browser and Navigate to:**
   - [Frontend - http://localhost:8080](http://localhost:8080)
   - [Backend - http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

5. **Make Changes to Code and Push**
   - Make your code changes.
   - Commit and push your changes to the repository.
   ```bash
   git add .
   git commit -m "Your commit message"
   git push origin <new_branch_name>
   ```

6. **Merge to Main Branch and Deploy**
   - The project is configured to be automatically deployed to Vercel upon merging changes to the `main` branch.
   - You must be a contributor to this project to sucsefully have your change deployed.
   - Once changes are approved, merge your branch into the `main` branch.
   - Upon merging, the project will be automatically deployed to Vercel.
   - The updated deployment link can be found at the top of this page [github.com/AndrewJesse/can_project_docker/deployments](https://github.com/AndrewJesse/can_project_docker/deployments).
