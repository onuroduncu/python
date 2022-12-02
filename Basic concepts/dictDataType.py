#dictionary data type (collections) {}
#key:value
#-------------------------------------------

myDict = {}
print(type(myDict)) #<class 'dict'>
myDict = dict()
print(type(myDict)) #<class 'dict'>

myDict2 = {1:"a",2:"b",3:"c"}
"""
myDict2 = {1:"a",
           2:"b",
           3:"c"}
"""
myDict3 = {"1":"a","2":"b","3":"c"}
print(myDict2) #{1: 'a', 2: 'b', 3: 'c'}
print(myDict3) #{'1': 'a', '2': 'b', '3': 'c'}
print(myDict3["1"]) #a
print(myDict3["2"]) #b
print(myDict3["3"]) #c

del myDict3["1"]
print(myDict3) #{'2': 'b', '3': 'c'}
print(len(myDict3)) #2
myDict3["4"] = "d"
print(myDict3) #{'2': 'b', '3': 'c', '4': 'd'}

myList = [1,2,3]
myDict4 = {"numbers":myList}
print(myDict4) #{'numbers': [1, 2, 3]}