class IntentRouter:

    def __init__(self):
        self.routes = []

    def register(self, checker, target):

        self.routes.append({
            "checker": checker,
            "target": target,
        })

    def route(self, message):

        for route in self.routes:

            if route["checker"](message):
                return route["target"]

        return None
