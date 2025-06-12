#lesson 13

#1

from datetime import datetime, date

def calculate_age(birthdate):
    today = date.today()
    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        last_month = (today.month - 1) if today.month > 1 else 12
        last_month_year = today.year if today.month > 1 else today.year - 1
        last_month_days = (date(today.year, today.month, 1) - date(last_month_year, last_month, 1)).days
        days += last_month_days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Foydalanuvchidan tug‘ilgan sanani olish
birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

try:
    birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d").date()
    years, months, days = calculate_age(birthdate)
    print(f"You are {years} years, {months} months, and {days} days old.")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")


#2

from datetime import datetime

def next_birthday(birthday_str):
    today = datetime.today().date()
    birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()

    birthday = birthday.replace(year= today.year)
    if birthday < today:
        birthday = birthday.replace(year = today.year + 1)
    return (birthday - today).days

user_birthday = input("enter your birthday(YYYY-MM-DD): ")
days_left = next_birthday(user_birthday)
print(f"days until your next birthday: {days_left}")


#3

from datetime import datetime, timedelta

current_datetime_str = input("enter the current date and time (YYYY-MM-DD): ")
current_datetime = datetime.strptime(current_datetime_str, "%Y-%m-%d %H:%M")

hours = int(input("enter meeting duration(hours): "))
minutes = int(input("enter meeting duration(minutes): "))

meeting_duration = timedelta(hours=hours, minutes=minutes)
end_time = current_datetime + meeting_duration

print(f"meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}")


#4

from datetime import datetime
import pytz

def convert_timezone(date_time_str, from_tz_str, to_tz_str):
    try:
        from_tz = pytz.timezone(from_tz_str)
        to_tz  = pytz.timezone(to_tz_str)
        naive_dt = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
        local_dt = from_tz.localize(naive_dt)
        converted_dt = local_dt.astimezone(to_tz)
        return converted_dt.strftime("%Y-%m-%d %H:%M %Z")
    except Exception as e:
        return f"error: {e}"
    
date_time = input("enter date and time(YYYY-MM-DD HH:MM): ")
from_timezone = input("enter your current timezone(e.g., Europe/Moscow): ")
to_timezone = input("enter target timezone(e.g., America/Texas): ")

converted_time = convert_timezone(date_time, from_timezone, to_timezone)
print(f"converted time: {converted_time}")

#5

import time
from datetime import datetime

def countdown_timer(target_time):
    target = datetime.strptime(target_time, "%Y-%m-%d %H:%M")
    while(remaining := (target - datetime.now()).total_seconds()) > 0:
        print(f"time remaining: {int(remaining)} seconds", end="\r")
        time.sleep(1)
    print("\n time is up")

future_time = input("enter future date and time(YYYY-MM-DD HH:MM): ")
countdown_timer(future_time)

#6

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

email = input("enter an email address: ")
if validate_email(email):
    print("valid email")
else:
    print("invalid email")


#7

def format_phone_number(phone):
       if len(phone) == 10 and phone.isdigit():
            return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
       return " Invalid phone number format"


phone_number = input("Enter a 10-digit phone number: ")
formatted_number = format_phone_number(phone_number)
print(f"Formatted Number: {formatted_number}")


#8

import re

def check_password(password):
    if len(password) < 8:
        return "minimun 8 characters required"
    if not re.search(r"[A-Z]", password):
        return "must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return "must contain at least one lowercase letter"
    if not re.search(r"\d", password):
        return "must contain at least one digit"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "must contain at least one special character"
    return "strong password"
user_password = input("enter your password: ")
print(check_password(user_password))


#9

import re

def find_word(text, word):
    matches = [match.start() for match in re.finditer(rf"\b{word}\b", text, re.IGNORECASE )]
    if matches:
        print(f"found '{word}' at positions: {matches}")
    else:
        print(f"'{word}' not found in the text")

sample_text = "Forests provide fresh air and shelter for countless species. Rivers flow, sustaining life everywhere."

search_word = input("enter a word: ")
find_word(sample_text, search_word)


#10

import re


def extract_dates(text):
    date_patterns = [
        r'\b\d{2}/\d{2}/\d{4}\b',           
        r'\b\d{2}-\d{2}-\d{4}\b',         
        r'\b\d{4}\.\d{2}\.\d{2}\b',       
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4}\b',  
    ]

    found_dates = []
    for pattern in date_patterns:
        found_dates.extend(re.findall(pattern, text))

    return found_dates

user_input = input("Enter a text that might contain dates: ")
dates = extract_dates(user_input)
if dates:
    print("\nDates found:")
    for date in dates:
        print("-", date)
else:
    print("\nNo dates found in the text.")
