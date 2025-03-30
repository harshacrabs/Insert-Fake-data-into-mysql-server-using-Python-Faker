import random
import datetime
from faker import Faker
import sqlalchemy
from sqlalchemy import text

# Initialize Faker and SQLAlchemy engine
fake = Faker()
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:harekrishna@localhost:3306/sql_practice', echo=True)

# Number of fake records to insert
num_records = 100

# Predefined job and department IDs for variety
job_ids = ['DEV1', 'HR01', 'FIN1', 'MKT1', 'OPS1']
department_ids = [10, 20, 30, 40]

with engine.begin() as connection:
    for i in range(1001, 1001 + num_records):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower()}.{last_name.lower()}@example.com"
        phone_number = random.randint(1000000000, 9999999999)
        # Random hire_date within the last 10 years
        hire_date = fake.date_between(start_date='-10y', end_date='today')
        job_id = random.choice(job_ids)
        salary = random.randint(40000, 90000)
        commission_pct = round(random.uniform(0, 0.1), 2)
        # For simplicity, assign manager_id as NULL for the first record and random existing IDs for others
        manager_id = i if i == 1001 else random.randint(1001, i - 1)
        department_id = random.choice(department_ids)

        # Create the SQL INSERT statement
        stmt = text("""
            INSERT INTO employees 
            (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, commission_pct, manager_id, department_id)
            VALUES 
            (:employee_id, :first_name, :last_name, :email, :phone_number, :hire_date, :job_id, :salary, :commission_pct, :manager_id, :department_id)
        """)

        # Execute the INSERT statement with parameter binding
        connection.execute(stmt, {
            'employee_id': i,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number,
            'hire_date': hire_date,
            'job_id': job_id,
            'salary': salary,
            'commission_pct': commission_pct,
            'manager_id': manager_id,
            'department_id': department_id
        })

print("Fake data inserted successfully!")