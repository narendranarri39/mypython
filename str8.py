#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
#example1:-
txt = "The best things in life are free!"
print("expensive" not in txt)
#example2:-
txt = "narendranani is learig devops"
print("devops" not in txt)
#example3:-
#Use it in an if statement:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")
