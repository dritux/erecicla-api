# -*- coding: utf-8 -*-
from collector import create_app

if __name__ == "__main__":
    app = create_app()
    app.run('0.0.0.0', 5000, debug=True)
