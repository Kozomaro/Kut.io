from __future__ import print_function
from website import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    