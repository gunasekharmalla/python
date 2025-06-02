def max_activities(start, end):
    n = len(start)
    activities = list(zip(start, end))  # Combine start and end into tuples like [(1,2), (3,4),...]
    activities.sort(key=lambda x: x[1])  # Sort activities by end time (Greedy key)

    count = 1  # We can always select the first one (earliest to finish)
    last_end = activities[0][1]  # Store the end time of the last selected activity

    for i in range(1, n):  # Loop over remaining activities
        if activities[i][0] >= last_end:  # If current start >= last end → no overlap
            count += 1
            last_end = activities[i][1]  # Update last_end to this activity’s end

    return count

input:
start = [1, 3, 0, 5, 8, 5]
end   = [2, 4, 6, 7, 9, 9]

output:
4

II:
to get activites 

def selection(s,e):
    activites = list(enumerate(zip(s,e)))
    #sorting
    activites.sort(key = lambda x: x[1][1])
    selected = []
    last_end = -1
    #count = 0
    for index, (st, en) in activites:
        if st >= last_end:
            #count += 1
            selected.append((index, st, en))
            last_end = en
    return selected


start = [1, 3, 0, 5, 8, 5]
end   = [2, 4, 6, 7, 9, 9]
print(selection(start, end))

output:
[(0, 1, 2), (1, 3, 4), (3, 5, 7), (4, 8, 9)]

