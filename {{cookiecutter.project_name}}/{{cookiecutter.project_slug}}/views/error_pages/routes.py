from flask import render_template


def error_404(error):
    return render_template("error_pages/404.html"), 404


def error_500(error):
    return render_template("error_pages/500.html"), 500