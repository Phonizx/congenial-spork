from unittest.mock import patch

import pytest

from app.middleware.pilot import create_pilot
from app.model.pilot import Pilot


@pytest.mark.asyncio
async def test_create_pilot_happy_flow(fix_pilot: Pilot):
    with patch("app.database.BaseCrud.CRUDBase.create"):
        await create_pilot(pilot=fix_pilot)
