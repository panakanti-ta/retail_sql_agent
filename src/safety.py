import re

BLOCKED_KEYWORDS = [
    "insert", "update", "delete", "drop", "alter", "truncate", 
    "create", "replace", "vacuum", "pragma", "attach"
]

def validate_sql(sql: str) -> str:
    cleaned = sql.strip().strip("`").strip()
    if cleaned.startswith("```sql"):
        cleaned = cleaned[6:]
    if cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    cleaned = cleaned.strip()
    
    lower_sql = cleaned.lower()
    
    if not lower_sql.startswith("select"):
        raise ValueError("Safety Violation: Only SELECT queries are permitted.")
    if ";" in cleaned.rstrip(";"):
        raise ValueError("Safety Violation: Multiple SQL statements are blocked.")
    if any(re.search(rf"\b{word}\b", lower_sql) for word in BLOCKED_KEYWORDS):
        raise ValueError("Safety Violation: Destructive operations are blocked.")
    
    return cleaned.rstrip(";")
