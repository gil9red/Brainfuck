#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


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
Интерпретатор языка Brainfuck.
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


def get_loops_block(source: str) -> dict[int, int]:
    begin_block: list[int] = []
    blocks: dict[int, int] = dict()
    for i, s in enumerate(source):
        if s == "[":
            begin_block.append(i)
        elif s == "]":
            b_i = begin_block.pop()  # b_i -- begin index
            blocks[i] = b_i
            blocks[b_i] = i
    return blocks


def execute(source: str):
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
    # Dictionary, which is stored in the key index of the cell, and in the value - its value
    bf: dict[int, int] = defaultdict(int)
    l = len(source)  # Number of code symbols
    loops_block = get_loops_block(source)

    while i < l:
        s = source[i]

        if s == ">":  # Go to the next cell
            x += 1
        elif s == "<":  # Go to the previous cell
            x -= 1
        elif s == "+":  # Increasing the value of the current cell on 1
            bf[x] += 1
        elif s == "-":  # Decrease the value of the current cell on 1
            bf[x] -= 1
        elif s == ".":  # Printing the value of the current cell
            print(chr(bf[x]), end="")
        elif s == ",":  # Enter a value in the current cell
            bf[x] = int(input("Input = "))
        elif s == "[":  # Begin loop
            # If bf[x] == 0, then gets the index of the closing parenthesis
            if not bf[x]:
                i = loops_block[i]
        elif s == "]":  # End loop
            if bf[x]:  # Если bf[x] != 0, then gets the index of the opening parenthesis
                i = loops_block[i]
        i += 1


if __name__ == "__main__":
    import sys
    import argparse

    from pathlib import Path

    parser = argparse.ArgumentParser(description="Interpreter language Brainfuck.")
    parser.add_argument("path", type=Path, help="Path to file")

    if len(sys.argv) == 1:
        parser.print_help()
    else:
        args = parser.parse_args()
        source = args.path.read_text(encoding="utf-8")
        execute(source)
