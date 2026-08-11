

import re

test_string = "My 2021 GPA was greater than 2019 and 2020 combined"

print("Test String: ", test_string)
print("Working ... ")


pattern = re.compile(r"\d+")

matches = pattern.findall(test_string)
print("Work Done ")
print("Matches: ", matches)


print("##Replacing")

replaced_string = pattern.sub("XXXX", test_string)
print("Replaced: ", replaced_string)
