import math

import matplotlib.pyplot as plt

# tracing = sum([-3, 0.21, 36, -2])
# inheritance = sum([-3, 0.35, 91, -2])
# sort = sum([-3, 0.24, 42, -2])
# multi = sum([-3, 0.28, 38, -2])

tracing = ((0.21-0.09)/(3.61-0.09))
inheritance = ((0.35-0.09)/(3.61-0.09))
sort = ((0.24-0.09)/(3.61-0.09))
multi = ((0.28-0.09)/(3.61-0.09))



# x axis values
x = [-1, 2, 4, 6, 8, 1000]
# corresponding y axis values
y = [-1, tracing, inheritance, sort, multi, 1000]

plt.xticks(x, [None, "Tracing", "Inheritance", "Sorting", "Multitasking", None])

# plotting the points
plt.plot(x, y, color='aqua', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='aqua', markersize=12, label = "Kotlin")
plt.grid(True)
# setting x and y axis range
plt.ylim(0, 1)
plt.xlim(1, 9)

# naming the x axis
plt.xlabel('Experiments - axis')
# naming the y axis
plt.ylabel('Total score - axis')

# giving a title to my graph
plt.title('Evaluation of Kotlin')

# function to show the plot
# plt.show()
