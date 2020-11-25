from setuptools import setup

setup(
    name="todo",
    version="1.0.0",
    packages=['todo'],
    entry_points={
        'console.scripts': ['todo = todo.__main__:main']
    }
)