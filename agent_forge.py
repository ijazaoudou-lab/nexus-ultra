from nexus_core import NexusCore

class AgentForge:
    @staticmethod
    def spawn(role: str) -> NexusCore:
        agent = NexusCore()
        print(f"Spawned specialized agent: {role}")
        return agent
