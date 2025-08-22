class Responses:
    def __init__(self):
        self.responses = dict()
        self.responses[400] = {
            "description": "Bad Request",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Bad Request",
                        "message": "string"
                    },
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string"},
                            "message": {"type": "string"}
                        }
                    }
                }
            }
        }
        self.responses[401] = {
            "description": "Unauthorized",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Unauthorized",
                        "message": "string"
                    },
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string"},
                            "message": {"type": "string"}
                        }
                    }
                }
            }
        }
        self.responses[422] = {
            "description": "Unprocessable Entity",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Validation failed",
                        "message": "string"
                    },
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string"},
                            "message": {"type": "string"}
                        }
                    }
                }
            }
        }
        self.responses[500] = {
            "description": "Internal Server Error",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Internal Server Error",
                        "message": "string"
                    },
                    "schema": {
                        "type": "object",
                        "properties": {
                            "error": {"type": "string"},
                            "message": {"type": "string"}
                        }
                    }
                }
            }
        }

    @staticmethod
    def get_responses():
        return Responses().responses
