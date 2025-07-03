#lesson 19
#Homework Assignment 1: Analyzing Sales Data


import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()
Faker.seed(42)
random.seed(42)


NUM_CUSTOMERS = 10000
NUM_BRANCHES = 50
NUM_EMPLOYEES = 500
NUM_ACCOUNTS = 12000
NUM_TRANSACTIONS = 50000


def generate_customers(n=NUM_CUSTOMERS):
    data = []
    for i in range(1, n + 1):
        data.append([
            i,
            fake.name(),
            fake.date_of_birth(minimum_age=18, maximum_age=80),
            fake.email(),
            fake.phone_number(),
            fake.address().replace('\n', ', '),
            fake.unique.random_number(digits=10),
            fake.unique.random_number(digits=9),
            random.choice(['Employed', 'Unemployed', 'Self-Employed', 'Student', 'Retired']),
            round(random.uniform(1000, 200000), 2),
            fake.date_time_between(start_date='-5y', end_date='-1y'),
            fake.date_time_between(start_date='-1y', end_date='now')
        ])
    columns = [
        "CustomerID", "FullName", "DOB", "Email", "PhoneNumber", "Address",
        "NationalID", "TaxID", "EmploymentStatus", "AnnualIncome",
        "CreatedAt", "UpdatedAt"
    ]
    return pd.DataFrame(data, columns=columns)


def generate_branches(n=NUM_BRANCHES):
    data = []
    for i in range(1, n + 1):
        data.append([
            i,
            f"Branch {i}",
            fake.address().replace('\n', ', '),
            fake.city(),
            fake.state(),
            fake.country(),
            random.randint(1, NUM_EMPLOYEES),
            fake.phone_number()
        ])
    columns = [
        "BranchID", "BranchName", "Address", "City", "State", "Country",
        "ManagerID", "ContactNumber"
    ]
    return pd.DataFrame(data, columns=columns)


def generate_employees(n=NUM_EMPLOYEES):
    data = []
    for i in range(1, n + 1):
        data.append([
            i,
            random.randint(1, NUM_BRANCHES),
            fake.name(),
            random.choice(['Teller', 'Manager', 'Analyst', 'Clerk', 'Officer']),
            random.choice(['HR', 'Finance', 'Operations', 'IT', 'Compliance']),
            round(random.uniform(20000, 120000), 2),
            fake.date_between(start_date='-10y', end_date='today'),
            random.choice(['Active', 'Inactive', 'On Leave'])
        ])
    columns = [
        "EmployeeID", "BranchID", "FullName", "Position", "Department",
        "Salary", "HireDate", "Status"
    ]
    return pd.DataFrame(data, columns=columns)


def generate_accounts(n=NUM_ACCOUNTS, customer_ids=None, branch_ids=None):
    data = []
    for i in range(1, n + 1):
        data.append([
            i,
            random.choice(customer_ids),
            random.choice(['Savings', 'Checking', 'Business']),
            round(random.uniform(0, 100000), 2),
            random.choice(['USD', 'EUR', 'UZS']),
            random.choice(['Active', 'Inactive', 'Closed']),
            random.choice(branch_ids),
            fake.date_between(start_date='-5y', end_date='today')
        ])
    columns = [
        "AccountID", "CustomerID", "AccountType", "Balance", "Currency",
        "Status", "BranchID", "CreatedDate"
    ]
    return pd.DataFrame(data, columns=columns)


def generate_transactions(n=NUM_TRANSACTIONS, account_ids=None):
    data = []
    for i in range(1, n + 1):
        acc_id = random.choice(account_ids)
        tx_type = random.choice(['Deposit', 'Withdrawal', 'Transfer', 'Payment'])
        data.append([
            i,
            acc_id,
            tx_type,
            round(random.uniform(10, 5000), 2),
            random.choice(['USD', 'EUR', 'UZS']),
            fake.date_time_between(start_date='-2y', end_date='now'),
            random.choice(['Success', 'Failed', 'Pending']),
            fake.uuid4()
        ])
    columns = [
        "TransactionID", "AccountID", "TransactionType", "Amount",
        "Currency", "Date", "Status", "ReferenceNo"
    ]
    return pd.DataFrame(data, columns=columns)


