swimming = int(input("Enter swimming time: "))
cycling = int(input("Enter cycling time: "))
running = int(input("Enter running time: "))
total = swimming + cycling+ running
print(total)
if swimming > cycling:
    award = "Swimming you are winner"
elif swimming > running:
    award = "Swimming you are a winner"
elif cycling > swimming:
    award = "Cycling you are a winner"
elif cycling > running:
    award = "Cycling you are a winner"  
elif running > swimming:
    award = "Running you are a winner"  
elif running > cycling:
    award = "Running you are a winner"  
print("Award:", award)