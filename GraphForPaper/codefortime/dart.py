import math

import matplotlib.pyplot as plt

# tracing = sum([-3, 0.67, 125, -2])
# inheritance = sum([-3, 0.94, 172, -2])
# sort = sum([-3, 0.88, 130, -2])
# multi = sum([-3, 1.8, 131, -1])

tracing = ((0.67-0.09)/(3.61-0.09))
inheritance = ((0.94-0.09)/(3.61-0.09))
sort = ((0.88-0.09)/(3.61-0.09))
multi = ((1.8-0.09)/(3.61-0.09))


# x axis values
x = [-1, 2, 4, 6, 8, 1000]
# corresponding y axis values
y = [-1, tracing, inheritance, sort, multi, 1000]

plt.xticks(x, [None, "Tracing", "Inheritance", "Sorting", "Multitasking", None])

# plotting the points 
plt.plot(x, y, color='purple', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='purple', markersize=12, label = "Dart")

# setting x and y axis range
plt.ylim(0, 1)
plt.xlim(1, 9)
plt.grid(True)
# naming the x axis
plt.xlabel('Experiments - axis')
# naming the y axis
plt.ylabel('Total score - axis')

# giving a title to my graph
plt.title('Evaluation of Dart')

# function to show the plot
# plt.show()
