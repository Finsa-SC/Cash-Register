


foods = {"Burger": 20000,
                "Fried Frice": 15000,
                "Spagethi": 10000}
drinks = {"Cola": 5000,
                 "Milk": 7000,
                 "Water": 0}
index = 1

print(5*"=", "FOODS",5*"=")

for i, food in enumerate(foods, 1):
    print(f"{i}. {food}")
    index = i + 1
    
print(5*"=", "DRINKS",5*"=")

for i, drink in enumerate(drinks, index):
    print(f"{i}. {drink}")


token = input("Input Number or Name of Food: ")

