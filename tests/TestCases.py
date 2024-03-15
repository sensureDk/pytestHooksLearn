import pytest
import time
def test_success():
	assert 1==1
def test_defeat():
	assert 1==2
def test_skip():
	time.sleep(3)
# @pytest.mark.xfail()
# def test_xfail():
# 	assert 2==2

def test_successO():
	assert 3==3
# if __name__ == '__main__':
#
# 	pytest.main()