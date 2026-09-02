from src.graph import workflow
from src.memory import ConversationMemory

def main():
    memory = ConversationMemory()
    print("--- Retail SQL Data Analyst Agent (SQLite Mode) ---")
    
    while True:
        question = input("\nUser Question: ")
        if question.lower().strip() in ["exit", "quit"]:
            break

        context = memory.get_context_prompt()
        initial_state = {"question": question, "context": context, "sql": "", "rows": [], "answer": "", "error": ""}
        
        result = workflow.invoke(initial_state)
        
        print("\n[Generated SQL]:", result.get("sql"))
        if result.get("error"):
            print("\n[Safety/Query Error]:", result.get("error"))
        else:
            print("\n[Business Answer]:", result.get("answer"))
            memory.add_turn(question, result.get("sql"), result.get("answer"))

if __name__ == "__main__":
    main()
