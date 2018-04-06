import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.0,1.0,100)
y=np.sin(x)

plt.plot(x,y)
plt.xlabel("$x$",fontsize=12)
plt.ylabel("$\sin (x)$",fontsize=12)
plt.xlim([0.0,1.0])
