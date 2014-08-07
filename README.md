﻿Interpreter Brainfuck.
===========

####EN:
Interpreter language Brainfuck.

| Character | Meaning                                                                                     |
|-----------|---------------------------------------------------------------------------------------------|
|     >     | increment the data pointer (to point to the next cell to the right).                        |
|     <     | decrement the data pointer (to point to the next cell to the left).                         |
|     +     | increment (increase by one) the byte at the data pointer.                                   |
|     -     | decrement (decrease by one) the byte at the data pointer.                                   |
|     .     | output the byte at the data pointer.                                                        |
|     ,     | accept one byte of input, storing its value in the byte at the data pointer.                |
|     [     | if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to thenext command, jump it forward to the command after the matching ] command.    |
|     ]     | if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the,next command, jump it back to the command after the matching [ command.      |


####RU:
Интерпрететаор языка Brainfuck.

| Команда Brainfuck |                                              Описание команды                                              |
|-------------------|------------------------------------------------------------------------------------------------------------|
|         >         | перейти к следующей ячейке                                                                                 |
|         <         | перейти к предыдущей ячейке                                                                                |
|         +         | увеличить значение в текущей ячейке на 1                                                                   |
|         -         | уменьшить значение в текущей ячейке на 1                                                                   |
|         .         | напечатать значение из текущей ячейки                                                                      |
|         ,         | ввести извне значение и сохранить в текущей ячейке                                                         |
|         [         | если значение текущей ячейки ноль, перейти вперёд по тексту                                                |
|                   | программы на ячейку, следующую за соответствующей ] (с учётом вложенности)                                 |
|         ]         | если значение текущей ячейки не нуль, перейти назад по тексту программы на символ,[ (с учётом вложенности) |