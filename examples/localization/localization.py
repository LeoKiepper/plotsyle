import numpy as np
import matplotlib.pyplot as plt
from plotstyle import PlotStyle
# Specify the language with the 'language' argument. In theory any language keys can be used, as long as they agree with what is defined within the yaml file.
# However, even though this is not enforced by this library, it is highly recommended to follow a widely accepted international standard such as ISO 639
# https://www.loc.gov/standards/iso639-2/php/code_list.php

PS = PlotStyle(yaml_file="localization.yaml", language='en')
magic = np.array([
	[8, 1, 6],
	[3, 5, 7],
	[4, 9, 2]
])
fig, ax = plt.subplots()
ax.imshow(np.ones_like(magic), cmap="gray", vmin=0, vmax=1)

for i in range(3):
	for j in range(3):
		ax.text(j, i, str(magic[i, j]), ha="center", va="center", fontsize=20)

ax.set_xticks(np.arange(-0.5, 3, 1))
ax.set_yticks(np.arange(-0.5, 3, 1))
ax.grid(color="black", linewidth=2)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_title(PS.title_str)

plt.show()
