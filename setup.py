import setuptools
try:
    with open("README.md", "r") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description ="Not available"


REQUIREMENTS = [
                'numpy',
                'pandas',
                'matplotlib',
                'seaborn',
                'tensorflow >= 2.2',
                'Fire'
                ]
setuptools.setup(
    name="stavpytools", # Replace with your own username
    version="1.0-rc",
    author="Kaustav Chaudhury",
    author_email="kaustav28c@gmail.com",
    description="This helps to reduce code by predefined packages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxkaustav/stavpytools",
    install_requires=REQUIREMENTS,
    python_requires='>=3.6',
)