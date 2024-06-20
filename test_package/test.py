import sys

sys.path.append(".")

import test_package

print("Adding 2 + 3 = {}".format(test_package.add(2, 3)))
assert test_package.add(2, 3) == 5

print("Message: '{}'".format(test_package.msg()))
assert len(test_package.msg()) > 0
