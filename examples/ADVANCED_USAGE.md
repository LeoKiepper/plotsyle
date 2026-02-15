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

## Recursive loading and template usage
To direct the parser to chain load fields from secondary yaml files, specify the property `validator: yaml`. The field that specifies which yaml file to read will not load onto the final object, but all fields declared in the file will. This will direct the parser to recurse itself into loading fields within the specified file. This functionality, along with derived fields, enables the creation of template yaml files. For instance, one might compose a number of figures for some document, that in all likelihood will share a number of options for it's constituent plot commands. Instead of repeating these options on however many yaml files are created for these figures, it is highly preferrable to define repeated options once in a template file, and reference these fields as necessary. This helps with code maintenance, editorializing and consistency. See the example `template_usage` and it's associated files

Specifying `validator: yaml` is the unambiguous flag for the parser to know a field should be processed in yaml chaining. It is strongly recommended to treat 'yaml' as a reserved field name.

It is also possible to chain yaml parsing on multiple levels by specifying files within files, but this is discouraged in favor of specifying a single-layer list of yaml files, which are loaded first to last (left to right), such as demonstrated in the configs section.

The primary purpose of this feature is to enable the creation of templates that comply with the formatting requirements of specific target publications. For example, one could define a template that specifies font sizes, figure dimensions, and other commonly used fields shared across multiple articles within a given two-column journal layout (e.g., IEEE). A separate template could be created for a one-column publication (such as an institutional repository), and another for slideshow presentations.

Crucially, all templates must use the same field names and represent the same underlying variables so that they remain fully interchangeable. This approach streamlines editorial workflows and eliminates redundant effort, particularly within large groups such as research teams.

## Localization
Fields can have a `localizable` property to allow for translation into different languages. For this, the user must define values for each language. See the `localization` example. This is meant for localization of text, but nothing impedes it to be used for other types of data, which may or may have niche use-cases.

## The 'configs' field
To fully utilize both the template and localization functionalities, it is best to define multiple combinations of these in the same yaml file, as though each of these combinations configures a different 'version' of the same figure. This is done using the reserved field name `configs`. When specifying a configs field, the user must, <ins>necessarily</ins>, generate the PlotStyle objects through the `load_plotstyle` and `PSTemplate.expand` methods, as the direct PlotStyle constructor will simply ignore this field. The `PSTemplate.expand` method will generate an iterable of PlotStyle objects that should drive a `for` block, where a typical plotting script should be placed. See the example `configs` for more details.
