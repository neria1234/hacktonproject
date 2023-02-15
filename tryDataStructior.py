import datastructior

firstList = datastructior.creatList(1)
firstList = datastructior.multiAppend(firstList, 2, 3, 4, 5, 6)

secendList = [1 ,3.55 ,1 ,4.15 ,5 ,6 ,5 ,52.453 ,7 ,435.3 ,1 ,8.3 ,9.134 ,0.13 ,5.534 ,1 ,8 ,7.756 ,9 ,2]

therdList = ["Neria", "David", "Ori", "Netanel", "Maya", "Hana", "Yakove", "Matan"]

if(datastructior.isElement(secendList, 1)):
    secendList = datastructior.multiAppendAndSort(secendList, 23, 4.235 ,17 ,188 ,33) 
    filteredList = datastructior.filterList(secendList, 1, 2)
    reversedList = datastructior.reversList(firstList)
    

firstDividList = datastructior.dividListByElemants(therdList, 3)
print(firstDividList)
secendDividList = datastructior.dividListByGroups(therdList, 4)
print(secendDividList)