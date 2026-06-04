class Validator:

    def validate(self, schemas):

        errors = []

        ui = schemas["ui"].model_dump()
        api = schemas["api"].model_dump()
        db = schemas["db"].model_dump()
        auth = schemas["auth"].model_dump()

        # ==========================
        # Basic Validation
        # ==========================

        if len(ui["pages"]) == 0:
            errors.append("No UI pages defined")

        if len(api["endpoints"]) == 0:
            errors.append("No API endpoints defined")

        if len(db["tables"]) == 0:
            errors.append("No database tables defined")

        if len(auth["roles"]) == 0:
            errors.append("No auth roles defined")

        # ==========================
        # DB Validation
        # ==========================

        db_table_names = [
            table["name"]
            for table in db["tables"]
        ]

        if "contact" not in db_table_names:
            errors.append("Contact table missing")

        # ==========================
        # Cross-Layer Validation
        # API -> DB
        # ==========================

        for endpoint in api["endpoints"]:

            required_table = endpoint.get("table")

            if required_table:

                if required_table not in db_table_names:

                    errors.append(
                        f"API references missing table: {required_table}"
                    )

        # ==========================
        # Auth Validation
        # ==========================

        required_roles = ["admin", "user"]

        for role in required_roles:

            if role not in auth["roles"]:

                errors.append(
                    f"Missing role: {role}"
                )

        return errors