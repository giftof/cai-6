"""
Module priority calculator
"""
from david.calculator import add, subtract, multiply, divide, to_int
from dataclasses import dataclass
from typing import Union, Callable


@dataclass
class Operation:
    left: Union[float, "Operation", None] = None
    op: Union[Callable[[int, int], float], None] = None
    right: Union[float, "Operation", None] = None
    depth: int = 0


operator_constants = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def get_key_by_operator_method(target_value: Callable[[int, int], float]):
    for key, value in operator_constants.items():
        if value == target_value:
            return key
    return None


def bracket_open(it: iter, container: Operation):
    print('bracket_open')


def bracket_close(it: iter, container: Operation):
    print('bracket close')


bracket_constants = {
    '(': bracket_open,
    ')': bracket_close,
}


def expression_operator(op: Callable[[int, int], float], group: Operation) -> Operation:
    if group.op is not None:
        raise ValueError(f'Syntax error: two consecutive operators found: {get_key_by_operator_method(group.op)}, {get_key_by_operator_method(op)}')
    elif group.left is None:
        raise ValueError(f'An operator was found without a corresponding operand.')
    else:
        group.op = op
        return group


def get_left(group: Operation) -> Union[int, 'Operation']:
    if isinstance(group.left, Operation):
        if group.left.op not in [multiply, divide]:
            return group.left.right
    return group.left


def set_left(group: Operation, attach: Union[int, 'Operation']) -> Operation:
    if isinstance(group.left, Operation):
        if group.left.op not in [multiply, divide]:
            group.left.right = attach
        else:
            group.left = attach
    else:
        group.left = attach
    return group


def expression_numbers(num: int, group: Operation) -> Operation:
    if group.op is None:
        group.left = num
        return group
    elif group.op is multiply or group.op is divide:
        re_group = Operation(left = get_left(group), op = group.op, right = num, depth=group.depth)
        group = set_left(group, re_group)
        return Operation(left = group.left, depth=group.depth)
    else:
        group.right = num
        return Operation(left = group)


def expression_grouping(it: iter, group: Operation) -> Operation:
    try:
        reserve = group
        depth = 0
        for e in it:
            if e == '(':
                depth += 1
            elif e == ')':
                depth -= 1
            else:
                is_op = operator_constants.get(e)
                group.depth = depth
                if is_op:
                    reserve = expression_grouping(it, expression_operator(is_op, group))
                else:
                    is_int = to_int(e)
                    reserve = expression_grouping(it, expression_numbers(is_int, group))
        return reserve
    except ValueError as e:
        raise e


def calculate(group: Operation) -> float:
    if isinstance(group.left, Operation):
        left = calculate(group.left)
    else:
        left = group.left
    if isinstance(group.right, Operation):
        right = calculate(group.right)
    else:
        right = group.right
    return group.op(int(left), int(right))


def main():
    """
    this is method docstring
    """
    try:
        array = [e for e in input('Enter Expression: ').split(' ') if e.strip().lower()]
        if not len(array):
            raise ValueError('Input Some Value...')
        expression = expression_grouping(iter(array), Operation())
        if not expression.op and not expression.right:
            print(f'Result: {calculate(expression.left)}')
        else:
            if expression.op:
                raise ValueError(f'An operator was found without a corresponding operand.')
            print(expression)
            raise ValueError('some thing Wrong...')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()

# ( 1 + 2 ) / ( 0 + ( 3 * ( 4 + 5 ) ) )
# ( 1 ) + ( 2 )
# 1 + 2 * 3
