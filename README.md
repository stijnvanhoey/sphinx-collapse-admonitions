# sphinx-collapse-admonitions


A small sphinx extension to make it possible to collapse admonition blocks (notes, warnings, etc)
in Sphinx.


## Installation

You can install `sphinx-collapse-admonitions` with `pip`:

```
pip install sphinx-collapse-admonitions
```

## Usage

In your `conf.py` configuration file, add `sphinx_collapse_admonitions` to your extensions list.
E.g.:

```
extensions = [
    ...
    'sphinx_collapse_admonitions'
    ...
]
```

Now, whenever you wish for an admonition to be collapsed, add the following key:val pair
to the directive that you use: `:class: collapsed`.

For example, this code would create a collapsed "note" admonition:

```yaml
.. note::
    :class: collapsed

    This is my note.
```

If you'd like to choose your own admonition text, use the `admonition` directive on its own:

```yaml
.. admonition:: This is my admonition title
    :class: collapsed

    This is the admonition body, it will be hidden.
```

Clicking on the title section of the collapsed admonition will toggle the body's visibility.
