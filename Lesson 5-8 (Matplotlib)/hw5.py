import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib.pyplot import colorbar
from numpy.ma.core import arange, masked_array, where
from pyparsing import alphas

## 1
fig = plt.figure(0)
ax = plt.axes()
x = np.array([1, 5, 10, 15, 20])
y1 = np.array([1, 7, 3, 5, 11])
y2 = np.array([4, 3, 1, 8, 12])
ax.plot(x, y1, marker='o', color="red", label='line1')
ax.plot(x, y2, '--p', color="green", label='line1')
ax.legend()

## 2
fig = plt.figure(1, figsize=(10, 8))
grid = plt.GridSpec(2, 2, hspace=0.4, wspace=0.3)

plt.subplot(grid[0, :])
x = np.arange(1, 6)
y1 = np.array([1, 7, 6, 3, 5])
plt.plot(x, y1)
ticks_x = np.arange(1, 5.5, 0.5)
ticks_y = np.arange(2, 9, 2)
plt.xticks(ticks_x)
plt.yticks(ticks_y)

plt.subplot(grid[1, 0])
y2 = np.array([9, 4, 2, 4, 9])
plt.plot(x, y2)
plt.xticks(ticks_x)
plt.yticks(ticks_y)

plt.subplot(grid[1, 1])
y3 = np.array([-7, -4, 2, -4, -7])
plt.plot(x, y3)
plt.ylim(-8, 2)
plt.xticks(ticks_x)
plt.yticks(np.arange(-6, 4, 2))


## 3
fig = plt.figure(2)
x = np.arange(-5, 6)
ticks_x = np.arange(-4, 5, 2)
ticks_y = np.arange(0, 26, 5)
y = np.array([25, 16, 8, 4, 1, 0, 1, 4, 8, 16, 25])
plt.plot(x, y)
plt.xticks(ticks_x)
plt.yticks(ticks_y)
plt.arrow(0,
          10,
          0,
          -10,
          length_includes_head=True,
          head_length=1,
          width = 0.1,
          facecolor="green",
          edgecolor="black")
plt.text(0, 10.5, 'min')


## 4
data = np.random.randint(0, 11, (7, 7))
fig = plt.figure(3)
plt.imshow(data)
plt.colorbar(shrink=0.5, aspect=5 ,anchor=(0,0), fraction=0.1)

## 5
fig = plt.figure(4)
x = np.linspace(0, 5, 1000)
plt.plot(x, np.cos(np.pi * x), color='red', alpha=0.7)
plt.fill_between(x, np.cos(np.pi * x), 0, color='blue', alpha=0.7)


## 6
fig = plt.figure(5)
x = np.linspace(0, 5, 10000)
y = np.cos(np.pi * x)
masked_y = np.ma.masked_less(y, -0.5)
plt.plot(x, masked_y, linewidth=3)
plt.ylim(-1, 1)


## 7
fig, axs = plt.subplots(1, 3)
x = np.arange(0,7)
y = x
where_arr = ['pre', 'post', 'mid']
for i, ax in enumerate(axs):
       ax.step(x, y, 'g-o', where=where_arr[i])
       ax.grid()


## 8
fig, ax = plt.subplots()
x = np.arange(11)
y1 = np.array([(-0.2)*i**2+2*i for i in x])
y2 = np.array([(-0.4)*i**2+4*i for i in x])
y3 = np.array([2*i for i in x])
ax.stackplot(x, y1, y2, y3, labels=['y1', 'y2', 'y3'])
ax.legend()


## 9
fig, ax = plt.subplots()
labels = 'Ford', 'Toyota', 'BMW', 'AUDI', 'Jaguar'
sizes = [15, 10, 33, 15, 22]
explode = (0, 0, 0.1, 0, 0)
ax.pie(sizes, labels=labels, explode=explode)


## 10
fig, ax = plt.subplots()
labels = 'Ford', 'Toyota', 'BMW', 'AUDI', 'Jaguar'
sizes = [15, 10, 33, 15, 22]
ax.pie(sizes, labels=labels)
centre_circle = plt.Circle((0, 0), 0.50, fc='white')
fig.gca().add_artist(centre_circle)


plt.show()