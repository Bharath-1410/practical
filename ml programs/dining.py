from threading import Lock

num_philosophers = 5
state = [0] * num_philosophers
locks = [Lock() for _ in range(num_philosophers)] 

THINKING, HUNGRY, EATING = 0, 1, 2

def philosopher(i):

  print(f"\nPhilosopher {i} falls hungry")
  
  if state[i] == THINKING:

    locks[i].acquire()
    locks[(i+1)%num_philosophers].acquire()

    state[i] = HUNGRY

    if state[(i+1)%num_philosophers] != EATING and state[(i-1)%num_philosophers] != EATING:

      print(f"\nPhilosopher {i} can eat")  
      state[i] = EATING
      
      print(f"\nEating in process for philosopher {i}...")

      locks[(i+1)%num_philosophers].release()
      locks[i].release()

    else:
      locks[(i+1)%num_philosophers].release()
      locks[i].release()

  print(f"\nPhilosopher {i} completed its work")
      

def main():

  for i in range(num_philosophers):
    philosopher(i) 

if __name__ == "__main__":
  print("\n\t\t\tDining Philosopher Problem")
  print("\t\t.............................")
  
  main()