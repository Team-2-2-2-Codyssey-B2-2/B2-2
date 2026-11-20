# Codyssey 팀 Git 협업 미션 학습자료

Nov 18, 2026 · @안흥

## 0. 이 문서 사용법과 미션 한눈에 보기

이 미션은 코드를 잘 짜는 시험이 아니라, **팀원 3\~5명이 Git/GitHub로 함께 일한 과정이 기록으로 남았는지**를 보는 시험입니다. 미션 원문도 "결과물 퀄리티보다 협업 과정(브랜치, PR, 리뷰, 이슈, 충돌 해결, 기록)이 더 중요"라고 적고 있습니다. 그래서 이 자료도 명령어 암기보다 "왜 이렇게 하는지"와 "무엇을 기록으로 남겨야 하는지"에 힘을 줬습니다.

### 읽는 순서

1. 처음이면 1장(Git 기초)부터 순서대로 읽습니다. 브랜치, 충돌, 되돌리기는 모두 1장 개념 위에 쌓입니다.
2. 각 장 끝의 **"미션 연결"** 문구가 그 내용이 요구사항 중 무엇을 채우는지 알려줍니다.
3. 팀원과 역할을 나눌 때는 11장(실행 순서)과 9장(체크리스트)을 먼저 봅니다.
4. 명령어 블록은 그대로 복사해 실습해도 됩니다. 이 문서의 명령어는 실제로 실행해 결과를 확인한 것들입니다(14장 검증 기록).

### 미션 요구사항과 이 문서의 대응표

| 미션 요구사항 | 누가 | 이 문서 |
| --- | --- | --- |
| 3\~5인 팀, 저장소 생성(Org 또는 Collaborator), README / docs / src / team 폴더 | 팀 | 2장 |
| main Branch Protection (직접 push 금지, PR 병합만, 승인 1명 이상) | 팀 | 2장 |
| GitHub Flow, feature/\* 브랜치, 네이밍 규칙, 선택 이유 3줄 | 팀 | 3장 |
| 작업마다 Issue 생성, PR 본문에 Closes #번호 | 전원 | 4장 |
| 커밋 메시지 컨벤션, 의미 없는 메시지 금지 | 전원 | 5장 |
| PR 2개 이상 생성·병합, 리뷰 2개 이상 작성, 리뷰 반영 1회 이상 | 전원 각각 | 4장, 9장 |
| PR 본문 What / Why / How, 리뷰에 실질 코멘트 1개 이상 | 전원 | 4장 |
| 충돌 해결 기록 2회 이상(비자명 1회 이상), conflict-resolution.md | 팀 | 6장 |
| 트러블슈팅 4종(amend, reset --soft, revert, stash), 팀원마다 1개 이상 기록 참여 | 팀 + 전원 | 7장 |
| CONTRIBUTING.md, conflict-resolution.md, troubleshooting-log.md, SUBMISSION.md | 팀 | 8장 |
| 간단한 결과물 택 1, 팀원마다 기여 커밋 1건 이상 | 전원 | 9장 |
| git log --oneline --graph --all 증빙 | 팀 | 8장 |
| 보너스: rebase -i 정리, CODEOWNERS | 선택 | 10장 |
| 운영 안정성: main 히스토리 재작성 금지, 합의 없는 force push/rebase 금지 | 전원 | 3장, 7장, 10장 |

### 용어 미리보기

- **저장소(repository, repo)**: 프로젝트 파일과 그 변경 이력을 함께 담은 폴더입니다.
- **커밋(commit)**: 변경 내용을 "저장 지점"으로 찍어 둔 기록입니다.
- **브랜치(branch)**: 작업 갈래입니다. 내부적으로는 특정 커밋을 가리키는 이름표입니다.
- **원격(remote)**: GitHub에 올라가 있는 저장소입니다. 보통 이름이 `origin`입니다.
- **PR(Pull Request)**: "내 브랜치를 main에 합쳐 주세요"라는 요청이자 리뷰가 오가는 공간입니다.
- **충돌(conflict)**: 같은 부분을 서로 다르게 고쳐서 Git이 자동으로 합치지 못하는 상황입니다.

## 1. Git 기초 개념

Git은 파일의 변경 이력을 "저장 지점(커밋)"마다 기록해 두는 도구이고, GitHub는 그 저장소를 인터넷에 올려 여러 사람이 함께 쓰게 해 주는 서비스입니다. 혼동하기 쉽지만 **Git은 도구(내 컴퓨터에서 동작), GitHub는 서비스(웹 사이트)**입니다. Issue, Pull Request, Branch Protection은 Git이 아니라 GitHub의 기능입니다.

### 1-1. 처음 한 번만 할 설정

```bash
git config --global user.name "내 이름"
git config --global user.email "github에 등록한@email.com"
git config --global init.defaultBranch main
git config --list --show-origin   # 설정 확인
```

이 이름과 이메일이 모든 커밋에 "누가 만들었는지"로 찍힐니다. 미션에서는 팀원별 기여를 커밋과 PR로 확인하므로, **GitHub 계정에 등록한 이메일과 동일하게** 설정해야 기여가 내 계정으로 집계됩니다.

### 1-2. 파일이 거치는 세 곳

Git 작업을 이해하는 가장 중요한 그림입니다. 6장과 7장(reset, stash)의 설명이 전부 이 세 영역에서 출발합니다.

| 영역 | 쉽게 말하면 | 이동 명령 |
| --- | --- | --- |
| 작업 디렉터리(Working Directory) | 내가 지금 파일을 고치는 실제 폴더 | 파일을 수정하면 여기에 쌓임 |
| 스테이징 영역(Staging Area, Index) | 다음 커밋에 넣을 변경을 고르는 장바구니 | `git add <파일>` |
| 저장소(Repository, `.git`) | 확정된 커밋이 쌍이는 기록 보관함 | `git commit` |

파일 하나는 세 가지 상태를 오갑니다. 새 파일은 **untracked**(Git이 아직 모름), 수정했지만 add 전이면 **modified**, add했지만 commit 전이면 **staged**, commit을 마치면 **committed**입니다. `git status`는 지금 내 파일이 어느 상태인지 알려 주는 가장 안전하고 중요한 명령어이므로, 무엇을 하기 전후로 습관처럼 치세요.

### 1-3. 커밋(commit)이란

커밋은 "변경점 목록"이 아니라 **그 시점 프로젝트 전체의 스냅샷**입니다. 하나의 커밋에는 다음이 들어 있습니다.

- 고유 ID(해시): `7946431e18...`처럼 긴 16진수 문자열입니다. 보통 앞 7자리만 봅니다.
- 부모 커밋: 바로 앞 커밋을 가리킵니다. 이 연결이 "히스토리"입니다.
- 작성자, 시간, 커밋 메시지

커밋을 만드는 기본 흐름입니다.

```bash
git status                       # 1) 현재 상태 확인
git add src/util.py              # 2) 담을 변경만 골라 스테이징
git commit -m "feat: add string utils"   # 3) 확정
git log --oneline                # 4) 기록 확인
```

팀 프로젝트에서는 `git add .`(전부 담기)보다 파일 이름을 직접 지정하는 습관이 안전합니다. 비밀 파일(.env)이나 내 컬퓨터에만 있어야 하는 파일이 딱 들어가는 사고를 막아 줍니다. 필요한 경우 `.gitignore` 파일에 무시할 파일 이름을 적습니다(예: `__pycache__/`, `.env`).

### 1-4. 브랜치는 "커밋을 가리키는 포인터"입니다

미션 과제 목표에 그대로 나오는 질문입니다("브랜치가 내부적으로 어떻게 동작하는지"). 브랜치는 파일을 복사해 두는 것이 아니라, **특정 커밋 하나를 가리키는 이름표**일 뿐입니다. 실제로 확인해 본 결과입니다.

```text
$ cat .git/HEAD
ref: refs/heads/feature/kim-demo

$ cat .git/refs/heads/main
442c96fe86feae8e79d2c867f999080add94329d
$ cat .git/refs/heads/feature/kim-demo
7946431e1872d65e1f1dc60560415cee2e48f294

$ git log --oneline --decorate --graph --all
* 7946431 (HEAD -> feature/kim-demo) feat: append line to a.txt
* 442c96f (main) docs: add a.txt
```

이 출력이 보여 주는 것은 다섯 가지입니다.

1. `main`이라는 브랜치는 파일 하나이고, 안에 커밋 ID 한 줄만 들어 있습니다.
2. 새 브랜치를 만들어도 이름표 한 장이 늘어날 뿐이라 매우 가볍고 빠릅니다.
3. 현재 브랜치에서 커밋하면 그 브랜치의 이름표만 새 커밋으로 앞으로 이동합니다. 다른 브랜치는 그대로입니다.
4. `HEAD`는 "지금 내가 서 있는 브랜치"를 가리키는 포인터입니다(포인터를 가리키는 포인터).
5. 그래서 `git switch`는 파일을 복사하는 게 아니라 HEAD가 가리키는 이름표를 바꾸고 작업 폴더를 그 커밋 모습으로 맞추는 동작입니다.

**왜 브랜치를 나눠서 작업하나요?** 여러 사람이 한 저장소에서 동시에 다른 일을 할 때, 각자 자기 갈래에서 작업하면 내 미완성 코드가 남의 작업을 깨뜨리지 않고, main은 항상 깨지지 않은 상태로 남습니다. 합칠 준비가 되면 리뷰를 거쳐 main에 병합합니다.

### 1-5. 브랜치 명령어와 병합(merge)

```bash
git branch                      # 로컬 브랜치 목록 (현재 것에 * 표시)
git switch main                 # main으로 이동
git switch -c feature/kim-utils # 새 브랜치를 만들고 바로 이동 (-c = create)
git merge feature/kim-utils     # 현재 브랜치에 다른 브랜치를 합침
git branch -d feature/kim-utils # 합친 브랜치 삭제(이미 합쳐진 것만 지워짐)
```

`git switch`는 Git 2.23(2019년)에 생긴 편한 명령어이고, 예전 글에서는 `git checkout`을 씁니다. 둔 다 브랜치 이동에 쓸 수 있지만 초보자는 `switch`만 쓰면 헷갈림이 적습니다.

병합의 두 가지 모양을 구분해 두세요.

- **Fast-forward**: main에 새 커밋이 없었을 때, main 이름표를 단순히 앞으로 밀어 주는 것. 병합 커밋이 생기지 않아 그래프가 일자로 보입니다.
- **병합 커밋(merge commit)**: 두 브랜치가 서로 다른 커밋을 가졌을 때 부모가 2개인 커밋을 만들어 합치는 것. 미션 결과 예시의 "Merge pull request #8 ..."가 이 모양입니다. GitHub에서 PR을 "Create a merge commit"로 합치면 항상 이 모양이 됩니다.

### 1-6. 로컬과 원격(remote)

내 컴퓨터의 저장소가 **로컬**, GitHub에 있는 저장소가 **원격**입니다. 원격의 기본 이름은 `origin`입니다. 내가 커밋을 해도 push하기 전까지 팀원에게는 안 보입니다.

```bash
git clone https://github.com/<조직>/<저장소>.git   # 원격 저장소를 내 컬퓨터로 복사
git remote -v                           # 연결된 원격 확인
git push -u origin feature/kim-utils    # 내 브랜치를 원격에 올리고, 다음부터 단순 git push만하도록 연결
git fetch                               # 원격 변경을 내려받지만 내 작업에는 반영 안 함
git pull                                # fetch + 현재 브랜치에 합치기를 한 번에
```

팀 작업의 일상 루틴은 이렇습니다. 작업 시작 전 `git switch main` → `git pull`로 최신을 받고, `git switch -c feature/...`로 새 브랜치를 따서 작업하고, 커밋한 뒤 `git push`로 올려 PR을 엽니다.

### 1-7. 자주 쓰는 확인 명령어

| 명령어 | 하는 일 |
| --- | --- |
| `git status` | 지금 어느 브랜치이고 무엇이 변경/스테이징되었는지 |
| `git diff` | 아직 add하지 않은 변경의 상세 내용 |
| `git diff --staged` | add해 둔(다음 커밋에 들어갈) 변경의 상세 내용 |
| `git log --oneline` | 커밋 목록을 한 줄씩 |
| `git log --oneline --graph --all` | 모든 브랜치를 그래프로(미션 증빙 자료로 제출) |
| `git show <해시>` | 특정 커밋 하나의 내용 |

> 미션 연결: 과제 목표 1번(브랜치 원리 설명), 증빙 자료(`git log --oneline --graph --all`) 준비의 바탕입니다.

## 2. GitHub 저장소와 팀 세팅

저장소를 만들고 팀원을 초대하고 main을 보호하는 것까지가 미션의 출발선입니다. **팀에서 한 명이 대표로 세팅하고**, 나머지는 수락하고 clone하면 됩니다.

### 2-1. 저장소 구성 방법 두 가지

|  | 옵션 A (권장) | 옵션 B (대체) |
| --- | --- | --- |
| 방법 | GitHub Organization을 만들고 그 안에 저장소 생성 | 한 명의 개인 계정에 저장소를 만들고 Collaborator로 초대 |
| 팀원 초대 | Organization > People에서 멤버 초대 | 저장소 Settings > Collaborators에서 추가 |
| 장점 | 저장소 소유가 한 사람에게 쏠리지 않고 권한 관리가 깔끔 | 시작이 빠름 |
| 주의 | 모든 멤버가 초대를 **수락**해야 함 | 저장소 주인이 admin이라 보호 규칙을 우회할 수 있음(2-5 참고) |

GitHub 메뉴 이름은 업데이트로 조금씩 바뀔 수 있습니다. 화면이 다르면 이름이 비슷한 메뉴를 찾아보세요.

### 2-2. 공개(public) 저장소로 만드세요 (중요)

GitHub 공식 문서("About protected branches")에 따르면 **무료 플랜(GitHub Free)에서는 브랜치 보호가 공개 저장소에서만 제공**되고, 비공개(private) 저장소에서는 Pro·Team 등 유료 플랜이 필요합니다. 무료 계정으로 Branch Protection 요구사항을 채우려면 저장소를 Public으로 만드는 게 가장 간단합니다. 그러니 팀원들과 미리 이름, 이메일, 비밀 정보를 저장소에 넣지 않기로 약속하세요(특히 팀 소개 문서를 선택했다면 공개해도 괜찮은 내용만 씁니다).

### 2-3. 처음 만들 때 순서

1. 저장소를 만들 때 **"Add a README file"**을 체크하면 초기 커밋이 생겨 main 브랜치가 바로 생깁니다.
2. 팀원 전원을 초대하고, 각자 초대를 **수락**합니다.
3. 기본 폴더(`docs/`, `src/`, 선택에 따라 `team/`)를 만든 다음 **Branch Protection을 켭니다**. 보호를 먼저 켜면 세팅 커밋도 PR을 거쳐야 해서 진행이 느려집니다.
4. 팀원 각자 `git clone`으로 내 컴퓨터에 내려받습니다.

```bash
git clone https://github.com/<조직이름>/<저장소이름>.git
cd <저장소이름>
git remote -v          # origin이 나오면 연결 성공
```

### 2-4. 기본 폴더 구조와 "빈 폴더" 함정

```text
팀저장소/
├─ README.md
├─ SUBMISSION.md
├─ docs/
│  ├─ CONTRIBUTING.md
│  ├─ conflict-resolution.md
│  └─ troubleshooting-log.md
├─ src/        (유틸 함수 등 코드를 선택했다면)
└─ team/       (팀 소개를 선택했다면)
```

