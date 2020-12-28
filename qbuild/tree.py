import os


def _tree(prefix, path, root_name=None):
    s = root_name or os.path.basename(path)
    s += "\n"
    if os.path.isfile(path):
        return s
    _, dirs, files = next(os.walk(path))
    dirs = sorted(dirs)
    files = sorted(files)
    items = [(i, "d") for i in dirs] + [(i, "f") for i in files]
    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        if is_last:
            s += prefix + "└── "
            prefix_2 = prefix + "    "
        else:
            s += prefix + "├── "
            prefix_2 = prefix + "│   "
        s += _tree(prefix_2, os.path.join(path, item[0]))
    return s


def tree(path, root_name=None):
    """
    :param path: Target path
    :param root_name: If supplied, will be used as the root name instead of real root folder's name
    :return:
    """
    return _tree("", path, root_name).strip()
