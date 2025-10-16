#!/usr/bin/env python3
import sys
#my_favs = {}
#my_favs["Book"] = "Paradise Lost (& Paradise Found)"
#my_favs["Season"] = "Autumn"
#my_favs["Disney movie"] = "The Jungle Book 2"
#print(my_favs)

#problem2
#print(my_favs["Book"])

#problem3
#fav_thing = "Book"
#print(my_favs[fav_thing])

#problem4
#print(my_favs["Disney movie"])

#problem5
#fav_thing = "organism"
#print(my_favs[fav_thing])

#question6
#for thing in my_favs:
	#item = my_favs[thing]
	#print(thing, item)

#question7
#my_favs["Book"] = sys.argv[1]
#my_favs["Season"] = sys.argv[2]
#my_favs["Disney movie"] = sys.argv[3]

#question8
#for thing in my_favs:
	#print(thing)

#question9
#my_favs["Book"] = "Revelation"
#print(my_favs)

#user input
my_favs = {"Book": " ", "Season": " ", "Disney movie": " "}
print(my_favs.keys())

x = input()
y = input()
z = input()


my_favs["Book"] = x
my_favs["Season"] = y
my_favs["Disney movie"] = z

print(my_favs)


