# Advanced cases
In the simple use case of example.yaml, as shown in this repository's root directory, fields are said to be 'implicit', i.e. a field name and value pair. Internally, fields are normalized to an 'explciit' form and default values for each property are assigned as necessary. 

Most advanced functionalities require declaring explicit field properties in the yaml file. The general structure for an explicit field is shown below:
```yaml
field_name:
  source: literal       # 'literal' OR 'field'
  value: # 
```

## Dervied fields
You can specify that a field's value to read value computed from a previously computed field.
The `source` property controls how the parser will interpret the `value` property. 
When it is `literal` (default value), the parser will load onto the PlotStyle object the verbatim value written in the value property. 
When it is `field`, the parser will look for a field whose name is read verbatim from `value`, and copy it's value. 

The most important use for this functionality is to enable writing fields for templates. See the example `derived_fields.py` and it's accompanying file `derived_fields.yaml`.
