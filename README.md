*qbuild* is a build system for our technology challenges.

# Installation

For installing or updating qbuild, run the following commands:

```bash
git clone git@gitlab.com:codamooz/challenges/qbuild.git
cd qbuild
sudo pip3 install . 
```

# Usage

## Build the challenge

First, `cd` to the root of the challenge's git repository. Then run `qbuild` command. That's it!

```bash
cd GIT-REPO
qbuild
```

Folder `dist` will be created, containing `..._initial.zip`, `model_solution.zip`, `test.zip`.

## Diff

```bash
cd GIT-REPO
qbuild diff
```

This command builds the challenges (like `qbuild` command), and then generates a diff between
`initial` and `model_solution`.

It's helpful for checking that things are set correctly.

## Version

For printing current installed version:

```bash
qbuild --version
```