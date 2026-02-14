# Advanced cases
In the simple use case of example.yaml, as shown in this repository's README, fields are said to be 'implicit', i.e. a field name and value pair. Internally, fields are normalized to an 'explciit' form and default values for each property are assigned as necessary. 

Most advanced functionalities require declaring explicit field properties in the yaml file. The general structure for a field declared explicitly is shown below:
```yaml
field_name:
  source: literal       # 'literal' OR 'field'
  value: # whatever value is required goes here
```

Moreover, in a sufficiently complex document, it is reasonable to expect a non-negligible number of yaml files would be created. Therefore, this library looks for yaml files in a `configs_folder` folder (defaults to 'plotstyle_configs') within the current directory. A different folder can be specified by passing the `configs_folder` to methods that accept yaml files as argument.

## Dervied fields
You can specify that a field's value be computed from a previously computed field.
The `source` property controls how the parser will interpret the `value` property. 
When it is `literal` (default value), the parser will load onto the PlotStyle object the verbatim value written in the `value` property. 
When it is `field`, the parser will look for a field whose name is read verbatim from `value`, and copy it's value. 

The most important use for this functionality is to enable writing fields for templates. See the example `derived_fields`.

## Recursive loading
To direct the parser to chain load fields from secondary yaml files, specify the property `validator: yaml`. The field that specifies which yaml file to read will not load onto the final object, but all fields declared in the file will. This will direct the parser to recurse itself into loading fields within the specified file. This functionality, along with derived fields, enables the creation of template yaml files. For instance, one might compose a number of figures for some document, that in all likelihood will share a number of options for it's constituent plot commands. Instead of repeating these options on however many yaml files are created for these figures, it is highly preferrable to define repeated options once in a template file, and reference these fields as necessary. This helps with code maintenance, editorializing and consistency. See the example `template_usage` and it's associated files

Specifying `validator: yaml` is the unambiguous flag for the parser to know a field should be processed in yaml chaining. It is strongly recommended to treat 'yaml' as a reserved field name.

It is also possible to chain yaml parsing on multiple levels by specifying files within files, but this is discouraged in favor of specifying a single-layer list of yaml files, which are loaded first to last (left to right), such as demonstrated in the configs section.


The most important use for this feature is the creation of templates that conform to formatting requirements for one or more specific target publications. For instance, one might create a template consisting of fontsizes, linewidths and figure sizes that result in well formatted figures for a two-column layout journal (e.g. associated with IEEE), a separate template for another one-column publication (e.g. for some institutional repository), and a third to make figures well formatted for slideshow presentations. Importantly, all these templates must agree in field names and the variables they represent, so they can be interchangeable. 

## Localization
Fields can have a `localizable` property to allow for translation into different languages. For this, the user must define values for each language. See the `localization` example. 

## The 'configs' field

