import os
from subprocess import Popen, PIPE

from shutil import rmtree


def test_thirdparty():
    import characterize
    from sample_program.second.definitions import a
    a(5,6)
    from third_party.library_functions import very_important_function
    very_important_function(5,6)
    result=Popen(['py.test',os.path.abspath(os.curdir)+'/autotests'],stdout=PIPE)
    result.wait()
    output = result.communicate()
    rmtree('autotests')
    assert 'passed' in output[0]
    assert 'very_important_function' not in output[0]
