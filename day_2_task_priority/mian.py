task_name = []
priority = []
n = input("Enter the number of task: ")
for i in range(int(n)):
    task_name.append(input(f"Enter task {i+1}:"))
    priority.append(int(input(f"Enter priority:")))

store = [tuple(zip(task_name, priority))]
sorted_data = sorted(store, key=lambda x: x[1])

print("\n--- Your Sorted Tasks ---")
for rank, (name, prio) in enumerate(sorted_data, 1):
    print(f"{rank}. [Priority {prio}] {name}")