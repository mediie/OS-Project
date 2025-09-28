from tabulate import tabulate

class Process:
  def __init__(self, pid, arrival, burst):
    self.pid = pid
    self.arrival = arrival
    self.burst = burst
    self.remaining = burst
    self.waiting = 0
    self.turnaround = 0
    self.start = -1
    self.completion = 0
    
def calc_times(processes):
  for p in processes:
    p.turnaround = p.completion - p.arrival
    p.waiting = p.turnaround - p.burst

def show_table(processes):
  table = [[p.pid, p.arrival, p.burst, p.waiting, p.turnaround] for p in processes]
  avg_wt = sum(p.waiting for p in processes) / len(processes)
  avg_tat = sum(p.turnaround for p in processes) / len(processes)
  print(tabulate(table, headers=["PID", "Arrival", "Burst", "Waiting", "Turnaround"], tablefmt="grid"))
  print(f"\nAverage Waiting Time: {avg_wt:.2f}")
  print(f"Average Turnaround Time: {avg_tat:.2f}")
  
def show_gantt(chart):
  print("\nGantt Chart:")
  for start, end, pid in chart:
    print(f"| P{pid} ({start}-{end}) ", end=" ")
  print("|\n")

def fcfs(processes):
  processes.sort(key=lambda p: p.arrival)
  time = 0
  chart = []
  for p in processes:
    if time < p.arrival:
      time = p.arrival
    p.start = time
    p.completion = time + p.burst
    chart.append((p.start, p.completion, p.pid))
    time = p.completion
  calc_times(processes)
  show_table(processes)
  show_gantt(chart)
  
def sjfP(processes):
  time = 0
  chart = []
  last_pid = -1
  while any(p.remaining > 0 for p in processes):
    ready = [p for p in processes if p.arrival <= time and p.remaining > 0]
    if ready:
      p = min(ready, key=lambda x: x.remaining)
      if p.start == -1:
        p.start = time
      p.remaining -= 1
      if last_pid != p.pid:
        chart.append((time, time + 1, p.pid))
      else:
        chart[-1] = (chart[-1][0], time + 1, p.pid)
      last_pid = p.pid
      time += 1
      if p.remaining == 0:
        p.completion = time
    else:
      time += 1
      last_pid = -1
  calc_times(processes)
  show_table(processes)
  show_gantt(chart)
  
def sjfNP(processes):
  time = 0
  chart = []
  done = []
  while len(done) < len(processes):
    ready = [p for p in processes if p.arrival <= time and p not in done]
    if ready:
      p = min(ready, key=lambda x: x.burst)
      p.start = time
      p.completion = time + p.burst
      chart.append((p.start, p.completion, p.pid))
      time = p.completion
      done.append(p)
    else:
      time += 1
  calc_times(processes)
  show_table(processes)
  show_gantt(chart)

def rr(processes, quantum):
    time = 0
    chart = []
    remaining = [p.burst for p in processes]
    n = len(processes)
    last_pid = -1
    queue = []
    visited = [False] * n

    while True:
        for i in range(n):
            if processes[i].arrival <= time and not visited[i]:
                queue.append(i)
                visited[i] = True

        if not queue:
            time += 1
            continue

        i = queue.pop(0)
        p = processes[i]

        if p.start == -1:
            p.start = time

        curr_quantum = min(quantum, remaining[i])
        remaining[i] -= curr_quantum

        if last_pid != p.pid:
            chart.append((time, time + curr_quantum, p.pid))
        else:
            chart[-1] = (chart[-1][0], time + curr_quantum, p.pid)

        last_pid = p.pid
        time += curr_quantum

        if remaining[i] == 0:
            p.completion = time
        else:
            for j in range(n):
                if processes[j].arrival <= time and not visited[j]:
                    queue.append(j)
                    visited[j] = True
            queue.append(i)

        if all(r == 0 for r in remaining):
            break

    calc_times(processes)
    show_table(processes)
    show_gantt(chart)


def get_processes():
  n = int(input("Enter number of processes: "))
  plist = []
  for i in range(n):
    a = int(input(f"Enter arrival time for P{i}: "))
    b = int(input(f"Enter burst time for P{i}: "))
    plist.append(Process(i, a, b))
  return plist
  
def main():
  while(True):
    print("\n1. FCFS\n2. SJF (Preemptive)\n3. SJF (Non-Preemptive)\n4. Round Robin\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
      break
    plist = get_processes()
    if choice == 1:
      fcfs(plist)
    elif choice == 2:
      sjfP(plist)
    elif choice == 3:
      sjfNP(plist)
    elif choice == 4:
      quantum = int(input("Enter quantum time: "))
      rr(plist, quantum)
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()


