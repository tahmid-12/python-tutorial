avengers = {
    "Iron Man": "Robert Downey Jr.",
    "Captain America": "Steve Rogers",
    "Black Widow": "Natasha Romanoff",
    "Hawkeye": "Clicn Barton"
}

key = input("Enter the name of th avengers:\n")
if(avengers.get(key) == None):
    print("Not Found")
else:
    print("The value corresponding to the key is:", avengers.get(key))