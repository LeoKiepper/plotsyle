import numpy as np
import matplotlib.pyplot as plt
from plotstyle import PlotStyle
PS1 = PlotStyle(yaml_file="figure1.yaml", folder=".") 
PS2 = PlotStyle(yaml_file="figure2.yaml", folder=".") 
PS3 = PlotStyle(yaml_file="figure3.yaml", folder=".") 
# fields loaded from base_style.yaml will appear on all PS objects, as all associated yaml files declare base_style.yaml for chain loading

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x + np.pi/4)


fig1, ax1 = plt.subplots()
ax1.plot(x, y1, label="sine wave", linewidth=PS1.linewidth)
ax1.set_title("Sine Function", fontsize = PS1.fontsize_title)
ax1.set_xlabel("x", fontsize = PS1.fontsize_axislabel)
ax1.set_ylabel("sin(x)", fontsize = PS1.fontsize_axislabel)
ax1.legend(fontsize=PS1.fontsize_legend)
ax1.grid(True)

fig2, ax2 = plt.subplots()
ax2.plot(x, y2, linestyle="--", label="cosine", linewidth=PS2.linewidth)
ax2.set_title("Cosine Function", fontsize = PS2.fontsize_title)
ax2.set_xlabel("x", fontsize = PS2.fontsize_axislabel)
ax2.set_ylabel("cos(x)", fontsize = PS2.fontsize_axislabel)
ax2.legend(fontsize=PS2.fontsize_legend)
ax2.grid(True)


fig3, ax3 = plt.subplots()
ax3.plot(x, y1, label="sin(x)", linewidth=PS3.linewidth_sine)
ax3.plot(x, y3, label="shifted sine", linewidth=PS3.linewidth_shiftedsine) 
ax3.set_title("Combined Waves", fontsize = PS3.fontsize_title)
ax3.set_xlabel("x", fontsize = PS3.fontsize_axislabel)
ax3.set_ylabel("value", fontsize = PS3.fontsize_axislabel)
ax3.legend(fontsize=PS3.fontsize_legend)
ax3.grid(True)

plt.show()
