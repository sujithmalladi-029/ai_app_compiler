class RepairEngine:

    def repair(self, schemas, errors):

        db = schemas["db"]

        table_names = [
            table["name"]
            for table in db.tables
        ]

        if "Contact table missing" in errors:

            if "contact" not in table_names:

                db.tables.append(
                    {
                        "name": "contact",
                        "columns": [
                            {
                                "name": "id",
                                "type": "integer"
                            }
                        ]
                    }
                )

        return schemas