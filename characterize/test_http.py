import os
from subprocess import Popen, PIPE

from shutil import rmtree



def test_http():
    import characterize
    from sample_program.second.definitions import c
    c("http://www.example.net")
    result=Popen(['py.test',os.path.abspath(os.curdir)+'/autotests'],stdout=PIPE)
    result.wait()
    output = result.communicate()
    rmtree('autotests')
    assert 'passed' in output[0]
