class RuntimeSimulator:

    def run(self, schemas):

        errors = []

        ui = schemas["ui"].model_dump()
        api = schemas["api"].model_dump()
        db = schemas["db"].model_dump()
        auth = schemas["auth"].model_dump()

        if len(ui["pages"]) == 0:
            errors.append("Runtime Error: No pages")

        if len(api["endpoints"]) == 0:
            errors.append("Runtime Error: No APIs")

        if len(db["tables"]) == 0:
            errors.append("Runtime Error: No DB tables")

        if len(auth["roles"]) == 0:
            errors.append("Runtime Error: No roles")

        if len(errors) == 0:
            return {
                "status": "PASS",
                "errors": []
            }

        return {
            "status": "FAIL",
            "errors": errors
        }