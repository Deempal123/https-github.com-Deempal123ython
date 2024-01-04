import numpy as np
import matplotlib.pyplot as mp
x = [15,20,25,35,40]
y = [20,40,50,70,90]
matrix = np.corrcoef(x,y)
mp.xlabel("Sales")
mp.ylabel("Temperature")
print(matrix)
mp.plot(x,y,marker="o",linestyle="dashed")
mp.grid()
mp.show()