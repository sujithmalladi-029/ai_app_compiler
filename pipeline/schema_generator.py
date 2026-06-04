from schemas.app_schema import (
    UISchema,
    APISchema,
    DBSchema,
    AuthSchema
)


class SchemaGenerator:

    def generate(self, architecture):

        ui_schema = UISchema(
            pages=[
                {
                    "name": page,
                    "components": []
                }
                for page in architecture.pages
            ]
        )

        api_schema = APISchema(
            endpoints=[
                {
                    "path": "/contacts",
                    "method": "GET",
                    "table": "contact"
                },
                {
                    "path": "/contacts",
                    "method": "POST",
                    "table": "contact"
                }
            ]
        )

        db_schema = DBSchema(
            tables=[
                {
                    "name": entity.lower(),
                    "columns": [
                        {
                            "name": "id",
                            "type": "integer"
                        }
                    ]
                }
                for entity in architecture.entities
            ]
        )

        auth_schema = AuthSchema(
            roles=architecture.role_permissions
        )

        return {
            "ui": ui_schema,
            "api": api_schema,
            "db": db_schema,
            "auth": auth_schema
        }