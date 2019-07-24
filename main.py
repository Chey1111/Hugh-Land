##################################################################
# Title":    Hugh-Land                                           #
# By:        Steven Jacks and Jeff Shipton                       #
# Date:      Started 7/23/2019                                   #
# Objective: Wtf?  go bleep urself.  This a text based game niku #
##################################################################

#MAP KEY:

##########   ###########   ###########
# CLOSET #---# KITCHEN #---# BEDROOM #
##########   ###########   ###########
                  |
               #########
               # PORCH #
               #########
                  |
###########   ############   #######   #########
# LIBRARY #---# SIDEWALK #---# BAR #---# STORE #
###########   ############   #######   #########
      |            |
############   ##########
# COMPUTER #   # STREET #
############   ##########
                   |
            ################
            # STOCK MARKET #
            ################
                   |
 ############   ########
 # DUMPSTER #---# ALLEY#
 ############   ########

# This is where we set up the initial game variables
 # when start show game is not over
   game = 0
# This variable shows where the starting location is at.
# You can change the hardcode if you wish for a different starting location.
    location = "porch"
# HP is made for what call hitpoints.  If your
# hitpoints drop below zero then you are diededs.
  HP = 100
# This variable is made for tracking the players amount
# of money carried.  Default is that it starts at zero.
  MO = 0

# THIS IS WHERE THE TEXT-GAME LOOP BEGINS

# This is in reference to the "game" variable instated earlier
# Which is set to a default of 0(zero).
while game < 1:

# Upon loop of text interface show basic variable values
# As associated with the players view of the game.

print("HP:{}".format(HP))
  print("You are at {}.".format(location))

###########################################################
# THIS SECTION IS FOR WHERE WHAT YOU CAN SEE IS DISPLAYED #
###########################################################

## disp is displayed in nsew order

  if location == "closet":
    print("To the east is the kitchen.")

  if location == "kitchen":
    print("To the south is the porch.")
    print("To the east is the closet.")
    print("To the west is the bedroom.")

  if location == "bedroom":
    print("To the west is the kitchen.")

  if location == "porch":
    print("To the north is the kitchen.")
    print("To the south is the sidewalk.")
  
  if location == "library":
    print("To the south is the computer.")
    print("To the east is the sidewalk.")

  if location == "sidewalk":
    print("To then north is the porch.")
    print("To the south is the street.")
    print("To the east is the library.")
    print("To the west is the bar.")
    
  if location == "bar":
    print("To the wast is the store.")
    print("To the east is the sidewalk.")

  if location == "store":
    print("To the west is the bar.")
    
  if location == "computer":
    print("To the north is the library.")
    
  if location == "street":
    print("To the north is the sidewalk.")
    print("To the south is the stock market.")
    
  if location == "stock market":
    print("To the north is the street.")
    print("To the south is the alley.")
    
  if location == "dumpster":
    print("To the east is the alley.")

  if location == "alley":
    print("To the north is the stock market.")
    print("To the west is the dumpster.")
    
#############################################################
#                                                           #
# Yeah.  So this part is where you ask the USER for input:? #
#                                                           #
#############################################################

# #####
#  /
# <-----
#  \
# #####

print(next)
  next =  input("WHAT NEXT?:")

# This line shows how to display the users input back
# to them for the fucking hell of it.

# #####
#  /
# <-----
#  \
# #####

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
    
#####################  
# THIS IS FOR WARPS #
#####################

  if next == "warp porch":
    location = "porch"
