from importlib.metadata import version

import axiolock


def test_package_imports() -> None:
    assert axiolock.__name__ == "axiolock"
    assert version("axiolock") == "0.1.0"
