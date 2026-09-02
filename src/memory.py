class ConversationMemory:
    def __init__(self):
        self.history = []

    def add_turn(self, question: str, sql: str, summary: str):
        self.history.append({"question": question, "sql": sql, "summary": summary})

    def get_context_prompt(self) -> str:
        if not self.history:
            return ""
        context = "Previous Conversation History:\n"
        for turn in self.history[-3:]:
            context += f"User: {turn['question']}\nGenerated SQL: {turn['sql']}\nSummary: {turn['summary']}\n---\n"
        return context
