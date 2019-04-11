"""
Module which allow to run the server, instead of views.py
"""

from grandpy import app


if __name__ == "__main__":
    app.run(debug=False)
