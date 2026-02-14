# Advanced cases
In the simple use case of example.yaml, as shown in this repository's root directory, fields are said to be 'implicit', i.e. a field name and value pair. Internally, fields are normalized to an 'explciit' form and default values for each property are assigned as necessary. 

Most advanced functionalities require declaring explicit field properties in the yaml file. The general structure for an explicit field is shown below:
```yaml
field_name:
  source: literal       # 'literal' OR 'field'
  value: # whatever value is required goes here
```

## Dervied fields
You can specify that a field's value to read value computed from a previously computed field.
The `source` property controls how the parser will interpret the `value` property. 
When it is `literal` (default value), the parser will load onto the PlotStyle object the verbatim value written in the value property. 
When it is `field`, the parser will look for a field whose name is read verbatim from `value`, and copy it's value. 

The most important use for this functionality is to enable writing fields for templates. See the example `derived_fields`.

## Recursive loading
To allow chain loading fields from secondary yaml files, specify the property `validator: yaml`. This will direct the parser to recurse itself into loading fields within the specified file. This functionality, along with derived fields, enables the creation of template yaml files. For instance, one might compose a number of figures for some publication, that in all likelihood will share a number of options for it's constituent plot commands. Instead of repeating these options on however many yaml files are created for these figures, it is highly preferrable to define repeated options once in a template file, and reference these fields as necessary. This helps with code maintenance, editorializing and consistency. See the example `template_usage` and it's associated files

Specifying `validator: yaml` is the unambiguous flag for the parser to know a field should be processed in yaml chaining. It is strongly recommended to treat 'yaml' as a reserved field name.
