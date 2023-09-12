
n = 5 

m = 3

available = [3, 3, 2]  

max_demand = [[7, 5, 3],  
              [3, 2, 2],
              [9, 0, 2],
              [2, 2, 2],
              [4, 3, 3]]

allocation = [[0, 1, 0],   
             [2, 0, 0],
             [3, 0, 2],
             [2, 1, 1],
             [0, 0, 2]]

def calculate_need(need, max_demand, allocation):
  for i in range(n):
    for j in range(m):
      need[i][j] = max_demand[i][j] - allocation[i][j]

processes = [i for i in range(n)]

need = [[0 for i in range(m)] for i in range(n)]  
calculate_need(need, max_demand, allocation)

def is_safe(processes, available, max_demand, allocation, need):
  
  finish = [False] * n

  for i in range(n):
    finish[i] = False
  
  count = 0 

  while (count < n):

    for p in range(n):
      if (finish[p] == False):

        for j in range(m):
          if (need[p][j] > available[j]):
            break
          
        if (j == m - 1):
          
          for k in range(m):
            available[k] += allocation[p][k]
            
          finish[p] = True
          count += 1

          break

  if (count < n):
    print("System is not in safe state")

  else:
    print("System is in safe state")

is_safe(processes, available, max_demand, allocation, need)