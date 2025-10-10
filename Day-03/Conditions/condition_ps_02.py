#Suppose your friend has told you that she will buy a Gucci Bag if she has 10 thousand taka or more. Otherwise if she has 5 thousand taka or more, she will buy a Levis Bag. Otherwise she will buy Something from New Market. She also told you that, if she could buy the Gucci bag and she has more than 20 thousand taka she will also buy a Gucci Belt.
#Write a program to help your friend decide what to buy based on the amount of money she has.
money = float(input("Enter the amount of money you have: "))
    
if money == 20000:
    print("You can buy a Gucci Bag.")
elif money>20000:
        print("You can also buy a Gucci Belt.")
        print("You can buy a Gucci Bag.")
elif money>=5000:
    print("You can buy a Levis Bag.")
else:
    print("You can buy Something from New Market.")
# money = float(input("Enter the amount of money you have: "))