df_customers = generate_customers()
df_branches = generate_branches()
df_employees = generate_employees()
df_accounts = generate_accounts(
    customer_ids=df_customers['CustomerID'].tolist(),
    branch_ids=df_branches['BranchID'].tolist()
)
df_transactions = generate_transactions(
    account_ids=df_accounts['AccountID'].tolist()
)


df_customers.to_excel("Customers.xlsx", index=False)
df_branches.to_excel("Branches.xlsx", index=False)
df_employees.to_excel("Employees.xlsx", index=False)
df_accounts.to_excel("Accounts.xlsx", index=False)
df_transactions.to_excel("Transactions.xlsx", index=False)

print("all files has created: Customers, Branches, Employees, Accounts, Transactions")




fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_CREDITCARDS = 8000
NUM_CARD_TRANSACTIONS = 40000
NUM_ONLINE_USERS = 7000
NUM_BILL_PAYMENTS = 20000
NUM_MOBILE_TX = 25000


customer_ids = list(range(1, 10001))  # 1 dan 10000 gacha CustomerID


def generate_credit_cards(n, customer_ids):
    return pd.DataFrame([[
        i,
        random.choice(customer_ids),
        fake.credit_card_number(),
        random.choice(['Visa', 'MasterCard', 'Amex', 'Discover']),
        random.randint(100, 999),
        fake.date_between(start_date='today', end_date='+5y'),
        round(random.uniform(1000, 20000), 2),
        random.choice(['Active', 'Blocked', 'Expired'])
    ] for i in range(1, n + 1)], columns=[
        "CardID", "CustomerID", "CardNumber", "CardType", "CVV",
        "ExpiryDate", "Limit", "Status"
    ])


def generate_card_tx(n, card_ids):
    return pd.DataFrame([[
        i,
        random.choice(card_ids),
        fake.company(),
        round(random.uniform(10, 5000), 2),
        random.choice(['USD', 'EUR', 'UZS']),
        fake.date_time_between(start_date='-2y', end_date='now'),
        random.choice(['Success', 'Failed', 'Pending'])
    ] for i in range(1, n + 1)], columns=[
        "TransactionID", "CardID", "Merchant", "Amount",
        "Currency", "Date", "Status"
    ])


def generate_online_users(n, customer_ids):
    used = random.sample(customer_ids, n)
    return pd.DataFrame([[
        i,
        cid,
        fake.user_name(),
        fake.sha256(),
        fake.date_time_between(start_date='-1y', end_date='now')
    ] for i, cid in enumerate(used, 1)], columns=[
        "UserID", "CustomerID", "Username", "PasswordHash", "LastLogin"
    ])


def generate_bill_payments(n, customer_ids):
    return pd.DataFrame([[
        i,
        random.choice(customer_ids),
        random.choice(['Electricity', 'Water', 'Gas', 'Internet', 'Mobile']),
        round(random.uniform(5, 500), 2),
        fake.date_time_between(start_date='-2y', end_date='now'),
        random.choice(['Paid', 'Failed', 'Pending'])
    ] for i in range(1, n + 1)], columns=[
        "PaymentID", "CustomerID", "BillerName", "Amount", "Date", "Status"
    ])


def generate_mobile_tx(n, customer_ids):
    return pd.DataFrame([[
        i,
        random.choice(customer_ids),
        fake.uuid4(),
        f"v{random.randint(1, 5)}.{random.randint(0, 9)}.{random.randint(0, 9)}",
        random.choice(['TopUp', 'Transfer', 'Payment', 'Deposit']),
        round(random.uniform(10, 3000), 2),
        fake.date_time_between(start_date='-2y', end_date='now')
    ] for i in range(1, n + 1)], columns=[
        "TransactionID", "CustomerID", "DeviceID", "AppVersion",
        "TransactionType", "Amount", "Date"
    ])


