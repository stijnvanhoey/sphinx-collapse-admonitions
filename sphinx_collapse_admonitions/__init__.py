"""A small sphinx extension to add "copy" buttons to code blocks."""
import os

__version__ = "0.0.2dev0"


def scb_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '_static'))
    app.config.html_static_path.append(static_path)

def setup(app):
    # Add our static path
    app.connect('builder-inited', scb_static_path)

    # Add relevant code to headers
    app.add_stylesheet('collapse_admonitions.css')
    app.add_js_file('collapse_admonitions.js')
    return {"version": __version__,
            "parallel_read_safe": True,
            "parallel_write_safe": True}
