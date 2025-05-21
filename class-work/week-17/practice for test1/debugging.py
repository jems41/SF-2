def calculate_total_price(prices, tax_rate):
    total = sum(prices)
    tax = total * tax_rate
    return total + tax

def find_oldest_person(people):
    oldest_age = 0
    oldest_person = ""
    for name, age in people:
        if age > oldest_age:
            oldest_age = age
            oldest_person = name
    return oldest_person

def generate_report(names, ages):
    report = ""
    for name, age in zip(names, ages):
        report += f"{name} is {age} years old.\n"
    return report

# Prices for products and tax rate
prices = [25.99, 13.45, 9.99, 20.00]
tax_rate = 0.07

# List of people in the format (name, age)
people = [
    ('Alice', 28),
    ('Bob', 34),
    ('Charlie', 32),
    ('David', 45)
]

# Names and ages of employees
names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [28, 34, 32, 45]

# Calculate total price after tax
total_price = calculate_total_price(prices, tax_rate)

# Find the oldest person
oldest_person = find_oldest_person(people)

# Generate a report about employees
report = generate_report(names, ages)

print(f"Total Price (with tax): {total_price:}$")
print(f"The oldest person is {oldest_person}.")
print("Employee Report:")
print(report)