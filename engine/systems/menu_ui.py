from multiprocessing import Queue

from engine.commands.command import Command


def MenuUISystem(snapshot: dict[str, any], entity_ids: list[int], queue: Queue):
    commands = []
    for eid in entity_ids:
        button = snapshot['ButtonComponent'].get(eid)
        scene = snapshot['SceneTag'].get(eid)
        if button and scene and button.clicked and scene.name == "main_menu":
            if button.id == "start_button":
                commands.append(Command('ChangeState', eid, {'state': 'PLAYING'}))
            elif button.id == "settings_button":
                commands.append(Command('ChangeState', eid, {'state': 'SETTINGS'}))
            elif button.id == "exit_button":
                commands.append(Command('ChangeState', eid, {'state': 'EXIT'}))
    queue.put(commands)