import numpy as np

nop = int(input("Enter number of processes: "))
bt = np.zeros(nop,dtype=int)
wt = np.zeros(nop,dtype=int)
tat = np.zeros(nop,dtype=int)


print("Enter burst time for each process:")
for i in range(nop):
    bt[i] = int(input(f"Process {i}: "))
    

for i in range(nop):
    for j in range(i+1,nop):
        if(bt[i] > bt[j]):
            temp = bt[i]
            bt[i] = bt[j]
            bt[j] = temp


wt[0] = 0 
for i in range(1, nop):
   wt[i] = wt[i-1] + bt[i-1]
   
  
tat = bt + wt


print("\nProcess ID | Burst Time | Waiting Time | Turnaround Time")
for i in range(nop):
    print(f"{i} | {bt[i]} | {wt[i]} | {tat[i]}")
    

total_wt = np.sum(wt)
total_tat = np.sum(tat)


avg_wt = total_wt / nop
avg_tat = total_tat / nop


print(f"\nTotal waiting time: {total_wt}")
print(f"Total turnaround time: {total_tat}") 


print(f"Average waiting time: {avg_wt}")
print(f"Average turnaround time: {avg_tat}")