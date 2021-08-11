from click.testing import CliRunner
from pytest_mock import MockerFixture

from check_patroni.cli import main

from tools import my_mock


def test_node_is_primary_ok(mocker: MockerFixture) -> None:
    runner = CliRunner()

    my_mock(mocker, "node_is_primary_ok", 200)
    result = runner.invoke(main, ["-e", "https://10.20.199.3:8008", "node_is_primary"])
    assert result.exit_code == 0


def test_node_is_primary_ko(mocker: MockerFixture) -> None:
    runner = CliRunner()

    my_mock(mocker, "node_is_primary_ko", 404)
    result = runner.invoke(main, ["-e", "https://10.20.199.3:8008", "node_is_primary"])
    assert result.exit_code == 2
