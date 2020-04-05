import pathlib
from setuptools import setup
from setuptools import find_packages
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
REQ = (HERE / "requirements.txt").read_text()

setup(
    name="python-layer",
    version="1.0.1",
    description="Manage aws layers",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Charalampos Mageiridis",
    author_email="cmageiridis@protonmail.com",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    include_package_data=True,
    install_requires=REQ,
    scripts=["scripts/layer"],
    zip_safe=False,
)
