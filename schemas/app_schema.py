from pydantic import BaseModel
from typing import List, Dict


class IntentSchema(BaseModel):
    app_type: str
    features: List[str]
    roles: List[str]


class ArchitectureSchema(BaseModel):
    entities: List[str]
    pages: List[str]
    role_permissions: Dict[str, List[str]]


class UISchema(BaseModel):
    pages: List[dict]


class APISchema(BaseModel):
    endpoints: List[dict]


class DBSchema(BaseModel):
    tables: List[dict]


class AuthSchema(BaseModel):
    roles: Dict[str, List[str]]