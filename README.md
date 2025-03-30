# SQL Practice Project

This project demonstrates how to create an `employees` table, generate fake data using Python, SQLAlchemy, and Faker, and then practice SQL queries. The project walks through each step—from setting up the environment to verifying the data insertion.


## Overview

This project was created to practice SQL queries on a MySQL database using fake data. The key tasks performed include:
- Creating a MySQL database (`sql_practice`).
- Defining the `employees` table with the following columns:

  - `employee_id` (decimal(4,0), Primary Key)
  - `first_name` (varchar(30))
  - `last_name` (varchar(30))
  - `email` (varchar(30))
  - `phone_number` (decimal(10,0))
  - `hire_date` (date)
  - `job_id` (varchar(4))
  - `salary` (decimal(8,0))
  - `commission_pct` (decimal(2,2))
  - `manager_id` (decimal(6,0))
  - `department_id` (decimal(4,0))

- Writing a Python script to generate and insert fake employee data.
- Practicing SQL queries

## Prerequisites

Before running the project, ensure you have the following installed:
- **MySQL Server** (with a database named `sql_practice`)
- **Python 3.13**

Install the required Python libraries using pip:

```bash
pip install sqlalchemy mysql-connector-python faker pandas tabulate
