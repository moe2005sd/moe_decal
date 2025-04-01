import numpy as np

#Q1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def containsPrimes(arr):
     result = []
     for row in arr:
        found_prime = False
        for num in row:
            if is_prime(num):
                found_prime = True
                break
        if found_prime:
            result.append(row)
     print(np.array(result))
    
arr = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
containsPrimes(arr)

#2.1
def checkerboard():
    print(np.zeros((8, 8), dtype=int))

checkerboard()

#2.2
def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    
    for i in range(0, 8, 2):
        board[i] = (np.arange(8) - 1) % 2
    
    print(board)

checkerboard()

#Q2.3
def checkerboard():
    board = np.zeros((8, 8), dtype=int)
    
    for i in range(0, 8, 2): 
        board[i] = (np.arange(8) - 1) % 2 
        
    for i in range(1, 8, 2): 
        board[i] = np.arange(8) % 2
    
    print(board)

checkerboard()

#Q2.4
def reverse_checkerboard():
    board = np.zeros((8, 8), dtype=int)
    
    for i in range(0, 8, 2): 
        board[i] = np.arange(8) % 2 
        
    for i in range(1, 8, 2): 
        board[i] = (np.arange(8) + 1) % 2
    
    print(board)

reverse_checkerboard()

#Q3
def expansion(arr, num_spaces):
    space = ' ' * num_spaces
    expanded = np.array([space.join(word) for word in arr])
    print(expanded)

universe = np.array(['galaxy', 'clusters'])
expansion(universe, 1)
expansion(universe, 2)

#Q4
def secondDimmest(arr):
    sorted_arr = np.sort(arr, axis=0)
    print(sorted_arr[1])

np.random.seed(123)
stars = np.random.randint(500, 2000, (5, 5))
print(stars)
secondDimmest(stars)