Git은 **빈 폴더를 추적하지 못합니다.** 폴더를 만들어도 안에 파일이 없으면 커밋에 포함되지 않아서 GitHub에 폴더가 보이지 않습니다. 폴더 안에 `README.md`나 관례적으로 쓰는 빈 파일 `.gitkeep`을 넣어 두세요.

### 2-5. Ruleset을 이용한 main 브랜치 보호 (미션 필수)

미션 요구사항은 세 가지입니다.

- main 브랜치에 직접 push 금지
- PR을 통한 병합만 허용
- 최소 1명 이상의 승인(Approve) 필요

GitHub에서는 Branch Protection Rule 또는 Ruleset을 이용해 브랜치를 보호할 수 있습니다.

우리 팀 저장소는 Ruleset 방식을 사용합니다.

**Ruleset 설정 확인 경로**

1. 저장소 메인 페이지에서 Settings 선택
2. 왼쪽 메뉴에서 Rules 선택
3. Rulesets 선택
4. `protect-main` Ruleset 확인

**주요 설정 확인 사항**

- 대상 브랜치(Target branches): `main`
- PR을 통한 변경만 허용
- PR 병합 전 최소 1명 이상의 승인 요구
- 강제 푸시 제한
- Ruleset의 bypass 대상 확인

우리 팀의 `protect-main` Ruleset은 bypass 대상이 비어 있습니다. 따라서 별도로 우회 권한을 부여받은 계정이 없는 현재 설정에서는 관리자도 Ruleset을 우회할 수 없습니다.

**주의:** Ruleset과 Classic Branch Protection Rule은 별개의 설정입니다. 이미 Ruleset으로 브랜치를 보호하고 있다면 같은 목적의 Classic Rule을 추가로 만들지 말고, 기존 Ruleset의 설정을 확인하고 관리하는 것이 좋습니다.

**설정 확인 방법**

테스트 PR을 생성하고 다음 사항을 확인합니다.

- 승인 전에는 병합할 수 없는지
- 승인 후 병합할 수 있는지
- main에 직접 push할 수 없는지
- 강제 푸시가 제한되는지

설정 화면과 테스트 결과를 캡처해 `SUBMISSION.md`에 증빙으로 첨부하면 좋습니다.

### 2-6. 승인 규칙이 팀 운영에 주는 영향

최소 1명 승인이 필요하다는 것은 **PR 작성자가 자기 PR을 혼자 승인해서 병합할 수 없다**는 뜻입니다. 다른 팀원의 리뷰와 Approve가 반드시 필요하기 때문에, 팀원들이 서로의 PR을 수시로 봐 줘야 합니다. 미션의 "리뷰 2개 이상 작성" 요구와 자연스럽게 연결됩니다.

> 미션 연결: 팀 구성(3\~5인), 옵션 A/B, README·docs·src·team 폴더, main Branch Protection(직접 push 금지 / PR만 병합 / 승인 1명) 요구사항을 모두 다룹니다.

## 3. GitHub Flow와 브랜치 네이밍

GitHub Flow는 "main은 건드리지 말고, 작업은 짧은 브랜치에서 하고, PR과 리뷰를 거쳐 합친다"는 가볍고 단순한 협업 방식입니다. 미션이 요구하는 구조(main + feature/\*)가 그대로 GitHub Flow입니다.

### 3-1. GitHub Flow 6단계

GitHub 공식 문서("GitHub flow")가 정리한 순서입니다.

1. **브랜치 생성**: 저장소에서 작업용 브랜치를 만든다.
2. **변경과 커밋, push**: 브랜치에서 작업하고 커밋하고 원격에 올린다.
3. **Pull Request 열기**: 피드백을 요청한다.
4. **리뷰 코멘트 반영**: 고친 내용을 같은 브랜치에 커밋·push하면 PR이 자동으로 갱신된다.
5. **병합(Merge)**: 승인되면 main에 합친다.
6. **브랜치 삭제**: 합쳐진 브랜치는 지운다.

공식 문서가 강조하는 원칙은 한 문장입니다. 브랜치를 만들면 기본 브랜치에 영향 없이 작업할 공간이 생기고, 변경은 브랜치를 병합할 때까지 기본 브랜치에 반영되지 않습니다.

### 3-2. 이 미션에서의 적용

| 구분 | 역할 | 규칙 |
| --- | --- | --- |
| `main` | 항상 깨지지 않는 상태 | 직접 push 금지, PR로만 병합 |
| `feature/*` | 작업 단위 브랜치 | Issue 1개 → 브랜치 1개 → PR 1개, 병합 후 삭제 |

미션의 "main 깨지지 않은 상태"는 도구적으로 정해 두어야 팀이 같은 말을 합니다. 현실적인 기준 예시입니다.

