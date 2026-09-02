from typing import TypedDict, Any
from langgraph.graph import StateGraph, END
from src.tiger_gateway_client import call_llm
from src.sql_tools import run_select_query
from src.safety import validate_sql

SCHEMA_INFO = """
Tables & Columns in SQLite:
- stores(store_id, store_name, region, city, store_type)
- products(product_id, product_name, category, sub_category, base_price)
- customers(customer_id, customer_segment, signup_date, preferred_channel, city)
- sales_transactions(order_id, order_date, store_id, product_id, customer_id, sales_channel, units_sold, unit_price, discount_pct, payment_status, delivery_status)
- returns(return_id, order_id, return_date, return_reason)
"""

class AgentState(TypedDict):
    question: str
    context: str
    sql: str
    rows: list[dict[str, Any]]
    answer: str
    error: str

def generate_sql_node(state: AgentState) -> dict:
    prompt = f"""You are an expert SQLite analyst. Write a valid SQLite SELECT query for the user question.
Schema:
{SCHEMA_INFO}

{state.get('context', '')}

Rules:
- Return ONLY the raw SQL query. No explanation, markdown code blocks, or extra text.
- Use exact column names provided.

Question: {state['question']}"""
    
    sql = call_llm([{"role": "user", "content": prompt}])
    return {"sql": sql}

def execute_sql_node(state: AgentState) -> dict:
    try:
        validated = validate_sql(state["sql"])
        rows = run_select_query(validated)
        return {"rows": rows, "error": ""}
    except Exception as e:
        return {"rows": [], "error": str(e)}

def summarize_node(state: AgentState) -> dict:
    if state.get("error"):
        return {"answer": f"Execution failed: {state['error']}"}
    
    prompt = f"""Provide a concise business summary based on the SQL query results.
Question: {state['question']}
SQL Used: {state['sql']}
Data Rows: {state['rows'][:20]}

Summarize clearly in simple business terms."""
    
    answer = call_llm([{"role": "user", "content": prompt}])
    return {"answer": answer}

builder = StateGraph(AgentState)
builder.add_node("generate_sql", generate_sql_node)
builder.add_node("execute_sql", execute_sql_node)
builder.add_node("summarize", summarize_node)

builder.set_entry_point("generate_sql")
builder.add_edge("generate_sql", "execute_sql")
builder.add_edge("execute_sql", "summarize")
builder.add_edge("summarize", END)

workflow = builder.compile()
