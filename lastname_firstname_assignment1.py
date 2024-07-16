#%%,
first_name = "Ian",
age = 17,
height_meters = 1.8,

x = height_meters + age 
print(x)
intro = f"{first_name} {age}"
print(intro)

intro_upper = intro.upper()
print("Uppercase:", intro_upper)

intro_lower = intro.lower()
print("Lowercase:", intro_lower)

intro_title = intro.title()
print("Title case:", intro_title)

intro_swapcase = intro.swapcase()
print("Swapped case:", intro_swapcase)

hobbies = ["Movies", "Sports", "Music"]
print(hobbies)

hobbies.append("Filmaking")
print("new list:", hobbies)

hobbies.pop(0)
print("newer list:", hobbies)

hobbies.reverse()
print("new reversed list:", hobbies)

hobbies.sort()
print("new sorted list:", hobbies)

name = Ian
age = 17
height = 1.8
hobbies = hobbies

profile = { 
    "name": name ,
    "age": age
}
print(profile)

profile["favorite_color"] = "Green"
print("with favorite color:", profile)

del profile["height"]
print("no height:", profile)

hobbies_value = profile["hobbies"]
print("Value hobbies:", hobbies_value)

profile["age"] = profile["age"] + 1
print("After updating age:", profile)
# %%
