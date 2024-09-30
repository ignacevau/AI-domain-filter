from abc import ABC, abstractmethod

from registrar.domain import Domain


class Provider(ABC):
    def __init__(self):
        self._total_chunks: int = 0
        self._current_chunk: int = 0

    @abstractmethod
    def _fetch_data(self, chunk_page: int) -> list[any]:
        pass

    @abstractmethod
    def _parse_data(self, data: list[any]) -> list[Domain]:
        pass

    def get_next_data(self) -> list[Domain]:
        self._current_chunk += 1

        raw_data = self._fetch_data(self._current_chunk)
        return self._parse_data(raw_data)

    def has_next_page(self) -> bool:
        return self._current_chunk <= self._total_chunks
