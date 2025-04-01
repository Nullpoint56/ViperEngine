from engine.components.ui_components import UITransform, TextComponent, ButtonComponent, SceneTag
from engine.ecs.registry import Registry


def load_main_menu_ui(registry: Registry):
    registry.add_entity(1, {
        UITransform: UITransform(x=300, y=180, width=200, height=60),
        TextComponent: TextComponent(text="Start Game"),
        ButtonComponent: ButtonComponent(id="start_button"),
        SceneTag: SceneTag(name="main_menu")
    })
    registry.add_entity(2, {
        UITransform: UITransform(x=300, y=260, width=200, height=60),
        TextComponent: TextComponent(text="Settings"),
        ButtonComponent: ButtonComponent(id="settings_button"),
        SceneTag: SceneTag(name="main_menu")
    })
    registry.add_entity(3, {
        UITransform: UITransform(x=300, y=340, width=200, height=60),
        TextComponent: TextComponent(text="Exit"),
        ButtonComponent: ButtonComponent(id="exit_button"),
        SceneTag: SceneTag(name="main_menu")
    })
