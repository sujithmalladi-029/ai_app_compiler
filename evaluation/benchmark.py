import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import json
import time

from pipeline.intent_extractor import IntentExtractor
from pipeline.system_designer import SystemDesigner
from pipeline.schema_generator import SchemaGenerator

from validators.validator import Validator
from repair.repair_engine import RepairEngine
from runtime.runtime_simulator import RuntimeSimulator


extractor = IntentExtractor()
designer = SystemDesigner()
generator = SchemaGenerator()

validator = Validator()
repair_engine = RepairEngine()
runtime = RuntimeSimulator()


with open("evaluation/test_prompts.json", "r") as f:
    prompts = json.load(f)


success_count = 0

for item in prompts:

    start = time.time()

    intent = extractor.extract(item["prompt"])

    architecture = designer.design(intent)

    schemas = generator.generate(architecture)

    errors = validator.validate(schemas)

    if errors:
        schemas = repair_engine.repair(
            schemas,
            errors
        )

    result = runtime.run(schemas)

    end = time.time()

    latency = round(end - start, 3)

    print("\nPrompt:", item["prompt"])
    print("Runtime:", result["status"])
    print("Latency:", latency, "seconds")

    if result["status"] == "PASS":
        success_count += 1


print("\n======================")
print("Success Rate:",
      f"{success_count}/{len(prompts)}")