import pytest

from utils.data_readers import BREWERY_TYPES_CSV_FILE_PATH
from csv import reader


def csv_brewery_types_reader():
    # brewery_types = []
    with open(BREWERY_TYPES_CSV_FILE_PATH) as brewery_types_file:
        brewery_types_reader = reader(brewery_types_file)
        for brewery_type in brewery_types_reader:
            yield pytest.param(brewery_type[0], id=brewery_type[0])
            # brewery_types += brewery_type
