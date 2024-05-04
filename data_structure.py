# 
def swapList(list):
     
    first = list.pop(0)  # remove the first element
    print(first) 
    # last = list.pop(-1)
    last = list.pop() # remove the last element
    # print(last)
    print(last)
    list.insert(0, last)  # insert last element to the first position 
    list.append(first) # append the first element to the last position  
     
    return list
     
# Driver code
newList = [12, 35, 9, 56, 24]
 
print(swapList(newList))

list = ["work","as","an","engineer"]
list.insert(0,"I")
list.append('.')
print(' '.join(list))


#swap two elements in a list
def swap_elements(list,post1,post2):
    list[post1],list[post2]=list[post2],list[post1]
    return list
list = [1,2,3,4,5]
pos1,pos2=1,3
print(swap_elements(list,pos1,pos2))

#Find elements of a 
# list by indices present in another list
def find_elements(list1,list2):
    return [list1[i] for i in list2]
list1 = ['a','b','c','d','e','f']
list2 = [0,2,5]
print(find_elements(list1,list2))

l = [1, 2.0, 'have', 'a', 'geeky', 'day']
# assign string
s = 'geeky' 
# check if string is present in list
if s in l:
    print("Yes")
else:
    print("No")

# find a string in a list
def find_string(list,string):
    return string in list;

# find most frequent element in a list
def most_frequent(list):
    return max(set(list), key = list.count) # set() removes duplicates and max() returns the most frequent element, key is used to specify a function to be called on each element before making comparisons

list = [1,2,3,4,1,2,1,2]
print(most_frequent(list))

# remove element from a list
def remove_element(list,element):
    return [i for i in list if i != element]
print(remove_element([1,2,3,4,5,2,2],2))

# creating a list
list1 = [11, 5, 17, 18, 23, 50] 
 
# items to be removed
unwanted_num = [11,5]
 
list1 = [ele for ele in list1 if ele not in unwanted_num]
 
# printing modified list
print("New list after removing unwanted numbers: ", list1)

# Python program to remove multiple
# elements from a list 
 
# creating a list
list1 = [11, 5, 17, 18, 23, 50] 
 
# given index of elements 
# removes 11, 18, 23
unwanted = [0, 3, 4]
 
for ele in sorted(unwanted, reverse = True): 
    del list1[ele]
 
# printing modified list
print (*list1)