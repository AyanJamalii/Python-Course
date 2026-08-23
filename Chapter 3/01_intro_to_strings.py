# there is many things in HANDBOOK to read about. so parhloo...

# aik String me 2 type k index hote hai aik positive jo first letter se start hota hai, and 2nd one is negative jo last letter se start hokr ulta chalta hai. for example 

name = "Ayan"

name2 = name[-4]  # here we will be getting the A in ans 
print("Through Negative Index:", name2)

name3 = name[3] # here we will be getting A again, cuz its just example, hum 2 tariko se slicing kr sakte hai apne str ki. 
print("Through Positive Index:", name3)


# agar hame multiple words ko slice karna ha str me se tu uske liye ye syntax hai, 

a = "Ayan Jamali"

b = name[0:7] # here colon ":" se pehle wali value ka matlab hota hai kaha se shoro karna ha and colon k bad value ka matlb kaha khtm, jo value likhte ha woh count nh hoti end me, in current case, 0 means A se shoro hokr : 6 means J tk chale gi, Result will be ---> "ayan j", (SPACE ALSO TAKES INDEX).

print("Your Name is:", b)