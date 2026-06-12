from app.models.ai_classification import AIClassification
from app.repositories.base_repository import BaseRepository


class AIClassificationRepository(
    BaseRepository[AIClassification]
):

    def __init__(self):

        super().__init__(AIClassification)


ai_classification_repository = AIClassificationRepository()