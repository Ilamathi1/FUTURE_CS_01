# Two-Factor Authentication Web Application

## Overview

This project demonstrates the implementation of Two-Factor Authentication (2FA) in a Flask web application. It supports user registration, login, and 2FA setup using SQLite for database management.

## Features

- **User Registration**: Register with a username and password.
- **User Login**: Login with username, password, and OTP.
- **2FA Setup**: Setup 2FA using a QR code.
- **Database Reset**: Reset the SQLite database.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- pyotp
- qrcode

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Ilamathi1/FUTURE_CS_01.git
   cd your-repository


### Directory Structure

**app.py** - Main application file containing Flask routes and logic.
**models.py** - Script for resetting the database.
**static/** - Directory for static files such as CSS and images.
**style.css** - Stylesheet for the application.
**templates/** - Directory for HTML templates.
**login.html** - Template for the login page.
**register.html** - Template for the registration page.
**requirements.txt** - List of Python package dependencies.
**README.md** - This file.
