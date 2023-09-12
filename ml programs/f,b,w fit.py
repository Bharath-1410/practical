
memory_size = int(input("Enter memory size: "))
num_blocks = int(input("Enter number of blocks: "))
block_sizes = [0]*num_blocks
block_status = [1]*num_blocks
allocated = [0]*num_blocks
free_space = [0]*num_blocks

for i in range(num_blocks):
  print("Block[",i+1,"]: ",end="")
  block_sizes[i] = int(input())
  free_space[i] = block_sizes[i]

num_processes = int(input("Enter number of processes: "))  
process_sizes = [0]*num_processes

for i in range(num_processes):
  print("Process[",i+1,"]: ",end="")
  process_sizes[i] = int(input())

print("\nFIRST FIT")
print("**********")

for i in range(num_processes):
  for j in range(num_blocks):
    if block_sizes[j] >= process_sizes[i] and block_status[j]==1:
      print("Process",i+1,"is allocated to Block",j+1)
      block_status[j] = 0
      free_space[j] -= process_sizes[i]
      allocated[j] = 1
      break
  if allocated[j] == 0:
     print("Process",i+1,"can't be allocated")

print("\nRemaining space in each block") 
for i in range(num_blocks):
  print("Block[",i+1,"]: ",free_space[i])

print("\nUnallocated blocks:")
for i in range(num_blocks):
  if block_status[i] == 1:
    print("Block[",i+1,"]")

print("\nBEST FIT")
print("********")

for i in range(num_blocks):
  for j in range(0, num_blocks-i-1):
    if block_sizes[j] > block_sizes[j+1] :
      block_sizes[j], block_sizes[j+1] = block_sizes[j+1], block_sizes[j]

for i in range(num_processes):
  for j in range(num_blocks):
    if block_sizes[j] >= process_sizes[i] and block_status[j]==1:
      print("Process",i+1,"is allocated to Block",j+1)
      block_status[j] = 0
      free_space[j] -= process_sizes[i]  
      break
  if block_status[j] == 1:
     print("Process",i+1,"can't be allocated")  

print("\nRemaining space in each block")
for i in range(num_blocks):
  print("Block[",i+1,"]: ",free_space[i])

print("\nUnallocated Blocks:")
for i in range(num_blocks):
  if block_status[i] == 1:
    print("Block[",i+1,"]")
    
print("\nWORST FIT")
print("**********")

for i in range(num_blocks):
  for j in range(0, num_blocks-i-1):
    if block_sizes[j] < block_sizes[j+1] :
      block_sizes[j], block_sizes[j+1] = block_sizes[j+1], block_sizes[j]

for i in range(num_processes):
  for j in range(num_blocks):
    if block_sizes[j] >= process_sizes[i] and block_status[j]==1:
      print("Process",i+1,"is allocated to Block",j+1)
      block_status[j] = 0
      free_space[j] -= process_sizes[i]
      break
  if block_status[j] == 1:
     print("Process",i+1,"can't be allocated")
     
print("\nRemaining space in each block")
for i in range(num_blocks):
  print("Block[",i+1,"]: ",free_space[i])
  
print("\nUnallocated Blocks:")
for i in range(num_blocks):
  if block_status[i] == 1:
    print("Block[",i+1,"]")