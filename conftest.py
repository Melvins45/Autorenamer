from main_for_tests import main as mainFunction
import pytest

@pytest.fixture
def main(qtbot) :
    principal = mainFunction()
    qtbot.addWidget(principal)
    # principal.show()
    # qtbot.waitExposed(principal)
    return principal