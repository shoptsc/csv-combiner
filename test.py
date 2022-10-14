
from csv_combiner import csvCombiner

import pytest


file = [['./fixtures/clothing.csv', './fixtures/accessories.csv', './fixtures/household_cleaners.csv']]
@pytest.mark.parametrize("a", csvCombiner(file))

def test_checkdata_from_file(a):
    print(a)
