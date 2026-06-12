from typing import Any, Generic, Optional, Type, TypeVar

from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):

    def __init__(self, model: Type[T]):
        self.model = model

    def create(self, db: Session, **kwargs) -> T:

        obj = self.model(**kwargs)

        db.add(obj)

        db.commit()

        db.refresh(obj)

        return obj

    def get_by_id(
        self,
        db: Session,
        object_id: int,
    ) -> Optional[T]:

        return (
            db.query(self.model)
            .filter(self.model.id == object_id)
            .first()
        )

    def get_all(
        self,
        db: Session,
    ):

        return db.query(self.model).all()

    def delete(
        self,
        db: Session,
        obj: T,
    ):

        db.delete(obj)

        db.commit()

    def update(
        self,
        db: Session,
        obj: T,
        **kwargs,
    ):

        for key, value in kwargs.items():

            setattr(obj, key, value)

        db.commit()

        db.refresh(obj)

        return obj