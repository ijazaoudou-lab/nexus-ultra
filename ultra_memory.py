class UltraMemory:
    def __init__(self):
        self.short_term = []   # current session
        self.long_term = {}    # key: topic → list of facts

    def add(self, text, topic="general"):
        self.short_term.append(text)
        if topic not in self.long_term:
            self.long_term[topic] = []
        self.long_term[topic].append(text)

    def recall(self, topic="general", limit=5):
        return self.long_term.get(topic, [])[-limit:]

    def get_context(self):
        return "\n".join(self.short_term[-10:])  # last 10 messages
