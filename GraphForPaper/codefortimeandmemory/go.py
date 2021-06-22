import math

import matplotlib.pyplot as plt

# tracing = sum([-3, 0.15, 6, -1])
# inheritance = sum([-1, 3.61, 600, -1])
# sort = sum([-3, 0.15, 5, -2])
# multi = sum([-3, 0.17, 5, -2])

tracing1 = (1/(1+ math.exp(-0.01*(6- 83.5))))
inheritance1 = (1/(1+ math.exp(-0.01*(600-83.5))))
sort1 = (1/(1+ math.exp(-0.01*(5-83.5))))
multi1 = (1/(1+ math.exp(-0.01*(5-83.5))))

tracing = (((0.15-0.09)/(3.61-0.09))+tracing1)/2
inheritance = (((3.61-0.09)/(3.61-0.09))+inheritance1)/2
sort = (((0.15-0.09)/(3.61-0.09))+sort1)/2
multi = (((0.17-0.09)/(3.61-0.09))+multi1)/2
# x axis values
x = [-1, 2, 4, 6, 8, 1000]
# corresponding y axis values
y = [-1, tracing, inheritance, sort, multi, 1000]

plt.xticks(x, [None, "Tracing", "Inheritance", "Sorting", "Multitasking", None])

# plotting the points 
plt.plot(x, y, color='darkorange', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='darkorange', markersize=12, label = "Go")

# setting x and y axis range
plt.grid(True)
plt.ylim(0, 1)
plt.xlim(1, 9)

# naming the x axis
plt.xlabel('Experiments - axis')
# naming the y axis
plt.ylabel('Total score - axis')

# giving a title to my graph
plt.title('Evaluation of Go fter merged time and memory criteria')

# function to show the plot
# plt.show()
