# CodeAlpha_SQLInjectionDetection
A Python-based educational project to demonstrate SQL injection detection and prevention using SQLite and secure parameterized queries.

 SQL Injection Detection and Prevention

Project Overview

This project is a Python-based educational application that demonstrates how to detect suspicious input and prevent SQL injection using secure database queries.

It uses SQLite to store demo user information and provides a simple login system for learning basic database security.

Features

- Detects selected suspicious input patterns
- Demonstrates a secure login system
- Uses parameterized SQL queries
- Stores demo user information in an SQLite database
- Displays login success or failure messages
- Helps beginners understand SQL injection prevention

Technologies Used

- Python
- SQLite
- Regular Expressions
- SHA-256 Hashing

How It Works

1. Creates a demo SQLite database.
2. Adds a sample user account.
3. Accepts a username and password.
4. Checks input for selected suspicious patterns.
5. Uses parameterized SQL queries to safely check login details.
6. Displays the login result.

Demo Login

- Username: "student"
- Password: "demo123"

Project File

- "main.py" — Contains the Python code for the demo, input checks, database setup, and login validation.

Future Enhancements

- Improved SQL injection detection
- Secure password hashing using a dedicated password-hashing algorithm
- Login attempt monitoring
- Security event logging
- Web-based user interface

Project Status

Educational prototype. It demonstrates basic suspicious-input checks and SQL injection prevention using parameterized queries.

Disclaimer

This project is intended for educational purposes only. The detection patterns are limited and may not identify every SQL injection attempt.

Author

CodeAlpha Cloud Computing Internship Project
