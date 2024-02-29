def minCostToPaintWalls(cost, time):
    n = len(cost)
    min_cost = 0
    free_printer_used = False

    for i in range(n):
        if not free_printer_used:
            if cost[i] * time[i] > time[i]:
                min_cost += time[i]
            else:
                min_cost += cost[i] * time[i]
                free_printer_used = True
        else:
            if cost[i] * time[i] > time[i]:
                min_cost += time[i]
            else:
                min_cost += cost[i] * time[i] - time[i]

    return min_cost

cost = [1,2,3,2]
time = [1,2,3,2]
print(minCostToPaintWalls(cost, time))  # Output: 10
