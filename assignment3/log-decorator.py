# Task 1

import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("./decorator.log", "a")
handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(handler)


def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        logger.info(f"function: {func.__name__}")

        if args:
            logger.info(f"positional parameters: {args}")
        else:
            logger.info("positional parameters: none")

        if kwargs:
            logger.info(f"keyword parameters: {kwargs}")
        else:
            logger.info("keyword parameters: none")

        logger.info(f"return: {result}")
        logger.info("")

        return result

    return wrapper


@logger_decorator
def say_hello():
    print("Hello, World!")


@logger_decorator
def positional_function(*args):
    return True


@logger_decorator
def keyword_function(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    say_hello()
    positional_function(10, "hello", True)
    keyword_function(name="Jocelyn", course="Python")


#Task 2
