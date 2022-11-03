# Enumerations
Enumerations for EB 2023 software.

## Usage
If you would like to use enums in your software module, please create a new python file
with the name of your `<module name>_enums.py` in the `EB23_Enums` directory.
After creating your enumerations, add them to the `__init__.py` imports.  
Lastly, import them in your module  

```python
from EB23_Enums import <name of your enum>
```