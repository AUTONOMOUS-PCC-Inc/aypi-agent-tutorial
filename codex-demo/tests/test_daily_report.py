"""이 파일이 명세다. 여기 적힌 기대값이 맞는 동작이고, `daily_report.py` 가 틀렸다.

실행 (`-X utf8` 를 빼면 윈도우에서 한글이 깨진다):
    python -X utf8 -m unittest discover -s tests -v

일곱 개 중 **다섯이 빨갛다** — 값이 틀린 것 셋(FAIL), 아예 터지는 것 둘(ERROR).
하지만 **원인은 세 곳뿐이다.** Codex에게 이렇게 시켜 보자:

    테스트를 돌려서 실패하는 걸 전부 고쳐 줘. 명세는 tests/ 안에 있어.
    data/logs.csv 와 tests/ 는 고치지 말고 daily_report.py 만 고쳐.
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import daily_report  # noqa: E402


# 이미 공백이 정리된 상태의 기록. 함수 하나씩 따로 보려고 손으로 만들었다.
ROWS = [
    {"날짜": "2026-11-07", "작업": "데이터 백업", "소요분": "30", "상태": "완료"},
    {"날짜": "2026-11-07", "작업": "회의록 정리", "소요분": "25", "상태": "완료"},
    {"날짜": "2026-11-07", "작업": "청구서 발송", "소요분": "60", "상태": "실패"},
    {"날짜": "2026-11-07", "작업": "재고 확인", "소요분": "15", "상태": "진행중"},
    {"날짜": "2026-11-07", "작업": "고객 응대", "소요분": "40", "상태": "완료"},
]


class TestLoadRows(unittest.TestCase):
    def test_값의_앞뒤_공백은_제거된다(self):
        """CSV에 손으로 적다 보면 공백이 섞인다. 읽을 때 정리해야 한다."""
        rows = daily_report.load_rows()
        for row in rows:
            for key, value in row.items():
                self.assertEqual(value, value.strip(), f"{key} 값에 공백이 남아 있다: {value!r}")


class TestFilterByDate(unittest.TestCase):
    def test_그_날짜만_추린다(self):
        rows = [
            {"날짜": "2026-11-06", "상태": "완료"},
            {"날짜": "2026-11-07", "상태": "완료"},
        ]
        self.assertEqual(len(daily_report.filter_by_date(rows, "2026-11-07")), 1)

    def test_공백이_섞인_날짜도_같은_날로_센다(self):
        """읽을 때 공백이 정리되면 이 테스트는 저절로 통과한다."""
        rows = daily_report.load_rows()
        self.assertEqual(len(daily_report.filter_by_date(rows, "2026-11-07")), 5)


class TestTotalMinutes(unittest.TestCase):
    def test_소요분을_숫자로_더한다(self):
        """CSV에서 읽은 값은 전부 문자열이다. 숫자로 바꿔 더해야 한다."""
        self.assertEqual(daily_report.total_minutes(ROWS), 170)


class TestCountStatus(unittest.TestCase):
    def test_완료_건수(self):
        self.assertEqual(daily_report.count_status(ROWS, "완료"), 3)

    def test_실패_건수(self):
        """'완료가 아닌 것'이 곧 '실패'는 아니다. 진행중이 섞여 있다."""
        self.assertEqual(daily_report.count_status(ROWS, "실패"), 1)


class TestReportLine(unittest.TestCase):
    def test_요약_한_줄(self):
        self.assertEqual(
            daily_report.report_line("2026-11-07"),
            "2026-11-07 · 5건 · 총 170분 · 완료 3 · 실패 1 · 진행중 1",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
