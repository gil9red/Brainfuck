"""
EN:
Interpreter language Brainfuck.
Character	Meaning
>	        increment the data pointer (to point to the next cell to the right).
<	        decrement the data pointer (to point to the next cell to the left).
+	        increment (increase by one) the byte at the data pointer.
-	        decrement (decrease by one) the byte at the data pointer.
.	        output the byte at the data pointer.
,	        accept one byte of input, storing its value in the byte at the data pointer.
[	        if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the
                next command, jump it forward to the command after the matching ] command.
]	        if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the
                next command, jump it back to the command after the matching [ command.

RU:
Интерпрететаор языка Brainfuck.
Команда Brainfuck   Описание команды
Начало программы 	выделяется память под 30 000 ячеек
    > 	            перейти к следующей ячейке
    <               перейти к предыдущей ячейке
    + 	            увеличить значение в текущей ячейке на 1
    - 	            уменьшить значение в текущей ячейке на 1
    . 	            напечатать значение из текущей ячейки
    , 	            ввести извне значение и сохранить в текущей ячейке
    [ 	            если значение текущей ячейки ноль, перейти вперёд по тексту программы на ячейку,
                        следующую за соответствующей ] (с учётом вложенности)
    ] 	            если значение текущей ячейки не нуль, перейти назад по тексту программы на символ
                        [ (с учётом вложенности)
"""

from collections import defaultdict
import sys
import argparse


__author__ = 'ipetrash'



def get_loops_block(source):
    begin_block = []
    blocks = {}
    for i, s in enumerate(source):
        if s is '[':
            begin_block.append(i)
        elif s is ']':
            b_i = begin_block.pop()  # b_i -- begin index
            blocks[i] = b_i
            blocks[b_i] = i
    return blocks


def execute(source):
    """
    EN:
    The function parses source code Brainfuck and execute it.

    RU:
    Функция выполняет разбор исходного кода Brainfuck и выполняет его.

    :param source: Исходный код
    :return:
    """

    i = 0  # A pointer to the row index in the code
    x = 0  # Cell index
    bf = defaultdict(int)  # Dictionary, which is stored in the key index of the cell, and in the value - its value
    l = len(source)  # Number of code symbols
    loops_block = get_loops_block(source)

    while i < l:
        s = source[i]

        if s is '>':  # Go to the next cell
            x += 1
        elif s is '<':  # Go to the previous cell
            x -= 1
        elif s is '+':  # Increasing the value of the current cell on 1
            bf[x] += 1
        elif s is '-':  # Decrease the value of the current cell on 1
            bf[x] -= 1
        elif s is '.':  # Printing the value of the current cell
            print(chr(bf[x]), end='')
        elif s is ',':  # Enter a value in the current cell
            bf[x] = int(input("Input = "))
        elif s is '[':  # Begin loop
            if not bf[x]:  # If bf[x] == 0, then gets the index of the closing parenthesis
                i = loops_block[i]
        elif s is ']':  # End loop
            if bf[x]:  # Если bf[x] != 0, then gets the index of the opening parenthesis
                i = loops_block[i]
        i += 1


def create_parser():
    parser = argparse.ArgumentParser(description='Interpreter language Brainfuck.')
    parser.add_argument("path", help="Path to file")
    return parser


if __name__ == '__main__':
    parser = create_parser()

    if len(sys.argv) is 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        file_name = args.path
        source = open(file_name).read()
        execute(source)