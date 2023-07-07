# treeGen -  A directory Tree Generator

Simple Python CLI App to generate a directory tree for a given path

## Current TaskList

- [ ] Add support for sorting files and directories
- [ ] Add icons and colors to the tree diagram
- [X] Set up the application to publish it as an open source project

## Run the App

To run **treGen**, you need to intall it via pip:

1. Create and activate a Python virtual environment

```sh
pip install treGen
```

**Note:** The `-h` or `--help` option provides help on how to use treGen.

To take a quick test on **treGen**, you can use the sample `home/` directory provided along with the application's code and run the following command:br

```sh
$ treGen ../hello/

../hello/
│
├── hello/
│   ├── __init__.py
│   └── hello.py
│
├── tests/
│   └── test_hello.py
│
├── requirements.txt
├── setup.py
├── README.md
```

That's it! You've generated a nice directory tree diagram.

## Current Features

If you run treGen with a directory path as an argument, then you get the full directory tree printed on your screen. The default input directory is your current directory.

treGen also provides the following options:

- `-v`, `--version` shows the application version and exits
- `-h`, `--help` show a usage message
- `-d`, `--dir-only` generates a directory-only tree
- `-o`, `--output-file` generates a tree and save it to a file in markdown format

## Release History

- 0.1.0
- 1.0.0
- 2.0.0
  - Serious breaking issues with console scripts
- 3.0.0
  - Finally got the setup.py to work xD
- 4.0.0
  - A work in progress

## About the Author + Original Fork Address

Leodanis Pozo Ramos - Email: leodanis@realpython.com
A fork from [https://github.com/realpython/materials/tree/master/directory-tree-generator-python](https://github.com/realpython/materials/tree/master/directory-tree-generator-python)
