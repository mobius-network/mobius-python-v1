from .requestor import Requestor
from .resources import AppStore, Tokens


class Mobius:

    def __init__(self, **kwargs):
        self.requestor = Requestor(**kwargs)

        self.app_store = AppStore(self.requestor)
        self.tokens = Tokens(self.requestor)
