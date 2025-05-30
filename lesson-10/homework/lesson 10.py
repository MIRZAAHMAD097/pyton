#lesson 10

#1

class Task:
    def __init__(self, title, description, due_date, status = "pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status  = status 

    def mark_completed(self):
        self.status = "completed"

    def display(self):
        print(f"title: {self.title}")
        print(f"description: {self.description}")
        print(f"due date: {self.due_date}")
        print(f"status: {self.status}")


task1 = Task("Finish Project", "Complete the final report", "2025-06-01")
task1.display()
task1.mark_completed()
task1.display()


#2

class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.status = "pending"

    def mark_completed(self):
        self.status = "completed"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_tasks(self, title, due_date):
        self.tasks.append(Task(title, due_date))

    def display(self):
        for task in self.tasks:
            print(f"{task.title} - {task.due_date} - {task.status}")

todo = ToDoList()
todo.add_tasks("Homework", "2025-06-01")
todo.display()
todo.tasks[0].mark_completed()
todo.display()

#3

class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.status = "Pending"

    def mark_completed(self):
        self.status = "Completed"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date):
        self.tasks.append(Task(title, due_date))

    def mark_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return f"Task '{title}' marked as completed"
        return "Task not found"

    def list_tasks(self):
        for task in self.tasks:
            print(f"{task.title} - {task.due_date} - {task.status}")

    def incomplete_tasks(self):
        for task in self.tasks:
            if task.status == "Pending":
                print(f"{task.title} - {task.due_date} - {task.status}")

# CLI Interface
todo = ToDoList()

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. List All Tasks")
    print("4. Show Incomplete Tasks")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Enter task title: ")
        due_date = input("Enter due date: ")
        todo.add_task(title, due_date)

    elif choice == "2":
        title = input("Enter task title to mark as complete: ")
        print(todo.mark_complete(title))

    elif choice == "3":
        todo.list_tasks()

    elif choice == "4":
        todo.incomplete_tasks()

    elif choice == "5":
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid option. Please try again.")

#4

class Task:
    def __init__(self, title, completed = False):
        self.title = title
        self.completed = completed

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def show_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
        else:
            print("invalid task number. ")

todo = ToDoList()


todo.add_task("Do Python homework")
todo.add_task("Read a book")
todo.add_task("Go for a walk")


print("All Tasks:")
todo.show_tasks()


todo.complete_task(1)


print("\nAfter marking task 2 complete:")
todo.show_tasks()


#ex 2

#1

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display(self):
        print(f"title: {self.title}\nAuthor: {self.author}\nContent: {self.content} ")

post = Post("Pyton basics", "learn pyton", "Jimmy")
post.display()

#2

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        self.posts.append(Post(title, content, author))

    def list_posts(self):
        for post in self.posts:
            print(f"{post.title} - {post.author}")

    def display_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(f"{post.title} - {post.content}")

blog = Blog()
blog.add_post("Python", "Learn Python basics", "Alice")
blog.add_post("AI", "Future of AI", "Bob")

blog.list_posts()
blog.display_by_author("Alice")

#3

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        self.posts.append(Post(title, content, author))

    def list_posts(self):
        for post in self.posts:
            print(f"{post.title} - {post.author}" )

    def display_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(f"{post.title} - {post.content}")

blog = Blog()

while True:
    choice = input("\n1. Add Post  2. List Posts  3. Show Author Posts  4. Exit\nChoose: ")

    if choice == "1":
        blog.add_post(input("Title: "), input("Content: "), input("Author: "))
    elif choice == "2":
        blog.list_posts()
    elif choice == "3":
        blog.display_by_author(input("Enter author name: "))
    elif choice == "4":
        break


#4

class Post:
    def __init__(self, title, content, author):
        self.title, self.content, self.author = title, content, author

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            self.posts.pop(index)
        else:
            print("invalid index")

    def edit_post(self, index, new_title = None, new_content = None):
        if 0 <= index < len(self.posts):
            if new_title:
                self.posts[index].title = new_title
            if new_content:
                self.posts[index].content = new_content
            else:
                print("invalid index")

    def latest_posts(self, n = 3):
        for post in self.posts[-n:]:
            print(f"{post.title} by {post.author}")

    def list_posts(self):
        for i, p in enumerate(self.posts):
            print(f"{i}:{p.title} by {p.author}")

