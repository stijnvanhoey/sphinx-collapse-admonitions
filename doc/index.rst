==========================
sphinx-collapse-admonition
==========================

A small sphinx extension to make it possible to collapse admonition blocks
(notes, warnings, etc) in Sphinx.

For example, see these admonition blocks:


.. admonition:: Here's a collapsed admonition
    :class: collapsed

    It was created with this code:

    .. code:: rst

        .. admonition:: Here's a collapsed admonition!
            :class: collapsed

            (admonition body here)

This will work for any sub-class of "admonition" such as note or warning:

.. note::
    :class: collapsed

    This is a note, you don't control it's title!

.. warning::
    :class: collapsed

    This is your warning!

You can even nest admonitions (for example, if you want to make a
terrible joke)

.. admonition:: What is the integral of :math:`\frac{1}{cabin}`?
    :class: collapsed

    .. admonition:: Is it a :math:`log(cabin)`?
        :class: collapsed

        Nope, it's a houseboat--you forgot the C.

        (I apologize for `this terrible pun <https://en.wikipedia.org/wiki/Mathematical_joke#Pun-based_jokes>`_).


============
Installation
============

You can install `sphinx-collapse-admonitions` with `pip`:

.. code:: bash

    pip install sphinx-collapse-admonitions

=====
Usage
=====

In your ``conf.py`` configuration file, add ``sphinx_collapse_admonitions``
to your extensions list.

E.g.:

.. code:: python

    extensions = [
        ...
        'sphinx_collapse_admonitions'
        ...
    ]

Now, whenever you wish for an admonition to be collapsed, add the
``:class: collapsed`` parameter to the admonition directive that you use.

For example, this code would create a collapsed "note" admonition:

.. code:: rst

    .. note::
        :class: collapsed

        This is my note.

Here's how it looks:

.. note::
    :class: collapsed

    This is my note.

If you'd like to choose your own admonition text, use the ``admonition``
directive on its own:

.. code:: rst

    .. admonition:: This is my admonition title
        :class: collapsed

        This is the admonition body, it will be hidden.

Clicking on the title section of the collapsed admonition will toggle the
body's visibility.
