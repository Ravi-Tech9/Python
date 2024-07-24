
'''
user query will be this way: please enter your workout? chest/back/shoulder/bicep/tricep/abs/legs
output to query: your todays workout is ['seated_knee_pull-ups', 'seated_cable_row_pull', 'seated_lat_pull_over', 'seated_weight_back_pull', 'dead-lift', 'standing_cable_pull_over', 'barbell_pull_over']
instead of printing the output as straight list box, the output should print one after another 
'''

#gym program 
# program should prompt the workout with specific area 
# if I type chest by checking the available list, it should display all chest workout with reps


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



# shoulder variables 

shoulder_1 = "seated_dumbell_shoulder_press"
shoulder_2 = "Standing_Barbell_shoulder_press"
shoulder_3 = "weight_plate_raise"
shoulder_4 = "dumbell_lateral_raise"
shoulder_5 = "Cable_rope_pull-to-face"
shoulder_6 = "Barbell_pull_over-to-neck"
shoulder_7 = "dumbell_shrugs"
shoulder_8 = "farmers_drag"
shoulder_9 = "seated_shoulder_press_machine"

shoulder = [shoulder_1,shoulder_2,shoulder_3,shoulder_4,shoulder_5,shoulder_6,shoulder_7,shoulder_8,shoulder_9]


# Biceps & tricep variables 

Bicep_1 = "Trap_bar_concentrated_curl"
Bicep_2 = "standing_dumbell_curl"
Bicep_3 = "seated_dubmell_curl"
Bicep_4 = "dumbell_concentrated_peach_row"
Bicep_5 = "dumbell_concetrated_curl"
Bicep_6 = "barbell_curl"

Tricep_1 = "stand_Bar_cable_pull"
Tricep_2 = "Dumbell_tricep_curl_behind"
Tricep_3 = "standing_rope_cable_pull"
Tricep_4 = "Standing_Bar_cable_pull_over_head"
Tricep_5 = "Tricep_bench_press_with_plates"
Tricep_6 = "Tricep_skull_crusher"

Bicep_Tricep = [Bicep_1,Tricep_1,Bicep_2,Tricep_2,Bicep_3,Tricep_3,Bicep_4,Tricep_3,Bicep_4,Tricep_4,Bicep_5,Tricep_5,Bicep_6,Tricep_6]



# Abs variables 

Abs_1 = "iron_bar_shoulder_twist"
Abs_2 = "upper_abs_crunch"
Abs_3 = "lower_abs_leg_raise"
Abs_4 = "side_abs_obliques"
Abs_5 = "Hanging_leg_raise"
Abs_6 = "Hanging_obliques"
Abs_7 = "side_ab_crunches"

Abs = [Abs_1,Abs_2,Abs_3,Abs_4,Abs_5,Abs_6,Abs_7]

# Legs variables 

Legs_1 = "Free_squats"
Legs_2 = "Barbell_squats"
Legs_3 = "Leg_extensions"
Legs_4 = "Leg_press_machine"
Legs_5 = "Calf_raise_machine"
Legs_6 = "Free_standing_calf_raise"
Legs_7 = "Leg_curls"

legs = [Legs_1,Legs_2,Legs_3,Legs_4,Legs_5,Legs_6,Legs_7]

# now user queried his workout 

workout = input("please enter your workout? chest/back/shoulder/bicep/tricep/abs/legs ")

# now you have to display workout based on user query
if workout == 'chest':           #if you are using same keyword to define a list and same word to logic it wont work code will confuse and skip, we have to use strings
    todays_workout = chest
    print(f"your todays workout is:")
    for i in chest:
        print(i)
    
elif workout == "back":
    todays_workout = back 
    for i in back:
        print(i)
    
elif workout == "shoulder":
    todays_workout = shoulder 
    print(f"your todays workout is:")
    for i in shoulder:
        print(i)
    
elif workout == "bicep":
    todays_workout = Bicep_Tricep 
    print(f"your todays workout is:")
    for i in Bicep_Tricep:
        print(i)
    
elif workout == "tricep":
    todays_workout = Bicep_Tricep 
    print(f"your todays workout is:")
    for i in Bicep_Tricep:
        print(i)
    
elif workout == "abs":
    todays_workout = Abs 
    print(f"your todays workout is:")
    for i in Abs:
        print(i)
    
elif workout == "legs":
    todays_workout = legs 
    for i in legs:
        print(i)
    

else:
    print("please plan for your workout")