- 충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`)가 파일에 남아 있지 않다.
- Python 코드를 선택했다면 `python src/파일.py` 실행 또는 간단 예시가 오류 없이 동작한다.
- README의 팀원 목록/목차 링크가 깨지지 않는다.

### 3-3. GitHub Flow를 선택한 이유 3줄 (미션 필수 기록)

미션은 "선택 이유를 3줄 이내로 README.md 또는 docs/CONTRIBUTING.md에 기록"하라고 합니다. 아래는 초안 예시이고, 팀 말로 바꿔서 적으세요.

```markdown
- main과 feature/* 두 종류뿐이라 초보자 팀도 바로 외울 수 있다.
- 작업마다 브랜치를 나눠 main이 깨지지 않고, PR마다 리뷰 기록이 남는다.
- 팀 프로젝트가 짧고 배포 틀이 없어 develop/release 같은 추가 브랜치가 과하다.
```

비교용 배경지식입니다. Git Flow는 main 외에 develop, release, hotfix 같은 브랜치를 추가로 두는 더 무거운 방식이어서, 짧은 팀 프로젝트에는 GitHub Flow가 맞는다고 많이 설명합니다.

### 3-4. 브랜치 네이밍 규칙 (docs/CONTRIBUTING.md에 기록)

미션 예시는 `feature/<name>-<topic>` 형태입니다. 추천 규칙을 아래처럼 정해 보세요.

```text
feature/<영문소문자 이름>-<작업 요약>
예) feature/kim-math-utils
    feature/lee-string-utils
    feature/park-contributing
```

- 영문 소문자와 하이픈(`-`)만 쓴다. 한글은 Git이 허용하지만 터미널·도구에서 깨질 수 있어 피한다.
- 작업 요약은 단어 2\~3개로 짧고 구체적으로 쓴다.
- 시작에 Issue 번호를 넣으면 추적이 더 쉬워진다(선택, 예: `feature/12-kim-math-utils`).

직접 확인해 본 이름 규칙입니다.

- 공백, `:`, `?`, `..` 가 들어가면 "not a valid branch name" 오류가 난다.
- `feature`라는 브랜치가 있으면 `feature/kim-x`를 만들 수 없고, 반대도 마찬가지다(`cannot lock ref`). 더시 `feature/`는 폴더처럼 쓰이므로 `feature`라는 단독 브랜치는 만들지 말아야 한다.

### 3-5. 작업 한 사이클 명령어 요약

```bash
# 1) 최신 main에서 시작
git switch main
git pull

# 2) 브랜치 생성
git switch -c feature/kim-math-utils

# 3) 작업 → 커밋 (작은 단위로 자주)
git add src/math_utils.py
git commit -m "feat: add add() and subtract() to math utils"

# 4) 원격에 올리기 → GitHub에서 PR 생성
git push -u origin feature/kim-math-utils

# 5) 리뷰 반영: 같은 브랜치에 커밋하고 다시 push
git add src/math_utils.py
git commit -m "refactor: rename helper per review comment"
git push

# 6) 병합 후 정리
git switch main
git pull
git branch -d feature/kim-math-utils   # 로컬 브랜치 삭제
git fetch --prune                       # 원격에서 사라진 브랜치 참조 정리
```

원격 브랜치는 PR 화면의 **Delete branch** 버튼으로 지우면 됩니다. `git branch -d`는 이미 병합된 브랜치만 지우고, 병합되지 않았으면 오류를 내서 실수를 막아 줍니다.

### 3-6. 작업을 작게 나눠야 하는 이유

PR이 크면 리뷰하기 어렵고 충돌 가능성도 커집니다. GitHub 공식 문서도 서로 관련 없는 변경은 별도 브랜치로 나눠야 리뷰가 집중되고 한 변경이 지연되어도 다른 변경이 막히지 않는다고 설명합니다. 미션의 "PR 2개 이상"을 채우는 방법도 큰 작업 1개보다 **작은 작업 2개**를 각각 따로 만드는 것이 좋습니다.

> 미션 연결: GitHub Flow 적용, feature/\* 브랜치, 네이밍 규칙 문서화, 선택 이유 3줄, 과제 목표 2번(GitHub Flow 설명)을 다룹니다.

## 4. Issue, Pull Request, 코드 리뷰

이 장이 미션 점수의 중심입니다. 팀원별 최소 기준(PR 2개, 리뷰 2개, 리뷰 반영 1회)이 모두 여기서 나옵니다. 흐름은 **Issue 생성 → 브랜치 → PR(본문에 Closes #번호) → 리뷰 → 반영 → 병합 → 이슈 자동 닫힘**입니다.

### 4-1. Issue: 할 일을 기록하는 카드

Issue는 "무엇을 할지"를 적는 게시글입니다. 미션은 "각 작업은 Issue로 생성하고 PR과 연동"하라고 합니다. 그래서 **코드를 만들기 전에 Issue부터** 만듭니다.

- 위치: 저장소의 **Issues** 탭 → **New issue**
- 제목은 할 일이 한눈에 보이게: 예) `수학 유틸 함수 추가 (add, subtract)`
- 본문에 목표와 완료 조건을 적고, 오른쪽에서 **Assignees**에 내가 담당임을 지정합니다.
- 번호는 자동으로 붙습니다(#1, #2 ...). 이 번호가 PR의 `Closes #번호`에 쓰입니다.

```markdown
## 목적
- src/math_utils.py에 덧셈·빼기 함수를 추가한다.

## 완료 조건
- [ ] add(), subtract() 구현
- [ ] 사용 예시를 docstring에 포함
```

**Issue 분배 팁**: 팀원 수 × 2개 이상의 Issue를 만들어야 PR을 1인 2개씩 채울 수 있습니다(4명이면 8개). 문서 작업(CONTRIBUTING, 충돌 기록 등)도 Issue로 만들면 좋습니다.

### 4-2. Pull Request(PR) 만들기

PR은 "내 브랜치를 main에 합쳐 달라"는 요청서이자, 리뷰와 대화가 남는 기록입니다. 푸시한 직후 저장소 화면에 나타나는 **Compare & pull request** 버튼이나 저장소의 **Pull requests** 탭 → **New pull request**로 엽니다. base는 `main`, compare는 내 `feature/...` 브랜치여야 합니다.

**PR 본문 템플릿** (미션 필수: What / Why / How + 이슈 연결)

```markdown
제목: feat: add math utils

## 연결 이슈
- Closes #3

## 변경 사항(What)
- src/math_utils.py에 add(), subtract() 함수 추가

## 변경 이유(Why)
- 팀 유틸 함수 모음 결과물의 한 부분

## 테스트/검증(How)
- [x] python -c "from src.math_utils import add; print(add(1, 2))" → 3 확인
- [x] 충돌 마커(<<<<<<<)가 남아 있지 않음
```

저장소에 `.github/pull_request_template.md` 파일을 두면 새 PR 본문에 이 템플릿이 자동으로 채워지는 기능이 있습니다(선택, 한 명이 PR로 추가하면 편합니다).

### 4-3. Closes #번호가 동작하는 조건

GitHub 공식 문서("Linking a pull request to an issue")에서 확인한 내용입니다.

- 닫는 키워드는 `close, closes, closed, fix, fixes, fixed, resolve, resolves, resolved` 9개입니다. 대문자나 뒤에 콜론(:)을 붙여도 됩니다.
- 같은 저장소의 이슈는 `Closes #10` 형태로 씁니다.
- **기본 브랜치(main)에 병합될 때** 연결된 이슈가 자동으로 닫힙니다. PR이 다른 브랜치를 향하면 키워드는 무시되고 연결도 생기지 않습니다.
- 여러 이슈를 닫을 때는 각 이슈마다 키워드를 반복합니다. 예) `Closes #3, closes #4`
- 본문에 못 썼다면 PR 오른쪽 사이드바 **Development**에서 수동으로 연결할 수 있습니다(같은 저장소의 이슈, PR당 최대 10개).

미션이 "PR 본문에" 넣으라고 했으니 제목이 아니라 **본문에** 쓰세요. 병합 후 Issue가 Closed로 바뀌고 연결 PR이 표시되면 연동이 제대로 된 것입니다.

### 4-4. 코드 리뷰란 어떤 일인가

코드 리뷰는 다른 사람이 내 변경을 합치기 전에 읽어 보고 피드백하는 일입니다. 목적은 틀린 점 찾기뿐 아니라 세 가지입니다. ① 버그·리스크를 main에 들어오기 전에 잡는다, ② 팀이 내 코드를 이해하고 지식을 공유한다, ③ 스타일과 규칙을 맞춘다.

GitHub 공식 문서의 리뷰 유형 3가지입니다.

| 유형 | 뜻 |
| --- | --- |
| Comment | 승인이나 변경 요청 없이 일반 피드백만 남김 |
| Approve | 변경이 병합될 준비가 되었다는 승인 |
| Request changes | 병합 전에 작성자가 반드시 처리해야 할 피드백 |

**리뷰 하는 법**

1. PR 화면의 **Files changed** 탭을 열어 변경된 파일을 봅니다.
2. 코멘트를 달고 싶은 줄 왼쪽의 **+** 모양 버튼을 눌러 줄 단위 코멘트를 작성합니다.
3. 실질 코멘트를 남긴 뒤 **Review changes** → Comment / Approve / Request changes 중 선택하고 제출합니다.

PR 작성자는 **자기 PR을 스스로 승인할 수 없습니다**(GitHub 공식 문서: "Pull request authors cannot approve their own pull requests"). 보호 규칙의 승인 1명 요건은 반드시 다른 팀원의 Approve가 필요하다는 뜻입니다.

### 4-5. 리뷰 최소 품질 기준과 코멘트 예시

미션 기준은 "LGTM/좋아요"만으로는 안 되고, **특정 라인/파일을 근거로 한 질문, 대안 제안, 리스크 지적, 개선 제안 중 1개 이상**의 실질 코멘트가 PR마다 있어야 한다는 것입니다.

| 종류 | 좋은 예 | 나쁜 예 |
| --- | --- | --- |
| 질문 | "`math_utils.py` 12번 줄에서 b가 0일 때는 어떻게 되나요?" | "이거 맞나요?" |
| 대안 제안 | "`for` 문 대신 `sum()`을 쓰면 더 짧아질 것 같아요." | "다르게 해 보세요" |
| 리스크 지적 | "함수 이름이 `calc`인데 다른 팀원 함수와 이름이 곹칠 수 있어요." | "위험해 보여요" |
| 개선 제안 | "docstring에 사용 예시를 한 줄 넣어 주면 README와 연결되는 요구를 만족할 거 같아요." | "수정 필요" |
| 승인 | "리뷰해 보니 정상 동작합니다. 12번 줄만 질문 남긴 뒤 Approve할게요." | "LGTM" |

리뷰는 **코드에 대한 의견**이지 사람에 대한 평가가 아니라는 점을 기억하세요. "너"가 아니라 "이 코드"를 주어로 쓰면 팀 분위기가 편해집니다.

### 4-6. 리뷰 반영 증빙 만들기 (상호작용 1회 이상)

미션은 "리뷰어와 작성자 사이에 최소 1회 상호작용(답글/수정 반영)이 기록으로 남아야 한다"고 합니다. 작성자가 할 일은 이렇습니다.

1. 리뷰 코멘트에 **답글(Reply)** 로 수용하는지, 왜 다르게 할지 쓴다.
2. 수정하기로 했다면 같은 브랜치에 커밋하고 push한다(새 PR을 만들지 않아도 PR이 자동으로 갱신되는 것이 공식 문서의 4단계입니다).
3. 답글에 "반영했습니다. 커밋 `abc1234`"처럼 커밋 해시를 남긴다.
4. 수정에 만족하면 리뷰어가 승인하고, 대화에 **Resolve conversation**을 누른다.

커밋 메시지 예: `refactor: rename calc to add_numbers per review`. 이 커밋과 리뷰 코멘트 링크를 SUBMISSION.md에 함께 적어 두면 증빙이 완성됩니다.

### 4-7. 누가 누구를 리뷰할지 미리 정하기

팀원별 리뷰 2개를 빠짐없이 채우려면 순환 배정이 편합니다. 4명(A, B, C, D) 예시입니다. 각자 PR을 2개씩 만든다고 하고, 첨자 1은 첫 PR, 2는 두 번째 PR입니다.

| 리뷰어 | 1차 리뷰 | 2차 리뷰 |
| --- | --- | --- |
| A | B의 PR 1 | D의 PR 2 |
| B | C의 PR 1 | A의 PR 2 |
| C | D의 PR 1 | B의 PR 2 |
| D | A의 PR 1 | C의 PR 2 |

이렇게 하면 모두 서로 다른 팀원의 서로 다른 PR을 2개씩 리뷰하게 됩니다. 인원이 3명이면 A→B→C→A 순환이고, 5명이면 같은 방식으로 한 칸씩 밀면 됩니다. 미션 문구가 "리뷰 2개(본인 PR 제외)"이므로, 같은 PR에 두 번 남기기보다 **서로 다른 PR 2개**로 채우는 것이 안전합니다.

### 4-8. 병합 방식(Merge 버튼)

GitHub에서 PR을 합칠 때 병합 방식을 고를 수 있습니다. 미션의 git log --graph 예시("Merge pull request #8 from ...")처럼 **브랜치 분기와 합류가 그래프로 보이려면 "Create a merge commit"** 방식을 쓰는 것이 좋습니다. 다른 방식(Squash and merge, Rebase and merge)은 커밋을 한 줄로 합치거나 편평하게 이어 붙여서, 증빙용 그래프에서 협업 흔적이 덜 드러날 수 있습니다.

> 미션 연결: Issue 기반 작업·PR 연동(Closes #), PR 생성·병합 2개, 리뷰 2개, 리뷰 반영 1회, PR 본문 What/Why/How, 리뷰 최소 품질, 과제 목표 3번(PR과 코드 리뷰의 가치)을 다룹니다.

## 5. 커밋 메시지 컨벤션

커밋 메시지는 "미래의 팀원이 이 변경을 한 줄로 이해하게 해 주는 메모"입니다. 미션은 팀 규칙을 정해 CONTRIBUTING.md에 적고, 의미 없는 메시지를 금지합니다.

### 5-1. 권장 형식

```text
<type>: <subject>

(선택) 본문: 무엇을, 왜 바꿨는지 줄글로
```

미션이 예로 든 `feat: subject`, `fix: subject`, `docs: subject`, `refactor: subject` 형식이 위 형식입니다(업계에서 널리 쓰는 Conventional Commits를 따른 것). 타입은 팀이 정하면 됩니다. 추천 세트입니다.

| 타입 | 쓰는 경우 | 예 |
| --- | --- | --- |
| `feat` | 새 기능·새 파일의 내용 추가 | `feat: add math utils (add, subtract)` |
| `fix` | 오류·오타 수정 | `fix: handle zero division in divide()` |
| `docs` | 문서 작성·수정 | `docs: add branch naming rules to CONTRIBUTING` |
| `refactor` | 동작은 그대로, 구조·이름 개선 | `refactor: rename calc to add_numbers` |
| `test` | 테스트 추가·수정 | `test: add cases for subtract()` |
| `chore` | 설정·잡무 | `chore: add .gitignore for pycache` |

작성 요령입니다.

- subject는 "무엇을 했는지"를 적고 마지막에 마침표를 붙이지 않습니다. 영어면 동사 원형(add, fix, rename)로 시작합니다. 한글로 써도 되지만 팀이 하나로 통일하세요.
- 한 커밋에는 **한 가지 의도**만 담습니다. "함수 추가 + 문서 수정 + 오타 수정"이 한 커밋이면 분리합니다.
- 리뷰를 반영한 커밋은 미션 예시처럼 `feat: add string utils (apply review feedback)` 또는 `refactor: ... per review` 형태로 적으면 리뷰 반영 증빙이 됩니다.

### 5-2. 미션의 "의미없는 메시지" 판정 기준

미션은 아래 중 하나라도 해당하면 의미 없는 메시지로 간주한다고 합니다.

1. 변경 대상을 유추할 수 없는 **단어만** 있는 경우: `update`, `fix`, `temp`, `wip`, `final` 등
2. 무엇을/왜 바꿨는지 드러나지 않는 경우: `bug fix`, `edit file` 등(구체 대상·효과 없음)

판정 예시입니다.

| 메시지 | 판정 | 이유 |
| --- | --- | --- |
| `update` | 금지 | 단어뿐, 무엇을 바꾼지 모름 |
| `fix` | 금지 | 단어뿐 |
| `wip`, `temp`, `final` | 금지 | 단어뿐 |
| `bug fix` | 금지 | 어떤 버그인지 대상이 없음 |
| `edit file` | 금지 | 어느 파일을 어떻게 바꾼지 없음 |
| `fix: handle zero division in divide()` | 허용 | 대상(divide)과 효과(0으로 나눔 처리)가 보임 |
| `docs: add CONTRIBUTING.md` | 허용 | 무엇을 추가했는지 보임 |

참고로 `fix` 또는 `update`라는 **단어 자체**가 아니라 "단어만 있는 경우"가 문제입니다. `fix: 대상과 효과` 형태는 아무 문제 없습니다.

### 5-3. 자동으로 생기는 메시지는?

- GitHub에서 PR을 병합할 때 자동으로 생기는 `Merge pull request #8 from ...`는 미션 결과 예시에도 나오는 형태라 그대로 두면 됩니다.
- `git revert`가 만드는 `Revert "..."` 메시지도 원래 커밋 제목이 들어 있어 의미가 있습니다(직접 확인했습니다).
- 충돌을 해결하고 만드는 병합 커밋은 직접 쓰는 것이므로 `fix: resolve team name conflict by combining Alpha and Beta`처럼 의미 있게 적습니다.

### 5-4. 실수로 잘못 쓴 메시지 고치기

아직 push하지 않은 **바로 앞 커밋**이면 `git commit --amend -m "새 메시지"`로 고칠 수 있습니다(7-2 참고). 이미 push했다면 히스토리를 고치지 말고 보통은 그대로 두고 다음부터 잘 쓰는 편이 안전합니다. 이는 미션의 "공유 브랜치 히스토리 재작성 금지"와 연결됩니다.

### 5-5. 팀 전체 커밋 한 번에 점검하기 (선택)

제출 전에 팀원 커밋에 의미 없는 메시지가 섭여 있지 않은지 확인하는 간단한 Python 스크립트입니다. 실제로 실행해 미션 금지 예시(`temp`, `wip 1`)는 NG, `Revert "..."`와 `feat: ...`는 OK로 나오는 것을 확인했습니다. 이 스크립트는 어디까지나 보조 도구이고, 최종 판단은 팀의 규칙에 따릅니다.

```python
"""커밋 메시지 점검 스크립트 (팀 컨벤션 검사용)
사용: python check_commits.py [범위]   예) python check_commits.py origin/main..HEAD
"""
import re
import subprocess
import sys

BANNED = {"update", "fix", "temp", "tmp", "wip", "final", "edit", "edit file", "bug fix"}
PATTERN = re.compile(r"^(feat|fix|docs|refactor|test|chore|style)(\([\w\-/]+\))?: \S.{4,}$")
REVERT = re.compile(r'^Revert ".+"$')  # git revert 가 자동으로 만드는 메시지는 허용


def main():
    rev = sys.argv[1] if len(sys.argv) > 1 else "HEAD"
    out = subprocess.run(
        ["git", "log", "--no-merges", "--format=%h%x09%s", rev],
        capture_output=True, text=True, check=True,
    ).stdout
    bad = 0
    for line in out.splitlines():
        short_hash, subject = line.split("\t", 1)
        is_ok = PATTERN.match(subject) or REVERT.match(subject)
        if subject.strip().lower() in BANNED or not is_ok:
            print(f"[NG] {short_hash} {subject}")
            bad += 1
        else:
            print(f"[OK] {short_hash} {subject}")
    print(f"\n문제 커밋 {bad}개")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
```

이 스크립트를 `src/`의 유틸 함수 결과물로 제출할 수도 있지만, 그러면 각 팀원이 함수 1개 이상을 더 추가해야 한다는 점을 기억하세요(9장).

> 미션 연결: 커밋 메시지 규칙의 CONTRIBUTING.md 문서화, 의미없는 메시지 금지(판정 기준) 요구사항을 다룹니다.

## 6. 충돌(Conflict) 이해와 해결 실습

충돌은 오류가 아니라 **"사람이 결정해야 할 일을 Git이 알려 주는 신호"**입니다. 먼저 왜 생기는지 이해하고, 그다음 팀에서 직접 만들어 해결하고 기록을 남깁니다.

### 6-1. 왜 충돌이 생기는가

Git은 두 브랜치를 합칠 때, 같은 갈래에서 갑자기 다르게 변한 부분을 비교해 자동으로 합칩니다. 서로 **다른 부분**을 고친 경우는 자동으로 합치지만, **같은 부분(일부 줄)을 서로 다르게** 고친 경우에는 어느 쪽이 맞는지 판단할 수 없어 멈추고 사람에게 맡깁니다. 이 상태가 충돌입니다.

### 6-2. 충돌 마커 읽는 법

직접 만들어 본 충돌의 실제 출력입니다. 두 팀원이 team.txt의 같은 줄 `TEAM: unknown`을 서로 다르게 고쏘습니다.

```text
$ git merge feature/lee-team
Auto-merging team.txt
CONFLICT (content): Merge conflict in team.txt
Automatic merge failed; fix conflicts and then commit the result.

$ git status -sb
## main
UU team.txt

$ cat team.txt
line1
<<<<<<< HEAD
TEAM: Alpha
=======
TEAM: Beta
>>>>>>> feature/lee-team
line3
```

마커 3종의 의미는 다음과 같습니다.

| 마커 | 의미 |
| --- | --- |
| `<<<<<<< HEAD` | 여기서 부터 "현재 브랜치(지금 내가 있는 쪽, HEAD)"의 내용 시작 |
| `=======` | 두 내용의 경계선 |
| `>>>>>>> feature/lee-team` | 여기까지가 합치려는 브랜치(feature/lee-team)의 내용 끝 |

`git status`에서 `UU`는 양쪽이 모두 수정한(Unmerged) 파일이라는 표시입니다. 중요한 점은 **마커가 들어 있는 파일은 아직 완성본이 아니라는 것**입니다. 마커를 지우지 않고 커밋하면 파일에 이상한 줄들이 그대로 남아 main이 깨집니다.

**주의: 리베이스에서는 반대입니다.** 리베이스로 합할 때는 `HEAD` 쪽이 "내가 옮겨 붙이려는 대상(main)의 내용", 마지막 쪽이 "내 커밋의 내용"으로 표시됩니다(직접 확인). 헷갈리면 마커 아래 커밋 해시·브랜치 이름을 보고 판단하세요.

### 6-3. 해결 절차 (병합으로 해결하는 기본형)

1. **상태 확인**: `git status`로 충돌 파일(`UU`)을 찾습니다. `git diff --name-only --diff-filter=U`로 충돌 파일만 모아 볼 수도 있습니다.
2. **파일 열기**: 마커 사이 두 내용을 읽고 무엇이 맞는지 팀원과 의논합니다.
3. **전략 선택**: 한쪽만 채택(choose one), 둘 다 유지(keep both), 새로 고쳐 쓰기(refactor) 중 하나를 고릅니다.
4. **마커 3종 줄을 모두 삭제**하고 최종 내용만 남깁니다.
5. **스테이징**: `git add <파일>`
6. **커밋**: `git commit -m "fix: resolve team name conflict by combining Alpha and Beta"` (병합 커밋이 만들어집니다)
7. **검증**: 파일을 실행·확인하고 `grep -rn "<<<<<<<" .`로 마커가 남아 있지 않은지 확인합니다.
8. **push 및 기록**: `git push` 후 docs/conflict-resolution.md에 적습니다(8장).

도중에 포기하고 처음 상태로 되돌리고 싶다면 `git merge --abort`를 씁니다(실제로 실행해 병합 이전 상태로 돌아가는 것을 확인). 리베이스 중이면 `git rebase --abort`입니다.

### 6-4. PR에서 충돌이 나면 어떻게 하나

PR을 열었는데 다른 팀원의 PR이 먼저 main에 병합된 경우에 충돌이 생기기 쉽습니다. 팀 규칙으로 아래 흐름을 추천합니다. 모두 직접 실행해 본 순서입니다.

```bash
git switch feature/kim-x          # 충돌이 난 내 브랜치로
git fetch                        # 원격 최신 정보 받기
git merge origin/main             # main을 내 브랜치에 합치기 → 충돌 발생
# (파일을 열어 마커 해결 → git add → git commit)
git push                          # 같은 브랜치에 push → PR이 자동으로 갱신
```

이 방법은 push가 일반 push로 끝나 강제 푸시가 필요 없습니다(확인함). 반면 내 feature 브랜치를 main 위로 **rebase**하고 이미 push한 브랜치를 올리려면 강제 푸시가 필요해질 수 있어, 미션의 "팀 합의 없는 강제 푸시/리베이스 금지"와 충돌할 수 있습니다. 초보자 팀은 **merge로 해결**하는 것을 규칙으로 정하세요.

GitHub PR 화면의 "This branch has conflicts that must be resolved" 안내 아래에는 브라우저에서 해결하는 버튼도 있습니다. 간단한 충돌에는 편하지만, 미션은 터미널에서의 해결 과정을 재현 가능하게 기록하라는 목적이므로 초보자가 배우는 용도라면 명령어 방식을 권합니다.

### 6-5. 비자명 충돌이란 무엇인가

미션은 최소 1회는 "비자명 충돌"을 요구하고, 아래 둘 중 하나를 충족하라고 합니다.

- (옵션 1) 같은 파일의 같은 hunk(인접 라인)를 서로 다르게 수정해 충돌
- (옵션 2) 한쪽은 파일 이동/이름 변경(또는 삭제), 다른 쪽은 내용 수정

이 두 옵션이 실제로 Git에서 어떻게 동작하는지 하나씩 실험해 본 결과입니다. 이 차이를 모르면 "충돌을 만들려고 했는데 안 난다"는 상황이 생깁니다.

| 실험 | 결과 | 여부 |
| --- | --- | --- |
| 한 쪽이 2번째 줄, 다른 쪽이 **3번째 줄**(인접) 수정 | `CONFLICT (content)` 발생 | 충돌 성공 |
| 한 쪽이 2번째 줄, 다른 쪽이 **4번째 줄**(한 줄 띄움) 수정 | 자동 병합 성공 | 충돌 없음 |
| 한 쪽은 파일을 `src/`로 **이름 변경**, 다른 쪽은 내용 수정 | 병합·리베이스 모두 **자동 성공**(수정이 이동된 파일에 적용됨) | 충돌 없음 |
| 한 쪽은 파일 **삭제**, 다른 쪽은 내용 수정 | `CONFLICT (modify/delete)` 발생, `git status`에는 `DU` | 충돌 성공 |

즉 **이름 변경 + 내용 수정은 충돌이 나지 않아서** 그것만으로는 "충돌 해결 기록"이 안 만들어집니다. 사실 Git이 이름 변경을 따라가서 자동으로 합쳐 주는 좋은 기능입니다. 미션이 말하는 "충돌 또는 리베이스/병합 시 이슈 유발"이 이 경우를 포함하는 표현일 수 있으나, **안전한 방법은 옵션 1(인접 줄 충돌)이거나 옵션 2를 쓸 때 삭제 vs 수정 충돌**입니다. 리뷰어에게 "충돌 마커 화면"을 보여 줄 수 있어야 하기 때문입니다.

삭제 vs 수정 충돌은 해결법이 약간 다릅니다.

```bash
# 실제 출력
# CONFLICT (modify/delete): util.py deleted in HEAD and modified in feature/edit.
#                          Version feature/edit of util.py left in tree.
# git status -sb → DU util.py

git add util.py     # 수정된 파일을 살리기로 결정한 경우
git rm util.py      # 삭제를 따르기로 결정한 경우
git commit -m "fix: resolve util.py delete/modify conflict by keeping the edited file"
```

### 6-6. 팀 충돌 실습 레시피 (미션: 팀 전체 2회 이상, 비자명 1회 이상)

아래 레시피대로 하면 두 경우가 모두 기록됩니다. 다만 충돌을 일부러 만드는 행위가 미션 목적이므로 자연스럽게 해도 됩니다.

**레시피 A (일반 충돌, 같은 줄)**: A와 B가 같은 파일(예: `team/README.md` 또는 `src/shared.py`)의 같은 줄을 각자 다른 내용으로 수정하고 각자 브랜치로 PR을 엽니다. 먼저 병합된 PR 때문에 다른 PR이 충돌을 겪습니다.

**레시피 B (비자명 충돌, 인접 줄)**: C와 D가 때로는 같은 파일의 **바로 위아래 줄**을 수정해 충돌을 만듭니다. 한 줄 띄우면 충돌이 안 난다는 점을 위 표로 미리 알았으므로 꼭 붙어 있는 줄로 합니다.

**레시피 C (비자명 충돌, 삭제 vs 수정)**: 한 명이 파일을 삭제하는 PR, 다른 명이 그 파일을 수정하는 PR을 열고 삭제쪽을 먼저 병합한 뒤, 수정쪽이 `git merge origin/main`을 합니다.

공통 규칙입니다.

- 충돌을 겪은 본인이 해결하고, 상대방과 어느 쪽을 쓸지 대화합니다(미션 템플릿의 "작성자/상대").
- 충돌 마커 화면을 클립보드에 남겨 복사해 두고 다른 해결 단계를 바로 기록합니다(해결하고 나면 마커가 사라지므로).
- 해결 커밋/PR 링크를 함께 적습니다.

> 미션 연결: 충돌 해결 실습(팀 2회 이상, 비자명 1회 이상), 충돌 마커 의미 설명(과제 목표 4번), 재현 가능한 기록 제약을 다룹니다.

## 7. 되돌리기 4종: amend, reset --soft, revert, stash

미션의 트러블슈팅 실습 4가지입니다. 핵심 판단 기준은 단 하나, **"그 커밋을 이미 팀원들이 볼 수 있는 원격(GitHub)에 올렸는가"**입니다. 올리기 전이면 내 로컬에서 마음껏 고치면 되고, 올린 뒤에는 히스토리를 고치지 말고 "되돌리는 새 커밋"을 추가해야 합니다.

### 7-0. 한 눈에 비교

| 명령 | 하는 일 | 커밋 히스토리 | push 이후 사용 | 언제 쓰나 |
| --- | --- | --- | --- | --- |
| `git commit --amend` | 가장 최근 커밋 1개를 고침(메시지·내용) | 커밋을 **새로 만들어 교체**(해시가 바뀔) | 비추천(강제 푸시 필요) | 아직 push 안 한 최근 커밋의 오타·누락 파일 |
| `git reset --soft HEAD~1` | 최근 커밋을 취소하되 **변경 내용은 스테이징 상태로 유지** | 커밋이 사라짐 | 비추천 | push 안 한 커밋을 재구성(나눠 다시 커밋 등) |
| `git revert <해시>` | 특정 커밋의 변경을 **정반대로 되돌리는 새 커밋 추가** | 기존 히스토리는 그대로, 끝에 커밋 추가 | **안전(일반 push)** | 이미 push한 커밋을 취소 |
| `git stash` / `git stash pop` | 커밋하지 않은 작업을 잠시 치워 두고 나중에 다시 꺼냄 | 커밋 히스토리에 영향 없음 | 해당 없음(로컬 작업) | 브랜치를 급히 옮겨야 하는데 작업이 덜 끝났을 때 |

### 7-1. git commit --amend: 바로 앞 커밋 고치기

커밋 메시지에 오타가 났거나, 파일 하나를 빼먹고 커밋했을 때 씁니다. 실제 실행 결과입니다.

```text
$ git commit -m "updte f"          # 오타 메시지
$ git log --oneline -1
3f860d3 updte f

$ git commit --amend -m "feat: add f.txt with initial value"
$ git log --oneline -2
29fc697 feat: add f.txt with initial value    # 해시가 3f860d3 → 29fc697 로 바뀜
34f01f7 feat: add app.py
```

해시가 바뀐 것이 핵심입니다. amend는 수정하는 것처럼 보여도 실제로는 **커밋을 새로 만들어 예전 것을 대체**합니다.

- 누락된 파일 추가: `git add f2.txt` → `git commit --amend --no-edit` (메시지는 그대로, 파일만 추가. 실제로 확인했습니다.)
- **push 이후에 amend하면** 원격에는 예전 커밋, 로컬에는 새 커밋이 있어 서로 갈라집니다. 그때 `git push`를 하면 실제로 다음과 같이 거부됩니다.

```text
 ! [rejected]  feature/kim-amend -> feature/kim-amend (non-fast-forward)
hint: Updates were rejected because the tip of your current branch is behind
```

이때 강제 푸시(`git push --force`)로 덮어쓰면 되지만, 미션이 "팀 합의 없는 강제 푸시"를 금지합니다. 그러니 amend는 **push 전에만** 쓰는 버릇을 들이세요.

### 7-2. git reset: 커밋을 취소하는 세 가지 강도

`reset`은 "브랜치가 가리키는 커밋을 뒤로 되감는" 명령입니다(1장의 포인터 개념). **되감은 뒤 변경 내용을 어디까지 남길지**가 옵션으로 나뉘며, 서로 다른 결과를 직접 확인했습니다.

| 옵션 | 커밋 | 스테이징 | 파일(작업 폴더) | 실제 확인 결과 |
| --- | --- | --- | --- | --- |
| `--soft HEAD~1` | 취소 | **유지** | 유지 | `git status -s` → `A  g.txt` (커밋 직전 상태) |
| `--mixed HEAD~1`(기본) | 취소 | 해제 | 유지 | `?? g.txt` (add 이전 상태) |
| `--hard HEAD~1` | 취소 | 해제 | **삭제** | g.txt 파일 자체가 사라짐 |

미션은 `git reset --soft HEAD~1`만 요구합니다. 실제 출력입니다.

```text
$ git log --oneline -3
bd4a9e2 feat: add g.txt
29fc697 feat: add f.txt with initial value
34f01f7 feat: add app.py

$ git reset --soft HEAD~1
$ git log --oneline -3
29fc697 feat: add f.txt with initial value    # bd4a9e2 커밋이 사라짐
34f01f7 feat: add app.py
$ git status -s
A  g.txt                                      # 변경은 스테이징 상태로 남아 있음
```

`HEAD~1`은 "현재에서 한 커밋 앞"입니다. `HEAD~2`면 두 커밋 앞입니다. `--hard`는 커밋하지 않은 작업도 함께 지우므로 가장 조심해야 합니다.

**실수로 `--hard`를 썼을 때 구조하는 법**: 커밋된 내용이었다면 `git reflog`에 기록이 남아 있어 복구할 수 있습니다(직접 확인).

```bash
git reflog -3                 # 사라진 커밋의 해시를 찾는다 (예: 72f69dd HEAD@{1}: commit: feat: add g.txt)
git reset --hard 72f69dd      # 그 커밋으로 되돌리기
```

다만 커밋조차 하지 않았던 변경은 복구할 수 없으므로, `--hard` 전에는 반드시 `git status`로 확인하세요.

reset도 amend와 같은 이유로 **push 이후에는 쓰지 않는 것**이 원칙입니다. 원격에 이미 있는 커밋을 로컬에서만 지우면 두 저장소의 히스토리가 갈라집니다.

### 7-3. git revert: 이미 push한 커밋 취소하기

`revert`는 "지우는" 것이 아니라 **그 커밋의 변경을 반대로 되돌리는 새 커밋을 하나 더 쌓는** 것입니다. 그래서 원격에 올려도 일반 push로 끝납니다(강제 푸시 불필요, 직접 확인). 실제 출력입니다.

```text
$ git log --oneline -3
2ecaea0 feat: add risky line to app.py
34f01f7 feat: add app.py

$ git revert --no-edit HEAD
[main 01d7377] Revert "feat: add risky line to app.py"

$ git log --oneline -4
01d7377 Revert "feat: add risky line to app.py"     # 새 커밋이 위에 쌓임
2ecaea0 feat: add risky line to app.py              # 원래 커밋은 남아 있음
34f01f7 feat: add app.py

$ git push        # 정상 push 성공
```

기록이 모두 남는 것이 장점입니다. 누가 언제 무엇을 또 되돌렸는지 팀이 알 수 있습니다. `git revert --no-edit`는 자동 메시지를 그대로 쓰는 옵션이고, 메시지를 수정하려면 옵션 없이 실행해 에디터에서 바꾸면 됩니다.

**중요: PR로 병합된 커밋(merge commit)을 revert할 때는 `-m 1`이 필요합니다.** 병합 커밋은 부모가 둘이라 어느 쪽을 기준으로 되돌릴지 지정해야 하기 때문입니다. 직접 확인한 결과입니다.

```text
$ git revert --no-edit aa871bf
error: commit aa871bf is a merge but no -m option was given.
fatal: revert failed

$ git revert --no-edit -m 1 aa871bf       # 1번 부모(= main 쪽)을 기준으로 되돌림
[main bb5e283] Revert "Merge pull request #1 from feature/m1"
```

**main이 보호되어 있으니** 로컬 main에서 revert해 바로 push할 수 없습니다. 실제 팀 작업에서는 `feature/...-revert` 브랜치를 만들어 거기서 revert하고, PR로 main에 올리는 것이 정석입니다.

### 7-4. git stash: 작업을 잠시 치워 두기

커밋하기에는 이른 작업 중에 다른 브랜치로 급히 가야 할 때 씁니다. 변경을 임시 보관함에 넣어 두고 작업 폴더를 깨끗하게 만듭니다.

```bash
git stash push -m "wip: half done"   # 보관 (-m 으로 이름을 달아 두면 나중에 구분 쉽다)
git stash list                        # stash@{0}: On feature/kim-stash: wip: half done
git switch main                       # 자유롭게 브랜치 이동
# ... 다른 일 ...
git switch feature/kim-stash
git stash pop                        # 꺼내서 적용하고, 보관함에서는 삭제함
```

실제로 확인한 중요한 사실들입니다.

- stash 후 `git status`가 깨끗해지고, `git stash pop` 후에는 stash 목록이 0개가 됩니다.
- `git stash apply`는 꺼내서 적용하되 stash를 **보관함에 남겨 둡니다**(남아 있는 것 확인). 필요 없으면 `git stash drop`으로 지웁니다.
- 기본 `git stash`는 **새로 만든(untracked) 파일은 보관하지 않습니다.** 변경이 새 파일뿐이면 `No local changes to save`라고 나옵니다. 새 파일까지 넣으려면 `git stash push -u`를 씁니다.
- `git stash show -p stash@{0}`로 보관한 변경 내용을 미리 볼 수 있습니다.
- 보관하지 않고 브랜치를 옮기려 하면, 두 브랜치에서 내용이 다른 파일을 고친 상태일 때 Git이 다음 오류로 막아 줍니다.

```text
error: Your local changes to the following files would be overwritten by checkout:
	app.py
Please commit your changes or stash them before you switch branches.
Aborting
```

이 오류를 만나면 "커밋하거나 stash 하라"는 뜻이므로 바로 위 stash 절차를 쓰면 됩니다.

### 7-5. 어떤 걸 써야 할까: 질문 흐름

1. **변경을 커밋하지 않았다** → `git stash`(잠시 보관) 또는 파일 복구(`git restore <파일>`).
2. **커밋했지만 push는 안 했다**
   - 메시지·파일 하나만 고치면 된다 → `git commit --amend`
   - 커밋을 취소하고 내용을 다시 나눠 담고 싶다 → `git reset --soft HEAD~1`
3. **이미 push했다** → `git revert <해시>` (병합 커밋이면 `-m 1`)

이 흐름이 미션의 "reset, revert, stash의 차이와 언제 사용하는지 설명"(과제 목표 5번)의 핵심 답입니다.

### 7-6. 실습 시나리오 4종 (팀 전체 수행, 팀원마다 최소 1개 기록 참여)

미션은 4개 시나리오를 팀 전체가 모두 수행해 docs/troubleshooting-log.md에 남기라고 하고, **각 팀원이 최소 1개 시나리오 기록 작성에 참여**해야 한다고 합니다(이름·역할이 문서에 드러나야 함). 4명 팀이면 시나리오 1개당 담당 1명 + 도우미 1명으로 나눠 맡으면 자연스럽게 전원이 참여합니다. 연습은 연습용 브랜치에서 하고 **터미널 출력을 복사해 기록**에 붙이면 "재현 가능한 기록"이 됩니다.

**시나리오 1. amend** (오타가 난 최근 커밋 메시지 수정)

```bash
git switch -c feature/<이름>-lab-amend
echo "amend practice" > docs/lab-amend.md
git add docs/lab-amend.md
git commit -m "docs: ad amend practice note"       # 일부러 오타
git log --oneline -1                               # 해시 기록해 둔다
git commit --amend -m "docs: add amend practice note"
git log --oneline -1                               # 해시가 바뀐 것을 확인
```

기록할 것: 수정 전·후 해시 비교, "push 전에만 써야 하는 이유".

**시나리오 2. reset --soft** (두 작업이 섞여 커밋된 것 나눠서 다시 커밋)

```bash
git switch -c feature/<이름>-lab-reset
echo "A" > docs/lab-a.md && echo "B" > docs/lab-b.md
git add docs/lab-a.md docs/lab-b.md
git commit -m "docs: add lab notes a and b"        # 두 파일이 한 커밋에 섞임
git reset --soft HEAD~1                            # 커밋만 취소, 변경은 스테이징 상태로 유지
git status -s                                      # A  docs/lab-a.md, A  docs/lab-b.md
git restore --staged docs/lab-b.md                 # b만 스테이징에서 빼기
git commit -m "docs: add lab note a"
git add docs/lab-b.md && git commit -m "docs: add lab note b"
```

기록할 것: reset 전·후 `git log --oneline`과 `git status -s`, soft/mixed/hard의 차이.

**시나리오 3. revert** (이미 push한 잘못된 커밋 취소)

```bash
git switch -c feature/<이름>-lab-revert
echo "bad line" > docs/lab-bad.md
git add docs/lab-bad.md && git commit -m "docs: add lab bad line"
git push -u origin feature/<이름>-lab-revert      # 이미 push했다고 가정
git revert --no-edit HEAD                          # 되돌리는 새 커밋 생성
git push                                           # 강제 푸시 없이 성공
git log --oneline -3
```

기록할 것: reset 대신 revert를 선택한 이유(원격 히스토리 보존), 병합 커밋이면 `-m 1`이 필요하다는 점.

**시나리오 4. stash / stash pop** (작업 중 브랜치 전환)

```bash
git switch -c feature/<이름>-lab-stash
echo "draft" >> README.md                          # 커밋하지 않은 작업 중 변경
git stash push -m "wip: readme draft"
git status -sb                                     # 깨끗해진 것 확인
git switch main
git switch feature/<이름>-lab-stash
git stash pop                                      # 복구
git stash list                                     # 비어 있음 확인
```

기록할 것: stash 목록 출력, pop과 apply의 차이, 새 파일은 `-u`가 필요하다는 점.

연습용 브랜치와 파일은 PR로 main에 병합할 필요가 없습니다(남기지 않아도 되는 연습이므로 기록문서에 결과만 남기면 됩니다). 다만 연습이 절차적으로 추적되어야 하면 팀 합의로 연습용 브랜치를 원격에 남겨 두어도 좋습니다.

### 7-7. 초보자가 자주 겪는 상황: main에 실수로 커밋했다

로컬 main에 저도 모르게 커밋해 버렸다면(보호 규칙 때문에 push는 막히고 "ahead 1"만 보입니다) 다음 순서로 구조합니다. 직접 실행해 본 절차입니다.

```bash
git status -sb                  # ## main...origin/main [ahead 1] → 실수 확인
git branch feature/kim-oops     # 1) 지금 커밋을 새 브랜치로 보존 (이름표만 붙이는 것)
git reset --hard origin/main    # 2) main을 원격 main 상태로 되돌림
git switch feature/kim-oops     # 3) 커밋이 살아 있는 새 브랜치로 이동 → 거기서 push, PR
```

1번을 빼먹고 2번부터 하면 커밋을 잃을 수 있으므로(물론 reflog로 구조 가능) **반드시 1번이 먼저**입니다.

> 미션 연결: 트러블슈팅 4종(amend, reset --soft, revert, stash/pop), 팀원별 1개 이상 기록 참여, 과제 목표 5번(reset, revert, stash의 차이와 사용 시점), 운영 안정성 제약(강제 푸시 금지)을 다룹니다.

## 8. 협업 문서 3종과 SUBMISSION.md 작성법

미션은 코드보다 **기록**을 봅니다. 문서 4개를 빈틈없이 채우는 것이 평가의 큰 부분입니다. 아래에서는 협업 문서 3종의 작성 요령과 SUBMISSION.md 템플릿을 안내합니다. 예시 문구가 있다면 팀의 실제 내용으로 바꾸어 쓰세요.

### 8-1. 문서 나눠 쓰는 법 (PR 한 개도 함께 채우기)

미션은 CONTRIBUTING.md를 "팀원이 분담하여 작성"하라고 합니다. 이것을 그대로 활용하면 문서도 쓰고 PR 기준도 채울 수 있습니다.

| 담당 | 작업 예시 (Issue 1개 → PR 1개) |
| --- | --- |
| 팀원 1 | CONTRIBUTING: 브랜치 전략·네이밍 + 선택 이유 3줄 |
| 팀원 2 | CONTRIBUTING: 커밋 컨벤션 |
| 팀원 3 | CONTRIBUTING: PR 규칙 + 코드 리뷰 규칙 |
| 팀원 4 | CONTRIBUTING: 충돌 대응 흐름 |
| 팀 전원 | conflict-resolution.md, troubleshooting-log.md는 실습한 사람이 자기 기록을 작성 |

같은 파일(CONTRIBUTING.md)을 여러 명이 동시에 고치면 자연스럽게 충돌이 나서, 6장 충돌 실습의 재료가 되기도 합니다. 다만 처음부터 서로 다른 절(섹션)을 맡도록 작업을 나눠야, 이를 실습이 아닌 실제 협업으로 만들 수 있습니다.



### 8-2. docs/CONTRIBUTING.md 작성

팀의 협업 규칙을 정리하는 문서입니다.

- [CONTRIBUTING.md](../CONTRIBUTING.md)

다음 항목이 포함되어 있는지 확인합니다.

- 브랜치 전략과 브랜치 네이밍 규칙
- 커밋 메시지 컨벤션
- Issue 및 PR 작성 규칙
- 코드 리뷰 규칙
- 충돌 발생 시 대응 흐름

팀원들이 함께 사용할 규칙이므로 실제 팀의 합의 내용을 작성해야 합니다.

### 8-3. docs/conflict-resolution.md 작성

Git 충돌이 발생했을 때 상황과 해결 과정을 기록하는 문서입니다.

- [conflict-resolution.md](../conflict-resolution.md)

충돌을 해결한 뒤 다음 내용을 기록합니다.

- 충돌에 참여한 사람과 작업 브랜치
- 충돌이 발생한 파일과 원인
- 충돌 해결에 사용한 명령어와 절차
- 최종 해결 방법과 결과
- 충돌을 통해 배운 점

실제로 발생한 충돌을 바탕으로 작성하고, 예시가 아닌 본인 팀의 기록을 남깁니다.

### 8-4. docs/troubleshooting-log.md 작성

Git 실습 중 발생한 문제와 해결 과정을 기록하는 문서입니다.

- [troubleshooting-log.md](../troubleshooting-log.md)

각 실습 기록에는 다음 내용을 포함합니다.

- 실습 시나리오와 참여자
- 발생한 상황과 문제
- 사용한 명령어 및 실행 절차
- 실행 결과와 주의사항
- 해당 방법을 선택한 이유

미션에서 요구하는 `commit --amend`, `reset --soft`, `revert`, `stash` 등의 실습 결과를 실제 터미널 기록과 함께 작성합니다.


### 8-5. SUBMISSION.md (제출물 인덱스) 템플릿

미션은 "팀원별로 내가 만든 Issue/PR를 빠르게 확인"할 수 있어야 한다고 합니다. 평가자가 이 한 페이지만 보고 모든 증빙을 클릭해 확인한다고 생각하고 쓰세요. 사람별 표로 만들면 누락이 한눈에 보입니다.

```markdown
# Submission Index

## Team
- 팀명: <팀 이름>
- 저장소: <repo_url>
- 선택한 간단한 결과물: (A) 유틸 함수 모음 / (B) 팀 소개 / (C) 학습 노트 중 1개

## Member Contributions

### <이름 1>
| 항목 | 링크 |
| --- | --- |
| 내가 만든 Issue | #3, #7 |
| 내가 만든 PR (병합 2개 이상) | <PR url>, <PR url> |
| 내가 쓴 코드 리뷰 (2개 이상, 본인 PR 제외) | <review url>, <review url> |
| 리뷰 반영 증빙 (1회 이상) | <리뷰 코멘트 url> → <반영 커밋 url> |
| 트러블슈팅 시나리오 참여 | amend (담당), revert (도우미) |
| 결과물 기여 커밋 | <commit url> |

### <이름 2>
(동일 표)

## Key Docs
- Contributing: docs/CONTRIBUTING.md
- Conflict log: docs/conflict-resolution.md
- Troubleshooting: docs/troubleshooting-log.md

## Team-level Evidence
- Branch Protection 설정 화면: <screenshot url>
- 충돌 해결 기록 2회 이상 (비자명 1회 이상): docs/conflict-resolution.md
- git log --oneline --graph --all 결과: docs/git-log.txt (아래 명령으로 생성)
```

### 8-6. git log 증빙 만들기

미션은 `git log --oneline --graph --all` 결과를 텍스트 또는 스크린샷으로 제출하라고 합니다. 모든 PR이 병합된 **마지막 시점에** 아래 순서로 만듭니다.

```bash
git switch main
git pull                                   # main을 최신으로
git fetch --all --prune                   # 모든 원격 브랜치 정보를 최신으로
git log --oneline --graph --all > docs/git-log.txt
```

그래프가 깨지지 않게 터미널 폭을 넓히고 확인하세요. 이 파일도 main에 들어가려면 PR이 필요하므로, 마지막 PR이 정리된 뒤 증빙 전용 PR을 하나 더 열면 됩니다. 그 PR 자체는 로그에 포함되지 않지만(로그를 만든 뒤에 생기는 커밋이므로), 미션이 요구하는 것은 협업 과정의 증빙이므로 큰 문제가 아닙니다. 확실하게 하려면 스크린샷을 함께 보관하세요.

> 미션 연결: CONTRIBUTING.md·conflict-resolution.md·troubleshooting-log.md·SUBMISSION.md 작성, git log 증빙, 키워드 "팀원별 PR/리뷰/시나리오 참여" 증빙을 다룹니다.

## 9. 간단한 결과물 선택과 팀원별 최소 기준 체크리스트

결과물은 **협업 연습을 위한 재료**일 뿐입니다. 미션 원문도 "복잡한 기능 구현이 목적이 아니다"라고 명시합니다. 팀에서 가장 빨리 합의할 수 있는 것을 고르고, 시간을 협업 기록에 쓰세요.

### 9-1. 세 가지 옵션 비교

| 옵션 | 미션 최소 완성 기준 | 하기 쉬운 점 | 주의 |
| --- | --- | --- | --- |
| (A) 유틸 함수 모음 | 팀원별 함수 1개 이상 + 간단 사용 예시(README 또는 docstring) | 파일을 팀원별로 나눠 충돌이 적음 | Python 코드가 실행되는지 확인해야 함 |
| (B) 팀 소개 | `team/`에 팀원별 소개 파일 + README에서 링크/목록 | 코드 부담 없음 | 개인정보를 공개 저장소에 올리지 않도록 주의(2-2) |
| (C) 학습 노트 | 팀원별 노트 1개 이상 + README에서 목차 | 내용이 자유로움, Git 학습 정리가 자연스럽게 끝남 | 노트 폴더 위치를 팀이 정해야 함(미션은 위치 미지정, `docs/notes/` 추천) |

어느 옵션이든 공통적으로 **팀원별 최소 1건의 기여 커밋**이 필요하고, README에서 한 눈에 보이도록 목록을 두는 것이 좋습니다.

### 9-2. (A)를 선택했을 때 실제 동작하는 예시

파일을 팀원 이름으로 나누면(`src/kim_math_utils.py`, `src/lee_string_utils.py`) 서로 같은 파일을 건드리지 않아 충돌이 줄어듭니다. 아래 코드는 실제로 실행해 사용 예시(docstring의 `>>>`)가 정말 맞는지 검증한 것입니다.

```python
"""김철수의 수학 유틸 함수 모음."""


def add(a, b):
    """두 수를 더해서 반환한다.

    사용 예시:
    >>> add(1, 2)
    3
    """
    return a + b


def safe_divide(a, b):
    """b가 0이면 None, 아니면 a / b 를 반환한다.

    사용 예시:
    >>> safe_divide(6, 3)
    2.0
    >>> safe_divide(1, 0) is None
    True
    """
    if b == 0:
        return None
    return a / b
```

```bash
python -m doctest -v src/kim_math_utils.py   # docstring의 사용 예시가 맞는지 자동 검사
```

미션이 요구하는 "간단 사용 예시(README 또는 docstring)"를 docstring으로 충족하고, 동시에 PR 본문의 "테스트/검증(How)"에 위 명령과 결과를 적을 수 있습니다. 함수 이름이 팀원끼리 곹치면 이름을 붙이지 않고 README만 함께 고치는 일이 생겨 충돌 실습에 좋습니다.

### 9-3. (B), (C)를 선택했을 때

- (B) `team/kim.md`, `team/lee.md` 처럼 파일을 나누고 README에 `- [김철수](team/kim.md)` 형태로 목록을 둔다. 이 목록 줄이 여러 명이 동시에 고치는 자리가 되어 자연스럽게 충돌 실습이 된다.
- (C) `docs/notes/kim-git-branch.md` 처럼 작성하고 README에 목차를 둔다. 노트 주제는 이 문서의 목차(브랜치, PR, 충돌, reset·revert·stash)를 나눠 맡으면 학습과 제출이 동시에 된다.

### 9-4. PR 2개를 어떻게 채울까 (추천 배분)

| PR | 내용 예시 |
| --- | --- |
| PR 1 | 선택한 결과물 중 내 몸의 부분(함수 1개, 소개 1개, 노트 1개) + README 목록 추가 |
| PR 2 | CONTRIBUTING.md 중 내가 맡은 절 또는 트러블슈팅/충돌 기록 |

이렇게 나눌 때 PR을 **최소한의 작은 단위**로 유지하고, 각 PR에 Issue를 하나씩 연결하면 "PR 2개 + Issue 연동"이 한번에 충족됩니다.

### 9-5. 팀원별 최소 기준 체크리스트 (본인 기준)

아래 실제 항목은 미션 원문에 그대로 나오는 **팀원 각자 기준(전원 충족)**입니다. 자기 이름으로 한 벌씩 복사해 확인하세요.

- [ ] Issue를 만들어 각 작업에 연결했다 (PR 2개 이상 → Issue 2개 이상)
- [ ] **PR 2개 이상을 생성하고 병합**했다
- [ ] 각 PR 본문에 What / Why / How와 `Closes #번호`가 있다
- [ ] 병합 후 연결된 Issue가 Closed로 바뀔는지 확인했다
- [ ] **다른 팀원의 PR에 코드 리뷰 2개 이상**을 작성했다 (본인 PR 제외, 각각 실질 코멘트 1개 이상)
- [ ] **내 PR에 달린 리뷰 코멘트를 1회 이상 반영**했다 (커밋/수정/답글로 증빙)
- [ ] 시나리오 4종 중 **최소 1개의 기록 작성에 참여**했고 이름/역할이 문서에 있다
- [ ] 선택한 결과물에 **내 기여 커밋**이 1건 이상 있다
- [ ] 내 커밋 메시지에 의미 없는 메시지(`update`, `fix`, `wip` 등)가 없다
- [ ] 위 모든 링크를 SUBMISSION.md에 내 이름 아래로 정리했다

### 9-6. 팀 전체 체크리스트

- [ ] 3\~5인 팀, 저장소(옵션 A 또는 B) 생성, 모든 팀원 초대 수락
- [ ] README.md, docs/, src/ (또는 team/) 구성
- [ ] main **Branch Protection** (직접 push 금지, PR만 병합, 승인 1명 이상)
- [ ] GitHub Flow 선택 이유 3줄 이내 기록 (README 또는 CONTRIBUTING)
- [ ] 브랜치 네이밍 규칙, 커밋 컨벤션, PR 규칙, 리뷰 규칙, 충돌 대응 흐름을 CONTRIBUTING.md에 작성
- [ ] 충돌 해결 기록 **2회 이상**, 그 중 **비자명 1회 이상** (conflict-resolution.md)
- [ ] 트러블슈팅 **4종**(amend / reset --soft / revert / stash·pop) 모두 기록 (troubleshooting-log.md)
- [ ] `git log --oneline --graph --all` 증빙 (텍스트 또는 스크린샷)
- [ ] SUBMISSION.md에 저장소 URL·팀원별 링크·문서 링크·증빙 링크 정리

### 9-7. 제출 전 마지막 점검 방법

```bash
git switch main && git pull
git log --oneline --graph --all | head -30           # 그래프가 분기/병합으로 보이는지
python check_commits.py                              # 5-5장 점검 스크립트(선택)
grep -rn -E '^(<<<<<<<|>>>>>>>)' . --include='*.md' --include='*.py'   # 충돌 마커 잔재 여부
```

또 GitHub에서 Pull requests 탭의 **Closed** 목록을 보고, 각 PR이 리뷰 코멘트 하나 이상과 답글/수정 기록을 가졌는지 직접 클릭해 확인하세요.

> 미션 연결: 간단한 결과물 택 1과 최소 완성 기준, 팀원별 최소 기준 5가지(PR 2, 리뷰 2, 리뷰 반영 1, 시나리오 기록 참여 1, 결과물 커밋 1)을 담은 장입니다.

## 10. 보너스: rebase -i 히스토리 정리, CODEOWNERS

보너스는 필수가 아닙니다. 필수 항목을 모두 끝낸 뒤 시간이 남을 때만 하세요. 다만 두 가지 모두 실무에서 자주 쓰여서 개념은 알아 둘 만합니다.

### 10-1. git rebase -i: 내 커밋 정리하기

미션 요구는 "개인 feature 브랜치의 커밋을 squash/reword하여 정리하고, 정리 전/후 히스토리를 비교해 간단히 문서화"입니다.

`git rebase -i HEAD~3`은 "최근 커밋 3개를 편집기에서 하나씩 어떻게 처리할지 정하면서 다시 쌓는다"는 뜻입니다. 편집기에 아래처럼 목록이 열립니다(오래된 커밋이 위).

```text
pick 6ec8f7e wip 1
pick 1c7e995 wip 2
pick 3875170 wip 3
```

맨 앞 단어를 바꾸면 처리 방식이 달라집니다.

| 명령 | 의미 |
| --- | --- |
| `pick` | 그대로 사용 |
| `reword` | 커밋은 그대로 두고 메시지만 수정 |
| `squash` | 앞 커밋에 합치고 메시지도 합침(편집기가 한 번 더 열림) |
| `fixup` | 앞 커밋에 합치되 이 커밋의 메시지는 버림 |

직접 실행해 확인한 결과입니다. 2·3번째를 `squash`로 바꿨더니 커밋 3개가 1개로 줄었습니다.

```text
[정리 전]
3875170 wip 3
1c7e995 wip 2
6ec8f7e wip 1

[정리 후]  (squash 2개)
4c89fd7 wip 1          # 실제로는 편집기에서 메시지를 의미 있게 고쳐 씁니다
```

`reword`+`fixup` 조합도 확인했습니다. 커밋 2개(`temp`, `wip: second`)가 `docs: add r.txt with two lines` 1개로 정리되고 파일 내용은 그대로 유지됐습니다.

**편집기가 vim으로 열렸을 때** (기본값인 환경이 많습니다)

1. `i`를 눌러 입력 모드로 바꾼다.
2. 단어를 고친다 (`pick` → `squash` 등).
3. `Esc`를 누른다.
4. `:wq` 입력 후 Enter (저장하고 종료).
5. 메시지 편집 창이 한 번 더 열리면 같은 방법으로 의미 있는 메시지로 고치고 저장한다.

**주의사항 (미션의 운영 안정성 제약과 직결)**

- 리베이스는 커밋을 **새로 만들어 교체**하므로 해시가 모두 바뀝니다(amend와 같은 원리).
- 이미 push한 브랜치를 리베이스하면 `git push`가 거부되고 강제 푸시가 필요해집니다. 미션은 "팀 합의 없이 강제 푸시/리베이스 금지", "공유 브랜치(main 포함) 히스토리 재작성 금지"를 명시합니다. 그래서 **push하기 전의 내 개인 feature 브랜치에서만** 하세요.
- 중간에 꼬이면 `git rebase --abort`로 시작 전 상태로 돌아갑니다(직접 확인).

**문서화 예시** (정리 전/후 비교)

```markdown
## 히스토리 정리 기록 (보너스)
- 대상 브랜치: feature/kim-math-utils (push 전, 개인 브랜치)
- 정리 전: wip 1 / wip 2 / wip 3 (3개)
- 정리 후: feat: add add() and safe_divide() to math utils (1개)
- 사용한 명령: git rebase -i HEAD~3 (2·3번째를 squash)
- 정리 전 git log --oneline 출력, 정리 후 출력 (붙여넣기)
```

### 10-2. CODEOWNERS: 파일별 책임 리뷰어 자동 지정

GitHub 공식 문서("About code owners")에서 확인한 내용입니다.

- 파일 이름은 `CODEOWNERS`이고 `.github/`, 저장소 루트, `docs/` 중 한 곳에 둡니다. 여러 곳에 있으면 이 순서로 찾습니다. 미션은 `.github/CODEOWNERS`를 요구하므로 그 위치에 두세요.
- 코드 오너로 지정된 사람은 그 파일을 바꾸는 PR이 열릴 때 **자동으로 리뷰 요청**을 받습니다.
- 지정되는 사람은 저장소에 **쓰기(write) 권한**이 있어야 합니다. 초대를 수락하지 않은 사람은 안 됩니다.
- 파일은 PR의 **base 브랜치(main)에 존재**해야 리뷰 요청이 동작합니다.
- 같은 패턴이 여러 줄이면 **마지막에 매칭된 줄이 우선**입니다.
- 무료 플랜은 공개 저장소에서만 코드 오너 기능을 쓸 수 있습니다(2-2에서 공개 저장소를 권장한 이유).

```text
# .github/CODEOWNERS
# 기본 오너 (아무 규칙에도 안 걸린 파일)
*                     @kim

# 문서는 문서 담당
/docs/                @park

# 결과물별 담당
/src/kim_*.py         @kim
/src/lee_*.py         @lee
/team/                @choi
```

`@` 뒤에는 GitHub 아이디를 씁니다. 브랜치 보호 규칙의 **Require review from Code Owners**를 켜면 오너의 승인이 병합 조건이 되고, 승인은 오너 중 한 명이면 충분합니다. 이 옵션을 켜면 전원이 한 사람에게 막힐 수 있어서, 보너스를 시도하는 팀은 처음엔 자동 리뷰 요청까지만 쓰는 것을 추천합니다.

> 미션 연결: 보너스 과제 두 가지(히스토리 정리, CODEOWNERS)와 "공유 브랜치 히스토리 재작성 금지" 제약의 경계선을 다룹니다.

## 11. 내가 해야 할 일: 단계별 실행 가이드라인

이 장만 위에서부터 순서대로 따라 해도 미션을 끝낼 수 있게 구성했습니다. 개념이 헷갈리면 괄호의 장(예: 2-5)으로 돌아가 읽으세요. 시간은 미션 학습시간 20시간을 기준으로 한 **제 제안**이며, 팀 사정에 맞게 조절하세요.

### 11-0. 한눈에 보는 로드맵

| 단계 | 목표 | 누가 | 예상 시간(제안) |
| --- | --- | --- | --- |
| 0 | 준비: 포인트 학습, 환경 확인, 팀 합의 | 전원 | 3시간 |
| 1 | 저장소와 팀 세팅, Branch Protection | 팀장(저장소 만드는 사람) + 팀원 초대 수락 | 1.5시간 |
| 2 | 처음 Issue 만들기와 담당 나눠 맡기 | 팀장 주도, 전원 참여 | 0.5시간 |
| 3 | 첨 PR: CONTRIBUTING 분담 작성 + 교차 리뷰 | 전원 | 3시간 |
| 4 | 두 번째 PR: 선택 결과물 + 교차 리뷰 + 리뷰 반영 | 전원 | 3시간 |
| 5 | 충돌 실습 2회(비자명 1회 이상) + 기록 | 팀 | 2시간 |
| 6 | 트러블슈팅 4종 + 기록 | 팀(시나리오당 담당+도우미) | 2.5시간 |
| 7 | 마무리: git log 증빙, SUBMISSION.md, 최종 점검 | 전원 | 2시간 |
| 8 | (선택) 보너스 + 버퍼 | 희망자 | 3시간 안에서(버퍼 2시간 포함) |

아래 표시는 역할입니다. **팀장**은 저장소를 만드는 한 명(아무나 할 수 있음, 사실상 초기 세팅 담당자)이고, **팀원**은 팀장을 포함한 전원입니다. 내가 팀장이면 팀장용·팀원용 항목을 모두, 팀원이면 팀원용만 따라 하면 됩니다.

### 단계 0. 준비 (전원)

- [ ] 이 문서 1장(Git 기초)와 3장(GitHub Flow)을 읽는다. 나머지는 해당 단계에서 참고하면 된다.
- [ ] 자기 PC에 Git이 설치되어 있는지 확인한다.
- [ ] 자기 PC에 Python 3.10 이상이 있는지 확인한다 (미션 개발 환경 요구).
- [ ] GitHub 계정을 준비하고 아이디를 팀 단톡방에 공유한다.
- [ ] 한 번만 하는 설정(1-1장)을 한다. 이메일은 GitHub 계정에 등록한 것과 같게.

```bash
git --version          # git version 2.x 가 나오면 설치됨
python --version       # Python 3.10 이상 (환경에 따라 python3 --version)
git config --global user.name "내 이름"
git config --global user.email "github에 등록한@email.com"
git config --global init.defaultBranch main
```

- [ ] **팀 합의 사항**을 정한다: ① 팀장(저장소 만드는 사람) ② 옵션 A(Organization) 또는 B(Collaborator) ③ 저장소를 Public으로 만들지(2-2) ④ 결과물 (A/B/C) ⑤ 연락·리뷰 요청 방식(예: 24시간 안에 리뷰)

확인 기준: 팀원 모두 `git --version`이 나오고, GitHub 아이디가 모였다.

### 단계 1. 저장소와 팀 세팅

**팀장이 할 일** (2장 참고)

- [ ] 1-1. Organization을 만들거나(옵션 A) 개인 계정에 저장소를 만든다(옵션 B). 저장소를 만들 때 **Public**, **Add a README file**을 선택한다.
- [ ] 1-2. 팀원을 초대한다(옵션 A: Organization → People, 옵션 B: 저장소 Settings → Collaborators).
- [ ] 1-3. 로컬에 clone하고 기본 폴더·문서 뼈대를 main에 올린다(아직 보호 규칙을 켜기 전이라 push가 가능).

```bash
git clone https://github.com/<조직또는계정>/<저장소>.git
cd <저장소>
mkdir -p docs src team
touch src/.gitkeep team/.gitkeep          # team/ 은 (B) 팀 소개를 선택했을 때만 사용
printf '# Contributing Guide\n' > docs/CONTRIBUTING.md
printf '# Conflict Resolution Log\n' > docs/conflict-resolution.md
printf '# Troubleshooting Log\n' > docs/troubleshooting-log.md
printf '# Submission Index\n' > SUBMISSION.md
printf '__pycache__/\n*.pyc\n.env\n' > .gitignore
git add .
git status                                # 올리기 전에 목록 확인
git commit -m "chore: add base folder structure and doc skeletons"
git push
```

- [ ] `protect-main` Ruleset이 Active 상태인지 확인
- [ ] 대상 브랜치가 `main`인지 확인
- [ ] PR 병합 전 최소 1명 이상의 승인이 필요한지 확인
- [ ] Bypass list에 불필요한 우회 대상이 없는지 확인

```bash
git commit --allow-empty -m "chore: verify main branch protection"
git push                                  # 거부되어야 정상
git reset --hard origin/main              # 로컬에 쌓인 테스트 커밋 정리
```

정상이면 push가 `protected branch` 또는 `Changes must be made through a pull request`와 비슷한 문구와 함께 거부됩니다(문구는 GitHub 버전에 따라 다를 수 있음). 만약 그대로 통과되면 보호가 적용되지 않은 것이니 설정(특히 `Do not allow bypassing` 항목)을 다시 확인하세요. 이 테스트 커밋은 빈 커밋이라 통과되더라도 파일이 망가지지는 않습니다.

- [ ] 1-6. 설정 화면과 거부된 push 화면을 스크린샷으로 남긴다(나중에 SUBMISSION.md에 링크).

**팀원이 할 일** (전원)

- [ ] 1-7. 초대를 **수락(Accept)** 한다(메일 또는 GitHub 알림).
- [ ] 1-8. 저장소를 clone 하고 `git remote -v`, `ls`로 폴더가 보이는지 확인한다.

확인 기준: 저장소에 README·docs·src·SUBMISSION.md가 보이고, main에 직접 push하면 거부되며, 팀원 전원이 clone에 성공했다.

### 단계 2. Issue 만들기와 담당 나눌 맡기

이슈는 코드를 쓰기 전에 먼저 만듭니다(4-1장). 팀원 수 × 2개 이상 필요하므로 한 번에 만들어 둔 뒤 각자 고르면 편합니다. 4명 팀 기준 예시입니다.

| Issue 제목 예시 | 담당 예시 |
| --- | --- |
| docs: CONTRIBUTING 브랜치 전략·네이밍 + 선택 이유 3줄 | 팀원 1 |
| docs: CONTRIBUTING 커밋 컨벤션 | 팀원 2 |
| docs: CONTRIBUTING PR 규칙·리뷰 규칙 | 팀원 3 |
| docs: CONTRIBUTING 충돌 대응 흐름 | 팀원 4 |
| feat: 결과물 — 팀원 1 분량 | 팀원 1 |
| feat: 결과물 — 팀원 2 분량 | 팀원 2 |
| feat: 결과물 — 팀원 3 분량 | 팀원 3 |
| feat: 결과물 — 팀원 4 분량 | 팀원 4 |
| docs: 충돌 해결 기록 / 트러블슈팅 기록 / SUBMISSION 정리 | 실습한 사람 |

- [ ] 2-1. (팀장 또는 각자) Issues 탭 → New issue로 위 표의 이슈를 만든다. 목적과 완료 조건을 적는다.
- [ ] 2-2. 각자 내 담당 이슈의 **Assignees**에 자기를 지정한다.
- [ ] 2-3. 내 이슈 번호(#숫자)를 메모해 둔다. PR의 `Closes #번호`에 쓴다.

확인 기준: 전원이 자기 담당 이슈 2개 이상을 가졌다.

### 단계 3. 첫 번째 PR: CONTRIBUTING 분담 작성 (전원)

이 단계가 한 사이클의 실제 연습입니다. 그대로 따라 하면 PR 1개가 만들어지고, 이 사이클을 두 번 반복하면 팀원별 PR 2개가 됩니다.

**3-A. 작업과 PR 만들기 (작성자)**

- [ ] 3-1. main을 최신으로 만든다.
- [ ] 3-2. 내 Issue에 맞는 브랜치를 만든다(네이밍 규칙 준수).
- [ ] 3-3. 파일을 수정하고, 작은 단위로 커밋한다(커밋 컨벤션 준수).
- [ ] 3-4. 원격에 push하고 PR을 열어 본문 템플릿(What/Why/How + `Closes #번호`)을 채운다.
- [ ] 3-5. 오른쪽 **Reviewers**에서 다른 팀원을 리뷰어로 지정하고, 단톡방에 PR 링크를 공유한다(4-7장 교차 리뷰 표).

```bash
git switch main && git pull                          # 3-1
git switch -c feature/kim-contributing-commit-rules  # 3-2
# ... docs/CONTRIBUTING.md 에서 내 절만 수정 ...
git status                                           # 수정된 파일 확인
git add docs/CONTRIBUTING.md                         # 3-3
git commit -m "docs: add commit message convention to CONTRIBUTING"
git push -u origin feature/kim-contributing-commit-rules   # 3-4
```

**3-B. 다른 사람 PR 리뷰하기 (리뷰어)**

- [ ] 3-6. 내가 지정된 PR을 열고 **Files changed**에서 변경을 읽는다.
- [ ] 3-7. 줄 단위로 실질 코멘트를 남긴다(질문/대안/리스크/개선 중 1개 이상, 4-5장 예시).
- [ ] 3-8. **Review changes** → 코멘트만 남길지(`Comment`), 승인할지(`Approve`), 고쳐야 하는지(`Request changes`) 고르고 제출한다.

**3-C. 리뷰를 반영하고 병합하기 (작성자)**

- [ ] 3-9. 리뷰 코멘트에 **답글**을 남긴다(수용/다른 의견).
- [ ] 3-10. 고친 내용을 같은 브랜치에 커밋·push한다(PR이 자동으로 갱신됨). 답글에 커밋 해시를 남긴다.
- [ ] 3-11. 다른 팀원의 **Approve**를 받으면 병합 버튼이 활성화된다. **Create a merge commit**으로 병합한다.
- [ ] 3-12. **Delete branch**로 원격 브랜치를 지우고, 로컬도 정리한다. 이슈가 자동으로 Closed 되었는지 확인한다.

```bash
# 3-10: 리뷰 반영
git add docs/CONTRIBUTING.md
git commit -m "docs: clarify commit types per review"
git push

# 3-12: 병합 후 정리
git switch main && git pull
git branch -d feature/kim-contributing-commit-rules
git fetch --prune
```

확인 기준: PR이 Merged 상태이고, 연결된 Issue가 Closed이며, PR에 실질 리뷰 코멘트 1개 이상 + 답글 또는 수정 커밋이 있다.

### 단계 4. 두 번째 PR: 선택 결과물 (전원)

- [ ] 4-1. 단계 3의 3-A 순서를 그대로 반복한다. 이번에는 선택한 결과물(A: 함수 파일, B: 소개 파일, C: 노트)을 내 이름 파일로 만든다.
- [ ] 4-2. README의 목록/목차에 내 항목을 한 줄 추가한다(여러 명이 같은 파일을 고치니 충돌이 날 수 있고, 그것이 5단계 재료가 된다).
- [ ] 4-3. (A 선택 시) PR 본문의 How에 `python -m doctest -v src/<내파일>.py` 결과를 넣는다(9-2장).
- [ ] 4-4. 다른 팀원의 PR 중 **서로 다른 PR 2개** 이상을 리뷰해 리뷰 2개 기준을 채운다.
- [ ] 4-5. 내 PR 중 하나 이상에서 리뷰를 **반영하는 커밋**을 남긴다.

확인 기준: 내 이름으로 병합된 PR이 2개 이상, 내가 쓴 리뷰가 서로 다른 PR 2개 이상이다. (9-5장 체크리스트로 점검)

### 단계 5. 충돌 실습 2회 + 기록 (팀)

6장의 레시피를 그대로 쓰면 됩니다. 핵심은 "우연히 날 때만 기다리지 말고, 두 명이 짝을 이뤄 일부러 같은 줄을 고치는 것"입니다.

- [ ] 5-1. 두 명(작성자 A, 상대 B)이 같은 파일의 같은 줄을 각자 다르게 고친 브랜치를 만든다(레시피 A).
- [ ] 5-2. 둘 다 PR을 열고, 한 사람의 PR을 먼저 병합한다.
- [ ] 5-3. 다른 사람 PR에 "충돌이 있습니다"가 뜨면, 로컬에서 `git merge origin/main`으로 충돌을 만들고 **화면을 복사·스크린샷**으로 남긴다.
- [ ] 5-4. 마커를 정리하고 `git add` → `git commit` → `git push`한다(6-3장 절차).
- [ ] 5-5. 또 다른 두 명이 **비자명 충돌**(인접 줄 또는 삭제 vs 수정)을 만들어 같은 방식으로 해결한다(레시피 B 또는 C).
- [ ] 5-6. `docs/conflict-resolution.md`에 기록한다(8-3장 템플릿: 참여자, 상황, 마커, 해결 절차, 결과, 배운 점).

확인 기준: 충돌 기록 2개 이상, 그 중 1개는 비자명 충돌이고 실제 해결 커밋/PR 링크가 들어 있다.

### 단계 6. 트러블슈팅 4종 + 기록 (팀)

- [ ] 6-1. 시나리오 4개(amend, reset --soft, revert, stash)를 팀원에게 나눠 맡긴다. 한 사람이 한 시나리오를 담당하고 다른 한 명이 도우미로 참여하면, 팀원이 4명일 때 전원이 최소 1개 기록에 참여하게 된다(3인이면 한 사람이 두 개, 5인이면 한 사람이 쉬는 대신 리뷰 담당).
- [ ] 6-2. 7-6장의 명령을 연습용 브랜치에서 실행하고, **터미널 출력을 복사**해 둔다.
- [ ] 6-3. `docs/troubleshooting-log.md`에 "참여자(이름·역할) / 상황 / 시도한 명령 / 결과·주의점 / 왜 이 방법인가"로 남긴다(8-4장).
- [ ] 6-4. 기록문서도 PR을 거쳐 main에 들어간다(한 사람이 한 번에 올리면 충돌이 늘어나므로 시나리오당 PR 하나씩도 좋다).

확인 기록: 시나리오 4개가 모두 문서에 있고, 각 팀원의 이름이 최소 1개 시나리오의 참여자로 드러난다.

### 단계 7. 마무리 (전원)

- [ ] 7-1. 전원이 자기 기준 체크리스트(9-5장)를 확인하고, 빠진 게 있으면 지금 보충한다.
- [ ] 7-2. 각자 SUBMISSION.md에 내 항목(Issue, PR, 리뷰, 리뷰 반영, 시나리오 참여, 결과물 커밋)을 채운다(8-5장). 이때 같은 파일을 동시에 고치므로 충돌이 날 수 있다. 기록할 사람을 나눠 순서대로 작업하면 편하다.
- [ ] 7-3. (팀장) 모든 PR이 병합된 뒤 `git log --oneline --graph --all`을 저장하고 스크린샷도 찍는다(8-6장).
- [ ] 7-4. 제출 전 점검(9-7장): 커밋 메시지 리스트, 충돌 마커 잔재, PR별 리뷰 코멘트 존재 여부.
- [ ] 7-5. GitHub 저장소 URL과 SUBMISSION.md를 미션 제출 창에 제출한다.

### 단계 8. (선택) 보너스

- [ ] 8-1. 히스토리 정리: 별도 연습 브랜치에서 wip 커밋 2\~3개를 만들고 `git rebase -i`로 squash/reword, 전·후 로그를 비교해 문서화(10-1장, 개인 브랜치에서만).
- [ ] 8-2. `.github/CODEOWNERS`를 PR로 추가(10-2장).

### 막혔을 때 빠르게 찾는 표

| 상황 | 보세요 |
| --- | --- |
| push가 거부됐다(`rejected`, `non-fast-forward`) | 13장 FAQ, 7-1 |
| PR에 충돌이 뜨는데 무엇부터 할지 모르겠다 | 6-3, 6-4 |
| 실수로 잘못 커밋했다 | 7-5 질문 흐름 |
| main에 커밋해 버렸다 | 7-7 |
| Merge 버튼이 회색이다 | 13장 FAQ |

> 미션 연결: 이 단계를 순서대로 따라가면 모든 필수 요구사항(저장소, 보호 규칙, GitHub Flow, Issue·PR 연동, 리뷰, 충돌, 트러블슈팅, 문서·증빙)이 충족됩니다.

## 12. 초보자가 자주 겪는 오류 FAQ

여기 실린 오류 문구는 이 문서를 만들면서 직접 재현해 확인한 것(재현 표시)과, GitHub의 일반적인 동작을 정리한 것(일반 안내 표시)을 구분해 두었습니다. 화면 문구는 Git·GitHub 버전에 따라 약간 다를 수 있습니다.

### Q1. push가 거부됩니다: `rejected ... (fetch first)` / `non-fast-forward` (재현)

원인: 원격에 내가 가지고 있지 않은 커밋이 있습니다(다른 팀원이 먼저 push). 실제 출력입니다.

```text
 ! [rejected]        main -> main (fetch first)
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. ... use 'git pull' before pushing again.
```

해결: `git pull`로 원격의 커밋을 가져와 합친 뒤 다시 push합니다. 같은 파일을 다르게 고친 경우에는 충돌이 나고, 그때는 6장 절차대로 해결합니다. **강제 푸시(`--force`)는 쓰지 마세요**(미션 제약).

### Q2. `git pull`했더니 "divergent branches"라고 합니다 (재현)

로컬과 원격이 서로 다른 커밋을 가진 상태에서 병합 방식이 정해져 있지 않으면 Git이 아래와 같은 안내를 띄웁니다(이 환경의 Git 2.43).

```text
hint: You have divergent branches and need to specify how to reconcile them.
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
```

팀 규칙이 "merge로 해결"이므로 한 번만 다음을 실행해 두면 됩니다. `pull.rebase false`로 설정하면 병합 커밋으로 합쳐집니다(실제 확인).

```bash
git config --global pull.rebase false
```

### Q3. 저장소 커밋이 안 됩니다: `Author identity unknown ... Please tell me who you are.` (재현)

1-1장의 `user.name`, `user.email` 설정을 아직 안 했습니다. 이메일은 GitHub 계정에 등록한 것으로 넣으세요. 이미 만든 커밋의 작성자를 바꾸려면 다른 문제가 되므로, 처음 작업 전에 설정하는 것이 좋습니다.

### Q4. 브랜치를 바꾸려고 하니 `Your local changes ... would be overwritten by checkout` (재현)

커밋하지 않은 변경이 이동할 브랜치의 파일과 부딪히는 상황입니다. 커밋하거나 `git stash push -m "이름"`로 임시 보관 후 이동하세요(7-4장).

### Q5. 메시지 편집기가 열렸는데 빠져나가는 법을 모르겠습니다 (일반 안내)

`git commit`을 `-m` 없이 실행하거나 merge·rebase 중에 편집기(대개 vim)가 열립니다. `Esc`를 누른 뒤 저장하고 나가려면 `:wq`, 저장 없이 나가려면 `:q!`를 입력하고 Enter를 누릅니다. 초보자는 커밋을 항상 `git commit -m "메시지"` 형태로 하면 편집기를 만날 일이 적습니다.

### Q6. `fatal: not a git repository` (일반 안내)

Git 저장소 폴더 밖에서 명령을 실행했습니다. `cd <저장소 폴더>`로 들어간 뒤 `git status`로 확인하세요.

### Q7. clone·push 할 때 `Permission denied`, `403`, `Repository not found` (일반 안내)

흔한 원인 세 가지입니다. ① 초대를 아직 수락하지 않았다. ② 저장소 주소·조직 이름이 틀렸다. ③ 인증이 안 되어 있다. GitHub는 HTTPS에서 계정 비밀번호로는 인증하지 않고, 브라우저 로그인(Git Credential Manager)이나 Personal Access Token을 사용합니다. 인증 절차는 운영체제마다 달라서 이 문서에서는 자세히 다루지 않았습니다. 막히면 팀원에게 어떤 방식을 쓰는지 묻고 같이 확인하세요.

### Q8. Merge 버튼이 회색이거나 눌러도 병합이 안 됩니다 (일반 안내)

- 다른 팀원의 Approve가 없다. 작성자 본인의 승인은 인정되지 않는다(4-4장).
- 충돌이 있다. 로컬에서 `git merge origin/main`으로 해결 후 push(6-4장).
- Request changes 상태이거나, 해결해야 할 리뷰 대화가 남아 있다(대화 해결 필수 옵션을 켰다면).

### Q9. `Closes #3`를 썼는데 이슈가 자동으로 안 닫혀요 (일반 안내, GitHub 공식 문서 확인)

원인 후보입니다. ① PR이 기본 브랜치(main)가 아닌 다른 브랜치를 향해 있다(이 경우 키워드는 무시됨). ② 키워드 형식이 다르다(`Closes #3`, `Fixes #3` 등 정해진 9개). ③ 아직 병합 전이다(병합 후에 닫힌다). ④ 이슈 번호가 다른 저장소의 것이다. 해결 못 하면 PR 오른쪽 **Development**에서 수동 연결하세요(4-3장).

### Q10. 충돌 마커를 지우지 않고 커밋·push해 버렸습니다 (일반 안내)

파일에 `<<<<<<<` 줄이 그대로 남아 있어야 확인이 됩니다(`grep -rn "<<<<<<<" .`). 이미 push했다면 amend하지 말고, 마커를 정리한 **새 커밋**(`fix: remove leftover conflict markers in team.txt`)을 추가로 push하세요. 이것도 "이미 push한 것은 히스토리를 고치지 않는다"는 원칙입니다.

### Q11. `HEAD detached`(분리된 HEAD) 라고 합니다 (재현)

브랜치가 아니라 특정 커밋을 직접 가리키는 상태입니다. `git status -sb`가 `## HEAD (no branch)`로 나옵니다. 작업을 하지 않았다면 `git switch main`으로 돌아가면 되고, 이 상태에서 커밋을 만들었다면 `git switch -c feature/이름-작업`으로 새 브랜치를 만들어 커밋을 보존하세요.

### Q12. `.gitignore`에 썼는데도 파일이 계속 추적됩니다 (재현)

이미 커밋된 파일은 `.gitignore`를 추가해도 자동으로 추적이 멈추지 않습니다. 실제로 `.env`를 실수로 커밋한 뒤 `.gitignore`에 적어도 상태가 그대로였고, 아래 명령으로 해결되었습니다. 파일은 내 폴더에 그대로 남습니다.

```bash
git rm --cached .env         # 추적만 중단, 파일은 유지
git add .gitignore
git commit -m "chore: stop tracking .env and ignore it"
```

다만 이미 push한 비밀정보(비밀번호, 토큰)는 히스토리에 남아 있으므로 노출된 것으로 간주하고 해당 비밀을 교체해야 합니다. 이 미션에서는 비밀정보를 저장소에 넣지 마세요.

### Q13. `git branch -d`로 브랜치를 지웠는데 내용이 날아갔나요? (재현 일부)

이미 합쳐진 브랜치라면 커밋은 main 히스토리에 남아 있습니다. 브랜치 삭제는 이름표를 지우는 것이지 커밋을 지우는 것이 아니기 때문입니다(1-4장). 다만 합치지 않은 브랜치를 `-D`(대문자)로 강제 삭제하면 커밋을 잃을 수 있으니 피하세요. 참고로 원격에 push해 둔 브랜치는 병합된 상태에서 `-d`를 쓰면 "원격에는 병합됐지만 내 HEAD에는 아직"이라는 경고만 내고 삭제되는 경우가 있었습니다(확인). 함께 정리하기 전에 `git switch main && git pull`로 로컬 main을 먼저 최신으로 만드는 습관을 들이세요(3-5장).

### Q14. 팀원이 작업을 안 해서 최소 기준이 안 채워지면? (운영 안내)

미션이 팀원별 최소 기준(전원 충족)을 요구하므로, 시작 시 "리뷰 요청 시 기한", "중간 점검 시점"을 미리 정해 두세요. 중간 점검에서 SUBMISSION.md의 사람별 표(8-5장)를 보면 누가 무엇이 남았는지 한눈에 보입니다. 내 기준은 내가 챙기되, 리뷰는 내 차례가 되면 팀원에게 미루지 말고 바로 남기는 것이 서로에게 가장 도움이 됩니다.

> 미션 연결: 트러블슈팅(기록 남기기) 정신과 과제 목표 6번(문제가 생겼을 때 기록하고 해결 과정을 설명)을 보조합니다.

## 13. 자가점검: 과제 목표 6개 설명 연습

미션은 완료한 뒤 다섯 줄이내로 **스스로 설명**할 수 있어야 한다고 합니다(동료 평가에서 답할 수 있는 수준). 아래 모범 답안을 보기 전에 **먼저 소리 내어 대답해 보고**, 마지막에 비교하세요. 모범 답안의 근거는 대부분 이 문서에서 직접 실행해 확인한 결과입니다.

### 목표 1. 브랜치는 내부적으로 어떻게 동작하고, 왜 나눠 작업하나요?

> 모범 답안: 브랜치는 파일을 복사해 둔 것이 아니라 특정 커밋 하나를 가리키는 이름표(포인터)입니다. 실제로 `.git/refs/heads/main` 파일을 열면 커밋 해시 한 줄만 들어 있습니다. 현재 브랜치에서 커밋하면 그 브랜치의 이름표만 새 커밋으로 이동하고, `HEAD`는 지금 어느 브랜치에 있는지 가리킵니다. 나눠서 작업하는 이유는 여러 사람의 미완성 변경이 서로에게 영향을 주지 않고 main이 깨지지 않게 유지되기 때문입니다.

점검 질문: `git switch`는 내부적으로 무엇을 바꾸나요? → HEAD가 가리키는 이름표를 바꾸고 작업 폴더를 그 커밋 모습으로 맞춥니다(1-4장).

### 목표 2. GitHub Flow는 무엇이고 왜 팀 협업에 필요한가요?

> 모범 답안: main은 항상 깨지지 않는 상태로 두고, 작업은 짧은 feature 브랜치에서 한 뒤 PR과 리뷰를 거쳐 합치는 방식입니다. 브랜치 생성 → 커밋·push → PR → 리뷰 반영 → 병합 → 브랜치 삭제의 6단계입니다. 이렇게 하면 사람마다 다른 일을 동시에 하더라도 병합 전에 리뷰로 품질을 확인하고 기록도 남습니다.

점검 질문: 우리 팀이 Git Flow가 아니라 GitHub Flow를 택한 이유는? → 짧고 단순한 팀 프로젝트라 develop·release 같은 추가 브랜치가 과하다(3-3장의 3줄 이유를 말로 풀어 보세요).

### 목표 3. PR의 목적과 코드 리뷰의 가치는 무엇인가요?

> 모범 답안: PR은 내 브랜치를 main에 합치기 전에 팀에 보여주고 피드백을 받는 요청이자, 변경 내용·이유·검증 방법과 대화가 기록으로 남는 공간입니다. 코드 리뷰는 버그와 리스크를 main에 들어오기 전에 잡고, 팀이 코드를 함께 이해하며, 규칙과 스타일을 맞추는 가치가 있습니다. 저희 팀에서는 전원이 PR 2개, 리뷰 2개, 리뷰 반영 1회 이상을 했고, main에는 다른 팀원 승인 1명 이상이 있어야 합쳐집니다.

점검 질문: 리뷰에서 "LGTM"만 남기면 안 되는 이유는? → 무엇을 봤는지 기록이 없어 리뷰의 가치가 남지 않고, 미션도 라인 근거의 실질 코멘트를 요구합니다(4-5장).

### 목표 4. 충돌이 왜 생기고 충돌 마커는 무엇을 뜻하나요?

> 모범 답안: 두 브랜치가 같은 파일의 같은 부분(또는 바로 붙어 있는 줄)을 서로 다르게 고칠 때, Git이 어느 쪽이 맞는지 판단할 수 없어 사람에게 결정을 맡기는 상태입니다. `<<<<<<< HEAD`부터 `=======`까지는 현재 브랜치의 내용, `=======`부터 `>>>>>>> 브랜치이름`까지는 합치려는 브랜치의 내용입니다. 마커 3종을 모두 지우고 최종 내용만 남긴 뒤 `git add`, `git commit`합니다. 리베이스에서는 HEAD 쪽이 옮겨 붙이려는 대상의 내용이라 반대로 보입니다.

점검 질문: 한 줄 띄운 두 수정은 충돌이 날까요? → 아니요, 자동 병합됩니다. 바로 인접한 줄이면 충돌이 납니다(6-5장 실험 표).

### 목표 5. reset, revert, stash의 차이와 언제 쓰나요?

> 모범 답안: 커밋하지 않은 작업을 잠시 치울 때는 `stash`, 아직 push하지 않은 커밋을 취소하거나 다시 나눌 때는 `reset`(변경을 남기려면 `--soft`), 이미 push한 커밋을 취소할 때는 히스토리를 고치지 않고 되돌리는 새 커밋을 추가하는 `revert`를 씁니다. `reset`은 포인터를 되감는 동작이라 원격과 히스토리가 갈라지므로 공유된 브랜치에서는 쓰지 않습니다.

점검 질문: `reset --soft`, `--mixed`, `--hard`의 차이는? → 커밋은 모두 취소되고, 변경이 각각 스테이징 유지 / 작업폴더만 유지 / 아예 삭제로 남습니다(7-2장 표).

### 목표 6. 문제가 생겼을 때 재현 가능하게 기록하고 설명할 수 있나요?

> 모범 답안: 충돌이나 실수 커밋이 생기면 상황(어느 브랜치·파일·누구), 실행한 명령과 그 출력, 결과와 주의점, 그 방법을 고른 이유를 `docs/conflict-resolution.md`, `docs/troubleshooting-log.md`에 남깁니다. 다른 사람이 그 기록만 보고 같은 절차로 다시 해볼 수 있어야 합니다. 저희는 시나리오마다 터미널 출력을 그대로 붙여 넣었고 참여자 이름과 역할도 적었습니다.

점검 질문: 왜 reset이 아니라 revert를 선택했나요? → 이미 원격에 올라간 커밋이라 히스토리를 고치면 팀원과 갈라지고 강제 푸시가 필요해지기 때문입니다.

### 빠른 확인 문제 10개

아래 질문의 답을 종이로 가리고 말해 보세요. 답은 표 오른쪽에 있습니다.

| # | 질문 | 답 |
| --- | --- | --- |
| 1 | Q. 관리자(admin)인데도 main 브랜치 보호 규칙을 우회할 수 없는 이유는 무엇인가요?

A. 브랜치 보호 설정의 우회 권한은 설정 방식에 따라 다릅니다.

Classic Branch Protection Rule: Do not allow bypassing the above settings 옵션을 활성화하지 않은 경우 관리자 등이 규칙을 우회할 수 있습니다.

Ruleset: Bypass list에 등록된 사용자나 팀만 규칙을 우회할 수 있습니다.

우리 팀 저장소의 protect-main Ruleset은 Bypass list가 비어 있으므로 관리자도 해당 규칙을 우회할 수 없습니다.


| 2 | `git commit --amend` 후 커밋 해시는? | 바뀜다(새 커밋으로 대체, 7-1장) |
| 3 | PR로 병합된 커밋을 `git revert`할 때 필요한 옵션은? | `-m 1`(부모 지정, 7-3장) |
| 4 | `git stash`는 새로 만든 파일도 보관하나? | 아니오, `-u`가 필요(7-4장) |
| 5 | 한 사람이 2번째 줄, 다른 사람이 4번째 줄을 고친 경우에는? | 충돌 없이 자동 병합(6-5장) |
| 6 | 파일 이름 변경과 다른 사람의 내용 수정이 만나면? 삭제와 내용 수정이 만나면? | 이름 변경은 자동 병합, 삭제와 수정은 `modify/delete` 충돌(6-5장) |
| 7 | 내가 쓴 PR을 내가 Approve해 병합할 수 있나? | 없다(공식 문서 확인, 4-4장) |
| 8 | `Closes #3`로 이슈가 자동으로 닫히려면 PR이 어느 브랜치로 병합되어야 하나? | 저장소의 기본 브랜치(main)(4-3장) |
| 9 | `git reset --soft HEAD~1` 후 변경 내용의 상태는? | 스테이징된 상태로 유지(`A  g.txt`, 7-2장) |
| 10 | 리베이스 중 충돌 마커에서 `HEAD` 쪽 내용은 누구 것인가? | 옮겨 붙이려는 대상(예: main) 측 내용(6-2장) |

> 미션 연결: 과제 목표 6개(브랜치 원리, GitHub Flow, PR·리뷰, 충돌, reset·revert·stash, 기록)를 모두 직접 설명할 수 있는지 확인합니다.

## 14. 검증 기록: 무엇을 어떻게 확인했는가

이 문서의 내용은 두 가지 방법으로 검증했습니다. ① Git 명령어는 샌드박스(Git 2.43.0, Python 3.13)에서 직접 실행해 출력을 확인했습니다. ② GitHub 동작은 2026년 11월 19일에 GitHub 공식 문서 페이지를 열어 확인했습니다. 확인하지 못한 부분도 숨기지 않고 아래에 적었습니다.

### 14-1. 직접 실행해 확인한 것 (Git)

실행은 로컬 저장소와 로컬 원격 저장소(bare repository)로 push/pull을 흘내 낸 것이라 GitHub의 PR·Issue·리뷰 화면은 실행할 수 없었습니다.

| 항목 | 결과 | 문서 위치 |
| --- | --- | --- |
| 브랜치는 `.git/refs/heads/<이름>` 파일에 커밋 해시 한 줄, HEAD는 브랜치 참조 | 확인됨 | 1-4 |
| 같은 줄 충돌 마커(`UU`, `<<<<<<< HEAD`) 모양과 해결 후 커밋 | 확인됨 | 6-2, 6-3 |
| 인접한 줄(2번째·3번째)은 충돌, 한 줄 띄운 줄(2번째·4번째)은 자동 병합 | 확인됨 | 6-5 |
| 이름 변경 + 내용 수정은 병합·리베이스 모두 자동 성공, 삭제 + 내용 수정은 `modify/delete` 충돌(`DU`) | 확인됨 | 6-5 |
| 리베이스 충돌에서 `HEAD` 쪽이 옮겨 붙이려는 대상(main)의 내용 | 확인됨 | 6-2 |
| `git merge --abort`, `git rebase --abort`로 되돌리기 | 확인됨 | 6-3, 10-1 |
| main을 내 feature에 합치고(`git merge origin/main`) 일반 push로 PR 갱신 방식 | 확인됨(강제 푸시 불필요) | 6-4 |
| amend: 해시 변경, `--no-edit`로 파일 추가, push 후 amend하면 `non-fast-forward` 거부 | 확인됨 | 7-1 |
| reset `--soft`/`--mixed`/`--hard` 결과 차이, reflog로 복구 | 확인됨 | 7-2 |
| revert: push 후에도 일반 push, 병합 커밋은 `-m 1` 필수 | 확인됨 | 7-3 |
| stash: push/list/pop/apply/drop, 새 파일은 `-u` 필요, 브랜치 전환 차단 오류 | 확인됨 | 7-4 |
| 로컬 main에 실수 커밋 → `git branch` + `reset --hard origin/main`으로 구조 | 확인됨 | 7-7 |
| 시나리오 4종 명령 블록 전체(`restore --staged` 포함)를 처음부터 끝까지 실행 | 정상 동작 | 7-6 |
| `rebase -i`: squash, reword, fixup | 확인됨 | 10-1 |
| 빈 폴더는 커밋에 안 들어가고 `.gitkeep`으로 해결 | 확인됨 | 2-4 |
| 브랜치 이름 규칙(공백·`:`·`?`·`..` 오류, `feature`와 `feature/x` 동시 생성 불가) | 확인됨 | 3-4 |
| 세팅 스크립트(폴더·문서 뼈대 커밋·push, 빈 커밋으로 보호 테스트 후 `reset --hard origin/main`) | 정상 동작 | 단계 1 |
| FAQ 재현: push 거부, divergent pull 안내, Author identity, detached HEAD, `git rm --cached` | 확인됨 | 12장 |
| 커밋 메시지 점검 스크립트: `temp`, `wip 1`, `fix`는 NG, `Revert "..."`, `fix: ...`는 OK | 확인됨 | 5-5 |
| (A) 유틸 함수 예시 `doctest` 3개 테스트 통과 | 확인됨 | 9-2 |

### 14-2. GitHub 공식 문서로 확인한 것

다음 페이지를 실제로 열어 내용을 확인했습니다.

| 확인한 내용 | 출처 |
| --- | --- |
| 무료 플랜은 공개 저장소에서만 브랜치 보호 가능, admin 기본 예외, 강제 푸시 기본 차단 | [About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) |
| Settings → Branches → Add classic branch protection rule, 옵션 이름 | [Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) |
| 닫는 키워드 9개, 기본 브랜치 병합 시에만 자동 닫힘, Development 사이드바 수동 연결 | [Linking a pull request to an issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue) |
| CODEOWNERS 위치·우선순위, write 권한, 자동 리뷰 요청, 비공개 저장소 제한 | [About code owners](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) |
| GitHub flow 6단계와 기본 브랜치 원칙 | [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) |
| PR 작성자는 자기 PR을 승인할 수 없음 | [Approving a pull request with required reviews](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/approving-a-pull-request-with-required-reviews) |
| 리뷰 유형 3가지(Comment, Approve, Request changes) | [About pull request reviews](https://docs.github.com/enterprise-cloud@latest//pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/about-pull-request-reviews) |

### 14-3. 확인하지 못한 것, 직접 한 번 확인하세요

- **GitHub 화면의 버튼·메뉴 이름 일부**: Compare & pull request, Reviewers, Delete branch, Resolve conversation, Require conversation resolution before merging, Organization 생성·People 초대 메뉴는 공식 문서로 직접 확인하지 못했습니다. 자주 쓰이는 이름이지만 화면이 다르면 비슷한 이름을 찾아보세요.
- **보호 규칙이 걸린 뒤 실제 push 거부 문구**: 샌드박스는 GitHub가 아니라서 직접 만들어 보지 못했습니다. 11장 단계 1의 테스트로 팀이 직접 확인하세요.
- **`.github/pull_request_template.md` 자동 적용**, **Merge 버튼 3종(Create a merge commit / Squash and merge / Rebase and merge) 설명**, **인증 방식(Q7)**: 일반적인 동작을 정리했고 공식 문서를 열어 확인하지는 않았습니다.
- **편집기(vim) 조작순서**: 일반적인 사용법입니다. 환경에 따라 편집기가 다를 수 있습니다.
- **시간 배분과 추천안**(네이밍, 커밋 타입, 리뷰 순환표, 시나리오 분담)은 제 제안이지 미션 요구사항이 아닙니다. 미션 요구사항과 충돌하면 미션이 우선입니다.
- **출력 차이**: Git 버전이나 운영체제(특히 Windows 터미널)에 따라 안내 문구가 조금 다를 수 있습니다. 명령의 동작 원리는 같습니다.

### 14-4. 마지막으로, 미션 원문과 대조한 결과

미션 원문의 요구사항을 하나씩 대조했습니다. 저장소·폴더·Branch Protection(2장), GitHub Flow 및 네이밍 및 3줄 이유(3장), Issue·PR 연동과 리뷰 기준(4장), 커밋 컨벤션과 금지 기준(5장), 충돌과 비자명 충돌(6장), 트러블슈팅 4종(7장), 문서 4개와 증빙(8장), 결과물 3옵션과 팀원별 최소 기준(9장), 보너스 2개(10장), 과제 목표 6개(13장)를 모두 다룹니다. 특히 팀원별 최소 기준 5가지(PR 2, 리뷰 2, 리뷰 반영 1, 시나리오 참여 1, 결과물 커밋 1)는 9-5장 체크리스트와 11장 실행 단계에 이중으로 연결해 두었습니다.
