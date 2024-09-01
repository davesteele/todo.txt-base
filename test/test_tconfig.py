
import textwrap
import subprocess
from unittest.mock import Mock

import pytest

from todo_txt_base import tconfig


@pytest.fixture
def config(monkeypatch):
    config_data = textwrap.dedent(
        """
            executable = /usr/bin/topydo
            config_file = /etc/topydo.conf
            extraneous = foo
        """
    )

    cpmock = Mock()
    cpmock.stdout = config_data
    runmock = Mock(return_value=cpmock)
    monkeypatch.setattr(tconfig.subprocess,"run", runmock)

    return None


def test_config_internal(config):
    assert tconfig.get_var("executable") == "/usr/bin/topydo"


def test_config_miss(config):
    with pytest.raises(tconfig.TDTBaseException):
        tconfig.get_var("bogus")

