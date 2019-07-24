game = 0
location = "porch"
HP = 100
MO = 0

while game < 1:
  print("HP:{}".format(HP))
  print("You are at {}.".format(location))

  if location == "porch":
    print("To the north is the kitchen.")
    print("To the south is the sidewalk.")
    
  if location == "kitchen":
    print("To the south is the porch.")
    print("To the east is the closet.")
    print("To the west is the bedroom.")
    
  if location == "closet":
    print("To the east is the kitchen.")
    
  if location == "bedroom":
    print("To the west is the kitchen.")
    
  if location == "sidewalk":
    print("To then north is the porch.")
    print("To the south is the street.")
    print("To the east is the library.")
    print("To the west is the bar.")
    
  if location == "library":
    print("To the south is the computer.")
    print("To the east is the sidewalk.")
    
  if location == "computer":
    print("To the north is the library.")
    
  if location == "bar":
    print("To the wast is the store.")
    print("To the east is the sidewalk.")
    
  if location == "store":
    print("To the west is the bar.")
    
  if location == "street":
    print("To the north is the sidewalk.")
    print("To the south is the stock market.")
    
  if location == "stock market":
    print("To the north is the street.")
    print("To the south is the alley.")
    
  if location == "alley":
    print("To the north is the stock market.")
    print("To the west is the dumpster.")
    
  if location == "dumpster":
    print("To the east is the alley.")
  
  next =  input("WHAT NEXT?:")
  print(next)
  if location == "porch" and next == "go kitchen":
    location = "kitchen"
  if location == "porch" and next == "go sidewalk":
    location = "sidewalk"

  if location == "kitchen" and next == "go porch":
    location = "porch"
  if location == "kitchen" and next == "go closet":
    location = "closet"
  if location == "kitchen" and next == "go bedroom":
    location = "bedroom"

  if location == "closet" and next == "go kitchen":
    location = "kitchen"
    
  if location == "bedroom" and next == "go kitchen":
    location = "kitchen"
    
  
