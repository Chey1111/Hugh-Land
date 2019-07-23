game = 0
location = "porch"
HP = 100
MO = 0

while game < 1:
  print("HP:{}".format(HP))
  print("You are at {}.".format(location))

  if location == "porch":
    print("To the north is the kitchen.")
    
  if location == "kitchen":
    print("To the south is the porch.")
  
  next =  input("WHAT NEXT?:")
  # print(" {}").format(next))
  if next == "go kitchen" and location == "porch":
      location = "kitchen"
  if next == "go porch" and location == "kitchen":
      location = "porch"
