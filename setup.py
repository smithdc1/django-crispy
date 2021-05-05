from setuptools import setup
import os

VERSION = "20.5"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="django-crispy",
    description="django-crispy is now django-crispy-forms",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    version=VERSION,
    install_requires=["django-crispy-forms"],
    classifiers=["Development Status :: 7 - Inactive"],
)
