import pytest
from src.safety import validate_sql

def test_valid_select():
    sql = "SELECT * FROM stores;"
    assert validate_sql(sql) == "SELECT * FROM stores"

def test_block_insert():
    with pytest.raises(ValueError, match="Safety Violation"):
        validate_sql("INSERT INTO stores VALUES ('ST-099', 'Test', 'North', 'Delhi', 'Mart');")

def test_block_pragma():
    with pytest.raises(ValueError, match="Safety Violation"):
        validate_sql("PRAGMA table_info(stores);")
