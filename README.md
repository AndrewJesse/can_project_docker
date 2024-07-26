# CAN_PROJECT

## Overview
This project consists of a frontend and backend application. The backend is built with Python and FastAPI, and the frontend is built with Vue.js. This guide will help you set up and run the project using Docker.

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)


## Environment Variables Disclaimer:
The project uses a .env file to store the SQLite connection string. This file is included in the repository for simplicity.

.env file contains the following text: ```DATABASE_URL=sqlite:///./can_project.db```


## Getting started and building the dev environment
1) Run Docker Desktop
2) Clone the Repository
3) CD to root folder and run
```docker-compose up```

4) Open your browser and navigate to:

- [Frontend - http://localhost:8080](http://localhost:8080)
- [Backend - http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

5) Make changes to code and push

6) Wait for email with the new Vercel link

## Additional Commands

-View Logs ```docker-compose logs -f```

-Stop All Containers ```docker-compose down```