df_cards = generate_credit_cards(NUM_CREDITCARDS, customer_ids)
df_card_tx = generate_card_tx(NUM_CARD_TRANSACTIONS, df_cards['CardID'].tolist())
df_online_users = generate_online_users(NUM_ONLINE_USERS, customer_ids)
df_bill_payments = generate_bill_payments(NUM_BILL_PAYMENTS, customer_ids)
df_mobile_tx = generate_mobile_tx(NUM_MOBILE_TX, customer_ids)


df_cards.to_excel("CreditCards.xlsx", index=False)
df_card_tx.to_excel("CreditCardTransactions.xlsx", index=False)
df_online_users.to_excel("OnlineBankingUsers.xlsx", index=False)
df_bill_payments.to_excel("BillPayments.xlsx", index=False)
df_mobile_tx.to_excel("MobileBankingTransactions.xlsx", index=False)

print("Digital Banking table has created.")


from datetime import timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_CUSTOMERS = 10000
NUM_LOANS = 6000
NUM_LOAN_PAYMENTS = 25000
NUM_CREDIT_SCORES = 10000
NUM_DEBT_COLLECTION = 1000

customer_ids = list(range(1, NUM_CUSTOMERS + 1))


def generate_loans(n, customer_ids):
    data = []
    for i in range(1, n + 1):
        start_date = fake.date_between(start_date='-5y', end_date='-1y')
        duration = random.randint(180, 1825)  # 6 months to 5 years
        end_date = start_date + timedelta(days=duration)
        data.append([
            i,
            random.choice(customer_ids),
            random.choice(['Mortgage', 'Personal', 'Auto', 'Business']),
            round(random.uniform(1000, 200000), 2),
            round(random.uniform(2.5, 15.0), 2),
            start_date,
            end_date,
            random.choice(['Active', 'Closed', 'Defaulted'])
        ])
    return pd.DataFrame(data, columns=[
        "LoanID", "CustomerID", "LoanType", "Amount",
        "InterestRate", "StartDate", "EndDate", "Status"
    ])


def generate_loan_payments(n, loan_ids):
    data = []
    for i in range(1, n + 1):
        loan_id = random.choice(loan_ids)
        paid = round(random.uniform(100, 5000), 2)
        remain = max(0, round(random.uniform(0, 100000) - paid, 2))
        data.append([
            i,
            loan_id,
            paid,
            fake.date_between(start_date='-4y', end_date='now'),
            remain
        ])
    return pd.DataFrame(data, columns=[
        "PaymentID", "LoanID", "AmountPaid", "PaymentDate", "RemainingBalance"
    ])

def generate_credit_scores(customer_ids):
    data = []
    for cid in customer_ids:
        data.append([
            cid,
            random.randint(300, 850),
            fake.date_between(start_date='-2y', end_date='now')
        ])
    return pd.DataFrame(data, columns=[
        "CustomerID", "CreditScore", "UpdatedAt"
    ])


def generate_debt_collection(n, customer_ids):
    data = []
    for i in range(1, n + 1):
        data.append([
            i,
            random.choice(customer_ids),
            round(random.uniform(500, 50000), 2),
            fake.date_between(start_date='-2y', end_date='today'),
            fake.name()
        ])
    return pd.DataFrame(data, columns=[
        "DebtID", "CustomerID", "AmountDue", "DueDate", "CollectorAssigned"
    ])


df_loans = generate_loans(NUM_LOANS, customer_ids)
df_loan_payments = generate_loan_payments(NUM_LOAN_PAYMENTS, df_loans['LoanID'].tolist())
df_credit_scores = generate_credit_scores(customer_ids)
df_debt_collection = generate_debt_collection(NUM_DEBT_COLLECTION, customer_ids)


