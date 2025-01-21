# User Account Management System

This project consists of two main Bash scripts that work together to manage user accounts in a Linux system.

## Scripts

### 1. data.sh
This script collects user information:
- Prompts for username and full name
- Confirms the information with the user
- Stores the data in a CSV file (employee.csv)

### 2. user.sh
This script creates user accounts:
- Reads from employee.csv
- Creates user accounts with random passwords
- Forces password change on first login
- Stores credentials in out.txt

## Requirements
- Linux system with bash shell
- Root privileges for user.sh
- openssl (for password generation)

## Usage

1. First, collect user information:
```bash
./data.sh
```

2. Then, create the user accounts (requires root):
```bash
sudo ./user.sh
```

## Output Files
- employee.csv: Stores user information (username, full name)
- out.txt: Stores username and initial random passwords

## Security Notes
- The user.sh script must be run as root
- Initial passwords are randomly generated
- Users are forced to change password on first login
- Passwords are stored in out.txt - make sure to secure this file

## Deleting Users
To delete a user and their home directory:
```bash
sudo deluser --remove-home username
```
