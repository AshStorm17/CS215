#include <iostream>
#include <vector>
#include <ctime>

void matrix_multiplication_int(int N) {
    struct timespec start_wall_total, end_wall_total, start_cpu_total, end_cpu_total, start_cpu_core, end_cpu_core;

    // Start total timing
    clock_gettime(CLOCK_MONOTONIC, &start_wall_total);
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start_cpu_total);
    
    std::vector<std::vector<int>> A(N, std::vector<int>(N));
    std::vector<std::vector<int>> B(N, std::vector<int>(N));
    std::vector<std::vector<int>> C(N, std::vector<int>(N, 0));

    // Fill matrices with random integers
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            A[i][j] = rand() % 100, B[i][j] = rand() % 100;

    // Start core timing (meat portion)
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start_cpu_core);
    // Matrix multiplication
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            for (int k = 0; k < N; ++k)
                C[i][j] += A[i][k] * B[k][j];

    // End core timing (meat portion)
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end_cpu_core);

    // End total timing
    clock_gettime(CLOCK_MONOTONIC, &end_wall_total);
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end_cpu_total);

    // Calculate elapsed time
    double wall_time_total = (end_wall_total.tv_sec - start_wall_total.tv_sec) + (end_wall_total.tv_nsec - start_wall_total.tv_nsec) / 1e9;
    double cpu_time_total = (end_cpu_total.tv_sec - start_cpu_total.tv_sec) + (end_cpu_total.tv_nsec - start_cpu_total.tv_nsec) / 1e9;
    double cpu_time_core = (end_cpu_core.tv_sec - start_cpu_core.tv_sec) + (end_cpu_core.tv_nsec - start_cpu_core.tv_nsec) / 1e9;
    
    std::cout << "Matrix size " << N << "x" << N << " (Integers):\n";
    std::cout << "  Total System time: " << wall_time_total << " seconds\n";
    std::cout << "  Total CPU time: " << cpu_time_total << " seconds\n";
    std::cout << "  Core CPU time (meat portion): " << cpu_time_core << " seconds\n";
}

void matrix_multiplication_double(int N) {
    struct timespec start_wall_total, end_wall_total, start_cpu_total, end_cpu_total, start_cpu_core, end_cpu_core;
    
    // Start total timing
    clock_gettime(CLOCK_MONOTONIC, &start_wall_total);
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start_cpu_total);

    std::vector<std::vector<double>> A(N, std::vector<double>(N));
    std::vector<std::vector<double>> B(N, std::vector<double>(N));
    std::vector<std::vector<double>> C(N, std::vector<double>(N, 0));

    // Fill matrices with random doubles
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            A[i][j] = (double)(rand() % 100), B[i][j] = (double)(rand() % 100);

    // Start core timing (meat portion)
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &start_cpu_core);
    // Matrix multiplication
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j)
            for (int k = 0; k < N; ++k)
                C[i][j] += A[i][k] * B[k][j];

    // End core timing (meat portion)
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end_cpu_core);

    // End total timing
    clock_gettime(CLOCK_MONOTONIC, &end_wall_total);
    clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &end_cpu_total);

    // Calculate elapsed time
    double wall_time_total = (end_wall_total.tv_sec - start_wall_total.tv_sec) + (end_wall_total.tv_nsec - start_wall_total.tv_nsec) / 1e9;
    double cpu_time_total = (end_cpu_total.tv_sec - start_cpu_total.tv_sec) + (end_cpu_total.tv_nsec - start_cpu_total.tv_nsec) / 1e9;
    double cpu_time_core = (end_cpu_core.tv_sec - start_cpu_core.tv_sec) + (end_cpu_core.tv_nsec - start_cpu_core.tv_nsec) / 1e9;
    
    std::cout << "Matrix size " << N << "x" << N << " (Doubles):\n";
    std::cout << "  Total System time: " << wall_time_total << " seconds\n";
    std::cout << "  Total CPU time: " << cpu_time_total << " seconds\n";
    std::cout << "  Core CPU time (meat portion): " << cpu_time_core << " seconds\n";
}


int main() {
    srand(time(0));
    int sizes[] = {64, 128, 256, 512, 1024};
    
    for(int size : sizes) {
        matrix_multiplication_int(size);
        matrix_multiplication_double(size);
    }
    return 0;
}