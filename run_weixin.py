# -*- coding: utf-8 -*-

from app import app


if __name__ == '__main__':
    app.run('0.0.0.0', 10023, debug=False, threaded=False)
