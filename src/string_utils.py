"""문자열 관련 유틸 함수 모음.

사용 예시는 각 함수의 docstring(doctest)에 있으며, 아래 명령으로 검증할 수 있습니다.

    python3 -m doctest src/string_utils.py -v
"""

import re

_WORD_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")
_SEPARATORS = re.compile(r"[\s\-_]+")


def to_snake_case(text: str) -> str:
    """CamelCase, 공백, 하이픈으로 구분된 문자열을 snake_case로 변환합니다.

    >>> to_snake_case("HelloWorld")
    'hello_world'
    >>> to_snake_case("getHTTPResponse")
    'get_http_response'
    >>> to_snake_case("user-name field")
    'user_name_field'
    >>> to_snake_case("already_snake")
    'already_snake'
    >>> to_snake_case("foo_-bar")
    'foo_bar'
    >>> to_snake_case("")
    ''
    """
    text = _WORD_BOUNDARY.sub("_", text.strip())
    text = _SEPARATORS.sub("_", text)
    return text.lower()


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """text가 max_length보다 길면 잘라서 suffix를 붙입니다.

    반환값의 길이는 suffix를 포함해 max_length를 넘지 않습니다.

    >>> truncate("Hello, World!", 8)
    'Hello...'
    >>> truncate("짧은 문장", 10)
    '짧은 문장'
    >>> truncate("Hello, World!", 8, suffix="~")
    'Hello, ~'
    >>> truncate("Hello", 2)
    Traceback (most recent call last):
        ...
    ValueError: max_length(2)는 suffix 길이(3) 이상이어야 합니다.
    """
    if len(text) <= max_length:
        return text
    if max_length < len(suffix):
        raise ValueError(
            f"max_length({max_length})는 suffix 길이({len(suffix)}) 이상이어야 합니다."
        )
    return text[: max_length - len(suffix)] + suffix
