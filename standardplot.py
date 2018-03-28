#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()
