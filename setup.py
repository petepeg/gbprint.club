import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="drafty",
    version="0.1",
    author="Petep",
    author_email="",
    description="create GB PDFs",
    packages=['drafty'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'Pillow']
)