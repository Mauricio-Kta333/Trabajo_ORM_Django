import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# #tabla #1

xpoints1 = np.array([0, 1, 2, 3])
ypoints1 = np.array([3, 8, 1, 10])
xpoints2 = np.array([0, 1, 2, 3])
ypoints2 = np.array([6, 2, 7, 11])

plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.grid()
plt.plot(xpoints1, ypoints1, xpoints2, ypoints2)
plt.show()



#tabla #2

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1) #tamaño de la tabla
plt.plot(x,y, '*:g') #llamamos al eje x y eje y con el color verde y una estrella
plt.grid() #lineas de fondo
plt.title("Sports Watch Data", loc = 'left') #titulo y posición
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()




#tabla #3
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "#4CAF50")
plt.show()



#tabla #4
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.5, 0, 0, 0]

plt.pie(y, labels = mylabels, shadow = True)
plt.legend()
plt.show() 