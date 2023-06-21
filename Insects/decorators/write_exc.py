import traceback

def write_exc(*argv, **kwargv):
    """If some Exceprion has happened decorator writes logs to file"""
    def _write_exc(func):
        def inner(*args, **kwargs):
            with open(f"logs\\{filename}", "w", encoding="utf-8") as file:
                try:
                    return func(*args, **kwargs)

                except Exception: # pylint: disable=broad-except
                    file.write(f"Method name: {func.__name__}\n")
                    traceback.print_exc(file=file)
                    return None
        return inner
    filename = "exception.txt"

    if len(argv) == 1 and callable(argv[0]):
        return _write_exc(argv[0])

    if "filename" in kwargv:
        filename = kwargv["filename"]
    elif len(argv) > 0:
        filename = argv[0]
    return _write_exc
