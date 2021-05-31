#Else in For Loop
#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

#Example
#rint all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

  for x in range(5):
    print(x)
  else:
   print("finished")


names = ("nani", "likhi")
for x in names:
  print(x)
else:
  print("they are couples")
