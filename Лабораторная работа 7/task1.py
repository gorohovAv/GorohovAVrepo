import doctest

class Book:
    """ Базовый класс книги.
    >>> p = Book(name = "someName", author = "someAuthor")
    """
    def __init__(self, name: str, author: str):
        self._name = None
        self._author = None

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_author(self):
        return self._author

    def set_author(self, author):
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """
        >>> p = PaperBook(name = "someName", author = "someAuthor", pages = 200)
    """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name = name, author = author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым")
        if pages < 0:
            raise ValueError("Количество страниц должно быть положительным")
        self.pages = pages

    # def __str__(self):
        # return f"Книга {self._name}. Автор {self._author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"


class AudioBook(Book):
    """
            >>> p = AudioBook(name = "someName", author = "someAuthor", duration = 200)
    """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        if not isinstance(duration, int):
            raise TypeError("Продолжительность должна быть целой")
        if duration < 0:
            raise ValueError("Продолжительность должна быть положительной")
        self.duration = duration

    # def __str__(self):
        # return f"Книга {self._name}. Автор {self._author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}), duration={self.duration}"


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
