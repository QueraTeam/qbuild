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


def _list_unignored_files(base_dir, exclude_dirs, path):
    base, dirs, files = next(os.walk(path))
    for f in files:
        ff = os.path.join(base, f)
        if f == '.gitignore':
            yield ff
        else:
            try:
                sh.git('check-ignore', '--no-index', '-q', ff, _cwd=base_dir)
            except sh.ErrorReturnCode_1:
                yield ff
    for d in dirs:
        if d == '.git':
            continue
        dd = os.path.join(base, d)
        try:
            sh.git('check-ignore', '--no-index', '-q', dd, _cwd=base_dir)
        except sh.ErrorReturnCode_1:
            if not exclude_dirs:
                yield dd
            yield from _list_unignored_files(base_dir, exclude_dirs, dd)


def _list_all_files(path, exclude_dirs):
    for base, dirnames, filenames in os.walk(path):
        for filename in filenames:
            yield os.path.join(base, filename)
        if not exclude_dirs:
            for dirname in dirnames:
                yield os.path.join(base, dirname)


def ls_recursive(path, relative=False, exclude_gitignore=False, exclude_dirs=False):
    """
    :param path: The path to list files (or dirs) inside it
    :param relative: If True, returned paths will be relative to `path`
    :param exclude_gitignore:  If True, only paths that are not ignored by .gitignore files will be returned.
                               In this case, `path` must be inside a git repo.
    :param exclude_dirs: If True, only files will be returned
    :return: A list of paths inside `path`
    """
    if exclude_gitignore:
        if not is_inside_git_repo(path):
            raise NotGitRepoException
        absolute_paths = list(_list_unignored_files(path, exclude_dirs, path))
    else:
        absolute_paths = list(_list_all_files(path, exclude_dirs))
    if relative:
        return [os.path.relpath(i, start=path) for i in absolute_paths]
    else:
        return absolute_paths
