import math

import matplotlib.pyplot as plt

# tracing = sum([-3, 0.15, 6, -1])
# inheritance = sum([-1, 3.61, 600, -1])
# sort = sum([-3, 0.15, 5, -2])
# multi = sum([-3, 0.17, 5, -2])

tracing = ((0.15-0.09)/(3.61-0.09))
inheritance = ((3.61-0.09)/(3.61-0.09))
sort = ((0.15-0.09)/(3.61-0.09))
multi = ((0.17-0.09)/(3.61-0.09))
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
plt.title('Evaluation of Go')

# function to show the plot
# plt.show()
