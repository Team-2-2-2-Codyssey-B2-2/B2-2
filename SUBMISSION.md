# Submission Index

## Team

- 팀명: B2-2 (코디세이 11월 미션톤)
- 저장소: https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2
- 구성: GitHub Organization 저장소(옵션 A), 3인
- 브랜치 전략: GitHub Flow (`main` + `feature/*`), `main`은 Ruleset `protect-main`으로 보호
  - PR 필수 + 승인 1명 이상, force push·브랜치 삭제 금지, bypass 대상 없음
- 결과물: (A) Python 유틸 함수 모음 (`src/`, 사용 예시는 doctest)

| 팀원 (GitHub) | 역할 |
|---|---|
| [tlswltjq](https://github.com/tlswltjq) | 저장소 admin, 기본 구조·`.gitignore`, `list_utils`, CONTRIBUTING 브랜치 전략 |
| [ewisewjd](https://github.com/ewisewjd) | Git 협업 학습자료, `dict_utils`, stash 시나리오, 충돌 기록 #2 |
| [NiceTry3675](https://github.com/NiceTry3675) | 충돌·트러블슈팅 템플릿, `string_utils`, 충돌 기록 #1, reset·revert 시나리오, SUBMISSION |

## Member Contributions

> PR 링크 형식: `https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/<번호>`, Issue는 `.../issues/<번호>`

### tlswltjq

- 만든 Issue: [#1](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/1), [#2](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/2), [#9](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/9), [#18](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/18)
- 만든 PR (병합)
  - [#3](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/3) docs: 프로젝트 디렉토리 구성 및 일부 문서 추가 (Closes #1)
  - [#10](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/10) feat: 리스트 유틸 함수(list_utils) 추가 (Closes #9)
  - [#19](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/19) docs: CONTRIBUTING 브랜치 전략·네이밍 규칙 (Closes #18) — 진행 중
- 리뷰 (본인 PR 제외)
  - [#5](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/5) 시나리오 담당자 지정 방식 의견 → 반영됨
  - [#8](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/8) `_SEPARATORS`에 `_` 추가 suggestion(`foo_-bar` 케이스) → 반영됨
  - [#13](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/13) README 중복 제목 제거 suggestion → 반영됨
  - [#15](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/15) 충돌 #1 해결 절차가 실제와 일치함을 확인 후 승인
  - [#17](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/17) 승인
- 리뷰 반영: #3 (`.gitignore` suggestion 적용, What/Why/How 보완), #10 (`5cd9624` 지원 범위 문서화)
- 트러블슈팅: 시나리오 1 `amend` (#10)
- 충돌 해결: 충돌 #1 해결(`8624041`, PR #8 웹 에디터)
- 결과물: `src/list_utils.py`

### ewisewjd

- 만든 Issue: [#11](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/11), [#12](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/12), [#16](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/16), [#20](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/20)
- 만든 PR (병합)
  - [#6](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/6) docs: Git 협업 학습자료 (Closes #11)
  - [#13](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/13) feat: 딕셔너리 유틸 함수(dict_utils) 추가 (Closes #12)
  - [#17](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/17) docs: stash 트러블슈팅 시나리오 기록 (Closes #16)
  - [#21](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/21) docs: README 충돌 해결 사례 기록 (Closes #20) — 진행 중
- 리뷰 (본인 PR 제외)
  - [#8](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/8) 음수 `max_length` 검사 제안 → 반영됨
  - [#10](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/10) `chunk`/`unique` 구현 피드백 코멘트
  - (추가 예정)
- 리뷰 반영: #6 (`14aa361`, `c29f19b`), #13 (`5210e3f`), #17 (`79bedd1`)
- 트러블슈팅: 시나리오 4 `stash` (#17)
- 충돌 해결: 충돌 #2 해결(`ba1e7b5`, PR #13)
- 결과물: `src/dict_utils.py`

### NiceTry3675

- 만든 Issue: [#4](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/4), [#7](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/7), [#14](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/14), [#22](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/22), [#23](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/issues/23)
- 만든 PR (병합)
  - [#5](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/5) docs: 충돌 해결 / 트러블슈팅 기록 템플릿 추가 (Closes #4)
  - [#8](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/8) feat: 문자열 유틸 함수(string_utils) 추가 (Closes #7)
  - [#15](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/15) docs: 충돌 기록 #1 및 시나리오 2(reset --soft) 기록 (Closes #14)
  - SUBMISSION.md 및 시나리오 3(revert) 기록 (Closes #23) — 이 PR
- 리뷰 (본인 PR 제외)
  - [#3](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/3) `.gitignore` 코드 펜스 suggestion, What/Why/How 요청 → 반영 후 승인
  - [#6](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/6) Issue 미연동 Request changes, 파일명·Ruleset 설명 지적 → 반영 후 승인
  - [#10](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/10) `chunk` 제너레이터 미지원 재현·대안 제시 → 문서화로 반영
  - [#13](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/13) 빈 dict 소실·`deep_merge` 원본 공유 재현 → 반영 후 승인
  - [#17](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/17) `stash pop` 실패 리스크 재현
  - [#19](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/19), [#21](https://github.com/Team-2-2-2-Codyssey-B2-2/B2-2/pull/21) 규칙 운영·충돌 기록 사실관계 지적
- 리뷰 반영: #5 (`7009702`), #8 (`dc8b769`, `5213a3c`)
- 트러블슈팅: 시나리오 2 `reset --soft` (#15), 시나리오 3 `revert` (이 PR)
- 충돌 기록: 충돌 #1 기록(#15, 해결 당사자 tlswltjq 확인)
- 결과물: `src/string_utils.py`

## Key Docs

- Contributing: [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)
- Conflict log: [docs/conflict-resolution.md](docs/conflict-resolution.md)
  - 충돌 #1 (비자명: 같은 hunk) README 유틸 함수 표 — PR #8 ↔ PR #10, 해결 `8624041`
  - 충돌 #2 README 유틸 함수 표 — PR #13 ↔ `main`, 해결 `ba1e7b5` (기록: PR #21)
- Troubleshooting: [docs/troubleshooting-log.md](docs/troubleshooting-log.md)
  - amend(tlswltjq) / reset --soft(NiceTry3675) / revert(NiceTry3675) / stash(ewisewjd)
- 결과물 목록: [README.md](README.md) "유틸 함수 목록"
- 학습자료: [docs/study/git-collaboration-guide.md](docs/study/git-collaboration-guide.md)

## Evidence

- Git 히스토리: `evidence/git-log.txt` (`git log --oneline --graph --all`) — 모든 PR 병합 후 최종 생성 예정
- 검증 방법: `python3 -m doctest src/<파일명>.py -v` (Python 3.10+)
