"""Checks that the interview guide's reference numbers and quiz parser stay consistent."""
import importlib.util
from pathlib import Path

GUIDE = Path(__file__).resolve().parent.parent / "interview-guide"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, GUIDE / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_ref_w_headline_numbers():
    ref = _load("ref_w")
    s = ref.summary(ref.BASE)
    assert round(s["revenue"], 1) == 193.9
    assert round(s["total_cost"], 1) == 162.9
    assert round(s["margin"], 3) == 0.160
    assert round(s["irr"], 3) == 0.236
    assert round(s["peak_funding"], 1) == 54.7


def test_ref_w_absorption_sensitivity():
    ref = _load("ref_w")
    assert round(ref.summary({**ref.BASE, "absorb_q": 20})["irr"], 3) == 0.134


def test_quiz_finds_tagged_questions():
    quiz = _load("quiz")
    questions = quiz.load_questions(GUIDE)
    tags = {q["tag"] for q in questions}
    assert {"land", "appr", "jda", "feas", "cf", "am", "cap", "model", "behav"} <= tags
    assert all(q["answer"] for q in questions)
    assert sum(q["tag"] == "model" for q in questions) == 40
