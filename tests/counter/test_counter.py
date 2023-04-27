from src.pre_built.counter import count_ocurrences


def test_counter():
    file_path = "data/jobs.csv"
    assert count_ocurrences(file_path, "PYTHON") == 1639
    assert count_ocurrences(file_path, "JavaSCRIPT") == 122
    assert count_ocurrences(file_path, "java") == 676
