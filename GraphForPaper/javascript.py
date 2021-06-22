import math

import matplotlib.pyplot as plt

# tracing = sum([-3, 0.51, 27, -2])
# inheritance = sum([-3, 0.8, 102, -2])
# sort = sum([-3, 0.52, 29, -2])
# multi = sum([-1, 1.65, 33, -0])

tracing1 = (1/(1+ math.exp(-0.01*(27-83.5))))
inheritance1 = (1/(1+ math.exp(-0.01*(102-83.5))))
sort1 = (1/(1+ math.exp(-0.01*(29-83.5))))
multi1 = (1/(1+ math.exp(-0.01*(33-83.5))))

tracing = (((0.51-0.09)/(3.61-0.09))+tracing1)/4
inheritance = (((0.8-0.09)/(3.61-0.09))+inheritance1)/4
sort = (((0.52-0.09)/(3.61-0.09))+sort1)/4
multi = (((1.65-0.09)/(3.61-0.09))+multi1)/2*1.3


# x axis values
x = [-1, 2, 4, 6, 8, 1000]
# corresponding y axis values
y = [-1, tracing, inheritance, sort, multi, 1000]

plt.xticks(x, [None, "Tracing", "Inheritance", "Sorting", "Multitasking", None])

# plotting the points
plt.plot(x, y, color='slategrey', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='slategrey', markersize=12, label = "JS")
plt.grid(True)
# setting x and y axis range
plt.ylim(0, 1)
plt.xlim(1, 9)

# naming the x axis
plt.xlabel('Experiments - axis')
# naming the y axis
plt.ylabel('Total score - axis')

# giving a title to my graph
plt.title('Evaluation of JavaScript after merged time and memory criteria')

# function to show the plot
# plt.show()
