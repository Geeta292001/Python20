#Logging in Python
#The Logging module allows developers to record messages about the program's execution, such as errors, warnings, or informational messages.
#This can be helpful for debugging and monitoring purposes.
# import logging
# logging.basicConfig(
#     level = logging.DEBUG,  #set the lowest level og logging to capture all messages
#     format = '%(asctime)s - %(levelname)s - %(message)s', #Format of the log message
#     filename = 'app.log',                   #Log messages will be written to this file
#     filemode = 'w'          #'w'  mode overwrites the file each time the script runs
# )
#
# #Log messages with different severity levels
# logging.debug("This is a DEBUG message - useful for diagnosing issues.")
# logging.info("This is an INFO message - shows general program events.")
# logging.warning("This is a WARNING message - something unexpected happened.")
# logging.error("This is a ERROR message - an error occurred in the program.")
# logging.critical("This is a CRITICAL message - the program may crash.")

#Advantages of logging:
#Debugging: Logs provide detailed information about program execution, helping developers identify and fix issues.
#Monitoring: Logs can be used to monitor application behaviour in production.
#Persistence: Unlike print statements, log messages can be saved to files for long-term analysis.
#Granularity: Different logging levels(DEBUG,INFO,etc.) let developers control the detailed og logged information.
#Customazation: The logging module allows for customized formatting and outputs (e,g,, files,console,or remote servers)

#Disadvantages of logging:
#Performance Overhead: Logging can slow down the application, especially if there are many log messages or complex formatting.
#Log Management: Large log files can become difficult to manage and analyze without tools.
#Security Risks: Sensitive information logged accidentally amy expose security vulnerabilities.
#Incoorect Configuration: Poorly configured logging(e,g., logging DEBUG level in production) can clutter logs and degrade performance.

#Types of Loggers:
#Default Logger: The logger obtained using logging.basicConfig and direct logging methods like logging.debug.
#Custom Logger: A logger created using logging.getLogger(name) for advanced use cases. Allows separation of logs by modules or components.
#Root Logger: The root logger is the default logger created when you use logging without a custom logger.

#Logging User Input Validation
import logging
logging.basicConfig(
     filename="age.log",
     level=logging.INFO,
     format='%(asctime)s - %(levelname)s - %(message)s'
 )

try:
     age = int(input("Enter your age: "))
     if age < 0:
         raise ValueError("Age cannot be negative.")
     logging.info(f"Valid age entered: {age}")
     print(f"Valid age entered: {age}")
except ValueError as e:
     logging.error(f"Invalid input: {e}")
     print("Invalid input. Please enter a valid integer.")
except KeyboardInterrupt:
     logging.warning("Program interrupted by the user.")
     print("\nProgram interrupted by the user.")
finally:
     logging.shutdown()
     print("Execution completed.")





import logging
import os

logging.basicConfig(filename='file_check.log', level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

file_path = 'data.txt'

if not os.path.exists(file_path):
 logging.warning(f"The file {file_path} does not exist.")
else:
  logging.info(f"The file {file_path} was found.")

#Logging Errors in calculator Function
import logging
logging.basicConfig(filename = 'calculator.log', level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
def calculator(a,b,operation):
    try:
        logging.info(f"performing {operation} on {a} and {b} ")
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "division":
            result = a / b
        else:
            raise ValueError("Invalid Operation")
        logging.info(f"Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero error.")
    except ValueError as e:
        logging.error(f"value error: {e}")
    except exception as e:
        logging.error(f"Unexpected Error: {e}")
calculator(10, 5, "add")
calculator(10, 0, "divide")
calculator(10, 5, "unknown")

#Logging User Authentication Attempts
import logging
logging.basicConfig(filename = 'authentication.log', filemode = 'w', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
def authenticate_user(username,password):
    correct_user = "admin"
    correct_password = "password123"
    try:
        if username == correct_user and password == correct_password:
            logging.info(f"Successfully login attempt by user: {username}")
            return True
        else:
            logging.warning(f"Failed login attempt by user: {username}")
    except Exception as e:
        logging.error(f"An error occurred during authentication: {e}")
        return False
authenticate_user("admin","password123")

authenticate_user("admin","password1456")

#Logging Function Execution Times
import logging
import time
logging.basicConfig(filename = 'execution_log.log', level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s' )
def slow_function():
    start_time = time.time()
    logging.info("Starting Slow Function.")
    time.sleep(4)
    logging.info("Completed the slow function")
    end_time = time.time()
    logging.info(f"Execution Time: {end_time - start_time:2f} seconds")
slow_function()

#Logging Bank Account Transactions:
import logging
logging.basicConfig(filename = 'bank_transactions.log', level = logging.INFO, format = '%(asctime)s - %(levelname)s - %(message)s')
class BankAccount:
    def __init__(self,account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance
        logging.info(f"Account created for {account_holder} with balance {balance}.")
    def deposit(self,amount):
        self.balance += amount
        logging.info(f"Deposited {amount} to {self.account_holder}'s account. New Balance {self.balance}")
    def withdraw(self,amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient Funds.")
            self.balance -= amount
            logging.info(f"Withdrew {amount} from {self.account_holder}'s account. New Balance {self.balance}")
        except Exception as e:
            logging.error(f"Withdrew Failed: {e}")
account = BankAccount('Bob',100)
account.deposit(50)
account.withdraw(200)
account.withdraw(100)

#Logging Attendance System
import logging
logging.basicConfig(filename = 'attendance.log',level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
def attendance(student_id, present):
    try:
        if not isinstance(present,bool):
            raise ValueError("Attendance must be boolean value.")
        status = "Present" if present else "Absent"
        logging.info(f"Student ID {student_id}: {status}")
    except ValueError as e:
        logging.error(f"Error making attendance for Student ID {student_id}: {e}")
attendance(101,True)
attendance(102,False)
attendance(105,"Yes")

#Logging Email Sending
import logging
import random
logging.basicConfig(
    filename = 'email.log',
    level = logging.INFO,
    format = '%(levelname)s - %(message)s - %(asctime)s'
)
def send_email(recipient,subject):
    try:
        if not "@" in recipient:
            raise ValueError("Invalid email address.")
        if random.random() > 0.5:
            logging.info(f"Email sent to {recipient} with subject '{subject}'")
        else:
            raise ConnectionError("Failed to connect to the email server.")
    except ValueError as e:
        logging.error(f"Email not sent to {recipient}: {e} ")
    except ConnectionError as e:
        logging.warning(f"Email delivered failed for {recipient}: {e}")
send_email("geethabandela.55@gmailcom","Hello!Welcome to python.")
send_email("radhaswamygmail.com","Welcome")

#Temperature Converter with Logging
import logging

logging.basicConfig(
    filename='temperature_conversion.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    logging.info(f"Converted {celsius}°C to {fahrenheit}°F")
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    logging.info(f"Converted {fahrenheit}°F to {celsius}°C")
    return celsius

def main():
    try:
        choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? ").strip().upper()
        print(f"User selected: {choice}")

        if choice == "C":
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C is {celsius_to_fahrenheit(celsius)}°F")

        elif choice == "F":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit)}°C")

        else:
            logging.error(f"Invalid conversion choice: {choice}")
            print("Invalid choice.")

    except ValueError as e:
        logging.error(f"Invalid temperature input: {e}")
        print("Error: Please enter a valid number for temperature.")

if __name__ == "__main__":
    main()