df_loans.to_excel("Loans.xlsx", index=False)
df_loan_payments.to_excel("LoanPayments.xlsx", index=False)
df_credit_scores.to_excel("CreditScores.xlsx", index=False)
df_debt_collection.to_excel("DebtCollection.xlsx", index=False)

print("Loans & Credit files created: Loans, LoanPayments, CreditScores, DebtCollection")



import pandas as pd
import random
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_CUSTOMERS = 10000
NUM_KYC = 9500
NUM_FRAUD = 3000
NUM_AML = 800
NUM_REGULATORY = 300

customer_ids = list(range(1, NUM_CUSTOMERS + 1))


def generate_kyc(n, customer_ids):
    used = random.sample(customer_ids, n)
    return pd.DataFrame([[
        i,
        cid,
        random.choice(['Passport', 'National ID', 'Driver License']),
        fake.uuid4(),
        fake.name()
    ] for i, cid in enumerate(used, 1)], columns=[
        "KYCID", "CustomerID", "DocumentType", "DocumentNumber", "VerifiedBy"
    ])


def generate_fraud(n, customer_ids):
    return pd.DataFrame([[
        i,
        random.choice(customer_ids),
        random.randint(1, 200000),  # TransactionID
        random.choice(['Low', 'Medium', 'High', 'Critical']),
        fake.date_between(start_date='-2y', end_date='now')
    ] for i in range(1, n + 1)], columns=[
        "FraudID", "CustomerID", "TransactionID", "RiskLevel", "ReportedDate"
    ])


def generate_aml(n, customer_ids):
    return pd.DataFrame([[
        i,
        random.choice(customer_ids),
        random.choice(['Structuring', 'Smurfing', 'Shell Company', 'Suspicious Transfers']),
        random.choice(['Open', 'Closed', 'Under Investigation']),
        random.randint(1000, 9999)  # InvestigatorID
    ] for i in range(1, n + 1)], columns=[
        "CaseID", "CustomerID", "CaseType", "Status", "InvestigatorID"
    ])


def generate_reg_reports(n):
    return pd.DataFrame([[
        i,
        random.choice(['KYC Summary', 'Fraud Report', 'AML Filing', 'Quarterly Audit']),
        fake.date_between(start_date='-2y', end_date='now')
    ] for i in range(1, n + 1)], columns=[
        "ReportID", "ReportType", "SubmissionDate"
    ])


df_kyc = generate_kyc(NUM_KYC, customer_ids)
df_fraud = generate_fraud(NUM_FRAUD, customer_ids)
df_aml = generate_aml(NUM_AML, customer_ids)
df_reg_reports = generate_reg_reports(NUM_REGULATORY)


df_kyc.to_excel("KYC.xlsx", index=False)
df_fraud.to_excel("FraudDetection.xlsx", index=False)
df_aml.to_excel("AML_Cases.xlsx", index=False)
df_reg_reports.to_excel("RegulatoryReports.xlsx", index=False)

print("Compliance & Risk files created: KYC, FraudDetection, AML_Cases, RegulatoryReports")



import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_DEPARTMENTS = 12
NUM_EMPLOYEES = 500  
NUM_SALARIES = 3000
NUM_ATTENDANCE = 5000

employee_ids = list(range(1, NUM_EMPLOYEES + 1))


def generate_departments(n, employee_ids):
    department_names = [
        "Finance", "IT", "HR", "Legal", "Risk", "Marketing", "Compliance",
        "Security", "Operations", "Treasury", "Customer Service", "Audit"
    ]
    return pd.DataFrame([[
        i + 1,
        department_names[i],
        random.choice(employee_ids)
    ] for i in range(n)], columns=[
        "DepartmentID", "DepartmentName", "ManagerID"
    ])


def generate_salaries(n, employee_ids):
    return pd.DataFrame([[
        i,
        random.choice(employee_ids),
        round(random.uniform(500, 5000), 2),
        round(random.uniform(0, 1000), 2),
        round(random.uniform(0, 500), 2),
        fake.date_between(start_date='-2y', end_date='today')
    ] for i in range(1, n + 1)], columns=[
        "SalaryID", "EmployeeID", "BaseSalary", "Bonus", "Deductions", "PaymentDate"
    ])


