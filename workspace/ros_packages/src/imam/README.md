# Internal Mechanics Action Manager (IMAM)
The internal mechanics action manager is a ros2 module which handles different robot actions:
- low level (e.g. move motor to/ by value or read sensor)
- high level (e.g. pick up cake, sort cake, ...)
- driving 

These robot actions can be started via ros actions. 
To see which actions and their according types are available run 
  
```bash
ros2 run imam main
```
  
and then 
  
```bash
ros2 action list -t
```
  
In order to run actions via console run 
  
```bash
ros2 action send_goal <action_name> <action_type> <goal>
```
