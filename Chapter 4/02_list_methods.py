list = ["apple", "banana", 18, 2.2, "Ayan", "J"]

print(list)

# here are some methods/functions that can we use in list, to modify it. 

# append kar sakte, Append means last me kuch bh add krna.
list.append("18 Sep 2007")
print(list)

# Sort, Sort karna list ko for example:
newList = [1, 22, 18, 2008, 2007,]
newList.sort()
print(f"this is the new sorted list: ", newList)

# Reverse, ye pori list ko ulta kar de ga, like abh agr list 1 se start hokr 2008 pr end ho rhi ha so ab iska ulta hoga.
newList1 = [1, 22, 18, 2008, 2007,]
newList1.reverse()
print(f"this the reverse list", newList1)

# Insert, kuch bh kahi bh insert kar sakte hai, 

insertList = [1, 22, 18, 2008, 2007,]
insertList.insert(3, "Ayan") # ab ye 3rd position yani 18 k bad Ayan add krde ga as an string.
print(f"this is an Insert List: ", insertList)

# POP, pop se ham kisi bh specific Index ki value delete kar sakte hai, 

popList = [1, 2, 3, 4, 5]
popList.pop(3) # 3rd index pr 4 ha tu woh gayab hojaye ka means delete.
print(f"This is POP List: ", popList)

# Remove, Kisi bh list se koi particular value delete krne k liye,

rEx = [1, 5, 45, 2, 2, 5, 6, 2, 4, 5, 6]
rEx.remove(2)
print(f"This is Remove List example: ", rEx) 