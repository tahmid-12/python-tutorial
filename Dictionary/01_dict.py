apps = {
    "facebook" : "informstion App",
    "instagram": "Picture uploading App",
    "youtube": "Video sharing app",
    "people": ["a","b",5,8]
}

# Accessing a list index in a dictionary
# print(apps["people"][3])

# Accessing a key in the dictionary
# print(apps["youtube"])

# Returns a tuple of key, value pair
# print(apps.items())

# For loop in dictionary
# for a,b in apps.items():
#     print(a, "=>", b)

# Prints all the keys in the dictionary
for key in apps.keys():
    print(key)

