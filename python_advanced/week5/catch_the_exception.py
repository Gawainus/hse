def exception_logger(func):
    def inner(**kwargs):
        try:
            func(**kwargs)
        except Exception as e:
            for e_class in \
                    [ZeroDivisionError, ArithmeticError, AssertionError]:
                if isinstance(e, e_class):
                    print(e_class.__name__)

    return inner
