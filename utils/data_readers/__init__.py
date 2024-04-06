from pathlib import Path

ROOT_DIR = Path(__file__).parents[2].joinpath("test_data")

POSTS_JSON_FILE_PATH = Path.joinpath(ROOT_DIR, "json_placeholders/posts_filters.json")
BREWERY_TYPES_CSV_FILE_PATH = Path.joinpath(ROOT_DIR, "openbrewerydb/brewery_types.csv")
