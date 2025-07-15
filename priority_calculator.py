"""
Module priority calculator
"""
from david.calculator import add, subtract, multiply, divide, to_int
from dataclasses import dataclass
from typing import Union, Callable


def import_test() -> None:
    print('hello world')
    print(add(1, 2))
    print(subtract(2, 1))
    print(multiply(2, 3))
    print(divide(6, 2))


@dataclass
class Operation:
    left: Union[float, "Operation", None] = None
    op: Union[Callable[[int, int], float], None] = None
    right: Union[float, "Operation", None] = None


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


def expression_operator(op: Callable[[int, int], float], container: Operation) -> Operation:
    if container.op is not None:
        raise(f'연속된 연산자 에러: {get_key_by_operator_method(container.op)}, {get_key_by_operator_method(op)}')
    elif container.left is None:
        raise(f'대상이 없는 연산자')
    else:
        container.op = op
        return container


def get_left_rigth(container: Operation) -> Union[int, 'Operation']:
    if isinstance(container.left, Operation):
        return container.left.right
    return container.left


def set_left_right(container: Operation, attach: Union[int, 'Operation']) -> Operation:
    if isinstance(container.left, Operation):
        container.left.right = attach
    else:
        container.left = attach
    return container


def expression_numbers(num: int, container: Operation) -> Operation:
    if container.op is None:
        container.left = num
        return container
    elif container.op is multiply or container.op is divide:
        re_container = Operation(left = get_left_rigth(container), op = container.op, right = num)
        container = set_left_right(container, re_container)
        return Operation(left = container.left)
    else:
        container.right = num
        return Operation(left = container)


def expression_grouping(it: iter, container: Operation) -> Operation:
    try:
        reserve = container
        for e in it:
            mod = e.strip().lower()
            is_op = operator_constants.get(mod)
            if is_op:
                reserve = expression_grouping(it, expression_operator(is_op, container))
            else:
                is_int = to_int(mod)
                reserve = expression_grouping(it, expression_numbers(is_int, container))
        return reserve
    except ValueError as e:
        raise e


def main():
    """
    this is method docstring
    """
    try:
        import_test()
        array = [e for e in input('Enter Expression: ').split(' ') if e.strip()]
        root = Operation()
        expression = expression_grouping(iter(array), root)
        print(expression)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
