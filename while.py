enter_number = int(input("Please enter a number: "))
while enter_number != -1:
    print(enter_number)
    enter_number = int(input("Please enter a number: "))

total = 0
count = 0

while True:
    number = float(input("Enter a number: "))
    if number == -1:
        break
    total += number
    count += 1

if count > 0:
    average = total / count
    print(f"\nAverage of the numbers: {average:.2f}")
else:
    print("\nNo valid numbers were entered.")