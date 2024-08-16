#include <iostream>
#include <vector>
#include <ctime>
using namespace std;

void fibonacci_loop(int n)
{
    long long x1 = 0;
    long long x2 = 1;
    long long x3;
    cout << x1 << " ";

    for (int i = 2; i <= n; i++)
    {
        cout << x2 << " ";
        x3 = x1 + x2;
        x1 = x2;
        x2 = x3;
    }
    cout << endl;
}

void fibonacci_dp(int n)
{
    vector<long long> fibs(n);
    fibs[0] = 0;
    fibs[1] = 1;
    cout << fibs[0] << " ";
    cout << fibs[1] << " ";

    for (int i = 2; i < n; i++)
    {
        fibs[i] = fibs[i - 1] + fibs[i - 2];
        cout << fibs[i] << " ";
    }
    
    cout << endl;
}

void fibonacci_recursion_helper(int n, long long a, long long b, int count)
{
    if (n == 0)
    {
        return;
    }

    cout << a << " ";
    if (count < n)
    {
        fibonacci_recursion_helper(n, b, a + b, count + 1);
    }
    else
    {
        cout << endl;
    }
}

void fibonacci_recursion(int n)
{
    vector<long long> fibs(n, -1);
    fibonacci_recursion_helper(n, 0, 1, 1);
}

void fibonacci_memo_helper(int n, int a, int b, vector<long long> &fibs, int count)
{
    fibs[count-1] = a;
    if (count < n)
    {
        fibonacci_memo_helper(n, b, a + b, fibs, count + 1);
    }
}

void fibonacci_memo(int n)
{
    vector<long long> fibs(n, -1);
    fibonacci_memo_helper(n, 0, 1, fibs, 1);

    for(int i = 0; i < n; i++){
        cout << fibs[i] << " ";
    }
    cout << endl;
}

int main() {
    int n = 50;
    struct timespec start, end;

    // Recursion
    clock_gettime(CLOCK_MONOTONIC, &start);
    fibonacci_recursion(n);
    clock_gettime(CLOCK_MONOTONIC, &end);
    cout << "Recursion Time: " << (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9 << " seconds" << endl;
    
    // Loop
    clock_gettime(CLOCK_MONOTONIC, &start);
    fibonacci_loop(n);
    clock_gettime(CLOCK_MONOTONIC, &end);
    cout << "Loop Time: " << (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9 << " seconds" << endl;

    // Loop with memoization
    clock_gettime(CLOCK_MONOTONIC, &start);
    fibonacci_dp(n);
    clock_gettime(CLOCK_MONOTONIC, &end);
    cout << "Loop with Memoization Time: " << (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9 << " seconds" << endl;
    
    // Recursion with memoization
    clock_gettime(CLOCK_MONOTONIC, &start);
    fibonacci_memo(n);
    clock_gettime(CLOCK_MONOTONIC, &end);
    cout << "Recursion with Memoization Time: " << (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9 << " seconds" << endl;
    
    return 0;
}