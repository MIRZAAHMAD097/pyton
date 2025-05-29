#lesson 9

#1

import math

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
circle = circle(5)
print("area: ", circle.area())
print("perimeter: ", circle.perimeter())

#2

from datetime import datetime
class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def get_age(self):
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year -((today.month, today.day) < (birth_date.month, birth_date.day))
        return age
    
    def display(self):
        print(f"name: {self.name}")
        print(f"country: {self.country}")
        print(f"date of birth: {self.dob}")
        print(f"age: {self.get_age()}")

person = Person("Jack", "USA", "1945-05-05")
person.display()

#3

operator = input("enter an operator(+ - * / ): ")
num1 = float(input("enter 1st number: "))
num2 = float(input("enter 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))

elif operator == "-":
    result = num1 - num2
    print(round(result, 2))

elif operator == "*":
    result = num1 * num2
    print(round(result, 2))

elif operator == "/":
    result = num1 / num2
    print(round(result, 2))

else:
    print(f"the {operator} is unvalid!")

#4

import math

class shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class circle(shape):
    def __init__ (self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi ** self.radius
    
class square(shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

class triangle(shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
circle =circle(5)
triangle = triangle(4,5,6)
square = square(6)

print("Circle -> Area:", circle.area(), "Perimeter:", circle.perimeter())
print("Square -> Area:", square.area(), "Perimeter:", square.perimeter())
print("Triangle -> Area:", triangle.area(), "Perimeter:", triangle.perimeter())


#5

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node
    
    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        return self._search_recursive(node.left, key) if key < node.key else self._search_recursive(node.right, key)

bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(15)

print("Found:", bst.search(5) is not None)  
print("Found:", bst.search(20) is not None)

#6

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None
    
    def is_empty(self):
        return len(self.items) == 0
    
stack = Stack()
stack.push(10)
stack.push(20)
print("pop: ", stack.pop())
print("is empty?" , stack.is_empty())


#7

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data !=key:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
    def display(self):
        current = self.head
        while current:
            print(current.data, end = " ->")
            current = current.next
        print("None")

ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()

ll.delete(20)
ll.display()


#8

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price, quantity=1):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def total_price(self):
        return sum(item["price"] * item["quantity"] for item in self.items.values())
    
    def display_cart(self):
        for name, details in self.items.items():
             print(f"{name}: {details['quantity']} x ${details['price']}")
        print(f"Total: ${self.total_price()}")

cart = ShoppingCart()
cart.add_item("Apple", 1.2, 3)
cart.add_item("Banana", 0.8, 2)
cart.display_cart()

cart.remove_item("Banana")
cart.display_cart()

#9

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None
    
    def display(self):
        print("stack: ", self.items)

stack = Stack()
stack.push(10)
stack.push(5)
stack.push(15)
stack.display()

print("popped: ", stack.pop())
stack.display()


#10

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None
    
    def display(self):
        print("queue: ", self.items)

queue = Queue()
queue.enqueue(10)
queue.enqueue(30)
queue.display()

print("dequeued:", queue.dequeue())
queue.display()

#11

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, balance = 0):
        self.accounts[name] = balance
    
    def deposit(self, name, amount):
        self.accounts[name] += amount

    def withdraw(self, name, amount):
        if self.accounts[name] >= amount:
            self.accounts[name] -= amount

    def show_balance(self, name):
        print(f"{name}'s balance: {self.accounts[name]}")

bank = Bank()
bank.add_account("Messi", 130000)
bank.deposit("Messi", 60000)
bank.withdraw("Messi", 30000)
bank.show_balance("Messi")
