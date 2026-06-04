from schemas.app_schema import ArchitectureSchema


class SystemDesigner:

    def design(self, intent):

        entities = ["User"]

        if "contacts" in intent.features:
            entities.append("Contact")

        pages = ["Dashboard"]

        if "login" in intent.features:
            pages.append("Login")

        if "contacts" in intent.features:
            pages.append("Contacts")

        role_permissions = {
            "admin": [
                "manage_users",
                "view_analytics"
            ],
            "user": [
                "view_contacts"
            ]
        }

        return ArchitectureSchema(
            entities=entities,
            pages=pages,
            role_permissions=role_permissions
        )