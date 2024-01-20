import pytest

from app.model.pilot import Pilot


@pytest.fixture
def fix_pilot() -> Pilot:
    return Pilot(id="Mocked#Pilot", name="TestPilot")
