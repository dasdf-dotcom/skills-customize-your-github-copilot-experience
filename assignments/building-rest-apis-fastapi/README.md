# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI that allows a client to create, read, update, and delete data while learning how routing, request validation, and response models work in a real web service.

## 📝 Tasks

### 🛠️ Set Up Your FastAPI App

#### Description
Create a basic FastAPI project and configure a simple API that responds to HTTP requests.

#### Requirements
Completed program should:

- Install and import the FastAPI framework
- Create an application instance with a descriptive title
- Add a health check endpoint at `/health`
- Run the app locally with Uvicorn or a similar ASGI server
- Return JSON data in a clear, consistent format

### 🛠️ Build CRUD Endpoints

#### Description
Implement API routes to manage a list of items such as books, tasks, or students.

#### Requirements
Completed program should:

- Define a data model for the resource being managed
- Add a route to list all items using `GET`
- Add a route to create a new item using `POST`
- Add a route to retrieve one item by ID using `GET`
- Add a route to update an existing item using `PUT` or `PATCH`
- Add a route to delete an item using `DELETE`
- Store data in memory for this assignment while keeping logic organized

### 🛠️ Validate Input and Improve the API

#### Description
Use FastAPI features to validate request data and make the API easier to use and understand.

#### Requirements
Completed program should:

- Use Pydantic models to validate incoming data
- Return meaningful responses for successful and invalid requests
- Support query parameters or path parameters in at least one endpoint
- Include a response model for clear output structure
- Test the API in the browser using the generated Swagger documentation at `/docs`
