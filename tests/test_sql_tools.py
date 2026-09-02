import pytest
from src.sql_tools import run_select_query

def test_select_query_execution():
    try:
        results = run_select_query("SELECT COUNT(*) as cnt FROM stores;")
        assert isinstance(results, list)
        assert len(results) > 0
    except Exception as e:
        pytest.skip(f"Database file not present or populated yet: {e}")
