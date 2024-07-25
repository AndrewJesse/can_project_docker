# CAN_PROJECT

## Overview
This project consists of a frontend and backend application. The backend is built with Python and FastAPI, and the frontend is built with Vue.js. This guide will help you set up and run the project using Docker.

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

- Clone the Repository

- Create a .env file in the root of the project and configure the necessary environment variables for the backend SQLite.

- content of .env file:
```DATABASE_URL=sqlite:///./can_project.db```


## Using Docker
Build and Run Containers
1) Open a terminal in the root project folder.

2) Run the following command:
```docker-compose up```

3) Open your browser and navigate to:

Frontend: ```http://localhost:8080```

Backend: ```http://127.0.0.1:8000/docs```

## Additional Commands

-View Logs ```docker-compose logs -f```

-Stop All Containers ```docker-compose down```
