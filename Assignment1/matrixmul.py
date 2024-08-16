import numpy as np
import time

def matrix_multiplication_int(N):
    # Total system and CPU time
    start_wall_total = time.time()
    start_cpu_total = time.process_time()
    
    A = np.random.randint(0, 100, (N, N)).astype(np.int32)
    B = np.random.randint(0, 100, (N, N)).astype(np.int32)
    C = np.zeros((N, N), dtype=np.int32)

    # Meat portion (only core matrix multiplication)
    start_cpu_core = time.process_time()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]
    end_cpu_core = time.process_time()

    end_wall_total = time.time()
    end_cpu_total = time.process_time()

    system_time_total = end_wall_total - start_wall_total
    cpu_time_total = end_cpu_total - start_cpu_total
    cpu_time_core = end_cpu_core - start_cpu_core

    return system_time_total, cpu_time_total, cpu_time_core

def matrix_multiplication_double(N):
    # Total system and CPU time
    start_wall_total = time.time()
    start_cpu_total = time.process_time()
    
    A = np.random.randint(0, 100, (N, N)).astype(np.float64)
    B = np.random.randint(0, 100, (N, N)).astype(np.float64)
    C = np.zeros((N, N), dtype=np.float64)

    # Meat portion (only core matrix multiplication)
    start_cpu_core = time.process_time()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i, j] += A[i, k] * B[k, j]
    end_cpu_core = time.process_time()

    end_wall_total = time.time()
    end_cpu_total = time.process_time()

    system_time_total = end_wall_total - start_wall_total
    cpu_time_total = end_cpu_total - start_cpu_total
    cpu_time_core = end_cpu_core - start_cpu_core

    return system_time_total, cpu_time_total, cpu_time_core

sizes = [64, 128, 256, 512, 1024]

for size in sizes:
    sys_time_int, cpu_time_total_int, cpu_time_core_int = matrix_multiplication_int(size)
    sys_time_double, cpu_time_total_double, cpu_time_core_double = matrix_multiplication_double(size)

    print(f"Matrix size {size}x{size} (Integers):")
    print(f"  Total System time: {sys_time_int:.6f} seconds")
    print(f"  Total CPU time: {cpu_time_total_int:.6f} seconds")
    print(f"  Core CPU time (meat portion): {cpu_time_core_int:.6f} seconds\n")

    print(f"Matrix size {size}x{size} (Doubles):")
    print(f"  Total System time: {sys_time_double:.6f} seconds")
    print(f"  Total CPU time: {cpu_time_total_double:.6f} seconds")
    print(f"  Core CPU time (meat portion): {cpu_time_core_double:.6f} seconds\n")
