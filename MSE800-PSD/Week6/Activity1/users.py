from decorators import log_activity


@log_activity
def student_login(username):
    # just prints - all the fancy logging is in decorators.py
    print(f"{username} logged into the system.")


@log_activity
def submit_assignment(username, assignment):
    # main passes two things in, wrapper doesn't mess with them
    print(f"{username} submitted {assignment}.")


@log_activity
def view_grades(username):
    # heads up - mohammad does login + submit but alex views grades in main
    # program's fine, names just don't match. noticed it in the terminal output
    print(f"{username} is viewing grades.")
