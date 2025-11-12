tax_codes_output_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "object": {
            "type": "string"
        },
        "url": {
            "type": "string"
        },
        "has_more": {
            "type": "boolean"
        },
        "data": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "string"
                        },
                        "object": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "name": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "id",
                        "object",
                        "description",
                        "name"
                    ]
                }
            ]
        }
    },
    "required": [
        "object",
        "url",
        "has_more",
        "data"
    ]
}

tax_code_output_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "object": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "name": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "object",
        "description",
        "name"
    ]
}
