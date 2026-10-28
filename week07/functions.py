# comments 

# 1 - first bug was in line 10, given to me by the error emssage and pretty easy to fix myself. The next bug was harder and codex had to explain it to me and it helped a lot. 

# 2 - calculates price with an applied discount that gets determined by customer tier. Yes, i think a colleague could understand it but to actually use it still need more info about the tiers and discounts 

# 3 - Used ai to help with exercise 5 finsing the second bug in line 16/6. Used it as explanation so i actually know what my fix did within the code and not just blindly changing. 


# Exercise 1

# define calculate tax function


def calculate_tax(price, rate):
   return price * rate

# calling the function with different values

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}")

# Exercise 2 

def apply_discount(price, tier):
    if tier == "gold":
     return price * 0.85  # 15% discount
    elif tier == "silver":
     return price * 0.90  # 10% discount
    elif tier == "bronze":
     return price * 0.95  # 5% discount
    else:
     return price  # no discount

# calling the function with different values

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

  # Exercise 3 

# write it out then refactor it to use a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${after_tax:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# refactor to use a function

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(f"Final Price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price}, Tier: {tier} Final: ${total:.2f}")

    # Exercise 6

x = 100 #apple // global variable

def double_it():
   x = 999 # another apple (not the same as line 68) // local variable
   return x * 2

print(x)
print(double_it())
print(x)




# ----- EXERCISE 5 -----



# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # addded the + sign to the end of the total += sale statement
print(f"Total: ${total}")

count = 0
for sale in sales:   # added the : to the end of sale for the loop statement
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):  # removed the = sign from the while loop statement
    print(sales[i])
    i += 1

print(total)
print(sales)

# i see that the issue is in line 10, where we need to add a colon at the end of the for loop statement.

# what codex said about the error message: "Python expects a colon (:) at the end of a for loop statement. Line 10 is missing it."


# after fixing the : it now says i have an error in line 16, Ai explained it as pyhton counts from 0 while the length of the list is 5, so when i = 5, it will try to access sales[5], which does not exist. The loop should be while i < len(sales): instead of while i <= len(sales):.


# after fixing these two issues, the code should run without errors and produce the correct output for total sales, count of sales, and print each sale in the list.