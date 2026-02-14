# plotsyle
Python library to organize matplotlib plots by loading plot command options from external yaml files. Requires the `parse` library
```python
pip install parse
```

The main logic of this library is declaring fields in a yaml file to be loaded onto a single object that contains all options for matplotlib commands to compose a specific figure within a script. The fields are read from the file top-to-bottom, and by design, eventual conflicts are resolved by overwriting.

Field names are user-defined and have nothing to do how matplotlib works. For instance, if you want to specify a fontsize and string for a figure title, one might write the yaml file 'example.yaml' and it's matching use in a plotting script as
```yaml
my_title: "This is an example title"
my_fontsize: 16
```
```python
import matplotlib.pyplot as plt
from plotstyle import PlotStyle
PS = PlotStyle(yaml_file="example.yaml", configs_folder=".")  # loads the yaml file from the current directory
plt.title(PS.my_title, fontsize=PS.my_fontsize)
plt.show()
```

At it's most basic, a yaml file will be just a list of fields. This, in itself, can be somewhat useful for organization if you need to keep track of many fields, insofar as separating field definitions out of your plotting script might significantly limit the number of lines. For general applications, more advanced functionalities are provided. Check the examples folder for documentation.
