# Troubleshooting Log

Git 트러블슈팅 4종 시나리오를 실제로 수행하고 기록합니다.

## 작성 규칙

- 4개 시나리오는 **팀 전체가 모두** 수행하고, 각 섹션을 채웁니다.
- 팀원은 **최소 1개 시나리오**에 참여하며, 참여자란에 **이름과 역할**을 적습니다.
  - 역할 예: 수행, 기록, 검증(리뷰)
- 명령은 실제로 실행한 순서대로, 출력(일부)과 함께 남겨 다른 사람이 재현할 수 있게 합니다.
- 공유 브랜치(`main`)에서는 히스토리 재작성(`reset`, `amend` 후 force push)을 하지 않습니다.
  - `amend`, `reset --soft`, `stash`는 **push 전 개인 feature 브랜치**에서 수행합니다.
  - `revert`는 이미 `main`에 병합된 커밋을 대상으로, **revert 커밋을 담은 PR**로 병합합니다.

> 담당/상태는 각 시나리오를 수행하는 **작업 PR에서 담당자가 직접 갱신**합니다(⬜ 미수행 → ✅ 완료).

| 시나리오 | 명령 | 담당 | 상태 |
|---|---|---|---|
| 1. amend | `git commit --amend` | tlswltjq | ✅ |
| 2. reset --soft | `git reset --soft HEAD~1` | NiceTry3675 | ✅ |
| 3. revert | `git revert <commit>` | TBD | ⬜ |
| 4. stash | `git stash` / `git stash pop` | TBD | ✅ |

---

## 시나리오 1: amend (최근 커밋 메시지 수정)

### 참여자
- tlswltjq (수행, 기록)