def generate_attendance(n, employee_ids):
    data = []
    for i in range(1, n + 1):
        emp_id = random.choice(employee_ids)
        check_in = fake.date_time_between(start_date='-6mo', end_date='now')
        work_hours = random.uniform(4, 9)
        check_out = check_in + timedelta(hours=work_hours)
        data.append([
            i,
            emp_id,
            check_in,
            check_out,
            round(work_hours, 2)
        ])
    return pd.DataFrame(data, columns=[
        "AttendanceID", "EmployeeID", "CheckInTime", "CheckOutTime", "TotalHours"
    ])


df_departments = generate_departments(NUM_DEPARTMENTS, employee_ids)
df_salaries = generate_salaries(NUM_SALARIES, employee_ids)
df_attendance = generate_attendance(NUM_ATTENDANCE, employee_ids)


df_departments.to_excel("Departments.xlsx", index=False)
df_salaries.to_excel("Salaries.xlsx", index=False)
df_attendance.to_excel("EmployeeAttendance.xlsx", index=False)

print("Human Resources files created: Departments, Salaries, EmployeeAttendance")


import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_CUSTOMERS = 10000
NUM_INVESTMENTS = 4000
NUM_STOCK_ACCOUNTS = 2000
NUM_FOREX = 3000

customer_ids = list(range(1, NUM_CUSTOMERS + 1))


def generate_investments(n, customer_ids):
    data = []
    for i in range(1, n + 1):
        start_date = fake.date_between(start_date='-3y', end_date='-1y')
        duration_days = random.randint(180, 1825)
        maturity_date = start_date + timedelta(days=duration_days)
        data.append([
            i,
            random.choice(customer_ids),
            random.choice(['Mutual Fund', 'Bonds', 'Stocks', 'Real Estate', 'ETF']),
            round(random.uniform(1000, 100000), 2),
            round(random.uniform(1.5, 12.0), 2),
            maturity_date
        ])
    return pd.DataFrame(data, columns=[
        "InvestmentID", "CustomerID", "InvestmentType", "Amount", "ROI", "MaturityDate"
    ])

def generate_stock_accounts(n, customer_ids):
    firms = ['Robinhood', 'E-Trade', 'Charles Schwab', 'TD Ameritrade', 'Fidelity']
    data = []
    for i in range(1, n + 1):
        invested = round(random.uniform(1000, 50000), 2)
        current = invested + round(random.uniform(-5000, 10000), 2)
        data.append([
            i,
            random.choice(customer_ids),
            random.choice(firms),
            invested,
            current
        ])
    return pd.DataFrame(data, columns=[
        "AccountID", "CustomerID", "BrokerageFirm", "TotalInvested", "CurrentValue"
    ])


def generate_forex(n, customer_ids):
    currency_pairs = ['USD/EUR', 'USD/JPY', 'EUR/GBP', 'GBP/USD', 'USD/UZS', 'EUR/CHF']
    data = []
    for i in range(1, n + 1):
        pair = random.choice(currency_pairs)
        rate = round(random.uniform(0.5, 15000.0), 4)
        amount = round(random.uniform(100, 20000), 2)
        data.append([
            i,
            random.choice(customer_ids),
            pair,
            rate,
            amount
        ])
    return pd.DataFrame(data, columns=[
        "FXID", "CustomerID", "CurrencyPair", "ExchangeRate", "AmountExchanged"
    ])


df_investments = generate_investments(NUM_INVESTMENTS, customer_ids)
df_stock_accounts = generate_stock_accounts(NUM_STOCK_ACCOUNTS, customer_ids)
df_forex = generate_forex(NUM_FOREX, customer_ids)


