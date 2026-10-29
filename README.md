<div align="center">

<img src="https://raw.githubusercontent.com/AUTONOMOUS-PCC-Inc/.github/main/mirrors/assets/agent-banner.svg" alt="바이브코딩 캠프 4회차 — 매주 반복하는 일 하나를 에이전트에게 넘긴다. 오전엔 코드로, 오후엔 노코드로." width="100%">

### 매주 반복하는 일 하나를, 오늘 안에 에이전트에게 넘긴다.

AUTONOMOUS PCC 바이브코딩 캠프 **4회차(자동화 에이전트 개발)** 실습 저장소입니다.<br>
오전에는 **코드로**, 오후에는 **노코드로** — 같은 일을 두 가지 방식으로 자동화합니다.

![Day](https://img.shields.io/badge/과정-4회차%20하루-0B1B33?style=for-the-badge)
![AM](https://img.shields.io/badge/오전-Codex-1E6FD9?style=for-the-badge)
![PM](https://img.shields.io/badge/오후-N8N-7C3AED?style=for-the-badge)
![Key](https://img.shields.io/badge/API%20키-0개-16A34A?style=for-the-badge)
![Install](https://img.shields.io/badge/추가%20설치-없음-EAB308?style=for-the-badge)

[**시작하기**](#시작하기) · [**폴더 지도**](#폴더-지도) · [**하루 흐름**](#하루-흐름) · [**오전**](#오전--코드-쪽-에이전트) · [**오후**](#오후--노코드-쪽-에이전트) · [**자주 막히는 곳**](#자주-막히는-곳)

</div>

---

## 시작하기

> [!IMPORTANT]
> **오늘은 새로 설치할 게 없습니다.** Codex는 1회차에 깔았고,
> N8N 계정은 3회차에 만들었습니다. 둘 다 그대로 씁니다.

```bat
git clone https://github.com/AUTONOMOUS-PCC-Inc/aypi-agent-tutorial.git
cd aypi-agent-tutorial
```

| 준비물 | 어디서 왔나 | 확인하는 법 |
|---|---|---|
| **Codex** 로그인 | 1회차에서 깐 것 | `codex --version` |
| **N8N** 계정 | 3회차에서 가입한 것 | 로그인이 되면 끝 |
| **파이썬** | 1회차 conda 환경 `aypi-car` | `conda activate aypi-car` 후 `python --version` |
| **구글 계정** | 각자 쓰던 것 | 오후에 메일 보낼 때 씁니다 |

> [!TIP]
> **개인 구글 계정을 권합니다.** 학교 계정은 관리자가 외부 앱 연결을 막아 둔
> 경우가 있어 오후에 메일 단계에서 막힐 수 있습니다.

---

## 폴더 지도

하루 종일 "지금 어느 폴더에 있어야 하지"가 가장 자주 막히는 지점이라,
먼저 봐 두면 좋습니다.

<div align="center">
<img src="https://raw.githubusercontent.com/AUTONOMOUS-PCC-Inc/.github/main/mirrors/assets/agent-layout.svg" alt="폴더 지도 — 클론에 따라오는 것, 직접 채우는 것, 끝까지 건드리지 않는 것을 색으로 구분" width="100%">
</div>

기억할 것은 둘입니다. **오전에 고치는 파일은 `codex-demo/daily_report.py` 하나**,
**`tests/` 와 `data/` 는 끝까지 건드리지 않습니다.**

---

## 하루 흐름

```
오전  개념 ──→ Codex의 루프를 눈으로 ──→ 도구 연동 ──→ 워크시트 작성
                                                           │
점심                                                        │ 설계도를 들고
                                                           ▼
오후  레일 한 번 ──→ 일부러 깨 보기 ──→ 내 업무로 변형 ──→ 비교
```

**오전의 산출물(워크시트)이 오후의 입력입니다.** 오전에 손을 놓고 있으면
오후에 만들 게 없습니다.

---

## 오전 — 코드 쪽 에이전트

> 자세한 건 [`codex-demo/README.md`](codex-demo/README.md)

깨진 프로그램을 Codex에게 고치게 하고, **그 과정을 눈으로 봅니다.**

<div align="center">
<img src="https://raw.githubusercontent.com/AUTONOMOUS-PCC-Inc/.github/main/mirrors/assets/agent-loop.svg" alt="에이전트 루프 — 돌린다, 돌아온 걸 읽는다, 한 군데 고친다. 오전엔 Codex로 오후엔 N8N으로, 도구만 바뀌고 원은 그대로다" width="100%">
</div>

답을 한 번에 뱉는 게 아니라 **스스로 다음 할 일을 고르는 것** — 이게 에이전트입니다.
그리고 **오후에 돌 원도 똑같이 생겼습니다.** 도구만 바뀝니다.

```bat
cd codex-demo
python -X utf8 -m unittest discover -s tests -v
```

일곱 개 중 다섯이 빨갛습니다. 원인은 세 곳뿐입니다.

---

## 오후 — 노코드 쪽 에이전트

> 자세한 건 [`n8n/README.md`](n8n/README.md)

오전과 **같은 일**을 N8N으로 합니다. 전원이 똑같은 레일을 한 번 돌린 다음,
각자 자기 업무로 갈아 끼웁니다.

<div align="center">
<img src="https://raw.githubusercontent.com/AUTONOMOUS-PCC-Inc/.github/main/mirrors/assets/agent-rail.svg" alt="오후 레일 — 스케줄, 공개 API 호출, LLM 1회, Gmail. API 키 0개, 계정 1개. 양 끝만 바꾸면 내 업무가 된다" width="100%">
</div>

**API 키가 하나도 필요 없습니다.** 계정은 구글 하나뿐입니다.
바꾸는 건 **양 끝 두 개**뿐이고, 가운데는 그대로 둡니다.

> [!CAUTION]
> **AI Agent 노드에 도구를 붙여 루프를 돌리지 마세요.** 실행 한 건에 모델 호출이
> 열 번 넘게 나갑니다. 체험판은 크레딧을 다 쓰면 **충전할 수 없어** 수업 중에
> 멈춥니다. 같은 이유로 **계정을 공유하지 마세요** — 잔액은 인스턴스 단위입니다.

---

## 자주 막히는 곳

| 증상 | 왜 | 어떻게 |
|---|---|---|
| 테스트 이름이 `test_������` 처럼 깨진다 | 윈도우 콘솔이 UTF-8이 아니다 | `python` 뒤에 **`-X utf8`** 을 붙인다 |
| `'python'은(는) 내부 또는 외부 명령...` | conda 환경이 켜지지 않았다 | `conda activate aypi-car` 를 먼저 |
| 테스트가 갑자기 전부 통과한다 | `tests/` 를 고쳤을 가능성이 높다 | `git restore tests/` 로 되돌린다 |
| Codex가 파일을 안 고치고 묻기만 한다 | 승인 모드가 `read-only` 다 | `workspace-write` 로 바꾼다 |
| 구글 로그인 창이 안 뜬다 | 브라우저가 팝업을 막았다 | 주소창 오른쪽에서 팝업 허용 |
| 구글 로그인이 거부된다 | 학교 계정이 외부 앱을 막았다 | **개인 구글 계정**으로 한다 |
| 요약 노드에서 멈춘다 | Gateway 크레딧을 다 썼을 수 있다 | 에이전트 루프를 썼는지 본다. 워크플로우를 다시 import |
| 워크플로우를 망가뜨렸다 | — | `rail-skeleton.json` 을 다시 import하면 처음 상태 |

---

## 만든 사람들

|     EL     |
|   :-----:   |
|   Aaron Yoon    |

1회차 실습 저장소는 [`aypi-car-tutorial`](https://github.com/AUTONOMOUS-PCC-Inc/aypi-car-tutorial),
2회차는 [`aypi-turtlebot-tutorial`](https://github.com/AUTONOMOUS-PCC-Inc/aypi-turtlebot-tutorial),
3회차는 [`aypi-metaverse-tutorial`](https://github.com/AUTONOMOUS-PCC-Inc/aypi-metaverse-tutorial) 입니다.

---

<div align="center">
<sub><strong>AUTONOMOUS PCC, Inc.</strong> · (주)오토노머스피씨씨 — 바이브코딩 캠프 4회차 실습</sub><br>
<sub><a href="https://github.com/AUTONOMOUS-PCC-Inc">github.com/AUTONOMOUS-PCC-Inc</a></sub>
</div>
