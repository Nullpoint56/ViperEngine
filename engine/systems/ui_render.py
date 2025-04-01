import pygame

from engine.components.ui_components import UITransform, TextComponent, ButtonComponent, SceneTag
from engine.ecs.registry import Registry


def UIRenderSystem(screen, registry: Registry, font, active_scene):
    for eid, transform in registry.components[UITransform].items():
        scene = registry.components[SceneTag].get(eid)
        if not scene or scene.name != active_scene:
            continue

        text = registry.components[TextComponent].get(eid)
        button = registry.components[ButtonComponent].get(eid)

        color = (200, 0, 0) if button and button.hovered else (100, 100, 100)
        pygame.draw.rect(screen, color, (transform.x, transform.y, transform.width, transform.height))

        if text:
            label = font.render(text.text, True, (255, 255, 255))
            text_rect = label.get_rect(center=(transform.x + transform.width / 2, transform.y + transform.height / 2))
            screen.blit(label, text_rect)