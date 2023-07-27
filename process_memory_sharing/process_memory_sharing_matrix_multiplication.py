import multiprocessing
from random import Random
import time
from multiprocessing import Barrier, Process, Event

# Initialization of matrix size and process count
process_count = 8
matrix_size = 200

# Create Random object
random = Random()


# Randomly generate values between -5 and 5
# populate values in matrix columns and rows
def generate_random_matrix(matrix):
    for row in range(matrix_size):
        for col in range(matrix_size):
            matrix[row * matrix_size + col] = random.randint(-5, 5)


# Create parameters for process variables that will share memory
def work_out_row(id, matrix_a, matrix_b, result, work_start, work_complete):
    while True:
        work_start.wait()
        for row in range(id, matrix_size, process_count):
            for col in range(matrix_size):
                for i in range(matrix_size):
                    result[row * matrix_size + col] += matrix_a[row * matrix_size + i] * matrix_b[i * matrix_size + col]
        work_complete.wait()


if __name__ == '__main__':

    # Start a process
    multiprocessing.set_start_method('spawn')

    # Start Barrier that keeps track of the process count
    work_start = Barrier(process_count + 1)
    work_complete = Barrier(process_count + 1)

    # Create Array for to pass shared data to
    matrix_a = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    matrix_b = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)
    result = multiprocessing.Array('i', [0] * (matrix_size * matrix_size), lock=False)

    # Initialize Process to run calculation on each row
    for p in range(process_count):
        Process(target=work_out_row, args=(p, matrix_a, matrix_b, result, work_start, work_complete)).start()

    # Time block to start timer and measure iterations of multiplication
    start = time.time()
    for t in range(10):
        generate_random_matrix(matrix_a)
        generate_random_matrix(matrix_b)

        for j in range(matrix_size * matrix_size):
            result[j] = 0
        work_start.wait()
        work_complete.wait()

    # Stop timer and print time
    end = time.time()
    print("Done, time taken", end - start)


