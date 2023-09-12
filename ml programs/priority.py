# Import libraries
import numpy as np

# Initialize variables
nop = int(input("Enter number of processes: "))
p = np.zeros(nop,dtype=int) 
bt = np.zeros(nop,dtype=int)
wt = np.zeros(nop,dtype=int)
tat = np.zeros(nop,dtype=int)

# Take burst time and priority input
print("Enter burst time and priority:")
for i in range(nop):
  print(f"Process {i}:")
  bt[i] = int(input("Burst time: "))
  p[i] = int(input("Priority: "))
  
# Sort burst time and priority based on priority  
for i in range(nop):
  for j in range(i+1,nop):
    if p[i] > p[j]:
      temp = p[i]
      p[i] = p[j]
      p[j] = temp
      
      temp = bt[i]
      bt[i] = bt[j]
      bt[j] = temp
      
# Calculate waiting time  
wt[0] = 0
for i in range(1,nop):
  wt[i] = wt[i-1] + bt[i-1]
  
# Calculate turnaround time
tat = bt + wt

# Display process details 
print("\nProcess No | Priority | Burst Time | Waiting Time | Turnaround Time")
for i in range(nop):
  print(f"{i} | {p[i]} | {bt[i]} | {wt[i]} | {tat[i]}")

# Calculate total waiting time and turnaround time
total_wt = np.sum(wt)
total_tat = np.sum(tat)

# Calculate average waiting time and turnaround time
avg_wt = total_wt/nop
avg_tat = total_tat/nop

# Display total waiting time and turnaround time
print(f"\nTotal Turnaround Time: {total_tat}")
print(f"Total Waiting Time: {total_wt}")

# Display average waiting time and turnaround time
print(f"Average Waiting Time: {avg_wt}")
print(f"Average Turnaround Time: {avg_tat}")