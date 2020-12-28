*qbuild* is a build system for Quera technology challenges.

[![PyPI](https://img.shields.io/pypi/v/qbuild)](https://pypi.org/project/qbuild/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Installation

For installing qbuild, run the following command:

```bash
$ sudo pip install qbuild 
```

# Challenge Structure

```
challenge-name (git repo)
├── src
│   ├── [ ... source and test files ... ]
│   ├── .gitignore (optional)
│   ├── .qignore (optional)
│   ├── .qsolution (optional)
│   ├── .qtest (optional, BUT USUALLY NEEDED)
│   └── .qrun.py (optional)
├── statement
│   ├── attachments
│   │   └── [ ... image files ... ]
│   └── statement.md
├── .gitignore
├── README.md  (generated from statement/statement.md, DO NOT EDIT)
├── tester_config.json
└── valid_files
```

# CLI Usage

### `qbuild`: Build the challenge

First, `cd` to the root of the challenge's git repository. Then run `qbuild` command. That's it!

```bash
$ cd GIT-REPO
$ qbuild
```

For `jupyter` problems if you need generate nonquera initial:

```bash
$ qbuild --jupyter
```

Folder `dist` and file `README.md` will be generated.
It creates folder `.qbuild` for its internal work.
Do not push it. Add `dist` and `.qbuild` to gitignore.

### `qbuild diff`

```bash
$ cd GIT-REPO
$ qbuild diff
```

This command generates a diff between
`initial` and `model_solution` exports.

It's helpful for checking that things are set correctly.

### `qbuild tree`

```bash
$ qbuild tree path/to/some/directory
```

Use `qbuild tree` to print the tree structure of a directory.
**Do not** use `tree` command or anything else.

### `qbuild --version`

Prints currently installed version.


# Features

### Problem Statement

```
statement
├── attachments
│   ├── image1.png
│   └── image2.png
└── statement.md
```

`statement.md` is a Jinja2 template and must inherit `statement_base.md`.
You can use variables `has_initial`, `initial_structure`, `solution_structure`.

    {% extends "statement_base.md" %}
    
    {% block name %}Problem Name{% endblock %}
    
    {% block readme %}
    ... extra info about problem ...
    {% endblock readme %}
    
    {% block intro %}
    ... intro ...
    ![Image 1](attachments/image1.png)
    {% endblock intro %}
    
    {% block details %}
    ... details ...
    {% endblock details %}
    
    {% block notes %}
    ... notes ...
    ```
    {{ solution_structure }}
    ```
    {% endblock notes %}


### Ignore files: `.qignore`, `.qsolution`, `.qtest`, `.qsampletest`

These files must be at the root of `src` folder.
Their syntax is like gitignore.
You can specify test files in `.qtest`
You can specify sample test files in `.qsampletest`. This files just hide in `model_solution` export.
and solution files in `.qsolution`.
Files ignored by `.qignore` will be removed in all exports.

**Warning**: `.qhide` is deprecated and is replaced by `.qsolution`.


### Replacement Rules: Comment Directives

```
// _q_solution_begin
  ... Part of Solution ...
// _q_end

// _q_test_begin
  ... Part of Test ...
// _q_end
```

They can also have a `replace` block:

```
// _q_solution_begin
  ... Part of Solution ...
// _q_replace
//  ... This will be uncommented & replaced ...
// _q_end

/* _q_test_begin */
  ... Part of Test ...
/* _q_replace */
/*  ... This will be uncommented & replaced ... */
/* _q_end */
```

Any one-line comment syntax is supported.

Comments in each block should follow the same syntax.
e.g. You can't mix `// ...` and `/* ... */`.

**Warning**: These directives are depricated:

- `_q_hide_from_users_begin`: replaced by `_q_solution_begin`
- `_q_hide_from_users_end`: replaced by `_q_end`

### Replacement Rules: `.nosolution`, `.notest`

When comment directives can't help... 

```
src/path/to/some/file.js
src/path/to/some/file.nosolution.js  (`file.js` without solution)

src/path/to/some/file.js
src/path/to/some/file.notest.js  (`file.js` without test)
```

**Warning**: `.initial` is deprecated and is replaced by `.nosolution`.


### Build hook: `.qrun.py`

`.qrun.py` must be at the root of `src`.
`qbuild` runs `.qrun.py` in each export.

Arguments passed to `.qrun.py`:

- `--hide-solution`: If passed, current export shouldn't contain solutions.
- `--hide-test`: If passed, current export shouldn't contain tests.

Use `.qrun.py` only if other features are not enough.
