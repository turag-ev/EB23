# Internal Mechanics Action Manager

## Notes
Actuators:
{
    Actuator: object
}

Actions structure:
- init()
- getActuators() -> list[Actuator]
- execute

How to handle sub-actions:
- execute(self, imam, **kw_actors)
- imam.start(Action, args)                    -> IMAM is server client and server (can send messages to itself)
- imam.startAsync(Action, args)               -> return future object then await before proceeding

Action ideas:
- ima.start_async("motorToPosition", motor, position) -> mini action for all motors