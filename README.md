# ZipAirlines API

## Overview

This project is a RESTful API for managing and assessing the fuel consumption and maximum flight time of airplanes for "ZipAirlines". The API is built using Django Rest Framework (DRF) and allows users to input data for 10 airplanes with custom IDs and passenger assumptions.

## Features

- Add airplanes with passenger counts.
- Calculate total fuel consumption per minute for each airplane.
- Calculate the maximum flight duration based on fuel tank capacity and consumption.


## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Sergi0bbb/zip-airlines
```

### 2. Install Dependencies
Ensure you have a virtual environment set up and activate it:
```bash
python -m venv venv
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Apply Migrations
Run the following command to set up the database:
```bash
python manage.py migrate
```

### 4. Run the Server
Start the development server:
```bash
python manage.py runserver
```

---

## Usage

### Adding Airplanes
Send a POST request to `/api/v1/zip_airlines/airplanes` with a list of airplane objects:
```json
[
  {"amount_of_passengers": 10},
  {"amount_of_passengers": 20}
]
```

### Retrieving Airplanes
- List all airplanes: `GET /api/v1/zip_airlines/airplanes`
- Retrieve a specific airplane: `GET /api/v1/zip_airlines/airplanes/{id}`

### Calculate Consumption and Flight Time
The API automatically calculates:
- **Fuel consumption per minute** (with and without passengers).
- **Maximum flight time** based on fuel capacity.

---


### Endpoints
| Method | Endpoint      | Description                          |
|--------|---------------|--------------------------------------|
| POST   | `/api/v1/zip_airlines/airplanes`            | Add airplanes                       |
| GET    | `/api/v1/zip_airlines/airplanes`            | List all airplanes                  |
| GET    | `/api/v1/zip_airlines/airplanes/{id}`      | Retrieve details of a specific airplane |
