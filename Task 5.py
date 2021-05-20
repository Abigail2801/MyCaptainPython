#Write a Python program to print all positive numbers in a range.
list2=[12,14,-95,3]

num = 0
while(num < len(list2)):
      
    # checking condition
    if list2[num] >= 0:
        print(list2[num], end = " ")
      
    # increment num 
    num += 1
