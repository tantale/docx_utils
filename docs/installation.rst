============
Installation
============

At the command line::

    pip install docx-utils


To use this library in your application, add the dependency in the :file:`setup.py`::

    setup(
        name="my_app",
        version="1.0.3",
        install_requires=[
            'docx-utils',
            ...
        ],
        ...
    )


Don't forget to update your virtualenv::

    pip install -e .


The ``docx_utils`` library should be available, check it with::

    docx_utils --version

