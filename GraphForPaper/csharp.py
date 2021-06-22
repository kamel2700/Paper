import math
import matplotlib.pyplot as plt

# tracing = sum([-3, 0.09, 13, -1])
# inheritance = sum([-3, 0.19, 34, -2])
# sort = sum([-3, 0.11, 16, -2])
# multi = sum([-3, 0.38, 23, -2])



tracing1 = ((0.09-0.09)/(3.61-0.09))
inheritance1 = ((0.19-0.09)/(3.61-0.09))
sort1 = ((0.11-0.09)/(3.61-0.09))
multi1 = ((0.38-0.09)/(3.61-0.09))

tracing = (((1/(1+ math.exp(-0.01*(13-83.5)))) +tracing1)/2)*0.66
inheritance = ((1/(1+ math.exp(-0.01*(34-83.5))))+inheritance1)/4
sort = ((1/(1+ math.exp(-0.01*(16-83.5))))+sort1)/4
multi = ((1/(1+ math.exp(-0.01*(23-83.5))))+multi1)/4


# x axis values
x = [-1, 2, 4, 6, 8, 1000]
# corresponding y axis values
y = [-1, tracing, inheritance, sort, multi, 1000]

plt.xticks(x, [None, "Tracing", "Inheritance", "Sorting", "Multitasking", None])

# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth=3,
         marker='o', markerfacecolor='green', markersize=12, label = "C# all normalized")

# setting x and y axis range
plt.ylim(0, 1)
plt.xlim(1, 9)

# naming the x axis
plt.xlabel('Experiments - axis')
# naming the y axis
plt.ylabel('Total score - axis')
plt.grid(True)
# giving a title to my graph
plt.title('Evaluation of C# after all normalizations')
plt.legend()
# function to show the plot
# plt.show()
