from hunt.scoring import MAX_COVERAGE, alignment, combo, priority


def test_max_coverage():
    assert MAX_COVERAGE == 66


def test_perfect_role_is_100():
    assert alignment({k: 3 for k in ["land", "appr", "jda", "feas", "design", "cf", "proc",
                                      "deliv", "cost", "lease", "am", "cap"]}) == 100


def test_combo_labels():
    assert combo({"feas": 3, "cap": 2}) == "Deal + money"
    assert combo({"land": 3, "jda": 3, "appr": 2}) == "Deal core"
    assert combo({"am": 3}) == "Money side"
    assert combo({"appr": 3}) == "Single-function"


def test_priority_uses_default_culture():
    s = {"land": 3, "jda": 3, "feas": 3, "appr": 2, "cf": 1, "design": 1}
    assert priority(s, "A", None) == round(0.55 * alignment(s) + 30 + 0.15 * 72)
