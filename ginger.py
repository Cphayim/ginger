# -*- coding: utf-8 -*-
"""
  Created by Cphayim at 2018/7/4 18:23
"""
from app.app import create_app

__author__ = 'Cphayim'

app = create_app()

if __name__ == '__main__':
    app.run(
        debug=app.config.get('DEBUG', False)
    )
