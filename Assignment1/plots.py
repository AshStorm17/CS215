import matplotlib.pyplot as plt

sizes = [64, 128, 256, 512, 1024]

# Data for C++ Full
cpp_full_integer_sys = [0.00322589, 0.0184266, 0.112976, 0.906322, 9.70922]
cpp_full_double_sys = [0.00335775, 0.0166197, 0.10767, 0.954922, 9.89645]
cpp_full_integer_cpu = [0.0032243, 0.0184264, 0.112976, 0.905428, 9.7092]
cpp_full_double_cpu = [0.0033576, 0.0166195, 0.10767, 0.954895, 9.89642]

# Data for C++ Meat
cpp_meat_integer_sys = [0.0029476, 0.0175317, 0.110256, 0.895415, 9.65738]
cpp_meat_double_sys = [0.0030752, 0.0158946, 0.105231, 0.94466, 9.84056]
cpp_meat_integer_cpu = [0.0029476, 0.0175317, 0.110256, 0.895415, 9.65738]
cpp_meat_double_cpu = [0.0030752, 0.0158946, 0.105231, 0.94466, 9.84056]

# Data for Python Full
python_full_integer_sys = [0.098616, 0.681301, 5.403862, 69.7223, 419.449969]
python_full_double_sys = [0.087268, 0.675906, 5.25701, 46.237827, 381.580608]
python_full_integer_cpu = [0.09375, 0.40625, 3.609375, 42.796875, 247.984375]
python_full_double_cpu = [0.046875, 0.375, 3.578125, 22, 230.359375]

# Data for Python Meat
python_meat_integer_sys = [0.078125, 0.40625, 3.609375, 42.796875, 247.96875]
python_meat_double_sys = [0.046875, 0.375, 3.578125, 21.984375, 230.359375]
python_meat_integer_cpu = [0.175187, 1.499178, 11.777554, 94.583349, 759.249259]
python_meat_double_cpu = [0.173845, 1.380686, 11.753643, 93.376873, 750.59177]

# Full Integer System Time
plt.figure(figsize=(7, 5))
plt.plot(sizes, cpp_full_integer_sys, label='C++ Full Integer (System Time)', color='b', marker='o')
plt.plot(sizes, python_full_integer_sys, label='Python Full Integer (System Time)', color='r', marker='x')
plt.xlabel('Matrix Size (N)')
plt.ylabel('System Time (seconds)')
plt.title('C++ Full Integer (System Time)')
plt.legend()
plt.grid(True)
plt.show()

# Full Double System Time
plt.figure(figsize=(7, 5))
plt.plot(sizes, cpp_full_double_sys, label='C++ Full Double (System Time)', color='g', marker='o')
plt.plot(sizes, python_full_double_sys, label='Python Full Double (System Time)', color='m', marker='x')
plt.xlabel('Matrix Size (N)')
plt.ylabel('System Time (seconds)')
plt.title('C++ Full Double (System Time)')
plt.legend()
plt.grid(True)
plt.show()

# Meat Integer System Time
plt.figure(figsize=(7, 5))
plt.plot(sizes, cpp_meat_integer_sys, label='C++ Meat Integer (System Time)', color='b', marker='s')
plt.plot(sizes, python_meat_integer_sys, label='Python Meat Integer (System Time)', color='r', marker='^')
plt.xlabel('Matrix Size (N)')
plt.ylabel('System Time (seconds)')
plt.title('C++ Meat Integer (System Time)')
plt.legend()
plt.grid(True)
plt.show()

# Meat Double System Time
plt.figure(figsize=(7, 5))
plt.plot(sizes, cpp_meat_double_sys, label='C++ Meat Double (System Time)', color='g', marker='s')
plt.plot(sizes, python_meat_double_sys, label='Python Meat Double (System Time)', color='m', marker='^')
plt.xlabel('Matrix Size (N)')
plt.ylabel('System Time (seconds)')
plt.title('C++ Meat Double (System Time)')
plt.legend()
plt.grid(True)
plt.show()

# Full Integer CPU Time
plt.figure(figsize=(7, 5))
plt.plot(sizes, cpp_full_integer_cpu, label='C++ Full Integer (CPU Time)', color='b', marker='o')
plt.plot(sizes, python_full_integer_cpu, label='Python Full Integer (CPU Time)', color='r', marker='x')
plt.xlabel('Matrix Size (N)')
plt.ylabel('CPU Time (seconds)')
plt.title('C++ Full Integer (CPU Time)')
plt.legend()
plt.grid(True)
plt.show()

# Full Double CPU Time
plt.figure(figsize=(7, 5))
plt.plot(sizes, cpp_full_double_cpu, label='C++ Full Double (CPU Time)', color='g', marker='o')
plt.plot(sizes, python_full_double_cpu, label='Python Full Double (CPU Time)', color='m', marker='x')
plt.xlabel('Matrix Size (N)')
plt.ylabel('CPU Time (seconds)')
plt.title('C++ Full Double (CPU Time)')
plt.legend()
plt.grid(True)
plt.show()

# Meat Integer CPU Time
plt.figure(figsize=(7, 5))
plt.plot(sizes, cpp_meat_integer_cpu, label='C++ Meat Integer (CPU Time)', color='b', marker='s')
plt.plot(sizes, python_meat_integer_cpu, label='Python Meat Integer (CPU Time)', color='r', marker='^')
plt.xlabel('Matrix Size (N)')
plt.ylabel('CPU Time (seconds)')
plt.title('C++ Meat Integer (CPU Time)')
plt.legend()
plt.grid(True)
plt.show()

# Meat Double CPU Time
plt.figure(figsize=(7, 5))
plt.plot(sizes, cpp_meat_double_cpu, label='C++ Meat Double (CPU Time)', color='g', marker='s')
plt.plot(sizes, python_meat_double_cpu, label='Python Meat Double (CPU Time)', color='m', marker='^')
plt.xlabel('Matrix Size (N)')
plt.ylabel('CPU Time (seconds)')
plt.title('C++ Meat Double (CPU Time)')
plt.legend()
plt.grid(True)
plt.show()
