# Conflict Resolution Log

팀에서 발생한 merge/rebase 충돌과 해결 과정을 기록합니다.

## 작성 규칙

- 충돌을 **해결한 사람**이 작성하고, 충돌 상대를 참여자에 함께 적습니다.
- 기록은 충돌이 난 PR 브랜치에서 해결 커밋과 **같은 PR**로 추가합니다.
- 충돌 마커는 해결 전 상태를 그대로 붙여넣습니다(재현 가능해야 함).
- 비자명 충돌이면 `유형`에 아래 중 무엇에 해당하는지 표시합니다.
  - 같은 hunk: 같은 파일의 같은/인접 라인을 서로 다르게 수정
  - 이동·삭제 vs 수정: 한쪽은 파일 이동/이름 변경/삭제, 다른 쪽은 내용 수정
- 팀 최소 기준: 충돌 해결 기록 **2회 이상**, 그중 **1회 이상 비자명 충돌**

## 기록 템플릿

새 기록은 아래 블록을 복사해 `## 기록` 섹션 맨 아래에 추가합니다.

````markdown
## 충돌 기록 #<번호>

### 참여자
- 작성자(해결): <name>
- 상대: <name>

### 유형
- [ ] 일반 충돌
- [ ] 비자명: 같은 hunk(인접 라인) 수정
- [ ] 비자명: 파일 이동/이름 변경/삭제 vs 내용 수정

### 상황(What happened)
- 브랜치: `<feature/...>` → `main`
- 파일: `<path>`
- 원인: 어떤 변경끼리 부딪혔는지

### 충돌 내용(Conflict markers)
```txt
<<<<<<< HEAD
...
=======
...
>>>>>>> feature/...
```

### 해결 과정(How)
- 선택한 전략: keep both / choose one / refactor 중 무엇을, 왜
- 실제 수행한 명령
  ```bash
  git switch <branch>
  git merge main        # 또는 git rebase main
  # 충돌 파일 수정
  git add <path>
  git commit            # rebase면 git rebase --continue
  ```

### 결과(Outcome)
- 최종 병합 결과 요약
- 관련 PR/커밋: <url>

### 배운 점(Learnings)
- 다음에 예방하려면 무엇을 할지
````

## 기록

<!-- 위 템플릿을 복사해 여기에 추가하세요. -->

## 충돌 기록 #1

