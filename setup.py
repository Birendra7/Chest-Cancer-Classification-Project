import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "Chest-Cancer-Classification-Project"
AUTHOR_USER_NAME = "Birendra7"
SRC_REPO = "ccclassificer"
AUTHOR_EMAIL = "birendraraaz620@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author="Birendra Kumar",
    author_email=AUTHOR_EMAIL,
    description="A small Python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}.git",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
