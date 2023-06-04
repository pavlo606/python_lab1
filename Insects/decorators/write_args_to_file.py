def write_args_to_file(*argv, **kwargv):
    """Decorator that writes args names and its value to file"""
    def _write_args_to_file(func):
        def inner(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [[k, repr(v)] for k, v in kwargs.items()]
            result = f"{func.__name__}:\n"
            args_names = func.__code__.co_varnames
            for arg_name, arg in list(zip(args_names, args_repr)) + kwargs_repr:
                result += f"\t{arg_name}={arg}\n"

            with open(f"logs\\{filename}", "w", encoding="utf-8") as file:
                file.write(result)

            return func(*args, **kwargs)
        return inner
    filename = "args.txt"

    if len(argv) == 1 and callable(argv[0]):
        return _write_args_to_file(argv[0])

    if "filename" in kwargv:
        filename = kwargv["filename"]
    elif len(argv) > 0:
        filename = argv[0]
    return _write_args_to_file