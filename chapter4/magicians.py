magicians = ['alice','david', 'carolina','啦啦啦']
for magician in magicians:
    print(magician.title() + ", that was a great trick")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

print("The first three itme in the list are:") 
for magician in magicians[0:3]:
    print(magician)
print("Three itmes form the middle of the list are:")
for magician in magicians[1:4]:
    print(magician)


print("The last three itmes in the list are.")
for magician in magicians[-3:]:
    print(magician)