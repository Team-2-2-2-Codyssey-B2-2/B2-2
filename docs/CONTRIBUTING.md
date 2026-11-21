# 기여 가이드 (CONTRIBUTING)

## 1. 브랜치 전략 (GitHub Flow)

- `main`: 항상 깨지지 않는 상태를 유지합니다. 직접 push는 금지되며(Ruleset `protect-main`), PR과 승인 1명 이상으로만 병합합니다.
- `feature/*`: 작업 1건(이슈 1개)마다 최신 `main`에서 분기하고, PR 병합 후 삭제합니다.

**GitHub Flow를 선택한 이유**
- 3인 팀의 짧은 미션이라 `develop`·`release` 브랜치를 따로 둘 필요가 없습니다.
- 모든 변경이 `feature/*` → PR → 리뷰 → `main` 한 경로로만 들어가서 리뷰와 이슈 추적이 빠지지 않습니다.
- 작업 단위가 작아 오래 갈라진 브랜치가 생기지 않으므로 충돌 범위도 작게 유지됩니다.

## 2. 브랜치 네이밍 규칙

- 형식: `feature/<작업-주제>`, "여러 명이 같은 주제를 나눠 할 때만 <GitHub-ID>- 접두사"
- 영어 소문자와 하이픈(`-`)만 사용합니다(kebab-case).
- 주제는 무엇을 하는 브랜치인지 드러나게 씁니다.

| 예시 | 판정 |
|---|---|
| `feature/string-utils`, `feature/tlswltjq-list-utils` | ✅ |
| `feature/troubleshooting-stash`, `feature/tlswltjq-revert-readme` | ✅ |
| `feature/test`, `feature/work`, `my-branch` | ❌ 주제 불명 / 접두사 없음 |

## 3. 커밋 메시지 및 PR 제목 컨벤션

- 커밋 메시지와 PR 제목은 `<type>: <변경 내용>` 형식을 따릅니다.
- 콜론(`:`) 뒤에는 반드시 공백 한 칸을 넣습니다.
- 변경 내용을 간결하고 명확하게 작성합니다.
- 가능한 경우 무엇을 변경했는지와 왜 변경했는지가 드러나도록 작성합니다.

### 사용 type

| type | 용도 |
|---|---|
| `feat` | 기능(유틸 함수) 추가 |
| `fix` | 버그 수정 |
| `docs` | 문서 추가·수정 |
| `refactor` | 동작 변화 없는 코드 구조 개선 |
| `test` | 테스트·doctest 추가 |
| `chore` | 설정·빌드·.gitignore 등 기타 |

### 작성 예시

**올바른 예시**
- `docs: 프로젝트 디렉토리 구성 및 일부 문서 추가`
- `feat: 사용자 로그인 기능 추가`
- `fix: 잘못된 파일 경로 수정`
- `chore: 불필요한 파일 추적 방지를 위한 gitignore 수정`

**잘못된 예시**
- `docs:프로젝트 디렉토리 구성 및 일부 문서 추가`
- `feat:로그인 기능 추가`

### 의미 없는 커밋 메시지 (금지)

아래 중 하나라도 해당하면 의미 없는 메시지로 보고, 병합 전에 수정합니다.
- 변경 대상을 알 수 없는 단어만 있는 경우: `update`, `fix`, `temp`, `wip`, `final`
- 무엇을/왜 바꿨는지 드러나지 않는 경우: `bug fix`, `edit file`, `Update README.md`
- 수정 방법: push 전이면 `git commit --amend`, 여러 커밋이면 `git rebase -i`(개인 브랜치에서만)

## 4. GitHub Suggestion 커밋 규칙

- PR 리뷰에서 Suggestion을 적용할 때도 동일한 커밋 메시지 컨벤션을 준수합니다.
- GitHub에서 자동 생성하는 `Update .gitignore` 등의 기본 커밋 메시지는 수정합니다.
- 커밋 메시지에는 변경 내용과 목적이 드러나도록 작성합니다.

### 작성 예시

- 변경 전: `Update .gitignore`
- 변경 후: `chore: 불필요한 파일 추적 방지를 위한 gitignore 규칙 수정`
