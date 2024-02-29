def max_profit(difficulty, profit, worker):
    jobs = sorted(zip(difficulty, profit))
    worker.sort()

    max_profit = 0
    current_max_profit = 0
    i = 0

    for ability in worker:
        while i < len(jobs) and ability >= jobs[i][0]:
            current_max_profit = max(current_max_profit, jobs[i][1])
            i += 1
        max_profit += current_max_profit

    return max_profit

difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]

result = max_profit(difficulty, profit, worker)
print(f"The maximum profit is: {result}")
