import os
import sh


class NotGitRepoException(Exception):
    pass


def is_inside_git_repo(path):
    if not os.path.isdir(path):
        return False
    try:
        sh.git('status', _cwd=path)
        return True
    except sh.ErrorReturnCode_128:
        return False


def _get_unignored_files(base_dir, path):
    base, dirs, files = next(os.walk(path))
    for f in files:
        if f == '.gitignore':
            continue
        ff = os.path.join(base, f)
        try:
            sh.git('check-ignore', '--no-index', '-q', ff, _cwd=base_dir)
        except sh.ErrorReturnCode_1:
            yield os.path.relpath(ff, start=base_dir)
    for d in dirs:
        if d == '.git':
            continue
        dd = os.path.join(base, d)
        try:
            sh.git('check-ignore', '--no-index', '-q', dd, _cwd=base_dir)
        except sh.ErrorReturnCode_1:
            yield from _get_unignored_files(base_dir, dd)


def get_unignored_files(path):
    """
    Returns a list of file paths (relative to `path`) that are inside `path` and are not ignored by git (.gitignore)
    :param path: path to a directory inside a git repo
    """
    if not is_inside_git_repo(path):
        raise NotGitRepoException
    return list(_get_unignored_files(path, path))
