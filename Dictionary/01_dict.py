apps = {
    "facebook" : "informstion App",
    "instagram": "Picture uploading App",
    "youtube": "Video sharing app",
    "people": ["a","b",5,8]
}

# Accessing a list index in a dictionary. Will throw error if not present
# print(apps["people"][3])

# Accessing a key in the dictionary
# print(apps["youtube"])

# Returns a tuple of key, value pair
# print(apps.items())

# For loop in dictionary
# for a,b in apps.items():
#     print(a, "=>", b)

# Prints all the keys in the dictionary
# for key in apps.keys():
#     print(key)

# Dictionary Update
# apps.update({
#     "instagram": "Photo upload and react",
#     "people": [56,85,98,41],
#     "Tahmid": "Knows Javascript, PHP and Python"
# })

# for key in apps.keys():
#     print(key)

# for a,b in apps.items():
#     print(a, "=>", b)

# Dictionary get. It wil return a value if the key is available in the dictionary. If not it will return None.
print(apps.get('instagram'))
