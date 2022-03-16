======================
Cookiecutter Package
======================

Cookiecutter_ template for a Python package.

Features
--------

* Build package

Build Status
-------------


Quickstart
----------

Prepare working environment (if you have'nt do this yet)::

    python3 -m venv env
    source env/bin/activate

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter <path_to_project>

Then:

* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Add a ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Use ``requirements-cpu.txt`` and ``requirements-cuda.txt`` files to specify CPU and CUDA specific the packages you will need for
  your project and their versions (i.e. ``onnxruntime`` and ``onnxruntime-gpu``).
* Wrap your AI assets into Model following guideline in the code
* Create CLI and Demo API for your project
* Build distributable ``whl`` files with the command::

    make dist

* Zip and share with us your *.whl and *.zip file and we will publish it in `neuromarket.ai`


For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
