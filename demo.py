from nexus_core import NexusCore
from agent_forge import AgentForge

def main():
    nexus = NexusCore()
    
    print("=== Nexus Ultra v0.3 Echo Expansion Demo ===\n")
    
    test_prompt = "How can we make Nexus Ultra the most powerful open collaborative AI framework?"
    
    print("Running Echo Chamber...\n")
    result = nexus.think(test_prompt, use_echo=True)
    
    print("SYNTHESIS:")
    print(result["synthesis"])
    print(f"\nConfidence: {result['confidence']}")
    
    print("\nIndividual Threads:")
    for thread in result["threads"]:
        print(f"→ {thread['angle']}: {thread['output'][:120]}...")

    # Spawn an agent
    researcher = AgentForge.spawn("Research Agent")
    print("\nDemo complete. Nexus Ultra is alive and echoing!")

if __name__ == "__main__":
    main()