df_investments.to_excel("Investments.xlsx", index=False)
df_stock_accounts.to_excel("StockTradingAccounts.xlsx", index=False)
df_forex.to_excel("ForeignExchange.xlsx", index=False)

print("Investments & Treasury files created: Investments, StockTradingAccounts, ForeignExchange")


import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_CUSTOMERS = 10000
NUM_POLICIES = 3000
NUM_CLAIMS = 1500
NUM_USERS = 5000
NUM_LOGS = 7000
NUM_INCIDENTS = 300

customer_ids = list(range(1, NUM_CUSTOMERS + 1))
user_ids = list(range(1, NUM_USERS + 1))


def generate_policies(n, customer_ids):
    return pd.DataFrame([[
        i,
        random.choice(customer_ids),
        random.choice(['Health', 'Life', 'Auto', 'Home', 'Travel']),
        round(random.uniform(50, 1000), 2),
        round(random.uniform(1000, 100000), 2)
    ] for i in range(1, n + 1)], columns=[
        "PolicyID", "CustomerID", "InsuranceType", "PremiumAmount", "CoverageAmount"
    ])


def generate_claims(n, policy_ids):
    return pd.DataFrame([[
        i,
        random.choice(policy_ids),
        round(random.uniform(100, 50000), 2),
        random.choice(['Pending', 'Approved', 'Rejected']),
        fake.date_between(start_date='-3y', end_date='today')
    ] for i in range(1, n + 1)], columns=[
        "ClaimID", "PolicyID", "ClaimAmount", "Status", "FiledDate"
    ])


def generate_logs(n, user_ids):
    return pd.DataFrame([[
        i,
        random.choice(user_ids),
        random.choice(['Login', 'Logout', 'PasswordChange', 'FailedLogin', 'TwoFactor']),
        fake.date_time_between(start_date='-6mo', end_date='now')
    ] for i in range(1, n + 1)], columns=[
        "LogID", "UserID", "ActionType", "Timestamp"
    ])


def generate_incidents(n):
    systems = ['OnlineBanking', 'MobileApp', 'CoreSystem', 'ATMNetwork', 'DatabaseServer']
    return pd.DataFrame([[
        i,
        random.choice(systems),
        fake.date_between(start_date='-3y', end_date='today'),
        random.choice(['Resolved', 'Investigating', 'Unresolved'])
    ] for i in range(1, n + 1)], columns=[
        "IncidentID", "AffectedSystem", "ReportedDate", "ResolutionStatus"
    ])


df_policies = generate_policies(NUM_POLICIES, customer_ids)
df_claims = generate_claims(NUM_CLAIMS, df_policies['PolicyID'].tolist())
df_logs = generate_logs(NUM_LOGS, user_ids)
df_incidents = generate_incidents(NUM_INCIDENTS)


df_policies.to_excel("InsurancePolicies.xlsx", index=False)
df_claims.to_excel("Claims.xlsx", index=False)
df_logs.to_excel("UserAccessLogs.xlsx", index=False)
df_incidents.to_excel("CyberSecurityIncidents.xlsx", index=False)

print("Insurance & Security files created: InsurancePolicies, Claims, UserAccessLogs, CyberSecurityIncidents")

import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_CUSTOMERS = 10000
NUM_MERCHANTS = 1500
NUM_MERCHANT_TRANSACTIONS = 6000

customer_ids = list(range(1, NUM_CUSTOMERS + 1))


def generate_merchants(n, customer_ids):
    industries = ['Retail', 'E-commerce', 'Electronics', 'Food & Beverage', 'Travel', 'Healthcare', 'Education']
    return pd.DataFrame([[
        i,
        fake.company(),
        random.choice(industries),
        f"{fake.city()}, {fake.country()}",
        random.choice(customer_ids)
    ] for i in range(1, n + 1)], columns=[
        "MerchantID", "MerchantName", "Industry", "Location", "CustomerID"
    ])


