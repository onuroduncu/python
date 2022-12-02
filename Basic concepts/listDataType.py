#list data type(collections) []
#elements of list changable
#---------------------------------
myList = []
print(type(myList)) #<class 'list'>
myList2 = list() #built-in function
print(type(myList2)) #<class 'list'>
fruits = ["apple", "banana", "pineapple", "pear"] #elements
print(fruits) #['apple', 'banana', 'pineapple', 'pear'] ->four elements
print(len(fruits)) #4
#list[x] x= indice
print(fruits[0]) #apple
print(fruits[1]) #banana
print(fruits[2]) #pineapple
print(fruits[3]) #pear
#print(fruits[4]) #IndexError: list index out of range
fruits[0] = "watermelon"
print(fruits) #['watermelon', 'banana', 'pineapple', 'pear']

diffList = [True , 'a', 12.4, 4, 2j]
print(diffList) #[True, 'a', 12.4, 4, 2j]
print(len(diffList)) #5
print(type(diffList[0])) #<class 'bool'>

diffList.append(False) #add new element to end of the list
print(diffList) #[True, 'a', 12.4, 4, 2j, False]

diffList.insert(4,'b') #add new element anywhere we want
print(diffList) #[True, 'a', 12.4, 4, 'b', 2j, False]

diffList.remove('a') #remove any element that we want
print(diffList) #[True, 12.4, 4, 'b', 2j, False]

#remove end element
print(diffList.pop()) #False -> deleted element
print(diffList) #[True, 12.4, 4, 'b', 2j]

print(diffList.pop(2)) #4 -> deleted element
print(diffList) #[True, 12.4, 'b', 2j]

#turn reverse the list
diffList.reverse()
print(diffList) #[2j, 'b', 12.4, True]

#for max and min function same data types
numbers = [5, 3, 8, 7, 9, 6, 1, 2]
print(min(numbers)) #1
print(max(numbers)) #9
print(max(fruits)) #watermelon
#print(min(diffList)) #TypeError: '<' not supported between instances of 'str' and 'complex'

fruits2 = fruits
print(fruits)
print(fruits2)
print(id(fruits)) #1582298850688
print(id(fruits2)) #1582298850688
print(fruits2 is fruits) #True
fruits2.append("kiwi")
#as you see same id and both of them changed
print(fruits) #['watermelon', 'banana', 'pineapple', 'pear', 'kiwi']
print(fruits2) #['watermelon', 'banana', 'pineapple', 'pear', 'kiwi']
print(id(fruits)) #2097266451840
print(id(fruits2)) #2097266451840

#id's changed
fruits2= list(fruits2)
print(id(fruits)) #1799629989248
print(id(fruits2)) #1799630517056

text = "Hello World"
print(list(text)) #['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

#it can hold the all of list in one list
newList = [fruits , fruits2 , numbers, diffList]
print(newList) #['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
               #[['watermelon', 'banana', 'pineapple', 'pear', 'kiwi'], ['watermelon', 'banana', 'pineapple', 'pear', 'kiwi'], [5, 3, 8, #7, 9, 6, 1, 2], #[2j, 'b', 12.4, True]]
print(newList[0][0]) #watermelon
print(newList[:2]) #[['watermelon', 'banana', 'pineapple', 'pear', 'kiwi'], ['watermelon', 'banana', 'pineapple', 'pear', 'kiwi']]