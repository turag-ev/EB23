# Enumerations
Enumerations for EB 2023 software.

## Usage
If you would like to use enums in your software module, please create a new python file
with the name of your `<module name>_enums.py` in the `EB23_Enums` directory.

In order to create enums
```python
from enum import Enum, auto, unique

@unique                             # unique tag ensures every member is unique
class Example(Enum):                # create subclass of your enum
    MEMBER1 = "string of member 1"
    MEMBER2 = 420,69
    MEMBER3 = auto()                # generates random value when value not relevant
```
After creating your enumerations, add them to the `__init__.py` imports.

```python
from .example_enums.py import Example
```

Lastly, import them in your module  

```python
from EB23_Enums import Example
```

Use them in your module

```python
from EB23_Enums import Example

# access member
Example.Member1
Example.Member2

# access values
example_string = Example.Member1.value()
example_integer = Example.Member2.value()
```