blog = Blog()
blog.add_post(Post("First", "Content 1", "Ali"))
blog.add_post(Post("Second", "Content 2", "Vali"))
blog.add_post(Post("Third", "Content 3", "Ali"))
blog.add_post(Post("Fourth", "Content 4", "Vali"))

print("All Posts:")
blog.list_posts()

print("\nLatest Posts:")
blog.latest_posts(2)

print("\nEditing post 1:")
blog.edit_post(1, new_title="Updated Second")

print("\nAfter edit:")
blog.list_posts()

print("\nDeleting post 0:")
blog.delete_post(0)

print("\nAfter delete:")
blog.list_posts()


#5

class Post:
    def __init__(self, title, content, author):
        self.title, self.content, self.author = title, content, author

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            self.posts.pop(index)
        else:
            print("invalid index")

    def edit_post(self, index, new_title = None, new_content = None):
        if 0 <= index < len(self.posts):
            if new_title:
                self.posts[index].title = new_title
            if new_content:
                self.posts[index].content = new_content
            else:
                print("invalid index")

    def latest_posts(self, n = 3):
        for post in self.posts[-n:]:
            print(f"{post.title} by {post.author}")

    def list_posts(self):
        for i, p in enumerate(self.posts):
            print(f"{i}:{p.title} by {p.author}")

blog = Blog()


post1 = Post("Python Basics", "Learn Python step by step.", "Alice")
post2 = Post("Django Intro", "Building web apps with Django.", "Bob")
post3 = Post("Data Science", "Data analysis techniques.", "Alice")


blog.add_post(post1)
blog.add_post(post2)
blog.add_post(post3)

print("All Posts:")
blog.list_posts()

print("\nLatest Posts:")
blog.latest_posts(2)

print("\nEditing post 1:")
blog.edit_post(1, new_title="Django for Beginners", new_content="A beginner-friendly guide to Django.")

print("\nAfter edit:")
blog.list_posts()

print("\nDeleting post 0:")
blog.delete_post(0)

print("\nAfter delete:")
blog.list_posts()


#ex 3
#1

class Account:
    def __init__(self, account_number, holder_name, balance = 0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("insufficient funds")

    def display(self):
        print(f"account: {self.account_number}, holder: {self.holder_name}, balance: {self.balance} ")

acc = Account("12345", "John Doe", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.display()


#2

class Account:
    def __init__(self, account_number, holder_name, balance = 0):
        self.account_number = account_number
        self.hoder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("insuffient funds")

    def check_balance(self):
        return self.balance
    
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, holder_name, balance = 0):
        self.accounts[account_number] = Account(account_number, holder_name, balance)

    def check_balance(self, account_number):
        return self.accounts.get(account_number).check_balance() if account_number in self.accounts else "account not found"
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)

bank = Bank()
bank.add_account("45672", "Robben", 250000)
bank.deposit("45672", 90000)
bank.withdraw("45672", 45000)
print("balance: ", bank.check_balance("45672"))


