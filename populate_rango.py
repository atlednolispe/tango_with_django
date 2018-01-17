import os
import django

# imported your project’s settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tango_with_django.settings")
django.setup()

# must under those settings
# or django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet
from rango.models import Category, Page


def populate():
    python_pages = [
        {
            "title": "Official Python Tutorial",
            "url": "http://docs.python.org/3/tutorial/",
            "views": 100,
        },
        {
            "title": "How to Think like a Computer Scientist",
            "url": "http://www.greenteapress.com/thinkpython/",
            "views": 80,
        },
        {
            "title": "Learn Python in 10 Minutes",
            "url": "http://www.korokithakis.net/tutorials/python/",
            "views": 60,
        },
    ]

    django_pages = [
        {
            "title": "Official Django Tutorial",
            "url": "https://docs.djangoproject.com/en/2.0/intro/tutorial01/",
            "views": 90,
        },
        {
            "title": "Django Rocks",
            "url": "http://www.djangorocks.com/",
            "views": 70,
        },
        {
            "title": "How to Tango with Django",
            "url": "http://www.tangowithdjango.com/",
            "views": 50,
        },
    ]

    other_pages = [
        {
            "title": "Bottle",
            "url": "http://bottlepy.org/docs/dev/",
            "views": 75,
        },
        {
            "title": "Flask",
            "url": "http://flask.pocoo.org",
            "views": 95,
        },
    ]

    cats = {
        "Python": {
            "pages": python_pages,
            "views": 128,
            "likes": 64,
        },
        "Django": {
            "pages": django_pages,
            "views": 64,
            "likes": 32,
        },
        "Other Frameworks": {
            "pages": other_pages,
            "views": 32,
            "likes": 16,
        }
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            v = p.get("views", 0)
            add_page(c, p["title"], p["url"], v)

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
