# Lab 0: Getting started

Advanced Python Course  
Chalmers DAT690 / DIT516 / DAT516  
2026

by John J. Camilleri

## Purpose

The purpose of this lab is to get you up and running with everything you need to start working on Labs 1–3.

## 1. Python development environment

Firstly, it is essential that you have a working Python installation on your computer,
together with a text editor or IDE such as VS Code.
You also need to have some familiarity with your computer's terminal/shell.

Hopefully you already have these from a previous course.
Note that web-based solutions like the Self Practice tool or Jupyter Notebook will **not** be enough.

Before progressing to the next step, ensure that you can:

1. Create, edit and save a "hello world" Python file on your computer.
2. Run this Python file from your IDE, e.g. by clicking the ▶ button in VS Code.
3. Run this Python file from your terminal, e.g. by running `python3 hello.py`

## 2. Virtual environments

In this course we are going to be installing and using external Python libraries.
In order to be able to do this, you need to be familiar with how to set up virtual environments.

The general idea is that each project has its own virtual environment into which packages are installed.
See the instructions in the lecture notes here: [Packages and virtual environments](https://cse-chalmers-gu-python.github.io/chalmers-advanced-python/lecture-notes/python-guide#311-tutorial-12-packages-and-virtual-environments)

Before progressing to the next step, ensure that you can:

1. Create a Python virtual environment and activate it
2. Install the external library `rich` into your virtual environment with `pip install rich`
3. Import this library in your own code and use it, e.g. with this code snippet:
    ```python
    from rich import print
    print("Hello, [bold green]World[/bold green]!", ":snake:")
    ```

## 3. Git

The Git version control tool will be used throughout this course for:

- distributing code templates
- collaboration between lab partners
- submission of code

It is therefore important to get the hang of Git early on.
To complete this step, do the following:

1. Familiarise yourself with Git by reading the walkthrough in the lecture notes: [Introduction to Git](https://cse-chalmers-gu-python.github.io/chalmers-advanced-python/lecture-notes/python-guide#a-appendix-git-version-control-system)
2. Set up an SSH key and ensure you have Git installed: [Setting up SSH and Git](../setup-ssh-and-git.md)
3. Access Chalmers GitLab as described here: [Working with Chalmers GitLab](../chalmers-gitlab.md)
4. Try out creating a repository and using it:
    1. Create a new repository in GitLab: <https://git.chalmers.se/projects/new#blank_project>
    2. Clone the repository locally, using `git clone ...`
    3. Add some files the repository, commit and push them.
    4. View your repository on GitLab and ensure that the new files appear there.

