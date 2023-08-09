from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name):
        super().__init__(name, capacity=15)
        self.robots = []

    def details(self):
        robots_ = ' '.join([r.name for r in self.robots])
        robots_or_none = "none" if not self.robots else robots_
        return f"{self.name} Secondary Service:\nRobots: {robots_or_none}"
