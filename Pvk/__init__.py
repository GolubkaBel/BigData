import math
import multiprocessing
import time
from multiprocessing import Pool
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def amdahl_law(n, k):
    return 1 / (n ** 2 * (1 + (k - 1) / n))


def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i ** 2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x


'''t = time.perf_counter()
if __name__ == '__main__':
    with Pool(1) as p:
        print(sum(p.map(if_prime, list(range(1000000)))))
print(time.perf_counter()-t)'''

t_list = [6.7184032, 3.771683, 2.7300703, 2.6283032, 3.1072733, 3.3554568, 4.0697841]
t_list_better = [6.0600467, 3.4295948, 2.69287739, 2.64353089, 3.1835462, 3.44356079, 4.1021091]
n_list = [1, 2, 4, 8, 10, 12, 16]

fig = plt.Figure()
plt.plot(n_list, t_list, color='g', label='(1)')
plt.plot(n_list, t_list_better, color='r', label='(2)')
plt.xlabel('n (processor)', fontsize=16)
plt.ylabel('time, s', fontsize=16)
plt.title('dependence of time on n')
plt.legend()
plt.show()

effect_list = [0, 0, 0, 0]
for i in range(0, 4):
    effect_list[i] = t_list[0] - t_list[i]
    print(effect_list[i])
plt.plot(effect_list, [t_list[0], t_list[1], t_list[2], t_list[3]],
         color='g', label='(1)')
plt.plot(effect_list, [t_list_better[0], t_list_better[1], t_list_better[2], t_list_better[3]],
         color='g', label='(1)')
plt.plot()
plt.xlabel('Effective')
plt.ylabel('Time')
plt.title('dependence of time on effective')
plt.legend()
plt.show()
