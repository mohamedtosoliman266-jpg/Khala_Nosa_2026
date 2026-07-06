from app.nlu.manager import NLUManager

from app.extractors.profile_extractor import ProfileExtractor
from app.extractors.facts_extractor import FactsExtractor


def create_nlu():

    nlu = NLUManager()

    nlu.register(ProfileExtractor())
    nlu.register(FactsExtractor())

    return nlu

