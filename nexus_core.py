from echo_chamber import EchoChamber
from ultra_memory import UltraMemory

class NexusCore:
    def __init__(self):
        self.memory = UltraMemory()
        self.echo = EchoChamber(self.memory)

    def think(self, prompt: str, use_echo: bool = True):
        self.memory.add(prompt, topic="user_input")
        
        if use_echo:
            result = self.echo.echo(prompt)
            self.memory.add(result["synthesis"], topic="echo_output")
            return result
        else:
            # Simple direct response
            return {"synthesis": f"Direct response to: {prompt}"}
