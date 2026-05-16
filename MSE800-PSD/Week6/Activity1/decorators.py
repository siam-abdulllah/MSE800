from datetime import datetime


def log_activity(func):
    # ok so this is the decorator bit
    # @log_activity on a function = python quietly does student_login = log_activity(student_login)
    # took me a sec to get that - you're not calling the function underneath, you're swapping it for wrapper

    def wrapper(*args, **kwargs):
        # when i was stuck i breakpointed here
        # banner shows up first, THEN the actual login/submit/whatever runs
        # seeing func.__name__ say student_login made me feel less crazy lol
        print("===================================")
        print(f"Function: {func.__name__}")
        print(f"Time: {datetime.now()}")
        print("Activity started...")

        result = func(*args, **kwargs)

        print("Activity completed.")
        print("===================================\n")

        return result

    return wrapper
