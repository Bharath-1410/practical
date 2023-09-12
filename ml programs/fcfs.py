import numpy as np
import matplotlib.pyplot as plt

nop = int(input("enter number of processes:"))
bt = np.zeros(nop)
wt = np.zeros(nop)
tat = np.zeros(nop)

#burst time input
print("enter burst time for each process:")
for i in range(nop):
    bt[i] = int(input(f"Process {i}: "))
#calculate waiting time 
wt[0] = 0
for i in range(1, nop):
    wt[i] = wt[i-1] + bt[i-1]
    
#cal tat
tat = bt + wt

print("\nprocess id | burst time | waiting time | turnaround time")
for i in range(nop):
    print(f"{i} | {bt[i]} | {wt[i]} | {tat[i]}")
    
#cal tw and tat
total_wt = np.sum(wt)
total_tat = np.sum(tat)

avg_wt = total_wt / nop
avg_tat = total_tat /nop

print(f"\nTotal waiting time: {total_wt}")
print(f"\nT0tal turnaround time: {total_tat}")
print(f"\naverage waiting time: {avg_wt}")
print(f"\n average waiting time: {avg_tat}")


 