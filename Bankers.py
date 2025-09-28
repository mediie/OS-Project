# Aban Alfaify - 202200484 
# Majid
# Samir


# functions 

def readingvector(prompt, m):
    while True:
        parts = input(prompt).split()
        if len(parts) == m:
            return list(map(int, parts))
        print(f"Please enter exactly {m} integers.")

def readingmatrix(name, processes, resources):
    matrix = []
    for p in range(processes):
        while True:
            row = readingvector(f"{name} [p{p}] (seperate by space, {resources} integers): ", resources)
            matrix.append(row)
            break
    return matrix

# need matrix calculation
def calculate_need(Max, allocated):
    need = []
    for i in range(len(Max)):
        row = []
        width = len(Max[0])
        for j in range(width):
            row.append(Max[i][j] - allocated[i][j])
        need.append(row)
    return need

#safe state check
def safetycheck(available, allocated, need):
    process = len(allocated)
    resources = len(available)

    work = available.copy()
    finish = [False] * process
    safe_sequence = []

    while len(safe_sequence) < process:
        found = False
        for p in range(process):
            if not finish[p] and all(need[p][r] <= work[r] for r in range(resources)):
                for r in range(resources):
                    work[r] += allocated[p][r]
                finish[p] = True
                safe_sequence.append(p)
                found = True
                break
        if not found:
            return False, []
    return True, safe_sequence

#request
def request(available, allocated, need):
    process = len(allocated)
    resources = len(available)

    p= int(input(f"Enter the process number: (0 to {process-1}) p"))

    request = readingvector(f"Request for process p{p}: ({resources} integers)", resources)

    for r in range(resources):
        if request[r] > need[p][r]:
            print("Request is higher than need. request denied.")
            return 
    for r in range(resources):
        if request[r] > available[r]:
            print("Not enough resources available.")
            return 
        

    old_available = available.copy()
    old_allocated = [row.copy() for row in allocated]
    old_need = [row.copy() for row in need]

    for r in range(resources):
        available[r] -= request[r]
        allocated[p][r] += request[r]
        need[p][r] -= request[r]

    #rerun safety check

    safe, sequence = safetycheck(available, allocated, need)
    if safe:
        print("Request granted. system remains in a safe state.")
        print("New safe sequence:", " -> ".join(f"p{i}" for i in sequence))
    else:
        print("Request cannot be granted. Reverting changes.")
        available[:] = old_available
        for i in range(process):
            allocated[i] = old_allocated[i]
            need[i] = old_need[i]


        print("\n After request, state is:")
        print("Available:", available)
        print("Allocation")
        for i in range(process):
            print(f"p{i}: {allocated[i]}")
        print("Need")
        for i in range(process):
            print(f"p{i}: {need[i]}")


#----------------------------- main -----------------------------#
if __name__ == "__main__":
    process = int(input("Enter the number of processes: "))
    resources = int(input("Enter the number of resources: "))
    available = readingvector(f"Available resources: ({resources} integers): ", resources)
    Max = readingmatrix("Max", process, resources)
    allocated = readingmatrix("Allocated", process, resources)

    print("\nCurrent State:")
    print(f"Available:", available)
    print("Max Matrix:")
    for i in range(process):
        print(f"p{i}: {Max[i]}")
    print("Allocated Matrix:")
    for i in range(process):
        print(f"p{i}: {allocated[i]}")
        

need = calculate_need(Max, allocated) 
print("Need Matrix:")
for i in range(process): print(f"p{i}: {need[i]}")


safe, sequence = safetycheck(available, allocated, need)


answer = input("Do you want to make a request? (y/n): ")
if answer.lower() == 'y':
    request(available, allocated, need)
elif answer.lower() == 'n':
        if safe:
            print("System is in safe state.")
            print("Safe sequence:", " -> ".join(f"p{i}" for i in sequence))
        else:
            print("System is not in safe state.")

