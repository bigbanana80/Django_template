from jinja2 import Environment
from django.urls import reverse
from django.contrib.staticfiles.storage import staticfiles_storage
from datetime import datetime


def get_year():
    return datetime.today().year


def url_for(endpoint, **values):
    if endpoint == "static":
        filename = values.get("filename", "")
        return staticfiles_storage.url(filename)
    return reverse(endpoint, args=values.get("args", ()), kwargs=values)


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": staticfiles_storage.url,
            "url": reverse,
            "url_for": url_for,
            "year": get_year,
        }
    )
    return env
