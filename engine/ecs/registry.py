from engine.components.ui_components import UITransform, TextComponent, ButtonComponent, SceneTag


class Registry:
    def __init__(self):
        self.entities = {}
        self.components = {
            UITransform: {},
            TextComponent: {},
            ButtonComponent: {},
            SceneTag: {},
        }

    def add_entity(self, entity_id: int, components: dict[any, any]):
        self.entities[entity_id] = True
        for comp_type, value in components.items():
            self.components[comp_type][entity_id] = value

    def create_snapshot(self):
        return {
            'UITransform': self.components[UITransform].copy(),
            'TextComponent': self.components[TextComponent].copy(),
            'ButtonComponent': self.components[ButtonComponent].copy(),
            'SceneTag': self.components[SceneTag].copy(),
            'entities': self.entities.copy()
        }