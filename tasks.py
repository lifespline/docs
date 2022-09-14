"""This is the project's task runner.
"""
from invoke import task
import os

@task
def docs(ctx, step='build'):
    """Generate documentation."""
    cmds = [
        "cd docs",
        "make html",
        "cp -a _build/html/. ../static/",
        "make clean",
        "echo && echo Your static documentation pages can be found at \'static\' && echo",
    ]

    ctx.run(';'.join(cmds))
