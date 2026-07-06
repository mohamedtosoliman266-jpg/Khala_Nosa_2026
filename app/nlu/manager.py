class NLUManager:

    def __init__(self):
        self.extractors = []

    def register(self, extractor):
        self.extractors.append(extractor)

    def analyze(self, message):

        for extractor in self.extractors:

            result = extractor.extract(message)

            if result:
                return result

        return {
            "intent": "chat"
        }
