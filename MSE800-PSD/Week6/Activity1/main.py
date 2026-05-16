from users import (
    student_login,
    submit_assignment,
    view_grades
)


def main():
    # debugged by running python main.py over and over
    # each call should get those === lines before and after
    # if not -> check @log_activity still there or imports broken

    student_login("Mohammad")

    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )

    view_grades("Alex")


if __name__ == "__main__":
    main()
