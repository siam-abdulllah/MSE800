# Week 6 Activity 1

## what's going on here

Small python thing that pretends to be a student app - login, hand in work, check grades. Nothing real behind it, just prints.

The decorator (`log_activity` in `decorators.py`) is the whole point. Instead of writing the same logging print stuff in every function in `users.py`, you slap `@log_activity` on top and it handles the before/after messages for you.

Files:
- `decorators.py` - where the wrapper lives
- `users.py` - the three fake actions
- `main.py` - runs them once so you can see output

## decorator in plain english

`@log_activity` looks neat above a function but under the hood python is basically saying "replace this function with whatever `log_activity` gives back."

So when main does `student_login("Mohammad")` you're not jumping straight into the print line in users.py. You hit `wrapper` first:

- prints the lines with === and the time
- then actually runs student_login
- prints activity completed

Did that for all three functions. Same wrapper, no copy paste.

## how i actually debugged it

Honestly? Ran `python main.py` a bunch of times and stared at the terminal.

First run i wanted to see three separate log chunks (those === blocks). Got three. Good.

Checked the "Function:" line each time - matched what i called. Also good.

When i was learning decorators i put a breakpoint inside `wrapper` in decorators.py. That's when it clicked - banner first, then the real function with the same args.

If it ever broke i'd probably:
- forget the `@` on a function
- mess up the import from decorators
- typo in main

Didn't hit any of that. No errors, program just runs.

## what i took away from it

Decorators are handy for stuff you want everywhere (logging, timing, whatever) without cluttering the actual logic.

The code works. Only weird bit: Mohammad logs in and submits but Alex views grades. Doesn't break anything, just looks odd if you imagine one person using the app. Could change the last line in main to "Mohammad" if you care.

Might add file logging or `functools.wraps` later but didn't need it for this lab.

## run it

```
python main.py
```

from the Activity1 folder. You should see three log sandwiches with one message in the middle each time.
