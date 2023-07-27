from random import Random
import time
from threading import Barrier, Thread

# Initialization of matrix size and matrices A and B
matrix_size = 200
matrix_a = [[0] * matrix_size for a in range(matrix_size)]
matrix_b = [[0] * matrix_size for b in range(matrix_size)]
result = [[0] * matrix_size for r in range(matrix_size)]

# Create Random object and Barrier objects
random = Random()
work_start = Barrier(matrix_size + 1)
work_complete = Barrier(matrix_size + 1)


# Randomly generate values between -5 and 5
# populate values in matrix columns and rows
def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row][col] = random.randint(-5, 5)


# Emplace barrier objects, Multiply Matrix A[row] with Matrix B[column]
def work_out_row(row):
    while True:
        work_start.wait()
        for col in range(matrix_size):
            for i in range(matrix_size):
                result[row][col] += matrix_a[row][i] * matrix_b[i][col]
        work_complete.wait()


# Initialize Thread to run calculation on each row
for row in range(matrix_size):
    Thread(target=work_out_row, args=([row])).start()

# Time block to start timer and measure iterations of multiplication
start = time.time()
for t in range(10):
    generate_random_matrix(matrix_a)
    generate_random_matrix(matrix_b)
    result = [[0] * matrix_size for r in range(matrix_size)]
    work_start.wait()
    work_complete.wait()

# Stop timer and print time
end = time.time()
print("Done, time taken", end - start)





