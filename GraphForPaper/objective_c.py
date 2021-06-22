import math

import matplotlib.pyplot as plt

# tracing = sum([-3, 0.16, 15, -0])
# inheritance = sum([-3, 0.28, 66, -0])
# sort = sum([-3, 0.16, 23.6, -2])
# multi = sum([-3, 0.17, 13, -2])

tracing1 = (1/(1+ math.exp(-0.01*(15-83.5))))
inheritance1 = (1/(1+ math.exp(-0.01*(66-83.5))))
sort1 = (1/(1+ math.exp(-0.01*(23.6-83.5))))
multi1 = (1/(1+ math.exp(-0.01*(13-83.5))))

tracing = (((0.16-0.09)/(3.61-0.09))+tracing1)/2
inheritance = (((0.28-0.09)/(3.61-0.09))+inheritance1)/2
sort = (((0.16-0.09)/(3.61-0.09))+sort1)/2
multi = (((0.17-0.09)/(3.61-0.09))+multi1)/2



# x axis values
x = [-1, 2, 4, 6, 8, 1000]
# corresponding y axis values
y = [-1, tracing, inheritance, sort, multi, 1000]

plt.xticks(x, [None, "Tracing", "Inheritance", "Sorting", "Multitasking", None])

# plotting the points
plt.plot(x, y, color='darkgoldenrod', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='darkgoldenrod', markersize=12, label = "Objective C")
plt.grid(True)
# setting x and y axis range
plt.ylim(0, 1)
plt.xlim(1, 9)

# naming the x axis
plt.xlabel('Experiments - axis')
# naming the y axis
plt.ylabel('Total score - axis')

# giving a title to my graph
plt.title('Evaluation of Objective C after merged time and memory criteria')

# function to show the plot
# plt.show()
