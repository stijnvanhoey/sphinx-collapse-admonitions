# Instructions for creating a new release

Spinx-Copybutton is [hosted on the pypi repository](https://pypi.org/project/sphinx-collapse-admonitions/).
To create a new release of Sphinx-Collapse-Admonitions, you need to do these things:

## Before you start

1. Ensure that you have push access to the [Sphinx-Collapse-Admonitions pypi repository](https://pypi.org/project/sphinx-collapse-admonitions/)
2. Install [the twine package](https://twine.readthedocs.io/en/latest/). This is a package that helps you
   bundle and push new Python package distributions to pip.

## To create the release

To create a new release, [open an issue](https://github.com/choldgraf/sphinx-collapse-admonitions/issues/new) to keep
track of the to-do list for the release. Copy/paste the following markdown into the issue
and check off the boxes as you complete items:


```
- [ ] Ensure that the [Sphinx-Collapse-Admonitions version number](https://github.com/choldgraf/sphinx-collapse-admonitions/blob/master/jupyter_book/__init__.py)
   is correct, and remove the `dev0` part of the version number.
   Make a PR with the new number and merge into master.
- [ ] Create a new distribution for Sphinx-Collapse-Admonitions by
   [following the twine release instructions](https://twine.readthedocs.io/en/latest/#using-twine)
- [ ] Confirm that the new version of Sphinx-Collapse-Admonitions [is posted to pypi](https://pypi.org/project/sphinx-collapse-admonitions/)
- [ ] Bump the [Sphinx-Collapse-Admonitions version number](https://github.com/choldgraf/sphinx-collapse-admonitions/blob/master/jupyter_book/__init__.py) to
   the next minor (or major) release and append `dev0` to the end.
- [ ] Celebrate! You've just released a new version of Sphinx-Collapse-Admonitions!
```