def generate_merchant_transactions(n, merchant_ids):
    payment_methods = ['Card', 'Wire Transfer', 'ACH', 'Cash', 'Mobile Pay']
    return pd.DataFrame([[
        i,
        random.choice(merchant_ids),
        round(random.uniform(10, 10000), 2),
        random.choice(payment_methods),
        fake.date_between(start_date='-1y', end_date='today')
    ] for i in range(1, n + 1)], columns=[
        "TransactionID", "MerchantID", "Amount", "PaymentMethod", "Date"
    ])


df_merchants = generate_merchants(NUM_MERCHANTS, customer_ids)
df_merchant_transactions = generate_merchant_transactions(NUM_MERCHANT_TRANSACTIONS, df_merchants["MerchantID"].tolist())


df_merchants.to_excel("Merchants.xlsx", index=False)
df_merchant_transactions.to_excel("MerchantTransactions.xlsx", index=False)

print("Merchant Services files created: Merchants, MerchantTransactions")


#1
top_balances = df_accounts[df_accounts["Status"] == "Active"] \
    .groupby("CustomerID")["Balance"].sum() \
    .sort_values(ascending=False).head(3).reset_index()
top_balances = top_balances.merge(df_customers[["CustomerID", "FullName"]], on="CustomerID")
print(top_balances)


#2
active_loans = df_loans[df_loans["Status"] == "Active"]
multi_loan_customers = active_loans.groupby("CustomerID") \
    .filter(lambda x: len(x) > 1)["CustomerID"].unique()
print(df_customers[df_customers["CustomerID"].isin(multi_loan_customers)][["CustomerID", "FullName"]])


#3
fraudulent_tx = df_fraud.merge(df_transactions, left_on="TransactionID", right_on="TransactionID", how="inner")
print(fraudulent_tx[["FraudID", "CustomerID", "TransactionID", "RiskLevel", "ReportedDate"]])


#4
loans_with_accounts = df_loans.merge(df_accounts[["CustomerID", "BranchID"]], on="CustomerID", how="left")
loan_per_branch = loans_with_accounts.groupby("BranchID")["Amount"].sum().reset_index()
loan_per_branch = loan_per_branch.merge(df_branches[["BranchID", "BranchName"]], on="BranchID")
print(loan_per_branch.sort_values(by="Amount", ascending=False))


#5
large_tx = df_transactions[df_transactions["Amount"] > 10000].sort_values(by="Date")
merged = large_tx.merge(df_accounts[["AccountID", "CustomerID"]], on="AccountID")
merged["NextDate"] = merged.groupby("CustomerID")["Date"].shift(-1)
merged["TimeDiff"] = (merged["NextDate"] - merged["Date"]).dt.total_seconds() / 60
suspicious_customers = merged[(merged["TimeDiff"] <= 60) & (merged["TimeDiff"] > 0)]["CustomerID"].unique()
print(df_customers[df_customers["CustomerID"].isin(suspicious_customers)][["CustomerID", "FullName"]])



#6
# Misol uchun country qo‘shamiz
df_transactions["Country"] = [fake.country_code() for _ in range(len(df_transactions))]

df_tx_loc = df_transactions.merge(df_accounts[["AccountID", "CustomerID"]], on="AccountID")
df_tx_loc.sort_values(by=["CustomerID", "Date"], inplace=True)
df_tx_loc["NextCountry"] = df_tx_loc.groupby("CustomerID")["Country"].shift(-1)
df_tx_loc["NextDate"] = df_tx_loc.groupby("CustomerID")["Date"].shift(-1)
df_tx_loc["TimeGapMin"] = (df_tx_loc["NextDate"] - df_tx_loc["Date"]).dt.total_seconds() / 60

suspicious_cross_country = df_tx_loc[
    (df_tx_loc["Country"] != df_tx_loc["NextCountry"]) & (df_tx_loc["TimeGapMin"] <= 10)
]
print(df_customers[df_customers["CustomerID"].isin(suspicious_cross_country["CustomerID"].unique())][["CustomerID", "FullName"]])
