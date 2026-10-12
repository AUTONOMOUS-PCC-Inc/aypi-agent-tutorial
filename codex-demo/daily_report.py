"""하루치 업무 로그에서 요약 한 줄을 만든다.

`data/logs.csv` 를 읽어 특정 날짜의 기록만 추려 이런 줄을 만드는 것이 목표다.

    2026-11-07 · 5건 · 총 170분 · 완료 3 · 실패 1 · 진행중 1

지금은 **테스트가 빨갛다.** 고치는 건 여러분이 아니라 Codex의 일이다.
`tests/test_daily_report.py` 가 기대하는 동작이 곧 명세다.
"""

import csv
from pathlib import Path

DATA = Path(__file__).parent / "data" / "logs.csv"


def load_rows(path=DATA):
    """CSV를 읽어 딕셔너리 목록으로 돌려준다."""
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def filter_by_date(rows, date):
    """그 날짜의 기록만 추린다."""
    return [row for row in rows if row["날짜"] == date]


def total_minutes(rows):
    """소요 시간을 모두 더한다."""
    total = 0
    for row in rows:
        total += row["소요분"]
    return total


def count_status(rows, status):
    """해당 상태인 기록이 몇 건인지 센다."""
    done = sum(1 for row in rows if row["상태"] == "완료")
    if status == "완료":
        return done
    return len(rows) - done


def report_line(date, path=DATA):
    """요약 한 줄을 만든다."""
    rows = filter_by_date(load_rows(path), date)
    return (
        f"{date} · {len(rows)}건 · 총 {total_minutes(rows)}분 · "
        f"완료 {count_status(rows, '완료')} · "
        f"실패 {count_status(rows, '실패')} · "
        f"진행중 {count_status(rows, '진행중')}"
    )


if __name__ == "__main__":
    print(report_line("2026-11-07"))
