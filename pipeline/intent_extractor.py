from schemas.app_schema import IntentSchema
from pipeline.mock_llm import MockLLM

class IntentExtractor:

    def __init__(self):
        self.llm = MockLLM()

    def extract(self, prompt):

        data = self.llm.generate(prompt)

        return IntentSchema(**data)