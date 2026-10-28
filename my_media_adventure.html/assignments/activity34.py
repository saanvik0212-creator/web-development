biryani = ("Chicken biryani", "Spices", "Indian", 50)
ramen = ("Cheese", "ramen noodles", "Chilli flakes", 20)
all_recipes = (biryani, ramen)
print("\nFirst recipe name:", all_recipes[0][0])
print("Second recipe time;", all_recipes[1][3])
print("ramen details:", ramen[1][3])

print("\nRamen details:")
for detail in ramen:
    print("-", detail)

fruits = {"mango", "orange", "banana", "apple", "dragon fruit", "banana"}
food = {"biryani", "apple", "sushi", "burrito", "banana", "biryanai"}
print("\nfruits:", fruits)
print("\nTotal:", len(fruits))
all = fruits.union(food)
common = fruits.intersection(food)
onlyfruits = fruits.difference(food)
unique = fruits.symmetric_difference(food)

print("\nall (union):", all)
print("common(intersection):", common)
print("only in fruits (difference):", onlyfruits)
print("Not coomon:", unique)
