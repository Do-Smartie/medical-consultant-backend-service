# Medical Consultant Backend Service

This repository contains the backend service for a medical consultant application that suggests home remedies based on common health problems. The application is built using Flask and connects to MongoDB Atlas for data storage.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have Python 3.6 or higher installed on your machine.
- You have a MongoDB Atlas account and a cluster set up. You will need the connection string to connect your application to the MongoDB Atlas database.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Do-Smartie/medical-consultant-backend-service.git
    cd medical-consultant-backend-service
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:

    ```bash
    pip install flask
    pip install pymongo
    ```

## Configuration

1. Create a `.env` file in the root directory of the project and add your MongoDB Atlas connection string:

    ```plaintext
    MONGO_URI=your_mongodb_atlas_connection_string
    ```

2. Ensure you have the necessary collections and documents in your MongoDB database as per the application requirements.

## Running the Application

To run the application, use the following command:

```bash
flask run
```

The application will start on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## API Endpoints

### Get Home Remedies

- **URL:** `/api/`
- **Method:** `GET`
- **Description:** Retrieve a list of home remedies based on common health problems.

#### Example Request

```http
GET 

