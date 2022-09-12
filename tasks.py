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
        "echo && echo Your static documentation pages can be found at \'docs/_build/html\' && echo",
    ]

    ctx.run(';'.join(cmds))
