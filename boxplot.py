import matplotlib.pyplot as plt
import numpy as np

d1 = np.random.rand(50) * 100	#generate random numbers
d2 = np.random.rand(50) * 100
d3 = np.random.rand(50) * 100

data = [d1, d2, d3]	# multiple box plots on one figure

plt.figure()
plt.boxplot(data)
plt.show()


