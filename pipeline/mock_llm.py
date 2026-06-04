class MockLLM:

    def generate(self, prompt):

        return {
            "app_type": "CRM",
            "features": [
                "login",
                "contacts",
                "dashboard",
                "payments"
            ],
            "roles": [
                "admin",
                "user"
            ]
        }