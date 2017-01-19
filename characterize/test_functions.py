import os
from subprocess import Popen, PIPE

from shutil import rmtree


def test_functions():
    import characterize
    from sample_program.first.definitions import b
    from sample_program.second.definitions import a
    a(3,4)
    a(6,5)
    b(12,12)
    b(13,12)
    b(11,12)
    b(16,12)
    b(10,12)
    result=Popen(['py.test',os.path.abspath(os.curdir)+'/autotests'],stdout=PIPE)
    result.wait()
    output = result.communicate()
    rmtree('autotests')
    assert 'passed' in output[0]