### 참여자
- 해결: tlswltjq (GitHub 웹 에디터에서 충돌 해결, `8624041`)
- 상대: NiceTry3675 (PR #8 작성자, 이 기록 작성)

### 유형
- [ ] 일반 충돌
- [x] 비자명: 같은 hunk(인접 라인) 수정
- [ ] 비자명: 파일 이동/이름 변경/삭제 vs 내용 수정

### 상황(What happened)
- 브랜치: `feature/string-utils`(PR #8) ← `main`(PR #10 병합 후 `3067dde`)
- 파일: `README.md`
- 원인: 두 PR이 모두 `main`(`6081252`)에서 출발해 README에 "유틸 함수 목록" 섹션을 각자 새로 추가함
  - PR #8: 표 헤더 아래에 `string_utils` 행 + `### 검증 방법` 섹션 추가
  - PR #10: 같은 표 헤더 아래에 `list_utils` 행 추가
  - 표 헤더(`|---|---|---|---|`) 바로 다음 줄을 서로 다르게 채워 Git이 자동 병합할 수 없음
- PR #10이 먼저 병합되면서 PR #8이 `CONFLICTING` 상태가 됨

### 충돌 내용(Conflict markers)
````txt
| 파일 | 함수 | 설명 | 담당 |
|---|---|---|---|
<<<<<<< HEAD
| [`src/string_utils.py`](src/string_utils.py) | `to_snake_case`, `truncate` | snake_case 변환, 최대 길이 말줄임 | NiceTry3675 |

### 검증 방법

```bash
python3 -m doctest src/<파일명>.py -v
```
=======
| [`src/list_utils.py`](src/list_utils.py) | `chunk`, `unique` | 고정 크기 분할, 순서 유지 중복 제거 | tlswltjq |
>>>>>>> 3067dde
````
- `HEAD`(위쪽) = 현재 브랜치(`feature/string-utils`)의 내용, `3067dde`(아래쪽) = 병합해 들어오는 `main`의 내용
- PR #10에는 `### 검증 방법` 섹션이 없어서, 행 1줄뿐 아니라 그 아래 섹션 전체가 충돌 구간에 포함됨

### 해결 과정(How)
- 선택한 전략: **keep both**. 두 행은 서로 다른 파일(유틸)을 설명하므로 둘 다 필요하고, `### 검증 방법` 섹션도 PR #8에서만 추가한 내용이라 그대로 유지
- 실제 수행: PR #8 화면 → **Resolve conflicts**(웹 에디터) → 마커 3줄 삭제, `list_utils` 행을 `string_utils` 행 위로 배치 → **Mark as resolved** → **Commit merge**
- 같은 충돌을 로컬에서 재현하는 명령
  ```bash
  git switch --detach 5213a3c      # PR #8 브랜치의 충돌 직전 커밋
  git merge 3067dde                # PR #10 병합 직후의 main
  # CONFLICT (content): Merge conflict in README.md
  git status -s                    # UU README.md
  # README.md에서 마커 제거, 두 행 모두 유지
  git add README.md
  git commit                       # 또는 확인만 했다면 git merge --abort
  ```

### 결과(Outcome)
- 머지 커밋 `8624041`(Merge branch 'main' into feature/string-utils) 이후 PR #8이 `MERGEABLE`로 바뀌었고, tlswltjq 승인 후 `c82fb14`로 `main`에 병합됨
- 최종 README 표에 `list_utils`, `string_utils` 두 행과 검증 방법 섹션이 모두 남음
- 관련: PR #8, PR #10, 커밋 `8624041`, `c82fb14`

### 배운 점(Learnings)
- 여러 PR이 같은 파일의 **같은 위치에 새 섹션/행을 추가**하면 내용이 달라 거의 확실히 충돌한다. 공용 문서(README 표 등)는 첫 PR이 뼈대(헤더·섹션)를 만들고 병합된 뒤, 다른 PR은 최신 `main`을 받아 **마지막 행 아래에 추가**하면 충돌 범위가 1줄로 줄어든다.
- 충돌 구간은 "바뀐 줄"만이 아니라 **양쪽이 서로 다르게 쓴 연속 구간 전체**다. 이번에는 `### 검증 방법` 섹션까지 마커 안에 들어가서, 마커를 지울 때 섹션을 함께 지우지 않도록 주의해야 했다.
- 웹 에디터로 해결하면 편하지만 로컬 실행 검증을 할 수 없고, 이번처럼 파일 끝 개행이 사라질 수 있다. 코드 파일 충돌은 로컬에서 `git merge main` 후 테스트(doctest)까지 돌리고 push하는 것을 기본으로 한다.


## 충돌 기록 #2

### 참여자
- 해결: ewisewjd (로컬에서 충돌 재현, 확인)
- 상대: main (`a3de3df` 변경 유입)

### 유형
- [x] 일반 충돌
- [ ] 비자명: 같은 hunk(인접 라인) 수정
- [ ] 비자명: 파일 이동/이름 변경/삭제 vs 내용 수정

### 상황(What happened)
- 브랜치: `feature/add-dict-utils`(PR #13) ← `main`(`a3de3df`)
- 파일: `README.md`
- 원인:
  - `feature/add-dict-utils`에서 README 유틸 함수 목록에 `dict_utils.py` 행을 추가함.
  - 이후 `main`을 병합하는 과정에서 README의 같은 위치 주변에 충돌이 발생함.
  - Git이 해당 구간을 자동으로 병합하지 못해 수동 해결이 필요했음.

### 충돌 내용(Conflict markers)
```txt
<<<<<<< HEAD
| [`src/dict_utils.py`](src/dict_utils.py) | `flatten_dict`, `deep_merge` | 중첩 딕셔너리 평탄화, 재귀적 병합 | ewisewjd |

=======
>>>>>>> a3de3df
```

### 해결 과정(How)
- 선택한 전략: **choose one**. 현재 브랜치(`feature/add-dict-utils`)에서 추가한 `dict_utils.py` 행을 유지하고, 병합해 들어오는 `main` 쪽에는 해당 구간에 별도로 유지할 내용이 없으므로 충돌 마커를 제거함.
- 실제 수행한 명령:
  ```bash
  git switch --detach 5210e3f
  git merge a3de3df
  git diff -- README.md
  git merge --abort
  ```

### 결과(Outcome)
- `ba1e7b5`에서 `main` 병합 과정의 README 충돌이 해결됨.
- 최종 README에는 `list_utils.py`, `string_utils.py`, `dict_utils.py` 행과 검증 방법 섹션이 모두 유지됨.
- `git show --cc ba1e7b5 -- README.md`와 `git show ba1e7b5:README.md`로 실제 병합 결과를 확인함.
- 관련 PR: [PR #13](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/13)
- 충돌 재현 과정은 `git merge --abort`로 종료했으며, 실제 병합 커밋과 구분하여 기록함.

### 배운 점(Learnings)
- README처럼 여러 브랜치에서 공통으로 수정하는 파일은 작은 행 추가만으로도 충돌이 발생할 수 있음.
- 충돌 발생 시 `git diff`로 양쪽 변경 사항을 확인하고, 각 변경의 목적에 따라 유지할 내용을 판단해야 함.
- 충돌 마커를 제거한 뒤에는 최종 파일에 필요한 내용이 모두 남아 있는지 확인해야 함.
- `git merge --abort`를 사용하면 충돌 해결을 진행하기 전에 재현한 병합을 안전하게 취소할 수 있음.
