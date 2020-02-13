# 1. create a string 
# 2. grab different elements from various index values 
# 3. test slice functionality 
# 4. test stride with slice
# 5. test step or stride with string slicing

str1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 

exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur 

sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
#print the full string 
print(str1 + '\n')

#printing string's index[44]
print (str1[44]+ '\n')

#printing string's chars form range 44 to 55
print(str1[44:55] + '\n')
print(len(str1))

#printing string's chars from range 5 to 444 but also stepping over by 2
print('=========\n' + str1[5:444:2]+ '\n')
print('=========\n')