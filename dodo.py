import glob

from doitpy.pyflakes import Pyflakes
from doitpy.coverage import PythonModule, Coverage
from doitpy.pypi import PyPi
from doitpy import docs

DOIT_CONFIG = {'default_tasks': ['pyflakes', 'test']}


def task_pyflakes():
    yield Pyflakes().tasks('*.py')

def task_test():
    """run unit-test"""
    return {
        'actions': ['py.test'],
        'file_dep': ['doitcmd.py', 'test_doitcmd.py'],
        }

def task_coverage():
    cov = Coverage([PythonModule('doitcmd.py', 'test_doitcmd.py')])
    yield cov.all()
    yield cov.src()


def task_docs():
    doc_files = glob.glob('doc/*.rst') + ['README.rst']
    yield docs.spell(doc_files, 'doc/dictionary.txt')
    yield docs.sphinx('doc/', 'doc/_build/html/', task_dep=['spell'])
    yield docs.pythonhosted_upload('doc/_build/html/', task_dep=['sphinx'])


def task_pypi():
    """upload package to pypi"""
    pkg = PyPi()
    yield pkg.manifest_git()
    yield pkg.sdist_upload()

