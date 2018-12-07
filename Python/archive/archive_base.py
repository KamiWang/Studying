import abc


class SQLMaker(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def table(self, name: str):
        pass

    @abc.abstractmethod
    def select(self, fields: list = None):
        pass

    @abc.abstractmethod
    def insert(self, key_values: dict):
        pass

    @abc.abstractmethod
    def update(self, key_values: dict):
        pass

    @abc.abstractmethod
    def delete(self):
        pass

    @abc.abstractmethod
    def count(self):
        pass

    @abc.abstractmethod
    def condition(self, cond: str, arguments: list):
        pass

    @abc.abstractmethod
    def order_by(self, fields: list, reverse: bool):
        pass

    @abc.abstractmethod
    def limit(self, count: int, offset: int = 0):
        pass

    @abc.abstractmethod
    def make(self):
        pass


class EngineBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sql_maker(self) -> SQLMaker:
        pass

    @abc.abstractmethod
    async def query(self, sql_maker) -> dict:
        pass

    @abc.abstractmethod
    async def query_once(self, sql_maker):
        pass

    @abc.abstractmethod
    async def execute(self, sql_maker) -> int:
        pass
