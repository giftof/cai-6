from david.calculator import add, subtract, multiply, divide, to_int
from dataclasses import dataclass
from typing import Callable, Union


op_const = {
    '*': multiply,
    '/': divide,
    '+': add,
    '-': subtract
}


@dataclass
class G:
    left: Union[int, 'G', None] = None
    op: Union[Callable[[float, float], float], None] = None
    right: Union[int, 'G', None] = None
    block: bool = False


def set_op(g, op):
    if g.left is None:
        raise ValueError(f'op need num: {g}')
    if g.op:
        raise ValueError('double op not allow')
    g.op = op
    return g


def h_pri(g, num):    
    if isinstance(g.left, G) and g.left.block is False:
        g.right = G(left = g.left.right, op = g.op, right = num)
        g.op = g.left.op
        g.left = g.left.left
    else:
        g.right = num
    g.block = True
    return G(left = g)


def set_num(g, num):
    if g.left is None:
        g.left = num
    elif g.op in [multiply, divide]:
        g = h_pri(g, num)
    elif g.op in [add, subtract]:
        g.right = num
        g = G(left = g)
    else:
        raise ValueError('double number not allow')
    return g


def calc(it: iter, g: G):
    for i in it:
        if i == '(':
            g = set_num(g, calc(it, G()))
        elif i == ')':
            if isinstance(g.left, G):
                g.left.block = True
            return g.left
        else:
            is_op = op_const.get(i)
            if is_op:
                g = set_op(g, is_op)
            else:
                is_num = to_int(i)
                g = set_num(g, is_num)
    return g


def result(g: G):
    left = result(g.left) if isinstance(g.left, G) else g.left
    right = result(g.right) if isinstance(g.right, G) else g.right
    return g.op(left, right)


def main():
    """
    this is method docstring
    """
    try:
        array = [e for e in input('Enter Expression: ').split(' ') if e.strip().lower()]
        if not len(array):
            raise ValueError('Input Some Value...')
        expression = calc(iter(array), G())
        if expression.op is None and expression.right is None and expression.left is not None:
            print(f'result: {result(expression.left)}')
        else:
            raise ValueError('not matched condition')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()

# ( 1 + 2 ) / ( 0 + ( 3 * ( 4 + 5 ) ) )
# ( 1 ) + ( 2 )
# 1 + 2 * 3
# 9 / 1 * 9