#3

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        """Stores account number, holder name, and balance"""
        self.account_number, self.holder_name, self.balance = account_number, holder_name, balance

    def deposit(self, amount):
        """Adds money to the account"""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraws money if balance is sufficient"""
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def check_balance(self):
        """Displays current balance"""
        return self.balance

class Bank:
    def __init__(self):
        """Manages a list of accounts"""
        self.accounts = {}

    def add_account(self, acc_num, holder, balance=0):
        """Adds a new account"""
        self.accounts[acc_num] = Account(acc_num, holder, balance)

    def deposit(self, acc_num, amount):
        """Deposits money into an account"""
        if acc_num in self.accounts:
            self.accounts[acc_num].deposit(amount)
        else:
            print("Account not found!")

    def withdraw(self, acc_num, amount):
        """Withdraws money from an account"""
        if acc_num in self.accounts:
            self.accounts[acc_num].withdraw(amount)
        else:
            print("Account not found!")

    def check_balance(self, acc_num):
        """Checks the account balance"""
        return self.accounts[acc_num].check_balance() if acc_num in self.accounts else "Account not found!"

# CLI Banking System
bank = Bank()

while True:
    choice = input("\n1. Add Account  2. Deposit  3. Withdraw  4. Check Balance  5. Exit\nChoose: ")

    if choice == "1":
        bank.add_account(input("Account Number: "), input("Holder Name: "), int(input("Initial Balance: ")))
    elif choice == "2":
        bank.deposit(input("Account Number: "), int(input("Deposit Amount: ")))
    elif choice == "3":
        bank.withdraw(input("Account Number: "), int(input("Withdraw Amount: ")))
    elif choice == "4":
        print("Balance:", bank.check_balance(input("Account Number: ")))
    elif choice == "5":
        break
    else:
        print("Invalid choice, please try again.")


#4

class Account:
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=0):
        """Stores account number, holder name, balance, and overdraft limit"""
        self.account_number, self.holder_name, self.balance, self.overdraft_limit = account_number, holder_name, balance, overdraft_limit

    def deposit(self, amount):
        """Adds money to the account"""
        self.balance += amount

    def withdraw(self, amount):
        """Withdraws money if balance or overdraft allows"""
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        """Transfers money to another account if sufficient funds"""
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            recipient.deposit(amount)
        else:
            print("Transfer failed: Insufficient funds!")

    def display(self):
        """Displays account details"""
        print(f"Account: {self.account_number}, Holder: {self.holder_name}, Balance: {self.balance}, Overdraft Limit: {self.overdraft_limit}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc_num, holder, balance=0, overdraft_limit=0):
        """Adds a new account"""
        self.accounts[acc_num] = Account(acc_num, holder, balance, overdraft_limit)

    def deposit(self, acc_num, amount):
        """Deposits money into an account"""
        if acc_num in self.accounts:
            self.accounts[acc_num].deposit(amount)
        else:
            print("Account not found!")

    def withdraw(self, acc_num, amount):
        """Withdraws money from an account"""
        if acc_num in self.accounts:
            self.accounts[acc_num].withdraw(amount)
        else:
            print("Account not found!")

    def transfer(self, from_acc, to_acc, amount):
        """Transfers money between two accounts"""
        if from_acc in self.accounts and to_acc in self.accounts:
            self.accounts[from_acc].transfer(self.accounts[to_acc], amount)
        else:
            print("One or both accounts not found!")

    def display_account(self, acc_num):
        """Displays details of an account"""
        if acc_num in self.accounts:
            self.accounts[acc_num].display()
        else:
            print("Account not found!")

# Example Usage:
bank = Bank()
bank.add_account("12345", "John Doe", 1000, overdraft_limit=500)
bank.add_account("67890", "Jane Smith", 500)

bank.deposit("12345", 200)
bank.withdraw("67890", 300)
bank.transfer("12345", "67890", 700)

bank.display_account("12345")
bank.display_account("67890")

#5

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} into account {self.account_number}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount} from account {self.account_number}")

    def transfer(self, target_account, amount):
        if amount > self.balance:
            print("Insufficient balance for transfer.")
        elif amount <= 0:
            print("Transfer amount must be positive.")
        else:
            self.withdraw(amount)
            target_account.deposit(amount)
            print(f"Transferred ${amount} from account {self.account_number} to {target_account.account_number}")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.account_number}] - {self.account_holder}, Balance: ${self.balance}"


# Creating two accounts
account1 = BankAccount("1001", "Alice", 1000)
account2 = BankAccount("1002", "Bob", 500)

# Display initial states
print(account1)
print(account2)


# Test deposit
account1.deposit(500)

# Test withdraw
account1.withdraw(200)

# Test transfer
account1.transfer(account2, 300)

# Check balances after transactions
print(account1)
print(account2)
