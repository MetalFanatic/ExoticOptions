from src.models.errors.ContinuousModelException import InvalidMertonModelInstantiation
from src.models.ContinuousModels import ContinuousModel


class BlackScholes(ContinuousModel):

    merton: bool = False

    def __post_init__(self):
        if self.merton and not self.q:
            raise InvalidMertonModelInstantiation(self.q, message="q should be > 0 if merton=True")

