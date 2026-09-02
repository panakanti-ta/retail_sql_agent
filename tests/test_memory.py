from src.memory import ConversationMemory

def test_conversation_memory():
    mem = ConversationMemory()
    assert mem.get_context_prompt() == ""
    
    mem.add_turn("What is total sales?", "SELECT SUM(units_sold*unit_price) FROM sales_transactions;", "Total sales is $100,000.")
    context = mem.get_context_prompt()
    assert "What is total sales?" in context
    assert "Total sales is $100,000." in context
