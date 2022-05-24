from .parse import parse_items
from .exceptions import ForsetiSyntaxError

import pytest


@pytest.mark.parametrize(
	"condition",
	[
		"TRUE AND )FALSE(",
		"TRUE AND (()FALSE))(",
	]
)
def test_parse_items_exceptions(condition):
	with pytest.raises(ForsetiSyntaxError, match="The closing bracket is met before using the opening one"):
		parse_items(condition)


@pytest.mark.parametrize(
	"condition, expected_result",
	[
		("TRUE AND ((FALSE))", [['TRUE AND ', 'ATOM_1'], ['ATOM_2'], ['FALSE']]),
		("TRUE AND FALSE OR (TRUE AND (FALSE OR TRUE))", [['TRUE AND FALSE OR ', 'ATOM_1'], ['TRUE AND ', 'ATOM_2'], ['FALSE OR TRUE']]),
		("TRUE AND FALSE", [['TRUE AND FALSE']]),
		("", [[]])
	]
)
def test_parse_items_results(condition, expected_result):
	assert parse_items(condition) == expected_result
