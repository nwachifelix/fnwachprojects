import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt


#Initialize data. 
x_values = [1, 2, 3, 4, 5,]
cubes = [1, 8, 27, 64, 125]

# ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Blues, s=15)

# Make the plot. 
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, s=80)

# ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Blues, s=15)

# Set the chart title and label axes. 
ax.set_title('Cubes', fontsize=20)
ax.set_xlabel('Values', fontsize=18)
ax.set_ylabel('Cubes of value', fontsize=18)
ax.tick_params(axis='both', labelsize=14)

# Show the plot. 
plt.savefig('cubes.png')



# Initialize data. 
x_values = range(1, 5001)
cubes = [x**3 for x in x_values]

# Make the plot. 
plt.style.use('seaborn')
fig, ax =plt.subplots()
ax.plot(x_values, cubes, linewidth=3)
ax.scatter(x_values, cubes, s=10)

ax.scatter(x_values, cubes, cmap=plt.cm.gray, s=15)


# Set the chart title and label axes. 
ax.set_title('Cubes', fontsize=18)
ax.set_xlabel('Values', fontsize=16)
ax.set_ylabel('Cobes of Value', fontsize=16)
ax.tick_params(axis='both', labelsize=12)
ax.axis([0, 5100, 0, 5100**3])

# Show the plot. 
plt.savefig('cubes.png')
