# Python to AP Pseudocode: Bridge Sheet

**Why this exists.** You write Python all year. The AP CSP multiple-choice section is written in College Board's own pseudocode, not Python or any real language. The concepts are identical; only the notation differs. This sheet teaches the translation so the exam's code reads as easily as your own.

**The official sheet.** College Board provides an authoritative reference sheet on exam day (and in Bluebook). Read it alongside this one: `https://apcentral.collegeboard.org/media/pdf/ap-computer-science-principles-exam-reference-sheet.pdf`. That sheet explains the pseudocode in isolation. This sheet connects it to the Python you already know.

**What is tested.** You read and trace pseudocode, you do not write it from scratch. The most common question is "what is the value of x after this runs?" So the skill to drill is tracing, slowly and by hand.

---

## The five differences that cause the most mistakes

1. **Lists are 1-indexed in AP pseudocode, 0-indexed in Python.** The first element is `aList[1]`, not `aList[0]`. This is the number-one source of wrong answers. When you see a list, mentally renumber it starting at 1.
2. **The equals sign means equality, not assignment.** In the pseudocode, `a = b` asks "are they equal?" Assignment uses the left arrow: `a ← b`. In Python those are `==` and `=`. Do not mix them up.
3. **A bad list index is an error, not a silent miss.** If an index is less than 1 or greater than the list length, the program terminates with an error. Python would raise an exception too, but on the exam this is a deliberate trap in trace questions.
4. **`RANDOM(a, b)` includes both ends.** `RANDOM(1, 3)` can return 1, 2, or 3. This matches Python's `random.randint(a, b)`, not `range()` or `randrange()`.
5. **`MOD` is the remainder operator.** `17 MOD 5` is `2`. It is Python's `%`.

---

## Rosetta tables

### Variables, input, output

| Python | AP pseudocode | Note |
|---|---|---|
| `x = 5` | `x ← 5` | Assignment is the left arrow |
| `print(x)` | `DISPLAY (x)` | Displays the value followed by a space |
| `x = input()` | `x ← INPUT ()` | Accepts a value from the user and returns it |

### Arithmetic and comparison

| Python | AP pseudocode | Note |
|---|---|---|
| `a + b`, `a - b`, `a * b`, `a / b` | `a + b`, `a - b`, `a * b`, `a / b` | Same; `/` gives a decimal result, e.g. `17 / 5` is `3.4` |
| `a % b` | `a MOD b` | Remainder; same precedence as `*` and `/` |
| `a == b` | `a = b` | Equality test |
| `a != b` | `a ≠ b` | Not equal |
| `a < b`, `a > b` | `a < b`, `a > b` | Same |
| `a <= b`, `a >= b` | `a ≤ b`, `a ≥ b` | Less/greater than or equal |

### Boolean operators

| Python | AP pseudocode |
|---|---|
| `a and b` | `a AND b` |
| `a or b` | `a OR b` |
| `not a` | `NOT a` |

### Conditionals

| Python | AP pseudocode |
|---|---|
| `if condition:` then indented block | `IF (condition) { block }` |
| `if / else` | `IF (condition) { block } ELSE { block }` |

Pseudocode uses braces and parentheses where Python uses a colon and indentation:

```
IF (score ≥ 60)
{
  DISPLAY ("pass")
}
ELSE
{
  DISPLAY ("fail")
}
```

### Loops

| Python | AP pseudocode | Note |
|---|---|---|
| `for i in range(n):` | `REPEAT n TIMES { block }` | Runs the block n times |
| `while not condition:` | `REPEAT UNTIL (condition) { block }` | Repeats until the condition becomes true |
| `for item in aList:` | `FOR EACH item IN aList { block }` | Visits each element in order |

### Lists

The first element is at index 1. `LENGTH` gives the number of elements.

| Python | AP pseudocode | Note |
|---|---|---|
| `aList = [10, 20, 30]` | `aList ← [10, 20, 30]` | Creates the list |
| `aList[0]` (first item) | `aList[1]` (first item) | 1-indexed: this is the big one |
| `x = aList[i]` | `x ← aList[i]` | Read element at index i |
| `aList[i] = x` | `aList[i] ← x` | Write element at index i |
| `len(aList)` | `LENGTH (aList)` | Number of elements |
| `aList.append(v)` | `APPEND (aList, v)` | Adds v to the end |
| insert at position | `INSERT (aList, i, v)` | Puts v at index i; items at i and beyond shift right; length grows |
| remove at position | `REMOVE (aList, i)` | Deletes the item at index i; later items shift left; length shrinks |

### Procedures

| Python | AP pseudocode |
|---|---|
| `def name(a, b):` then block | `PROCEDURE name (a, b) { block }` |
| `return expr` | `RETURN (expr)` |
| `name(3, 4)` | `name (3, 4)` |

