from main import digital_root


def test_digital_root_16():
  assert digital_root(16) == 7


def test_digital_root_942():
  assert digital_root(942) == 6


def test_digital_root_132189():
  assert digital_root(132189) == 6


def test_digital_root_7():
  assert digital_root(7) == 7
