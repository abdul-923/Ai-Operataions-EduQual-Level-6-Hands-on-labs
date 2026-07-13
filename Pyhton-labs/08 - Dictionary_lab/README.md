
##Practicing Dictionary , key value pairs in python lab


#Commands used:

#Creat Dictionary

user_profile = {
   "name": "Alice",
   "age": 30,
   "city": "New York"
}

print("Dictionary:", user_profile)


##Updating values:

user_profile["age"] = 31

print("updated:", user_profile)

user_profile.pop("city")

print("removed_dict:", user_profile)


##Output##

ictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}
updated: {'name': 'Alice', 'age': 31, 'city': 'New York'}
removed_dict: {'name': 'Alice', 'age': 31}

##Removing key

