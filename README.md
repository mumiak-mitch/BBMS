# Uzima Blood Bank Management System


## Overview

This is a Blood Bank Management System built using Django. It helps manage blood donation and distribution activities efficiently.


## Table of Contents

- [Features](#features)
- [Functions] (#functions)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Features

- User authentication for staff and donors
- Donor registration and profile management
- Blood donation and inventory tracking
- Request and distribution of blood units
- Reporting and analytics


## Functions

### Admin
- After Login, can see Unit of blood of each blood group available, Number Of Donor, Number of blood request, Number of approved request, Total Unit of blood on Dashboard.
- Can View, Update, Delete Donor.
- Can View, Update, Delete Patient.
- Can View Donation Request made by donor and can approve or reject that request based on disease of donor.
- If Donation Request approved by admin then that unit of blood added to blood stock of that blood group.
- If Donation Request rejected by admin then 0 unit of blood added to stock.
- Can View Blood Request made by donor / patient and can approve or reject that request.
- If Blood Request approved by admin then that unit of blood reduced from blood stock of that blood group.
- If Blood Request rejected by admin then 0 unit of blood reduced from stock.
- Can see history of blood request.
- Can Update Unit Of Particular Blood Group.

### Donor
- Donor can create account by providing basic details.
- After Login, Donor can donate blood, After approval from admin only, blood will be added to blood stock.
- Donor can see their donation history with status (Pending, Approved, Rejected).
- Donor can also request for blood from blood stock.
- Donor can see their blood request history with status.
- Donor can see number of blood request Made, Approved, Pending, Rejected by Admin on their dashboard.
> **_NOTE:_**  Donor can donate blood and can also request for blood.

### Patient
- Create account (No Approval Required By Admin, Can Login After Signup)
- After Login, Can see number of blood request Made, Approved, Pending, Rejected by Admin on their dashboard.
- Patient can request for blood of specific blood group and unit from blood stock.
- Patient can see their blood request history with status (Pending, Approved, Rejected).


## Requirements

- Python 3.x
- Django 3.x
- Other dependencies listed in requirements.txt


## Installation

```bash
Clone the repository
git clone https://github.com/mumiak-mitch/blood-bank-management.git

Install dependencies
pip install -r requirements.txt

Perform migrations
python manage.py migrate
python manage.py makemigrations


## Configuration

Create a .env file in the project root and add the following:

# .env
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
Adjust the values for SECRET_KEY and DATABASE_URL as needed.


## Usage

Run the development server
python manage.py runserver
Visit http://localhost:8000 in your web browser to access the application.

## Contributing

We welcome contributions! Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.