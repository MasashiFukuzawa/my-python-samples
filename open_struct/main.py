from collections.abc import MutableMapping
from typing import Any, Dict, Generic, Iterator, Self, TypeVar

K = TypeVar('K')
V = TypeVar('V')


class OpenStruct(MutableMapping, Generic[K, V]):
    """
    >>> OpenStruct({'a': 1, 'b': 2})
    OpenStruct({'a': 1, 'b': 2})
    >>> struct = OpenStruct(a=1, b=2)
    >>> struct.add({'c': 3})
    OpenStruct({'a': 1, 'b': 2, 'c': 3})
    >>> struct['a'] = 3
    >>> struct.b = 4
    >>> struct
    OpenStruct({'a': 3, 'b': 4, 'c': 3})
    >>> struct.is_empty()
    False
    >>> struct.to_dict()
    {'a': 3, 'b': 4, 'c': 3}
    >>> struct.add({5: "d"})
    OpenStruct({'a': 3, 'b': 4, 'c': 3, 5: 'd'})
    >>> struct.a
    3
    >>> struct.b
    4
    >>> struct.c
    3
    >>> struct[5]
    'd'
    >>> struct.get(5)
    'd'
    >>> struct.get('d')
    """

    def __init__(self, *args, **kwargs) -> None:
        self.__dict__.update(*args, **kwargs)

    def __setitem__(self, key, value) -> None:
        self.__dict__[key] = value

    def __getitem__(self, key) -> Any:
        return self.__dict__[key]

    def __delitem__(self, key) -> None:
        del self.__dict__[key]

    def __iter__(self) -> Iterator[str]:
        return iter(self.__dict__)

    def __len__(self) -> int:
        return len(self.__dict__)

    def __str__(self) -> str:
        return str(self.__dict__)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.__dict__})'

    def add(self, struct: Self | Dict) -> Self:
        self.update(struct)
        return self

    def is_empty(self) -> bool:
        return len(self) == 0

    def to_dict(self) -> Dict:
        return self.__dict__


if __name__ == '__main__':
    import doctest
    doctest.testmod()
