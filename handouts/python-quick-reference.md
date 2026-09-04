# Python Quick Reference

Keep this one bookmarked. When you are in the middle of an exercise and cannot remember what something is called or why it is not working, look here first, then follow the link to the official Python documentation.

You do not need all of this. Work down the page: the sections are in the order we cover them, so if we are in Week 6, everything you need is in the first two sections and the rest is a preview.

A note on the help rule: this page and the official Python documentation are always allowed, along with your notes, your textbook, your classmates, and me. AI helpers like ChatGPT are not, until the AI unit later in the year. Looking something up in the documentation is not cheating; it is the actual job.

## How to look something up

The official documentation lives at [docs.python.org/3](https://docs.python.org/3/). Two pages cover most of what you will want:

- [Built-in Functions](https://docs.python.org/3/library/functions.html) is the alphabetical list of everything you can call without importing anything: `print`, `input`, `int`, `len`, `abs`, `range`, and the rest.
- [Built-in Types](https://docs.python.org/3/library/stdtypes.html) is what lists, strings, and dictionaries can do, including all their methods.

The documentation is written for working programmers, not for people learning. That is worth knowing so it does not discourage you. When you open a page, skip the formal definition at the top and scroll to the examples. The examples are the part that will answer your question.

Faster than any of it: try it in the Thonny shell. The shell is the bottom panel where you can type one line and press return. Nothing there can break your program, so guessing is free.

```python
>>> len("hello")
5
>>> abs(-4)
4
```

You can also ask Python itself, which prints the same text the website shows:

```python
>>> help(len)
```

## When something goes wrong

Read the last line of the error first. It names the problem. The line above it tells you where.

| What you see | What it usually means | First thing to check |
| --- | --- | --- |
| [SyntaxError](https://docs.python.org/3/library/exceptions.html#SyntaxError) | Python could not read your code at all | A missing `)`, `"` or `:` on that line or the line above |
| [IndentationError](https://docs.python.org/3/library/exceptions.html#IndentationError) | The spacing at the start of a line is wrong | Everything inside an `if`, `for` or `def` is indented the same amount |
| [NameError](https://docs.python.org/3/library/exceptions.html#NameError) | You used a name Python has never seen | A typo in a variable name, or using it before you set it |
| [TypeError](https://docs.python.org/3/library/exceptions.html#TypeError) | Right idea, wrong kind of thing | Text where a number belongs. `input` always gives text, so wrap it in `int()` |
| [ValueError](https://docs.python.org/3/library/exceptions.html#ValueError) | Right kind of thing, impossible value | `int("hello")` cannot work. Check what the user actually typed |
| [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError) | You asked for an item that is not there | Counting starts at 0, so the last item of a 5-item list is `[4]` |
| [KeyError](https://docs.python.org/3/library/exceptions.html#KeyError) | That key is not in the dictionary | Spelling and capitalization of the key |
| [AttributeError](https://docs.python.org/3/library/exceptions.html#AttributeError) | That thing does not have that method | Spelling, and whether you are calling it on the right object |
| [ZeroDivisionError](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError) | Something divided by zero | An empty list you took an average of |

The full list is at [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html).

## The basics

Covered in Weeks 1 to 5.

**Showing and asking.** [`print()`](https://docs.python.org/3/library/functions.html#print) shows something. [`input()`](https://docs.python.org/3/library/functions.html#input) asks the user and always hands back text, even when they type a number.

```python
name = input("What is your name? ")
print("Hello, " + name)
```

**Variables.** A name for a value, made with a single `=`. See [assignment](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements).

**Numbers and text.** [`int()`](https://docs.python.org/3/library/functions.html#int) turns text into a whole number, [`str()`](https://docs.python.org/3/library/functions.html#func-str) turns a number into text, and [`float()`](https://docs.python.org/3/library/functions.html#float) handles decimals. This is the fix for the most common early error:

```python
age = int(input("Age? "))
print(age + 1)
```

**Arithmetic.** The [operators](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations) are `+`, `-`, `*`, `/`, `//`, `%` and `**`. Two of them surprise people: `//` divides and throws away the remainder, and `%` gives you only the remainder.

**Comparing.** The [comparison operators](https://docs.python.org/3/library/stdtypes.html#comparisons) are `==`, `!=`, `<`, `>`, `<=` and `>=`. One `=` sets a value, two `==` asks a question. That is the single most common beginner bug.

**Combining conditions.** [`and`, `or`, `not`](https://docs.python.org/3/reference/expressions.html#boolean-operations). `and` needs both sides true, `or` needs either one.

**Making a decision.** The [`if` statement](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement). Python takes the first branch that is true and skips the rest, so order matters.

```python
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("C")
```

**Repeating a set number of times.** The [`for` statement](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) with [`range()`](https://docs.python.org/3/library/functions.html#func-range). `range(5)` counts 0, 1, 2, 3, 4, which is five numbers starting at zero and stopping before five.

```python
for i in range(5):
    print(i)
```

**Repeating until something changes.** The [`while` statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement). If it never stops, press Control-C in the shell.

**Your own functions.** [`def`](https://docs.python.org/3/reference/compound_stmts.html#function-definitions). `return` hands a value back to whoever called it, which is not the same as printing it.

```python
def add(a, b):
    return a + b
```

**Randomness.** The [`random`](https://docs.python.org/3/library/random.html) module. `random.randint(1, 10)` gives a whole number from 1 to 10 inclusive, and `random.choice(items)` picks one item from a list.

```python
import random
secret = random.randint(1, 10)
```

## Lists and text

Covered in Weeks 6 to 10.

**Lists.** A [list](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types) holds several things in order. Positions start at 0, and `-1` means the last one.

```python
scores = [90, 85, 100, 72]
print(scores[0])    # 90
print(scores[-1])   # 72
print(len(scores))  # 4
```

| What you want | How | Note |
| --- | --- | --- |
| Add to the end | `scores.append(65)` | Changes the list in place |
| Remove by value | `scores.remove(85)` | Errors if it is not there |
| Remove by position | `scores.pop(0)` | Hands the removed item back |
| Sort it | `scores.sort()` | Changes the list and returns nothing |
| Is it in there | `85 in scores` | Gives True or False |
| How many | `len(scores)` | A function, not a method |

A trap worth remembering: `scores = scores.sort()` throws your list away, because `.sort()` sorts in place and hands back nothing. Just write `scores.sort()`.

**Going through a list.**

```python
for score in scores:
    print(score)
```

**Text.** A string behaves like a list of characters, so indexing, `len()` and `in` all work the same way. [Slicing](https://docs.python.org/3/library/stdtypes.html#common-sequence-operations) takes a piece of it.

```python
word = "computer"
print(word[0:4])   # comp
print(word[4:])    # uter
print(word[::-1])  # retupmoc
```

Common [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods): `.upper()`, `.lower()`, `.strip()` to remove spaces at the ends, and `.split()` to break a sentence into a list of words. None of them change the original string, because strings cannot be changed. They hand you a new one, so you have to catch it:

```python
word = word.upper()
```

**Loops inside loops.** The inner loop runs all the way through for every single pass of the outer one. `print("x", end="")` stops it moving to a new line, and a bare `print()` moves to one.

## Dictionaries, objects, and structure

Covered in Weeks 11 to 16.

**Dictionaries.** A [dictionary](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) stores pairs, so you look things up by name instead of by position.

```python
phones = {"Ada": "555-0100", "Grace": "555-0199"}
print(phones["Ada"])
phones["Alan"] = "555-0142"
```

Asking for a key that is not there is a `KeyError`. The two defenses are checking first with `if "Alan" in phones` or using `.get("Alan", "not found")`, which hands back your fallback instead of crashing. Loop over a dictionary with `.items()`:

```python
for name, number in phones.items():
    print(name, number)
```

**Classes and objects.** A [class](https://docs.python.org/3/reference/compound_stmts.html#class-definitions) is a blueprint. `__init__` runs when you make one, and `self` means this particular object.

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5

    def feed(self):
        self.hunger = self.hunger - 1
```

Two mistakes account for most class problems: forgetting `self` in the method definition, and writing `hunger = hunger - 1` instead of `self.hunger = self.hunger - 1`.

**Nothing.** `None` is Python's word for no value. Check for it with `is None` rather than `==`.

**Checking your own work.** `assert` states something you believe is true, and says nothing at all if you are right.

```python
assert add(2, 2) == 4
```

**Also useful here.** [`abs()`](https://docs.python.org/3/library/functions.html#abs) makes a number positive, [`sum()`](https://docs.python.org/3/library/functions.html#sum) totals a list, and [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) hands back a sorted copy without touching the original.

## Files, the terminal, and the network

Covered in Weeks 17 to 21.

**Paths and folders.** [`pathlib`](https://docs.python.org/3/library/pathlib.html) is how Python talks about places on disk. The `/` joins path pieces regardless of which operating system you are on.

```python
from pathlib import Path
folder = Path.home() / "Documents" / "CS Class"
for item in folder.iterdir():
    print(item.name)
```

**Reading and writing files.** [`open()`](https://docs.python.org/3/library/functions.html#open) inside a `with` block, which closes the file for you even if something goes wrong.

```python
with open("access.log") as f:
    for line in f:
        if "404" in line:
            print(line.strip())
```

Opening with `"w"` erases the file first. Opening with `"a"` adds to the end. Be sure which one you meant.

**Command-line arguments.** [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv) is the list of words typed after your program's name.

**Names and addresses.** [`socket`](https://docs.python.org/3/library/socket.html) looks up what address a site name points at, and [`ipaddress`](https://docs.python.org/3/library/ipaddress.html) does the arithmetic on networks and ranges.

**Fetching a page.** [`requests`](https://requests.readthedocs.io/en/latest/) is not part of Python itself, so it has to be installed, and its documentation lives on its own site.

## Bigger tools

Covered in Weeks 22 to 28. You will not need these until the second half of the year.

**Catching errors instead of crashing.** The [`try` statement](https://docs.python.org/3/reference/compound_stmts.html#the-try-statement). Catch the specific thing you expect rather than everything.

```python
try:
    age = int(input("Age? "))
except ValueError:
    print("That was not a number.")
```

**Spreadsheet data.** The [`csv`](https://docs.python.org/3/library/csv.html) module, and `csv.DictReader` in particular, which hands you each row as a dictionary keyed by the column headings.

**Data as text.** The [`json`](https://docs.python.org/3/library/json.html) module, which is how programs hand structured data to each other over the web.

**Hashing.** The [`hashlib`](https://docs.python.org/3/library/hashlib.html) module. Note that [`secrets`](https://docs.python.org/3/library/secrets.html), not `random`, is the right module whenever the result needs to be unguessable.

**Your own web app.** [Flask](https://flask.palletsprojects.com/), which like `requests` is installed separately and documented on its own site.

## Not on this page

- AP pseudocode, and how it lines up with Python, is in `ap-track/AP-Pseudocode-Bridge.md`. AP writes `=` where Python writes `==`, which is the reverse of our usual trap, so check there rather than guessing.
- The official AP CSP Exam Reference Sheet is provided by the College Board during the exam. Use theirs, not this page, when you practice exam questions.
- Anything specific to one week's exercise is in that week's handout.
