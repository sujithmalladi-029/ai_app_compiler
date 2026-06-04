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

import streamlit as st

from pipeline.intent_extractor import IntentExtractor
from pipeline.system_designer import SystemDesigner
from pipeline.schema_generator import SchemaGenerator

from validators.validator import Validator
from repair.repair_engine import RepairEngine
from runtime.runtime_simulator import RuntimeSimulator


st.title("AI App Compiler")

prompt = st.text_area(
    "Enter application requirements"
)

if st.button("Generate"):

    extractor = IntentExtractor()
    designer = SystemDesigner()
    generator = SchemaGenerator()

    validator = Validator()
    repair_engine = RepairEngine()
    runtime = RuntimeSimulator()

    intent = extractor.extract(prompt)

    architecture = designer.design(intent)

    schemas = generator.generate(architecture)

    errors = validator.validate(schemas)

    if errors:
        schemas = repair_engine.repair(
            schemas,
            errors
        )

    runtime_result = runtime.run(schemas)

    st.subheader("Intent")
    st.json(intent.model_dump())

    st.subheader("Architecture")
    st.json(architecture.model_dump())

    st.subheader("UI Schema")
    st.json(schemas["ui"].model_dump())

    st.subheader("API Schema")
    st.json(schemas["api"].model_dump())

    st.subheader("DB Schema")
    st.json(schemas["db"].model_dump())

    st.subheader("Auth Schema")
    st.json(schemas["auth"].model_dump())

    st.subheader("Runtime Result")
    st.json(runtime_result)