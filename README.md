# Tempest Car Dealership Management System

A command-line application built with Python and MySQL to manage the core operations of a car dealership — browsing available cars, registering customers, and tracking purchases.

## Features

- **Available Car Details** — Browse cars filtered by type (SUV, Sedan, Hatchback, MUV/MPV, Luxury/Convertible, or all), showing model, mileage, price, engine, seater capacity, and type.
- **Registration** — Register as a new customer (auto-generates a customer ID) or as an existing customer purchasing another car. Captures name, mobile number, address, email, chosen car, and mode of payment (cash/loan/EMI).
- **Customer Details Lookup** — Look up your purchase history and personal details using your customer ID as a "pass."
- **Persistent Storage** — All data is stored in a MySQL database that's automatically set up on first run.
- **Interactive Menu-Driven Navigation** — Move freely between all sections (Available Cars, Registration, Customer Details) or exit anytime.

## Tech Stack

- **Language:** Python
- **Database:** MySQL
- **Library:** `mysql-connector-python`

## Database Schema

The system auto-creates a database `CDS` with three tables:

| Table | Description |
|---|---|
| `ACD` | Car inventory — `CID` (Primary Key), `Car_Model`, `Mileage`, `Price`, `Engine`, `Seater`, `Type` |
| `Customer` | Customer info — `customer_id` (Primary Key), `Name`, `Mobile_no`, `address`, `Email_id` |
| `CP` | Customer–car purchase link — `customer_id` (FK), `CID` (FK), `MOP` (mode of payment) |

On first run, `ACD` is pre-populated with 10 sample cars across SUV, Sedan, Hatchback, MUV/MPV, and Luxury/Convertible categories.

## Setup & Installation

1. Clone this repository
```bash
   git clone https://github.com/your-username/your-repo-name.git
```

2. Install the required dependency
```bash
   pip install mysql-connector-python
```

3. Update the database connection details in the script with your own MySQL credentials:
```python
   con = sql.connect(host="Your_host_name", user="your_user_name", password="your_password")
```

4. Run the script
```bash
   python "Project Car Dealership Shaurya Chauhan.py"
```

## How to Use

On launch, you'll see the main menu with four options:

1. **Available car details** — pick a car type to view matching inventory
2. **Customer details** — enter your customer ID to view your purchase and personal info
3. **Registration** — register as a new or returning customer and complete a purchase
4. **Exit**

Each section loops back into the others, so you can navigate freely without restarting the program.

## Author

Shaurya Chauhan