```
PROCEDURE addOne (n)
{
  RETURN (n + 1)
}
```

### Robot commands (grid-navigation questions)

These appear in some questions where a robot moves on a grid. There is no Python equivalent; just learn them.

| Command | Meaning |
|---|---|
| `MOVE_FORWARD ()` | Move one square in the direction the robot faces |
| `ROTATE_LEFT ()` | Turn 90 degrees left |
| `ROTATE_RIGHT ()` | Turn 90 degrees right |
| `CAN_MOVE (direction)` | True if the robot can move in that direction (left, right, forward, backward) |

---

## Side-by-side worked example

Sum the even numbers in a list.

**Python**
```python
nums = [3, 6, 7, 8, 10]
total = 0
for n in nums:
    if n % 2 == 0:
        total = total + n
print(total)
```

**AP pseudocode**
```
nums ← [3, 6, 7, 8, 10]
total ← 0
FOR EACH n IN nums
{
  IF (n MOD 2 = 0)
  {
    total ← total + n
  }
}
DISPLAY (total)
```

Both print `24`. Notice every difference at once: `=` became `←`, `%` became `MOD`, `==` became `=`, `for ... in` became `FOR EACH ... IN`, `print` became `DISPLAY`, and indentation became braces.

---

## Trace practice problems

Work each by hand. Write the value of every variable at each step. Answers are at the bottom; do not look until you have an answer.

**1.**
```
a ← 5
b ← 3
a ← a + b
b ← a - b
DISPLAY (a)
DISPLAY (b)
```

**2.**
```
n ← 17
r ← n MOD 5
DISPLAY (r)
```

**3.**
```
sum ← 0
i ← 1
REPEAT 4 TIMES
{
  sum ← sum + i
  i ← i + 1
}
DISPLAY (sum)
```

**4.**
```
x ← 8
IF (x MOD 2 = 0)
{
  DISPLAY ("even")
}
ELSE
{
  DISPLAY ("odd")
}
```

**5.**
```
nums ← [10, 20, 30, 40]
DISPLAY (nums[1])
DISPLAY (nums[3])
```

**6.**
```
data ← [5, 8, 11]
APPEND (data, 14)
DISPLAY (LENGTH (data))
DISPLAY (data[4])
```

**7.**
```
letters ← ["a", "b", "c", "d"]
REMOVE (letters, 2)
DISPLAY (letters[2])
DISPLAY (LENGTH (letters))
```

**8.**
```
vals ← [1, 2, 3]
INSERT (vals, 2, 9)
DISPLAY (vals[2])
DISPLAY (vals[3])
```

**9.**
```
count ← 0
total ← 1
REPEAT UNTIL (total > 20)
{
  total ← total * 2
  count ← count + 1
}
DISPLAY (count)
DISPLAY (total)
```

**10.**
```
PROCEDURE doubleIt (n)
{
  RETURN (n * 2)
}

result ← 0
nums ← [3, 5, 7]
FOR EACH v IN nums
{
  result ← result + doubleIt (v)
}
DISPLAY (result)
```

**11.**
```
scores ← [4, 9, 2, 9, 5]
max ← scores[1]
FOR EACH s IN scores
{
  IF (s > max)
  {
    max ← s
  }
}
DISPLAY (max)
```

---

## Answer key

1. `8 5`. (a becomes 5+3=8, then b becomes 8-3=5.)
2. `2`. (17 MOD 5 is the remainder, 2.)
3. `10`. (Adds 1+2+3+4.)
4. `even`. (8 MOD 2 is 0, and `=` tests equality, so the condition is true.)
5. `10 30`. (1-indexed: the first element is `nums[1]`. A Python habit would wrongly give 20 and 40.)
6. `4 14`. (After APPEND the list is [5, 8, 11, 14]; length 4; the fourth element is 14.)
7. `c 3`. (REMOVE index 2 deletes "b", leaving ["a", "c", "d"]; the second element is now "c"; length 3.)
8. `9 2`. (INSERT 9 at index 2 gives [1, 9, 2, 3]; second element 9, third element 2.)
9. `5 32`. (total doubles 1, 2, 4, 8, 16, 32; it passes 20 after 5 doublings.)
10. `30`. (doubleIt returns 6, 10, 14; their sum is 30.)
11. `9`. (max starts at the first element 4, then updates to 9.)

---

## How to use this in class

- Introduce it any time after Unit 3, once students are fluent with lists and procedures in Python.
- Use two or three trace problems as a warm-up at the start of class for a few weeks. The skill is built by repetition, not by reading the tables once.
- Drill the 1-indexing difference deliberately. It is the most common error and the easiest point to lose.
- Pair this with the free pseudocode practice on Code.org and Khan Academy for additional reps.
- Only AP-track students strictly need this, but the translation exercise helps everyone see Python as one instance of general programming ideas rather than the only way code can look.
