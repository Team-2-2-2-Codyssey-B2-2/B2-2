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
| 2. reset --soft | `git reset --soft HEAD~1` | TBD | ⬜ |
| 3. revert | `git revert <commit>` | TBD | ⬜ |
| 4. stash | `git stash` / `git stash pop` | TBD | ⬜ |

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
- <name> (역할)

### 상황
- 

### 시도한 명령/절차
```bash
git log --oneline -2
git reset --soft HEAD~1
git status
```

### 결과
- 
- 주의할 점: 

### 왜 이 방법을 선택했는가(Why)
- `--soft` / `--mixed` / `--hard` 중 `--soft`를 고른 이유

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

## 시나리오 4: stash / stash pop (작업 보관 후 전환)

### 참여자
- <name> (역할)

### 상황
- 

### 시도한 명령/절차
```bash
git stash push -m "<보관 이유>"
git switch <other-branch>
# 다른 작업 수행
git switch <original-branch>
git stash pop
```

### 결과
- 
- 주의할 점: 

### 왜 이 방법을 선택했는가(Why)
- 임시 커밋 대신 `stash`를 쓴 이유
