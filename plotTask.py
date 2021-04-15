# A program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
#Author: Enda Lynch
#Credit: https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color
#Credit: https://stackoverflow.com/questions/18962063/matplotlib-setting-title-bold-while-using-times-new-roman
#Credit: https://www.programcreek.com/python/example/4890/matplotlib.rcParams

import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0, 5, 1)      #The numpy arange() function takes four parameters that includes start, stop, step, and dtype and returns evenly spaced values within a given interval

#generate plotpoints for x and y axis
y1 = x
y2 = x**2
y3 = x**3

#set the colour of the face and background of the image - this code has to be in before the plt.plot
fig = plt.figure()
fig.patch.set_facecolor('xkcd:mint green')
plt.rcParams['axes.facecolor'] = 'xkcd:sky blue'

#plot the points and set the style of the plot
plt.plot(y1, label = 'f(x)', color = 'magenta', linewidth = 2, linestyle = 'solid', marker = 'd', markersize = 7, markerfacecolor = 'gold')
plt.plot(y2, label = 'g(x)', color = 'green', linewidth = 2, linestyle = 'dotted', marker = 'd',markersize = 7, markerfacecolor = 'gold')
plt.plot(y3, label = 'h(x)', color = 'red', linewidth = 2, linestyle = 'dashed', marker = 'd', markersize = 7, markerfacecolor = 'gold')

#input a title, lables and a legend for the plot - set style as required
plt.title('Wk8 Lab: f(x)=x, g(x)=x**2 and h(x)=x**3', fontweight = 'bold', fontsize = 14)
plt.xlabel('x-axis', fontweight = 'bold', fontsize = 12)
plt.ylabel('y-axis', fontweight = 'bold', fontsize = 12)
plt.legend()
#show plot
plt.show()
#save plot
#plt.savefig('plotTask - Wk8.png')