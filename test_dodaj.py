import pytest


#@pytest.mark.skip
#@pytest.mark.xfail
@pytest.mark.parametrize("input1, input2, output",[(5,5,10),(3,5,12)])
def test_dodaj(input1, input2, output):
    assert input1+input2 == output, 'nie bangla'