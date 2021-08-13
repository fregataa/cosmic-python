
import abc
import model
from typing import Protocol

class RepositoryProtocol(Protocol):
    # if we set a type hint with this protocol to a variable or an argument,
    # static type checker can check whether it has attributes which RepositoryProtocol has.
    def add(self, batch: model.Batch) -> None:
        ...

    def get(self, reference) -> None:
        ...

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, batch: model.Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> model.Batch:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, batch):
        self.session.add(batch)

    def get(self, reference):
        return self.session.query(model.Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.Batch).all()