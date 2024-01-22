



#store the two given list in variables
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

#create a empy list variable 
result_list = []

#create a for loop to iterate the first and second list with the formula of checking if the number is odd or even number.
for num in list1:
    if num % 2 != 0:
        result_list.append(num) # insert or add the value to the result list
    
for num in list2:
    if num % 2 == 0:
        result_list.append(num) # insert or add the value to the result list


#print the result list
print("result list:", result_list)





