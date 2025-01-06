# Birthday Wisher

A Python-based application to automatically send personalized birthday wishes to your friends and family via email. The program checks a CSV file containing birthday data and sends a customized email if a birthday matches the current date.

## Features
- Automatically reads and checks birthdays from a CSV file (`birthdays.csv`).
- Sends personalized birthday wishes using pre-written letter templates.
- Utilizes Python's `smtplib` to send emails via Gmail.

## Prerequisites
Before using this program, ensure you have:

1. Python installed on your machine.
2. The following Python libraries:
   - `datetime`
   - `os`
   - `pandas`
   - `random`
   - `smtplib`

Install missing libraries with pip:
```bash
pip install pandas
```

3. A Gmail account with App Passwords enabled.
   - [Learn more about App Passwords](https://support.google.com/accounts/answer/185833?hl=en).

## How It Works
1. **Setup the `birthdays.csv` File:**
   The `birthdays.csv` file should contain the following columns:
   ```csv
   name,email,month,day
   John Doe,john.doe@example.com,1,15
   Jane Smith,jane.smith@example.com,2,28
   ```

2. **Create Letter Templates:**
   Create personalized letter templates in the `letter_templates/` directory. Use `[NAME]` as a placeholder for the recipient's name. For example:
   ```txt
   Happy Birthday [NAME]!

   Wishing you a fantastic year ahead filled with joy and success.
   ```

3. **Run the Program:**
   Execute the script to check if today's date matches any birthdays in `birthdays.csv`. If a match is found, the program selects a random letter template, personalizes it, and sends it via email.

## Directory Structure
```
.
├── birthdays.csv          # File containing birthday information
├── letter_templates/      # Directory containing letter templates
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
├── birthday_wisher.py     # Main Python script
```

## Configuration
### Gmail Configuration
Update the following variables in the script with your Gmail credentials:
```python
my_email = "your_email@gmail.com"
password = "your_app_password"
```

### File Paths
Ensure the paths for `birthdays.csv` and `letter_templates/` are correct in the script:
```python
data = pandas.read_csv("birthdays.csv")
directory_path = "/path/to/letter_templates"
```

## Usage
Run the script using Python:
```bash
python birthday_wisher.py
```

## Notes
- Ensure your Gmail account allows App Passwords to use this program.
- The script only sends emails for birthdays matching the current date.
- Customize the letter templates to make your wishes more personal.

## Example Output
- **Letter Template:**
  ```txt
  Happy Birthday [NAME]!
  Wishing you a fantastic year ahead filled with joy and success.
  ```

- **Email Sent:**
  ```txt
  Subject: Happy Birthday!

  Happy Birthday John!
  Wishing you a fantastic year ahead filled with joy and success.
  ```



