#gym program 
# if I type chest, it should display all chest workout with reps
# If I give input about the reps it should store my input and collect the data 

# chest variables 

# creating data to variables 
chest_1 = "dumbell-bench-Press"
chest_2 = "dubmbell-incline-bench press"
chest_3 = "dumbell-flyes"
chest_4 = "barbell-bench-press"
chest_5 = "barbell-incline-bench-press"
chest_6 = "seated-chest-press"
chest_7 = "seated-chest-row"

# loading data to data_type 

chest = [chest_1,chest_2,chest_3,chest_4,chest_5,chest_6,chest_7]

# print(chest)
# print(type(chest))

# back variables 

back_1 = "seated_knee_pull-ups"
back_2 = "seated_cable_row_pull"
back_3 = "seated_lat_pull_over"
back_4 = "seated_weight_back_pull"
back_5 = "dead-lift"
back_6 = "standing_cable_pull_over"
back_7 = "barbell_pull_over"

back = [back_1,back_2,back_3,back_4,back_5,back_6,back_7]


# now user queried his workout 

workout = input("please enter your workout? ")

# now you have to display workout based on user query
if workout == 'chest':           #if you are using same keyword to define a list and same word to logic it wont work code will confuse and skip, we have to use strings
    todays_workout = chest
    print(f"your todays workout is {todays_workout}")
elif workout == "back":
    todays_workout = back 
    print(f"your todays workout is {todays_workout}")    
else:
    print("please plan for your workout")





