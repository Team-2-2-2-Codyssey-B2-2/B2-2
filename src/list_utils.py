"""리스트 관련 유틸 함수 모음.

사용 예시는 각 함수의 docstring(doctest)에 있으며, 아래 명령으로 검증할 수 있습니다.

    python3 -m doctest src/list_utils.py -v
"""

from collections.abc import Hashable, Iterable, Sequence
from typing import TypeVar

T = TypeVar("T")
H = TypeVar("H", bound=Hashable)


def chunk(items: Sequence[T], size: int) -> list[list[T]]:
    """items를 size개씩 나눈 리스트를 반환합니다. 마지막 묶음은 size보다 작을 수 있습니다.

    >>> chunk([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    >>> chunk("abcdef", 3)
    [['a', 'b', 'c'], ['d', 'e', 'f']]
    >>> chunk([], 3)
    []
    >>> chunk([1, 2, 3], 0)
    Traceback (most recent call last):
        ...
    ValueError: size(0)는 1 이상이어야 합니다.
    """
    if size < 1:
        raise ValueError(f"size({size})는 1 이상이어야 합니다.")
    return [list(items[i : i + size]) for i in range(0, len(items), size)]


def unique(items: Iterable[H]) -> list[H]:
    """처음 나온 순서를 유지하면서 중복을 제거합니다.

    set()과 달리 원래 순서가 보존됩니다.

    >>> unique([3, 1, 3, 2, 1])
    [3, 1, 2]
    >>> unique("banana")
    ['b', 'a', 'n']
    >>> unique([])
    []
    """
    return list(dict.fromkeys(items))
