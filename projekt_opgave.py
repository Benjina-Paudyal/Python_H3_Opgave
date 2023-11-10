
# H3 Python Project " ANALYSER AF LØBSFIL "

from geopy.distance import distance # to calculate distance between geographical points of the earth(lat & long)
from fitparse import FitFile # to read and parse FIT files, a binary file format
from tabulate import tabulate # to use formatted table to print out 

#OPGAVE 1

# pace:how fast you are running or walking?(speed)
# velocity:how fast and in which direction you are running or walking? 

# converting pace(min/km) to velocity (m/s)
def pace_to_velocity(pace):
    return (10000/60)/pace
#print (pace_to_velocity(10))

# converting velocity to pace
def velocity_to_pace(v):
    return (1000/60)/v
#print (velocity_to_pace(1.67))



#OPGAVE 2

# Defining the fit file 
def read_from_fit(fname=r'C:\Users\benjm\Desktop\projektopgave\data\CA8D1347.FIT'):
    from fit_file import read
    points = read.read_points(fname)
    return points

# Calling the read from the fit file
punkter = read_from_fit()

# Printing the number of points and data for the 300th point
print(f"Der er indlæst {len(punkter)} punkter fra filen")
print(punkter[300])


#OPGAVE 3 & 4

# Function to calculate pace zones
def calculate_pace_zones(points):
    run_distance = 0
    run_time = 0
    walk_distance = 0
    walk_time = 0
    stand_distance = 0
    stand_time = 0

    for i, p in enumerate(points[1:]):  # theory : for example, if the points is [a, b, c], result would be (1,b) & (2,c)
        #pp = previous point
        #p = recent point
        #dd = difference in distance between 2 points(pp & p) i.e d2-d1
        #dt = time between two points i.e t2-t1

        pp = points[i]
        dt = (p['timestamp'] - pp['timestamp']).total_seconds()
        dd = distance((pp['latitude'], pp['longitude']),
                      (p['latitude'], p['longitude'])).meters
        velocity = dd / dt

        if velocity > running_threshold:
            run_distance += dd
            run_time += dt
        elif velocity > walking_threshold:
            walk_distance += dd
            walk_time += dt
        else:
            stand_distance += dd
            stand_time += dt

    return {
        'run_distance': run_distance,
        'run_time': run_time,
        'walk_distance': walk_distance,
        'walk_time': walk_time,
        'stand_distance': stand_distance,
        'stand_time': stand_time
    }

# setting threshold for walking and running
walking_threshold = 0.333 # if velocity is greater than 0.333 then assuming it as a walking
running_threshold = 1.667  # if velocity is greater than 1.667 then assuming it as a running

# Calling the calculate_pace_zones function with the values of different points
result = calculate_pace_zones(punkter)

# Printing the  results
print("Run Distance:", result['run_distance'])
print("Run Time:", result['run_time'])
print("Walk Distance:", result['walk_distance'])
print("Walk Time:", result['walk_time'])
print("Stand Distance:", result['stand_distance'])
print("Stand Time:", result['stand_time'])

# Calculating total time
total_time = result['run_time'] + result['walk_time'] + result['stand_time']

# Calculating and printing the percentages in all three zones
run_percentage = (result['run_time'] / total_time) * 100
walk_percentage = (result['walk_time'] / total_time) * 100
stand_percentage = (result['stand_time'] / total_time) * 100

print(f"Percentage of time in Running zone: {run_percentage:.2f}%")
print(f"Percentage of time in Walking zone: {walk_percentage:.2f}%")
print(f"Percentage of time in Standing zone: {stand_percentage:.2f}%")

# Calculating and printing the total times in each zone
total_run_time = result['run_time']
total_walk_time = result['walk_time']
total_stand_time = result['stand_time']

print(f"Total Run Time: {total_run_time:.2f} seconds")
print(f"Total Walk Time: {total_walk_time:.2f} seconds")
print(f"Total Stand Time: {total_stand_time:.2f} seconds")

# Calculating and printing the total time
total_time = total_run_time + total_walk_time + total_stand_time
print(f"Total Time: {total_time:.2f} seconds")

# Calculate and printing the percentages
run_percentage = (total_run_time / total_time) * 100
walk_percentage = (total_walk_time / total_time) * 100
stand_percentage = (total_stand_time / total_time) * 100

print(f"Percentage of time in Run zone: {run_percentage:.2f}%")
print(f"Percentage of time in Walk zone: {walk_percentage:.2f}%")
print(f"Percentage of time in Stand zone: {stand_percentage:.2f}%")

# Calculating and printing the total percentage (run + walk + stand)
total_percentage = run_percentage + walk_percentage + stand_percentage
print(f"Total Percentage of time across all zones: {total_percentage:.2f}%")
print()
print()


# OPGAVE 5

# Printing the data in the table 

table_data = [
    ["Run:", result['run_distance'], total_run_time, f"{run_percentage:.2f}%"],
    ["Walk:", result['walk_distance'], total_walk_time, f"{walk_percentage:.2f}%"],
    ["Idle:", result['stand_distance'], total_stand_time, f"{stand_percentage:.2f}%"],
    ["Total:", result['run_distance'] + result['walk_distance'] + result['stand_distance'], total_time, f"{total_percentage:.1f}%"]
]

table_header = ['', 'meters', 'seconds', '% of time']
table = [table_header] + table_data
print(tabulate(table, headers='firstrow', tablefmt='plain'))




