"""Manager"""
import traceback
from Insects.models.insect import Insect

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

def write_exc(*argv, **kwargv):
    """If some Exceprion has happened decorator writes logs to file"""
    def _write_exc(func):
        def inner(*args, **kwargs):
            with open(f"logs\\{filename}", "w", encoding="utf-8") as file:
                try:
                    return func(*args, **kwargs)

                except Exception: # pylint: disable=broad-except
                    file.write(f"Mathod name: {func.__name__}\n")
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

class InsectManager:
    """This class saves list of insects"""
    def __init__(self, insects: list[Insect]):
        self.insects = insects
        self.current = 0

    def add_insect(self, insect: Insect):
        """Append insect"""
        self.insects.append(insect)

    def del_insect(self, insect: Insect):
        """Delete insect"""
        self.insects.remove(insect)

    def find_all_dangerous(self) -> list[Insect]:
        """Finds all dangerous insects"""
        return list(filter(lambda insect: insect.is_dangerous, self.insects))

    def find_all_with_legs_more_then(self, number_of_legs: int) -> list[Insect]:
        """Finds all insects with number of legs more then"""
        return list(filter(lambda insect: insect.number_of_legs >= number_of_legs, self.insects))

    def get_insects_poisonous(self) -> list[bool]:
        """Return list of results of method can_inject_poison of each insect"""
        return [insect.can_inject_poison() for insect in self.insects]

    def get_enumarated(self) -> list[tuple[int, Insect]]:
        """Return enumerated list of insects"""
        return list(enumerate(self.insects))

    def get_insects_poisonous_zip(self) -> list[tuple[bool, Insect]]:
        """Return a concatenation of object and result of method get_insects_poisonous"""
        return list(zip(self.get_insects_poisonous(), self.insects))

    @write_args_to_file
    def check_condition_all_any(self, func) -> dict[str, bool]:
        """
        Return dict with keys:
            all - true if all insects satisfied condition,
            any - true if any of insects satisfied condition
        """
        return {"all": all([func(insect) for insect in self.insects]),
                "any": any([func(insect) for insect in self.insects])}

    def __str__(self) -> str:
        out = str()
        for insect in self.insects:
            out += f"{insect}\n"

        return out

    def __len__(self) -> int:
        return len(self.insects)

    def __getitem__(self, index) -> Insect:
        if abs(index) < len(self.insects):
            return self.insects[index]
        else:
            raise IndexError

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < len(self.insects):
            last = self.current
            self.current += 1
            return self.insects[last]
        raise StopIteration

    @write_exc
    def test(self):
        """Method to test decorator write_log"""
        raise IndexError
