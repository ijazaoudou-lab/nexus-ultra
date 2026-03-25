import random
from typing import List, Dict

class EchoChamber:
    def __init__(self, memory=None):
        self.memory = memory or UltraMemory()
        self.angles = ["optimistic", "critical", "creative", "practical", "futurist"]

    def echo(self, prompt: str, num_threads: int = 4, depth: int = 1) -> Dict:
        """
        Run Echo Chamber on a prompt.
        Returns merged synthesis + individual threads for transparency.
        """
        threads = []
        for i in range(min(num_threads, len(self.angles))):
            angle = self.angles[i]
            # Simulate parallel reasoning (in real version, spawn async LLM calls here)
            thread_output = self._reason_thread(prompt, angle, depth)
            threads.append({"angle": angle, "output": thread_output})

        # Merge: simple weighted synthesis (expand with LLM later)
        synthesis = self._merge_threads(threads, prompt)

        return {
            "prompt": prompt,
            "threads": threads,
            "synthesis": synthesis,
            "confidence": round(0.75 + random.random() * 0.2, 2)  # placeholder
        }

    def _reason_thread(self, prompt: str, angle: str, depth: int) -> str:
        context = self.memory.get_context()
        # Placeholder reasoning — replace with real LLM call in production
        return f"[{angle.upper()}] {context}\nPrompt: {prompt}\n" \
               f"Response ({depth} depth): Thoughtful {angle} analysis with new ideas."

    def _merge_threads(self, threads: List[Dict], prompt: str) -> str:
        merged = f"Synthesis for: {prompt}\n\n"
        for t in threads:
            merged += f"• From {t['angle']}: {t['output'][:150]}...\n"
        merged += "\nFinal refined answer: Echo Chamber converged on a balanced, high-quality solution combining all angles."
        return merged
