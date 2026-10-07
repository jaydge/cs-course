# Week 5 Add-on: Calculator and Rock Paper Scissors

These are the two builds from Week 4 that we did not get to in class. Both use what you already have: input, conditionals, and a loop. Plan on about 40 to 50 minutes for the two of them. The third item is optional and open-ended.

## 1. Build a calculator

- Ask for two numbers and an operator, then print the result.
- Use conditionals to pick the operation from the operator the user typed.
- Wrap the whole thing in a `while` loop so it keeps going until the user types `quit`.
- Guard the divide-by-zero case with an `if`, and print something useful instead of letting it crash.

Save it into your CS Class folder.

## 2. Build Rock Paper Scissors

- Play against the computer, using the `random` module for the computer's throw.
- Use conditionals to decide who won.
- Loop it for best of five, and keep the score in two variables.

Save it into your CS Class folder.

If you run short of time, finish the calculator first and get Rock Paper Scissors as far as you can.

## 3. Optional: start your own adventure game

Optional, not graded, and yours to take as far as you like. This is the choose-your-own-adventure idea from class, as a side project for your own time.

**Plan it on paper first.** Write down five to eight scenes. For each one, note the situation the player is in, the two choices they get, which choice ends the game, and which scene the other choice leads to. That sheet is your map, and it is the hard part. The code is easier than the map.

**Then write one function per scene.** A scene prints some story, asks a question, and calls the next scene. That is exactly the shape of the functions we are working on, which is why this project is worth doing now.

```python
def ask(question, option_a, option_b):
    while True:
        answer = input(question + " (" + option_a + "/" + option_b + ") ").lower().strip()
        if answer == option_a or answer == option_b:
            return answer
        print("Please type", option_a, "or", option_b)

def game_over(message):
    print(message)
    print("Game over.")

def scene_cave():
    print("You are at the mouth of a cave. Something inside is breathing.")
    choice = ask("Do you go in, or walk away?", "in", "away")
    if choice == "in":
        scene_tunnel()
    else:
        game_over("You walk home. Safe, but you will always wonder.")

scene_cave()
```

A few things that will save you time:

- Test after every scene you add. Do not write all eight and then run it for the first time.
- Keep each scene short: a few lines of story, one question, two branches.
- Name each function after its scene, so you can follow the story by reading the function names.
- The last line of the file calls your first scene. Nothing happens without it.

If you want to push further later: keep a list of items the player has picked up, track a score, or use `random` so one choice goes well or badly. A tidier way to hold a large map is a dictionary, which arrives in Week 11, so if your game gets big, that is the upgrade to come back for.

---

A reminder on getting help: do this yourself, without AI helpers like ChatGPT. We will learn to use those tools properly later in the course. If you get stuck, try for a few minutes, write down your question, and bring it to class. Stuck is normal; it is where the learning is.
