#Import Matplotlib and Pandas
import matplotlib.pyplot as plt


y=[]
x=[0,2,4,6,8,10,12,14,16]


for i in x:
    y.append(i**2)

#Use the .plot() function to create a line plot
plt.plot(x,y)
#Use the .title() method to add the title
plt.title("line plot")
#Display the plot
plt.show()

#Use the .scatter() function to create a scatter plot
plt.scatter(x,y)
#Use the .title() method to add the title
plt.title("dot plote")
#Display the plot
plt.show()

#Use the .bar() function to create a bar chart
plt.bar(x,y)
#Use the .title() method to add the title
plt.title("bar plote")
#Display the chart
plt.show()


#SUBPLOT
#Create a figure object of the size 18x5
fig=plt.figure(figsize=(18,5))
#Use the .add_subplot() method to add the line plot
bir=fig.add_subplot(1,3,1)
#Change the color to red
bir.plot(x,y,color='red')
#Add the title
bir.set_title("line plot")

#Use the .add_subplot() method to add the scatter plot
iki=fig.add_subplot(1,3,2)
#Change the color to green
iki.scatter(x,y,color='green')
#Add the title
iki.set_title("dot plot")

#Use the .add_subplot() method to add the bar chart
uc=fig.add_subplot(1,3,3)
#Change the color to orange
uc.bar(x,y,color='orange')
#Add the title
uc.set_title("bar plot")

#Display the figure
plt.show()

