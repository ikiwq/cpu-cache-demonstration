from utils import *

n = 5000

a = generate_nxn_matrix(n)
b = generate_nxn_matrix(n)

timer = Timer()

timer.start()
# Optimized case
for i in range(0, n):
    for j in range(0, n):
        a[i][j] += b[i][j]
timer.stop_and_print("Optimized case took %s seconds.")

a = generate_nxn_matrix(n)
b = generate_nxn_matrix(n)

timer.start()
# Non optimized case
for i in range(0, n):
    for j in range(0, n):
        # Accessing b column first
        a[i][j] += b[j][i]
timer.stop_and_print("Non optimized case took %s seconds.")

a = generate_nxn_matrix(n)
b = generate_nxn_matrix(n)

timer.start()
# Even worse case
for i in range(0, n):
    for j in range(0, n):
        # Accessing a and b columns first
        a[j][i] += b[j][i]
timer.stop_and_print("Worst case took %s seconds.")