# Rule Engine using DSL #

# Please follow below steps to run the project
> git clone <URL> <br />
> create virtualenv <br />
> cd project dir <br />
> pip install -r requirements.txt <br />
> python process_rule.py rule1 '/path/to/file.json'

###### `rule1` is a file name under rules/ package . This file defines the rules to be run.
###### All operators are defined under operator/ package, operators are defined for Integer, String, Datetime dataypes as of now.
###### You can add more operators by adding more functions for each datatype.py file under operators/ package. ######
## Below are the operators defined for each datatype:
* # Integer
  * Equals
  * Not_Equals
  * Greater_Than
  * Greater_Than_Equals
  * Less_Than
  * less_than_equals
  
* # String
  * Equals
  * Not_equals
  * Contains

* # Datetime
  * Less_than_equals
  * Greater_than_equals
  
## Below are the rules to write .dsl file
```
<Atrribute> <function_name> <value>
ATL1 Less_Than_Equals 20
ATL9 greater_Than_equals 2016-06-13_22:40:10
```
  
###### NOTE: in case of datetime please add _ to separate date and time part.
