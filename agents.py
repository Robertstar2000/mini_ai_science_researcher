# agents.py
from pydantic import BaseModel
from typing import Dict, Any
from settings import client
import os

class Agent(BaseModel):
    def __init__(self):
        super().__init__()

class ResearcherAgent(Agent):
    def research(self, topic: str) -> str:
        prompt = f"Conduct an in-depth research on the topic: '{topic}'. Use graduate-level language and focus on formal research paper content."
        response = self._generate_response(prompt)
        return response

    def _generate_response(self, prompt: str) -> str:
        try:
            completion = client.chat.completions.create(
                model=os.environ.get("GROQ_MODEL_NAME"),
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1024,
                top_p=1,
                stream=False,
                stop=None,
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error during Groq API request: {e}")
            return ""

class WriterAgent(Agent):
    def write(self, research: str, feedback: str = "") -> str:
        prompt = f"Based on the research: '{research}', write a detailed section for a formal research paper. {feedback}"
        response = self._generate_response(prompt)
        return response

    def _generate_response(self, prompt: str) -> str:
        # Similar implementation as in ResearcherAgent
        try:
            completion = client.chat.completions.create(
                model=os.environ.get("GROQ_MODEL_NAME"),
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=1024,
                top_p=1,
                stream=False,
                stop=None,
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error during Groq API request: {e}")
            return ""

class CriticAgent(Agent):
    def critique(self, content: str) -> str:
        prompt = f"Review the following content for a formal research paper. Provide feedback for improvement: '{content}'"
        response = self._generate_response(prompt)
        return response

    def _generate_response(self, prompt: str) -> str:
        # Similar implementation as in ResearcherAgent
        try:
            completion = client.chat.completions.create(
                model=os.environ.get("GROQ_MODEL_NAME"),
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=512,
                top_p=1,
                stream=False,
                stop=None,
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error during Groq API request: {e}")
            return ""
