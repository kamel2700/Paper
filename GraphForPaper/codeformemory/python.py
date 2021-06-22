import math

import matplotlib.pyplot as plt

# tracing = sum([-3, 0.15, 8, -2])
# inheritance = sum([-3, 0.19, 15, -2])
# sort = sum([-3, 0.2, 11, -2])
# multi = sum([-3, 0.19, 10, -2])

tracing = (1/(1+ math.exp(-0.01*(8-83.5))))
inheritance = (1/(1+ math.exp(-0.01*(15-83.5))))
sort = (1/(1+ math.exp(-0.01*(11-83.5))))
multi = (1/(1+ math.exp(-0.01*(10-83.5))))



# x axis values
x = [-1, 2, 4, 6, 8, 1000]
# corresponding y axis values
y = [-1, tracing, inheritance, sort, multi, 1000]

plt.xticks(x, [None, "Tracing", "Inheritance", "Sorting", "Multitasking", None])

# plotting the points 
plt.plot(x, y, color='slategray', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='slategray', markersize=12,label = "Python")
plt.grid(True)
# setting x and y axis range
plt.ylim(0, 1)
plt.xlim(1, 9)

# naming the x axis
plt.xlabel('Experiments - axis')
# naming the y axis
plt.ylabel('Total score - axis')

# giving a title to my graph
plt.title('Evaluation of Python')

# function to show the plot
# plt.show()
