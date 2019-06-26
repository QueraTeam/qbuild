import os
import re

import sh


class NotGitRepoException(Exception):
    pass


def _get_cwd(path):
    if os.path.isdir(path):
        return path
    else:
        return os.path.dirname(path)


def is_inside_git_repo(path):
    try:
        sh.git('status', _cwd=_get_cwd(path))
        return True
    except sh.ErrorReturnCode_128:
        return False


def is_ignored_by_gitignore(path):
    try:
        sh.git('check-ignore', '--no-index', '-q', path, _cwd=_get_cwd(path))
        return True
    except sh.ErrorReturnCode_1:
        return False


def _list_unignored(base_dir, only_files, path):
    base, dirs, files = next(os.walk(path))
    for f in files:
        ff = os.path.join(base, f)
        if f == '.gitignore':
            yield ff
        elif not is_ignored_by_gitignore(ff):
            yield ff
    for d in dirs:
        if d == '.git':
            continue
        dd = os.path.join(base, d)
        if not is_ignored_by_gitignore(dd):
            if not only_files:
                yield dd
            yield from _list_unignored(base_dir, only_files, dd)


def _list_all(path, only_files):
    for base, dirnames, filenames in os.walk(path):
        for filename in filenames:
            yield os.path.join(base, filename)
        if not only_files:
            for dirname in dirnames:
                if dirname == '.git':
                    continue
                yield os.path.join(base, dirname)


def ls_recursive(path, relative=False, exclude_gitignore=False, only_files=False):
    """
    Always skips .git folder
    :param path: The path to list files (or dirs) inside it
    :param relative: If True, returned paths will be relative to `path`
    :param exclude_gitignore:  If True, only paths that are not ignored by .gitignore files will be returned.
                               In this case, `path` must be inside a git repo.
    :param only_files: If True, only files will be returned (skips directories)
    :return: A list of paths inside `path`
    """
    if exclude_gitignore:
        if not is_inside_git_repo(path):
            raise NotGitRepoException
        absolute_paths = list(_list_unignored(path, only_files, path))
    else:
        absolute_paths = list(_list_all(path, only_files))
    if relative:
        return [os.path.relpath(i, start=path) for i in absolute_paths]
    else:
        return absolute_paths


def load_statement_templates(statement_dir):
    from jinja2 import FileSystemLoader
    return FileSystemLoader([os.path.join(os.path.dirname(__file__), 'templates'), statement_dir])


def get_comment_style(commented_line, scb):
    comment_parts = commented_line.split(scb)
    if len(comment_parts) != 2:
        raise Exception
    ss, ff = comment_parts[0].lstrip(), comment_parts[1].rstrip()
    s, f = ss.rstrip(), ff.lstrip()
    return [s, ss[len(s):], ff[:-len(f)], f]


def uncomment(commented_line, comment_style):
    """
    Uncomments a single line of code
    :param commented_line: the line of code to be uncommented
    :param comment_style: a list of length 4, e.g. ['//', ' ', '', ''], ['/*', ' ', ' ', '*/']
    :return: the uncommented code
    """
    if not comment_style or len(comment_style) != 4:
        raise Exception
    pattern = r'^(\s*){}(?:{})?(.*?)(?:{})?{}\s*?(\n?)$'.format(*[re.escape(i) for i in comment_style])
    return re.sub(pattern, r'\1\2\3', commented_line)
