 Python - Everything is object

Introduction to Python Programming and Databases — ALU.

This project is mostly about *understanding* rather than writing code. Almost
every file is a one-line answer to a question about how Python handles objects,
references, aliases, and mutability.

## Requirements

- Answer files (`.txt`): one line, no shebang, no space before or after the answer
- `19-copy_list.py`: starts with `#!/usr/bin/python3`, executable, max 3 lines
- All files end with a new line
- pycodestyle 2.7.*
- No modules imported

## Files

| File | Question | Answer |
| --- | --- | --- |
| `0-answer.txt` | Function to print the type of an object | `type` |
| `1-answer.txt` | Function to get the variable identifier | `id` |
| `2-answer.txt` | `a = 89`, `b = 100` — same object? | No |
| `3-answer.txt` | `a = 89`, `b = 89` — same object? | Yes |
| `4-answer.txt` | `a = 89`, `b = a` — same object? | Yes |
| `5-answer.txt` | `a = 89`, `b = a + 1` — same object? | No |
| `6-answer.txt` | `s2 = s1`, `s1 == s2` | True |
| `7-answer.txt` | `s2 = s1`, `s1 is s2` | True |
| `8-answer.txt` | Two equal strings, `==` | True |
| `9-answer.txt` | Two equal strings, `is` | False |
| `10-answer.txt` | Two equal lists, `==` | True |
| `11-answer.txt` | Two equal lists, `is` | False |
| `12-answer.txt` | Aliased lists, `==` | True |
| `13-answer.txt` | Aliased lists, `is` | True |
| `14-answer.txt` | `l1.append(4)` then print `l2` | `[1, 2, 3, 4]` |
| `15-answer.txt` | `l1 = l1 + [4]` then print `l2` | `[1, 2, 3]` |
| `16-answer.txt` | Incrementing an int inside a function | `1` |
| `17-answer.txt` | Appending to a list inside a function | `[1, 2, 3, 4]` |
| `18-answer.txt` | Reassigning a parameter inside a function | `[1, 2, 3]` |
| `19-copy_list.py` | Return a copy of a list | — |
| `20-answer.txt` | `a = ()` — a tuple? | Yes |
| `21-answer.txt` | `a = (1, 2)` — a tuple? | Yes |
| `22-answer.txt` | `a = (1)` — a tuple? | No |
| `23-answer.txt` | `a = (1, )` — a tuple? | Yes |
| `24-answer.txt` | `a = (1)`, `b = (1)`, `a is b` | True |
| `25-answer.txt` | `a = (1, 2)`, `b = (1, 2)`, `a is b` | False |
| `26-answer.txt` | `a = ()`, `b = ()`, `a is b` | True |
| `27-answer.txt` | `a = a + [5]` — same id? | No |
| `28-answer.txt` | `a += [4]` — same id? | Yes |

## The ideas behind the answers

**Small integer caching.** CPython pre-allocates the integers from `-5` to
`256` at startup, so `a = 89` and `b = 89` end up pointing at the same cached
object. Outside that range you get separate objects.

**String interning.** Short strings that look like identifiers are interned by
the compiler. `"Best"` is interned, so two separate assignments share one
object. `"Best School"` contains a space, so it is not, and `is` returns False.

**Mutable vs immutable.** Lists, dicts, sets and bytearrays can be changed in
place, so an alias sees the change. Numbers, strings, tuples, frozensets and
bytes cannot, so any "change" actually builds a new object and rebinds the name.

**`+` versus `+=` on a list.** `l1 = l1 + [4]` builds a new list and rebinds the
name, leaving any alias pointing at the original. `l1 += [4]` calls
`__iadd__`, which mutates the list in place, so the id does not change and every
alias sees the new element.

**Passing arguments.** Python passes by assignment. The parameter becomes a new
name for the same object. Mutating that object through the parameter is visible
to the caller; rebinding the parameter is not.

