from engine.components.ui_components import UITransform, ButtonComponent
from engine.ecs.registry import Registry


def UIInputSystem(registry: Registry, mouse_pos, mouse_pressed):
    for eid, transform in registry.components[UITransform].items():
        button = registry.components[ButtonComponent].get(eid)
        if not button:
            continue

        in_bounds = (transform.x <= mouse_pos[0] <= transform.x + transform.width and
                     transform.y <= mouse_pos[1] <= transform.y + transform.height)
        button.hovered = in_bounds
        button.clicked = in_bounds and mouse_pressed[0]