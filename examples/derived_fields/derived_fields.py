import numpy as np
import matplotlib.pyplot as plt
from plotstyle import PlotStyle
PS = PlotStyle(yaml_file="derived_fields.yaml", folder=".")


x = np.linspace(0, 10, 100)
y1 = np.random.rand(100)
y2 = np.random.rand(100)
y3 = np.random.rand(100)
y_sum = y1 + y2 + y3


plt.plot(x, y1, linewidth=PS.linewidth_others)
plt.plot(x, y2, linewidth=PS.linewidth_others)
plt.plot(x, y3, linewidth=PS.linewidth_others)
plt.plot(x, y_sum, linewidth=PS.linewidth_sum)
plt.show()
