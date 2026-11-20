
def flatten_dict(data, parent_key=""):
    """중첩된 딕셔너리를 점(.)으로 구분된 키를 사용해 평탄화한다.

    >>> flatten_dict({"user": {"name": "Kim", "age": 20}, "active": True})
    {'user.name': 'Kim', 'user.age': 20, 'active': True}
    >>> flatten_dict({"a": {"b": {"c": 1}}})
    {'a.b.c': 1}
    >>> flatten_dict({})
    {}
    """
    result = {}

    for key, value in data.items():
        new_key = f"{parent_key}.{key}" if parent_key else str(key)

        if isinstance(value, dict):
            result.update(flatten_dict(value, new_key))
        else:
            result[new_key] = value

    return result


def deep_merge(dict1, dict2):
    """두 딕셔너리를 재귀적으로 병합한다.

    동일한 키가 존재하면 두 번째 딕셔너리의 값으로 덮어쓴다.
    원본 딕셔너리의 최상위 구조는 변경하지 않는다.

    >>> deep_merge({"user": {"name": "Kim", "age": 20}},
    ...            {"user": {"age": 21}, "active": True})
    {'user': {'name': 'Kim', 'age': 21}, 'active': True}
    >>> deep_merge({"a": 1}, {"b": 2})
    {'a': 1, 'b': 2}
    >>> deep_merge({}, {"a": 1})
    {'a': 1}
    """
    result = dict1.copy()

    for key, value in dict2.items():
        if isinstance(result.get(key), dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value

    return result
