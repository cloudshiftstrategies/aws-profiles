from aws_profile import aws_profile
from io import TextIOWrapper, BytesIO
from unittest import mock


@mock.patch('configparser.open')
def test_list(mock_file_open: mock.MagicMock):
    with open("tests/resources/mock_config.ini") as fh:
        config = bytes(fh.read(), "utf-8")
    mock_file_open.return_value = TextIOWrapper(BytesIO(config))
    result = aws_profile.list_profiles()
    assert result == ["foo"]