### 상황
- 브랜치 `feature/tlswltjq-list-utils`에서 `src/list_utils.py`를 추가하고 커밋 메시지를 `add list utils`로 남김 (PR #10, Issue #9)
- 팀 컨벤션(`<type>: <변경 내용>`)에 어긋나고, 어떤 함수를 추가했는지 드러나지 않는 메시지
- 아직 push 전이라 원격에는 이 커밋이 없는 상태

### 시도한 명령/절차
```bash
git log --oneline -1
# a978ba0 add list utils

git commit --amend -m "feat: 리스트 유틸 함수(chunk, unique) 추가"

git log --oneline -1
# 7b10085 feat: 리스트 유틸 함수(chunk, unique) 추가

git reflog -3
# 7b10085 HEAD@{0}: commit (amend): feat: 리스트 유틸 함수(chunk, unique) 추가
# a978ba0 HEAD@{1}: commit: add list utils
# 6081252 HEAD@{2}: checkout: moving from main to feature/tlswltjq-list-utils
```

### 결과
- 파일 내용은 그대로이고 메시지만 바뀐 새 커밋 `7b10085`가 생기고, 브랜치 포인터가 그쪽으로 이동함
- 커밋 해시는 메시지까지 포함해 계산되므로 `a978ba0` → `7b10085`로 바뀜(같은 커밋 수정이 아니라 교체)
- 이전 커밋 `a978ba0`은 어떤 브랜치도 가리키지 않지만 `git reflog`에 남아 있어 `git reset --hard a978ba0`으로 되돌릴 수 있음
- 주의할 점
  - amend는 히스토리를 바꾸므로 **push 전, 개인 feature 브랜치에서만** 사용
  - 이미 push한 커밋을 amend하면 원격과 해시가 달라져 force push가 필요하고, 같은 브랜치를 받은 팀원 히스토리가 꼬임
  - 마지막 커밋만 고칠 수 있음(더 이전 커밋은 `git rebase -i`)

### 왜 이 방법을 선택했는가(Why)
- push 전이고 마지막 커밋 1개의 메시지만 잘못됐으므로, 커밋을 하나 더 쌓지 않고 바로 고칠 수 있는 amend가 가장 간단함
- `reset --soft HEAD~1`도 가능하지만 커밋을 취소한 뒤 다시 커밋해야 해서 단계가 많음
- `revert`는 이미 공유된 커밋을 되돌리는 방법이라 메시지 수정에는 맞지 않음

---

## 시나리오 2: reset --soft (로컬 커밋 취소 + 변경 유지)

### 참여자
- NiceTry3675 (수행, 기록)

### 상황
- 브랜치 `feature/conflict-log-reset-soft`에서 `docs/conflict-resolution.md`에 충돌 기록 #1을 작성하고 커밋(`6465624`)함 (Issue #14)
- 커밋 직후 템플릿 필수 항목인 **"배운 점(Learnings)" 섹션을 빠뜨린 것**을 발견
- 아직 push 전이라 원격에는 이 커밋이 없는 상태
- "섹션 추가" 커밋을 하나 더 쌓으면 미완성 커밋이 히스토리에 남으므로, 커밋을 취소하고 내용을 보완해 **하나의 완성된 커밋**으로 다시 만들기로 함

### 시도한 명령/절차
```bash
$ git log --oneline -2
6465624 docs: add conflict record #1 (README same-hunk conflict between PR #8 and #10)
c82fb14 Merge pull request #8 from Team-2-2-2-Codyssey-B2-2/feature/string-utils

$ git reset --soft HEAD~1

$ git log --oneline -2
c82fb14 Merge pull request #8 from Team-2-2-2-Codyssey-B2-2/feature/string-utils
8624041 Merge branch 'main' into feature/string-utils

$ git status -s
M  docs/conflict-resolution.md        # 첫 글자 M = 스테이징 영역에 그대로 남아 있음

$ git diff --cached --stat
 docs/conflict-resolution.md | 58 +++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 58 insertions(+)

# "배운 점" 섹션 추가 후 다시 커밋
$ git add docs/conflict-resolution.md
$ git commit -m "docs: add conflict record #1 (README same-hunk conflict between PR #8 and #10)"

$ git log --oneline -2
a945f27 docs: add conflict record #1 (README same-hunk conflict between PR #8 and #10)
c82fb14 Merge pull request #8 from Team-2-2-2-Codyssey-B2-2/feature/string-utils

$ git reflog -4
a945f27 HEAD@{0}: commit: docs: add conflict record #1 (README same-hunk conflict between PR #8 and #10)
c82fb14 HEAD@{1}: reset: moving to HEAD~1
6465624 HEAD@{2}: commit: docs: add conflict record #1 (README same-hunk conflict between PR #8 and #10)
c82fb14 HEAD@{3}: checkout: moving from main to feature/conflict-log-reset-soft
```

### 결과
- `reset --soft HEAD~1`은 **브랜치 포인터만** `6465624` → `c82fb14`로 한 칸 되돌림. 작성한 58줄은 스테이징 상태(`M `)로 그대로 남아 있어 다시 `add`할 필요 없이 보완만 하면 됐음
- 보완 후 새 커밋 `a945f27`이 생김. 같은 메시지지만 내용(트리)이 달라 해시도 다름
- 취소된 `6465624`는 어떤 브랜치도 가리키지 않지만 `reflog`(`HEAD@{2}`)에 남아 있어, 필요하면 `git reset --hard 6465624`로 복구 가능
- 주의할 점
  - push 전 **개인 feature 브랜치에서만** 사용. 이미 push한 커밋을 reset하면 원격보다 뒤처져 force push가 필요해지고, 같은 브랜치를 받은 팀원의 히스토리와 갈라짐 → 공유된 커밋은 `revert`(시나리오 3) 사용
  - `HEAD~1`의 `~1`은 "현재 커밋의 첫 번째 부모". 머지 커밋 위에서 쓸 때는 어느 쪽으로 이동하는지 `git log --graph`로 먼저 확인

### 왜 이 방법을 선택했는가(Why)
- **`--soft` vs `--mixed` vs `--hard`**: 변경 내용을 지우면 안 되므로 `--hard`는 제외. `--mixed`(기본값)도 파일은 남지만 스테이징이 풀려 다시 `git add`해야 함. 커밋만 취소하고 **스테이징까지 그대로 유지**하는 `--soft`가 "조금만 보완해서 다시 커밋"하는 상황에 가장 적합
- **amend와 비교**: 이번처럼 마지막 커밋 1개만 보완하는 경우 `git add` 후 `git commit --amend`로도 같은 결과를 얻을 수 있음. 다만 `reset --soft`는 `HEAD~2`, `HEAD~3`처럼 **여러 커밋을 한 번에 풀어 하나로 다시 묶을 때**도 같은 방식으로 쓸 수 있어 원리를 익히는 목적에 맞음
- **새 커밋 추가와 비교**: "docs: add missing learnings" 커밋을 추가하면 미완성 커밋이 히스토리에 남아 리뷰어가 두 커밋을 합쳐서 봐야 함. push 전이므로 히스토리를 정리하는 쪽을 선택

---

## 시나리오 3: revert (원격에 push된 커밋 취소)

### 참여자
- <name> (역할)

### 상황
- 

### 시도한 명령/절차
```bash
git switch -c feature/<name>-revert-<topic> main
git revert <commit>
git push -u origin feature/<name>-revert-<topic>
# PR 생성 → 리뷰 → 병합
```

### 결과
- 
- 관련 PR: <url>

### 왜 이 방법을 선택했는가(Why)
- `reset` 대신 `revert`를 선택한 이유

---

## 시나리오 4: stash / stash pop (작업 임시 보관 및 복원)

### 참여자
- ewisewjd (수행, 기록)

### 상황
- 브랜치 `feature/add-dict-utils`에서 기존 학습 자료인 `docs/study/`를 작업 중인 상태
- Issue #16의 stash 실습을 위해 별도 브랜치 `feature/troubleshooting-stash`를 생성해야 하는 상황
- 기존 작업을 커밋하거나 다른 브랜치로 이동하면서 유실하지 않도록 임시 보관하기로 함
- `docs/study/`는 Git이 추적하지 않는 파일이므로 `-u` 옵션을 사용해야 하는 상황

### 시도한 명령/절차
```bash
# 1. 기존 작업 상태 확인
git status
# Untracked files:
#   docs/study/

# 2. 기존 작업을 미추적 파일까지 포함해 임시 보관
git stash push -u -m "backup: preserve study docs before issue-16"
# Saved working directory and index state ...

# 3. 작업 디렉터리 확인
git status
# nothing to commit, working tree clean

# 4. stash 목록 확인
git stash list
# stash@{0}: On feature/add-dict-utils: backup: preserve study docs before issue-16

# 5. 최신 원격 main을 기준으로 작업 브랜치 생성
git fetch origin
git switch -c feature/troubleshooting-stash origin/main

# 6. 별도 브랜치에서 stash 동작 실습
# 임시 파일 생성 후 -u 옵션으로 stash
git stash push -u -m "practice: stash untracked file for issue-16"

# 7. 실습 항목 복원
git stash pop 'stash@{0}'

# 8. 기존 백업 stash가 남아 있는지 확인
git stash list
# stash@{0}: On feature/add-dict-utils: backup: preserve study docs before issue-16
```

### 결과
- 기존 `feature/add-dict-utils` 브랜치의 `docs/study/`를 `git stash push -u`로 임시 보관함
- stash 이후 작업 디렉터리가 clean 상태가 된 것을 확인함
- 기존 작업을 보존한 상태로 최신 `origin/main`을 기준으로 `feature/troubleshooting-stash` 브랜치를 생성함
- 별도의 임시 파일을 이용해 untracked 파일도 stash 대상에 포함되는 것을 확인함
- `git stash pop`으로 실습용 파일을 복원하고 해당 stash 항목이 제거되는 것을 확인함
- 기존 `docs/study/` 백업 stash는 유지되어 있음을 확인함
- 실습용 임시 파일을 삭제한 후 작업 디렉터리가 clean 상태임을 확인함
- 주의할 점:
  - 기본 `git stash`는 untracked 파일을 포함하지 않으므로 `-u` 옵션을 사용해야 함
  - `git stash pop`은 복원과 동시에 해당 stash 항목을 제거하므로 대상 항목을 확인한 후 실행해야 함
  - 기존 작업을 보관한 stash와 실습용 stash가 함께 존재할 수 있으므로 `git stash list`로 구분해야 함
  - 기존 `docs/study/` 백업은 아직 복원하지 않았으므로 이후 원래 브랜치에서 복원해야 함

### 왜 이 방법을 선택했는가(Why)
- 기존 작업을 완료하지 않은 상태에서 다른 브랜치로 이동해야 했으므로 임시 커밋 대신 `stash`를 선택함
- `docs/study/`가 untracked 상태였기 때문에 일반 `git stash`가 아닌 `git stash push -u`를 사용함
- 별도의 백업 커밋을 만들지 않고 작업 디렉터리를 clean 상태로 만들어 다른 작업을 진행할 수 있음
- `git stash pop`은 복원과 동시에 해당 stash 항목을 제거하므로 복원 완료 후 불필요한 stash가 남지 않음