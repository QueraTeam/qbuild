import os


def _tree(prefix, path):
    s = os.path.basename(path) + '\n'
    if os.path.isfile(path):
        return s
    _, dirs, files = next(os.walk(path))
    dirs = sorted(dirs)
    files = sorted(files)
    items = [(i, 'd') for i in dirs] + [(i, 'f') for i in files]
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        if is_last:
            s += prefix + '└─ '
            prefix_2 = prefix + '    '
        else:
            s += prefix + '├─ '
            prefix_2 = prefix + '│   '
        s += _tree(prefix_2, os.path.join(path, item[0]))
    return s


def tree(path):
    return _tree('', path).strip()
