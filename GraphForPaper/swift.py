import math

import matplotlib.pyplot as plt



# tracing = sum([-3, 0.15, 7, -2])
# inheritance = sum([-3, 0.23, 60, -2])
# sort = sum([-3, 0.2, 8, -2])
# multi = sum([-3, 0.16, 13, -2])

tracing1 = ((0.15-0.09)/(3.61-0.09))
inheritance1 = ((0.23-0.09)/(3.61-0.09))
sort1 = ((0.2-0.09)/(3.61-0.09))
multi1 = ((0.16-0.09)/(3.61-0.09))

tracing = (((0.15-0.09)/(3.61-0.09))+tracing1)/2
inheritance = (((0.23-0.09)/(3.61-0.09))+inheritance1)/2
sort = (((0.2-0.09)/(3.61-0.09))+sort1)/2
multi = (((0.16-0.09)/(3.61-0.09))+multi1)/2




# x axis values
x = [-1, 2, 4, 6, 8, 1000]
# corresponding y axis values
y = [-1, tracing, inheritance, sort, multi, 1000]

plt.xticks(x, [None, "Tracing", "Inheritance", "Sorting", "Multitasking", None])

# plotting the points
plt.plot(x, y, color='cadetblue', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='cadetblue', markersize=12,label = "Swift")
plt.grid(True)
# setting x and y axis range
plt.ylim(0, 1)
plt.xlim(1, 9)

# naming the x axis
plt.xlabel('Experiments - axis')
# naming the y axis
plt.ylabel('Total score - axis')

# giving a title to my graph
plt.title('Evaluation of Swift after merged time and memory criteria')

# function to show the plot
# plt.show()
