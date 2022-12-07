myDict = {
    "Fast": "In a quick manner",
    "Suraj": "Refers to the bright like a sun",
    "Marks" :[1, 100, 50, 55],
    "anotherdict": {'fast':'quick'},
    1: 2
    }

# Dictionary Methods
print("\n")
print(list(myDict.keys())) #Print the keys of the dictionary
print(myDict.values()) #Print the keys of the dictionary
print(myDict.items()) #Print the (key, value) for all items of the dictionary
print(myDict)
updateDict={
    "Samir": "friend",
    "Sandy": "friend",
}
myDict.update(updateDict) #update the dictionary by adding key-value pairs from updatedict
print(myDict)

print(myDict.get("Suraj")) 
print(myDict["Suraj"])
print(myDict.get("parbati")) # return none as parbati is not present in the dictionary
# print(myDict["parbati"]) # throws an error as parbati is not present in the dictionary 