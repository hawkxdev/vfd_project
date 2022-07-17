from colorama import init, Fore

init(True)


def print_color(msg: str, color: Fore = Fore.WHITE):
    print(f'{color}{msg}')


def error(msg: str, is_exit: bool = False) -> None:
    print_color(f'ERROR: {msg}', Fore.RED)
    if is_exit:
        exit()


def warning(msg):
    print_color(f'WARNING: {msg}', Fore.YELLOW)


def print_list(mylist: list, name: str = None, color: Fore = Fore.WHITE):
    if isinstance(mylist, list):
        print_color(f'{name}=[', color) if name else print_color('[', color)
        [print_color(f'\t{x}', color) for x in mylist]
        print_color(']', color)
    else:
        print_color(f'{name}={mylist}', color) if name else print_color(f'{mylist}', color)
