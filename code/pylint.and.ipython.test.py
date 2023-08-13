"""Simple python script

This is an example to use Pylint and IPython on VScode

Entire docstring is necessary to avoid the follow Pylint message:
pylint.and.ipython.test.py:1:0: C0114: Missing module docstring (missing-module-docstring)
There is also a comment "# pylint: disable=" with the list of error codes disabled.

How to use Pylint:

    $ pip install pylint
    $ pylint pylint.and.ipython.test.py
    ************* Module pylint.and.ipython.test
    pylint.and.ipython.test.py:13:0: W0104: Statement seems to have no effect (pointless-statement)

# license MIT
# support https://github.com/bilardi/neuromatch/issues
"""
# pylint: disable=C0103

a = 1
b = 2
c = a + b
c

# install extension of Hoang Kim Lai
    # IPy [vsc], ipython v2023.3.0
# select statements
# and click right over the selection
    # and select "Run Selection / Line in Interactive Window"
    # from "Run in Interactive Window"
# or shift + enter for running into the terminal
