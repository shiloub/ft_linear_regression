import shutil


def get_terminal_width():
    """return the current terminal width"""
    terminal_size = shutil.get_terminal_size(fallback=(80, 24))
    return terminal_size.columns


def get_prog_bar(i, size):
    """return the progression bar in string format"""
    bar_size = get_terminal_width() // 3 * 2
    current_percentage = i / size * 100
    n_block = int(current_percentage * bar_size / 100)
    n_space = bar_size - n_block
    bar = "|"

    for i in range(n_block):
        bar += "■"
    for i in range(n_space):
        bar += " "
    bar += "|"
    return bar


def ft_tqdm(iterable):
    """Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested"""
    i = 0
    print()
    while i <= len(iterable):

        display = "{:-4,.0%}{} {} / {}".format(
            i/len(iterable),
            get_prog_bar(i, len(iterable)), i, len(iterable))
        print(display, end="\r")
        i += 1
        yield
    print()