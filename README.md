# Uzima Blood Bank Management System


## Overview

This is a Blood Bank Management System built using Django. It helps manage blood donation and distribution activities efficiently.


## Table of Contents

- [Features](#features)
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