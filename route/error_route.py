from flask import render_template

import app


@app.app.errorhandler(404)
def page_not_found(error):
    return render_template('Not found'), 404
