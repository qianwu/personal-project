stuff = {"food":15,"energy":100, "enemies":3}

# print(stuff.get("food"))

# print(stuff.items())

# print(stuff.keys())

# print(stuff.popitem())
# print(stuff)
'''
print(stuff.setdefault("food"))
print(stuff)
print(stuff.setdefault("friends",123))
print(stuff)
'''

new_items = {"rock":4,"arrows":18}
stuff.update(new_items)
print(stuff)

new_items = {"rock":2,"arrows":8}
stuff.update(new_items)
print(stuff)

up_new = {"food":5,"web":2}
stuff.update(up_new)
print(stuff)

stuff.update(food = 500, web = 200)
print(stuff)