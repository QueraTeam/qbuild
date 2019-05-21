*qbuild* is a build system for our technology challenges.

# Installation

For installing or updating qbuild, run the following commands:

```bash
$ git clone git@gitlab.com:codamooz/challenges/qbuild.git
$ cd qbuild
$ sudo pip3 install . 
```

# Challenge Structure

```
challenge-name (git repo)
├── src
│   ├── [ ... source and test files ... ]
│   ├── .gitignore (optional)
│   ├── .qignore (optional)
│   ├── .qsolution (optional)
│   └── .qtest (optional, BUT USUALLY NEEDED)
├── statement
│   ├── attachments
│   │   └── [ ... image files ... ]
│   └── statement.md
├── .gitignore
├── README.md  (generated from statement/statement.md, DO NOT EDIT)
├── tester_config.json
└── valid_files
```

# CLI Usage

## `qbuild`: Build the challenge

First, `cd` to the root of the challenge's git repository. Then run `qbuild` command. That's it!

```bash
$ cd GIT-REPO
$ qbuild
```

Folder `dist` and file `README.md` will be generated.
It creates folder `.qbuild` for its internal work.
Do not push it. Add `dist` and `.qbuild` to gitignore.

## `qbuild diff`

```bash
$ cd GIT-REPO
$ qbuild diff
```

This command generates a diff between
`initial` and `model_solution` exports.

It's helpful for checking that things are set correctly.

## `qbuild --version`

Prints currently installed version.


## Features

### Problem Statement

```
statement
├── attachments
│   ├── image1.png
│   └── image2.png
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


### Ignore files: `.qignore`, `.qsolution`, `.qtest`

These files must be at the root of `src` folder.
Their syntax is like gitignore.

You can specify test files in `.qtest`
and solution files in `.qsolution`.

Files ignored by `.qignore` will be removed in all exports.

**Note**: `.qhide` is deprecated and is replaced by `.qsolution`.

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

- `_q_hide_from_user_begin`: replaced by `_q_solution_begin`
- `_q_hide_from_users_end`: replaced by `_q_end`

### Replacement Rules: `.nosolution`, `.notest`

When comment directives can't help... 

```
src/path/to/some/file.js
src/path/to/some/file.nosolution.js  (`file.js` without solution)

src/path/to/some/file.js
src/path/to/some/file.notest.js  (`file.js` without test)
```

**Note**: `.initial` is deprecated and is replaced by `.nosolution`.
