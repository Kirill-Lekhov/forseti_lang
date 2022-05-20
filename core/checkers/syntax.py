from typing import List


_OPERATORS = ("AND", "OR", "NOT", "И", "ИЛИ")
ERRORS = {
	"operator_position": "Оператор '{}' используется без {} выражения. Позиция {}",
}


def check_syntax(command: str):
	command = command.replace(" И ", " AND ")
	command = command.replace(" ИЛИ ", " OR ")
	command_parts = command.split()
	parts_number = len(command_parts)

	for i in range(parts_number):
		if command_parts[i] in _OPERATORS:
			word_start_symbol_num = get_word_start_symbol_num(i, command_parts)

			if i == 0:
				raise SyntaxError(ERRORS['operator_position'].format(command_parts[i], 'левостороннего', word_start_symbol_num))

			elif i == parts_number - 1:
				raise SyntaxError(ERRORS['operator_position'].format(command_parts[i], 'правостороннего', word_start_symbol_num))

			if command_parts[i] == "NOT":
				if command_parts[i - 1] != "AND":
					raise SyntaxError("Оператор 'NOT' не может использоваться без оператора 'AND'")

			if command_parts[i] in _OPERATORS:
				if command_parts[i - 1]:
					pass



def get_word_start_symbol_num(word_position: int, split_text: List[str]):
	word_start_symbol_num = sum(map(len, split_text[:word_position])) + word_position

	return word_start_symbol_num + 1
