product_output_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "object": {
      "type": "string"
    },
    "active": {
      "type": "boolean"
    },
    "created": {
      "type": "integer"
    },
    "default_price": {
      "type": ["string","null"]
    },
    "description": {
      "type": ["string","null"]
    },
    "images": {
      "type": "array",
      "items": {}
    },
    "marketing_features": {
      "type": "array",
      "items": {}
    },
    "livemode": {
      "type": "boolean"
    },
    "metadata": {
      "type": "object"
    },
    "name": {
      "type": "string"
    },
    "package_dimensions": {
      "type": ["string","null"]
    },
    "shippable": {
      "type": ["string","null"]
    },
    "statement_descriptor": {
      "type": ["string","null"]
    },
    "tax_code": {
      "type": ["string","null"]
    },
    "unit_label": {
      "type": ["string","null"]
    },
    "updated": {
      "type": "integer"
    },
    "url": {
      "type": ["string","null"]
    }
  },
  "required": [
    "id",
    "object",
    "active",
    "created",
    "default_price",
    "description",
    "images",
    "marketing_features",
    "livemode",
    "metadata",
    "name",
    "package_dimensions",
    "shippable",
    "statement_descriptor",
    "tax_code",
    "unit_label",
    "updated",
    "url"
  ]
}
product_deleted_output_schema={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "object": {
      "type": "string"
    },
    "deleted": {
      "type": "boolean"
    }
  },
  "required": [
    "id",
    "object",
    "deleted"
  ]
}
product_list_output_schema = {
    "type": "object",
    "properties": {
        "object": {"type": "string"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "object": {"type": "string"},
                    "active": {"type": "boolean"},
                    "attributes": {"type": "array", "items": {}},
                    "created": {"type": "integer"},
                    "default_price": {"type": ["string", "null"]},
                    "description": {"type": ["string", "null"]},
                    "images": {"type": "array", "items": {"type": "string"}},
                    "livemode": {"type": "boolean"},
                    "marketing_features": {"type": "array", "items": {}},
                    "metadata": {"type": "object"},
                    "name": {"type": "string"},
                    "package_dimensions": {"type": ["object", "null"]},
                    "shippable": {"type": ["boolean", "null"]},
                    "statement_descriptor": {"type": ["string", "null"]},
                    "tax_code": {"type": ["string", "null"]},
                    "type": {"type": "string"},
                    "unit_label": {"type": ["string", "null"]},
                    "updated": {"type": "integer"},
                    "url": {"type": ["string", "null"]},
                },
                "required": [
                    "id", "object", "active", "attributes", "created", "default_price",
                    "description", "images", "livemode", "marketing_features", "metadata",
                    "name", "package_dimensions", "shippable", "statement_descriptor",
                    "tax_code", "type", "unit_label", "updated", "url"
                ]
            }
        },
        "has_more": {"type": "boolean"},
        "url": {"type": "string"}
    },
    "required": ["object", "data", "has_more", "url"]
}
