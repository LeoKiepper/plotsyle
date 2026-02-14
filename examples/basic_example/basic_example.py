import matplotlib.pyplot as plt
from plotstyle import PlotStyle
PS = PlotStyle(yaml_file="basic_example.yaml", folder=".")  # loads the yaml file from the current directory
plt.title(PS.my_title, fontsize=PS.my_fontsize)
plt.show()