                                  ⚒️ Greedy Problem : Job Sequencing with Deadlines
💡 Problem Statement:

You are given n jobs, each has:
A deadline
A profit
Takes 1 unit of time
👉 Your task: Schedule the jobs to maximize profit, without overlapping and only before deadlines.
📥 Input:
jobs = [
    {"id": "A", "deadline": 2, "profit": 100},
    {"id": "B", "deadline": 1, "profit": 19},
    {"id": "C", "deadline": 2, "profit": 27},
    {"id": "D", "deadline": 1, "profit": 25},
    {"id": "E", "deadline": 3, "profit": 15}
]
🎯 Output:
Max profit jobs to schedule → ['A', 'C', 'E']
Total profit → 142

🧠 Greedy Strategy:
Sort jobs by profit (high → low)
Try to put each job in the latest free slot before its deadline
Use a time slot array to mark which slots are filled
==========================================================================
✅ Python Code:
def job_sequencing(jobs):
    # Step 1: Sort jobs by profit descending
    jobs.sort(key=lambda x: x["profit"], reverse=True)
    
    n = max(job["deadline"] for job in jobs)  # max time slots needed
    slots = [False] * n  # Track free time slots
    result = [None] * n  # Store job IDs
    total_profit = 0

    for job in jobs:
        # Find a free slot from job.deadline-1 to 0
        for i in range(min(n, job["deadline"]) - 1, -1, -1):
            if not slots[i]:
                slots[i] = True
                result[i] = job["id"]
                total_profit += job["profit"]
                break

    return [j for j in result if j], total_profit
============================================================================
# Test
jobs = [
    {"id": "A", "deadline": 2, "profit": 100},
    {"id": "B", "deadline": 1, "profit": 19},
    {"id": "C", "deadline": 2, "profit": 27},
    {"id": "D", "deadline": 1, "profit": 25},
    {"id": "E", "deadline": 3, "profit": 15}
]

scheduled_jobs, total_profit = job_sequencing(jobs)
print("Jobs scheduled:", scheduled_jobs)
print("Total profit:", total_profit)

✅ Output:
Jobs scheduled: ['C', 'A', 'E']
Total profit: 142

input:
jobs = [
    {"id": "J1", "deadline": 2, "profit": 50},
    {"id": "J2", "deadline": 1, "profit": 60},
    {"id": "J3", "deadline": 3, "profit": 20},
    {"id": "J4", "deadline": 2, "profit": 30}
]

output:
total_profit: 130
