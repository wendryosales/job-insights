from src.counter import count_ocurrences


def test_counter():
    path = "src/jobs.csv"
    python_results = count_ocurrences(path, "Python")
    javascript_results = count_ocurrences(path, "Javascript")
    assert python_results == 1639
    assert javascript_results == 122
