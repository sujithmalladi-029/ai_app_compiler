from pipeline.intent_extractor import IntentExtractor
from pipeline.system_designer import SystemDesigner
from pipeline.schema_generator import SchemaGenerator

from validators.validator import Validator
from repair.repair_engine import RepairEngine
from runtime.runtime_simulator import RuntimeSimulator


# ==========================
# Stage 1: Intent Extraction
# ==========================

extractor = IntentExtractor()

intent = extractor.extract(
    "Build CRM with login, contacts, dashboard and payments. Admins can see analytics."
)

print("Intent:")
print(intent.model_dump())


# ==========================
# Stage 2: System Design
# ==========================

designer = SystemDesigner()

architecture = designer.design(intent)

print("\nArchitecture:")
print(architecture.model_dump())


# ==========================
# Stage 3: Schema Generation
# ==========================

generator = SchemaGenerator()

schemas = generator.generate(architecture)

print("\nUI Schema:")
print(schemas["ui"].model_dump())

print("\nAPI Schema:")
print(schemas["api"].model_dump())

print("\nDB Schema:")
print(schemas["db"].model_dump())

print("\nAuth Schema:")
print(schemas["auth"].model_dump())


# ==========================
# TEST REPAIR ENGINE
# ==========================

# Uncomment this line to simulate an error
# schemas["db"].tables = []


# ==========================
# Stage 4: Validation
# ==========================

validator = Validator()

errors = validator.validate(schemas)

print("\nValidation Results:")

if len(errors) == 0:
    print("PASS")
else:
    for error in errors:
        print("-", error)


# ==========================
# Stage 5: Repair Engine
# ==========================

repair_engine = RepairEngine()

if len(errors) > 0:

    print("\nRepairing...")

    schemas = repair_engine.repair(
        schemas,
        errors
    )

    errors = validator.validate(
        schemas
    )

    print("\nAfter Repair:")

    if len(errors) == 0:
        print("PASS")
    else:
        for error in errors:
            print("-", error)


# ==========================
# Stage 6: Runtime Simulator
# ==========================

runtime = RuntimeSimulator()

result = runtime.run(schemas)

print("\nRuntime Validation:")
print(result)