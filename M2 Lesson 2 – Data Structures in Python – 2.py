idli = ("Soft Idli", "Breakfast", 15, "Easy")
biryani = ("Ambur Biryani", "Main Course", 50, "Hard")
print("Dish 1:", idli)
print("Name:", idli[0])
print("Course:", idli[1])
print("Complexity:", idli[-1])

menu = (idli, biryani)
print("\nFirst dish name:", menu[0][0])
print("Second dish cooking time:", menu[1][2], "mins")
print("Idli details (sliced):", idli[1:3])

print("\nIdli Dish details:")
for detail in idli:
    print(" -", detail)

idli_ingredients = {"rice", "urad dal", "water", "salt", "fenugreek", "rice"}
biryani_ingredients = {"rice", "chicken", "curd", "mint", "urad dal", "chilli"}
print("\nIdli ingredients:", idli_ingredients)
print("Biryani ingredients:", biryani_ingredients)
print("Total unique Idli staples:", len(idli_ingredients))

idli_ingredients.add("oil")
idli_ingredients.discard("fenugreek")
print("\nUpdated Idli ingredients:", idli_ingredients)

all_ingredients = idli_ingredients.union(biryani_ingredients)
shared_ingredients = idli_ingredients.intersection(biryani_ingredients)
exclusive_idli = idli_ingredients.difference(biryani_ingredients)
non_overlapping = idli_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll ingredients (union):", all_ingredients)
print("Shared ingredients (intersection):", shared_ingredients)
print("Exclusive to Idli (difference):", exclusive_idli)
print("Non-overlapping ingredients (sym. difference):", non_overlapping)