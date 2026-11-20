# B2-2
코디세이 11월 미션톤 B2-2

## 유틸 함수 목록

팀원별 유틸 함수 모음입니다(Python 3.10+). 사용 예시는 각 파일의 docstring(doctest)에 있습니다.

| 파일 | 함수 | 설명 | 담당 |
|---|---|---|---|
| [`src/list_utils.py`](src/list_utils.py) | `chunk`, `unique` | 고정 크기 분할, 순서 유지 중복 제거 | tlswltjq |
| [`src/string_utils.py`](src/string_utils.py) | `to_snake_case`, `truncate` | snake_case 변환, 최대 길이 말줄임 | NiceTry3675 |
| [`src/dict_utils.py`](src/dict_utils.py) | `flatten_dict`, `deep_merge` | 중첩 딕셔너리 평탄화, 재귀적 병합 | ewisewjd |

### 검증 방법

```bash
python3 -m doctest src/<파일명>.py -v
```