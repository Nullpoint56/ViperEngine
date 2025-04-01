from multiprocessing import Queue

from engine.components.dummy import Position, Command


def physics_system(snapshot: dict[str, any], entity_ids: list[int], queue: Queue):
    commands = []
    for eid in entity_ids:
        pos = snapshot['Position'].get(eid)
        vel = snapshot['Velocity'].get(eid)
        if pos and vel:
            new_pos = Position(pos.x + vel.dx * snapshot['delta_time'],
                               pos.y + vel.dy * snapshot['delta_time'])
            commands.append(Command('SetPosition', eid, {'position': new_pos}))
    queue.put(commands)