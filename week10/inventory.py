# 1 - all the numbers come before letters and then signs before numbers surprised me, its a whole system, especially Z being higher than a and things like that.

# 2 - had a shoe reselling hustle in middle school and early highschool, id love to jsut have all my purchases come ina nd get sorted instead of me manually going through each to see how much i spent. since they are different prices i could just sort by exact amoutn charged and know. 

# inventory.py

print("--- Exercise 1: Build the list ---")

inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) #first
print(inventory[-1]) # last
middle = len(inventory) // 2
print(inventory[middle]) # middle item

print("--- Exercise 3: Slicing Practice ---")
print(inventory[:3]) # first three items
print(inventory[-2:]) # last two items
print(inventory[::2]) # every second item

print("--- Exercise 4: Modifying the list ---")
inventory.append("envelope") # add an item to the end
# inventory.append("tape") 
print(inventory)
inventory.remove("tape") # remove an item
print(inventory)

inventory.append("Zoo")
inventory.append("zoo")
inventory.append("apple")
inventory.append("1")
inventory.append("%")
inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple comparison ---")

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordincates: a location should never change by accident.")

print(coords)

print("--- Exercise 6: Average List of Sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total sales: {total}")
print(f"Count: {count}")
print(f"Average sales: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * 0.9, 2)) # apply 10% discount 

print("Original prices:", prices)
print("Discounts:", discount)

print("exercise 8: Filter above a threshhold ---")
sales = [340, 170, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)


print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"average: {sum(high_sales)/len(high_sales)}")

