#1.1
print("EXERCISE 1.1")

x = 1

while x < 30:
    if x in (4, 6, 10):
        print('The value ' + str(x) + ' of x was skipped')
        x += 1
        continue
    
    if x == 15:
        print('The execution of the loop was broken when x was ' + str(x))
        break
    
    print('The value of the loop is: ' + str(x))
    x += 1


#1.2
print("EXERCISE 1.2")

while True:
    line = input("Enter a line (or leave it blank to finish): ")
    
    if line == "":
        break
    
    print(line.upper())

print("Input process finished.")


#2...
print("EXERCISE 2")

balance = 0

while True:
    input_text = input("Enter an operation (D amount / R amount) or leave it blank to finish: ")

    if input_text == "":
        break

    parts = input_text.split()
    
    if len(parts) != 2:
        print("Incorrect format. It should be 'D amount' or 'R amount'.")
        continue

    operation_type, amount = parts
    print(operation_type)
    print(amount)
    
    if operation_type == "D":
        balance += float(amount)
    elif operation_type == "R":
        balance -= float(amount)
    else:
        print("Invalid operation. It should be 'D' for deposit or 'R' for withdrawal.")

print("The final balance is:", balance)


#3...
print("EXERCISE 3")

prime_numbers = 0

while True:
    input_number = input("Enter a number greater than 1 (or 0 to finish): ")
    number = int(input_number)

    if number == 0:
        break

    if number <= 1:
        print("Invalid number. It should be greater than 1.")
    else:
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_numbers += 1

print("The number of prime numbers entered is:", prime_numbers)


#4...
print("EXERCISE 4")

while True:
    start_year = int(input("Enter the starting year: "))
    end_year = int(input("Enter the ending year: "))

    if start_year > end_year:
        print("The starting year should be less than or equal to the ending year.")
    else:
        print("Leap years and multiples of 10 in the range:")
        for year in range(start_year, end_year + 1):
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if year % 10 == 0:
                    print(year)
        break


#5...
print("EXERCISE 5")

for number in range(1, 21):
    if number % 2 != 0:
        continue

    print(number)


#6...
print("EXERCISE 6")

numbers = [10, 25, 35, 45, 50, 60, 70, 80, 90]

target_number = int(input("Enter the number to search in the list: "))

for number in numbers:
    if number == target_number:
        print(f"The number {target_number} was found in the list.")
        break

else:
    print(f"Number {target_number} wasn't found in the list.")


#7...
print("EXERCISE 7")

while True:
    print("MENU OPTIONS:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("0. Exit")

    choice = input("Enter your choice (0 to exit): ")

    if choice == "0":
        print("Exiting the program.")
        break
    elif choice == "1":
        print("You selected Option 1.")
    elif choice == "2":
        print("You selected Option 2.")
    elif choice == "3":
        print("You selected Option 3.")
    else:
        print("Invalid choice. Please select a valid option.")
