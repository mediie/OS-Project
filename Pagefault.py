from tabulate import tabulate

def FIFO(ref, f_size):
  memory = []
  p_faults = 0
  for page in ref:
    if page not in memory:
      p_faults += 1
      if len(memory) < f_size:
        memory.append(page)
      else:
        memory.pop(0)
        memory.append(page)
  hits = len(ref) - p_faults
  return p_faults, hits, p_faults / len(ref), hits / len(ref)
def LRU(ref, f_size):
  memory = []
  recent = []
  p_faults = 0
  for page in ref:
    if page in memory:
      recent.remove(page)
      recent.append(page)
    else:
      p_faults += 1
      if len(memory) < f_size:
        memory.append(page)
        recent.append(page)
      else:
        lru = recent.pop(0)
        i = memory.index(lru)
        memory[i] = page
        recent.append(page)
  hits = len(ref) - p_faults
  return p_faults, hits, p_faults / len(ref), hits / len(ref)
    
def optimal(ref, f_size):
  memory = []
  p_faults = 0
  for i in range(len(ref)):
    page = ref[i]
    if page not in memory:
      p_faults += 1
      if len(memory) < f_size:
        memory.append(page)
      else:
        future = ref[i+1:]
        i = []
        for m_page in memory:
          if m_page in future:
            i.append(future.index(m_page))
          else:
            i.append(float('inf'))
        repl = i.index(max(i))
        memory[repl] = page
  hits = len(ref) - p_faults
  return p_faults, hits, p_faults / len(ref), hits / len(ref)
            
def show_Ptable(ref, f_size):
  print("\nRefrence String: ", ref)
  print("Frame Size: ", f_size)

  table = []
  headers = ["Algorithm", "Page Faults", "Hits", "Miss Rate", "Hit Rate"]

  for s, func in [("FIFO", FIFO), ("LRU", LRU), ("Optimal", optimal)]:
    faults, hits, miss_rate, hit_rate = func(ref, f_size)
    table.append([s, faults, hits, f"{miss_rate*100:.2f}", f"{hit_rate*100:.2f}"])

  print(tabulate(table, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
  f_size = int(input("Enter frame size: "))
  ref_input = input("Enter reference string (space-separated): ")
  ref = list(map(int, ref_input.split()))
  show_Ptable(ref, f_size)