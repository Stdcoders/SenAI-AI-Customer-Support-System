from app.models.action import Action
from app.repositories.base_repository import BaseRepository


class ActionRepository(
    BaseRepository[Action]
):

    def __init__(self):

        super().__init__(Action)


action_repository = ActionRepository()