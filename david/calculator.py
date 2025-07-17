from typing import Callable, TypedDict, Optional
import math

def add(a, b) -> float:
    return float(a + b)

def subtract(a, b) -> float:
    return float(a - b)

def multiply(a, b) -> float:
    return float(a * b)

def divide(a, b) -> float:
    if (b == 0):
        raise ValueError('Error: Division by zero.')
    return float(a / b)


def to_int(user_input: str) -> int:
    val = user_input.strip().lower()

    constants = {
        'e': math.e,
        'pi': math.pi,
        'tau': math.tau,
        'inf': math.inf,
        '-inf': -math.inf,
        'infinity': math.inf,
        '-infinity': -math.inf
    }

    try:
        if val in constants:
            return int(constants[val])
        return int(val)
    except:
        raise ValueError(f'Invalid number input: {user_input}')


def to_operater(user_input: str) -> None:
    val = user_input.strip().lower()

    constants = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    try:
        record['operator'] = constants[val]
    except:
        raise ValueError('Invalid operator.')

def parse(user_input: str):
    val = user_input.strip().lower()
    array = val.split(' ')
    filtered = [i for i in array if i.strip()]

    if len(filtered) == 1:
        record['num1'] = to_int(filtered[0])
    elif len(filtered) == 3:
        record['num1'] = to_int(filtered[0])
        to_operater(filtered[1])
        record['num2'] = to_int(filtered[2])
    else:
        raise ValueError('Invalid expression: [1 number] OR [number operator number]')

class UserRecord(TypedDict):
    num1: Optional[int]
    num2: Optional[int]
    operator: Optional[Callable[[int, int], float]]

record: UserRecord = {
    'num1': None,
    'num2': None,
    'operator': None
}

def main():
    try:
        parse(input('Enter expression: '))
        if (record['num2'] == None):
            record['num2'] = to_int(input('Enter Second Number: '))
            to_operater(input('Enter Operator (Allowed Type: +-*/): '))
        print(f"Result: <{record['operator'](record['num1'], record['num2'])}>")
    except ValueError as error:
        print(error)

if __name__ == '__main__':
    main()
