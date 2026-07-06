from app.nlu.manager import NLUManager
from app.extractors.profile_extractor import ProfileExtractor


def create_nlu():

    nlu = NLUManager()

    nlu.register(ProfileExtractor())

    return nlu
