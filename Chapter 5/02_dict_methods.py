marks = {
    "Ayan": 200, 
    "harry": 100,
    "Faizy": 11
}


# Methods

# print(marks.items()) # jitne items ha sab ajaye ge.

# print(marks.keys()) # jitni keys(left side wali values) ha sab ajaye ge.

# print(marks.values()) # jitni values(right side wali values) ha sab ajaye ge.

# print(marks.values()) # jitni values(right side wali values) ha sab ajaye ge.

marks.update({"Ayan": 199, "mota":0})
# Dictionaries mutable hoti ha tu hum unki values ko change and update kar sakte hai, here the new value of ayan will be 199, and mota will be added.
print(marks)