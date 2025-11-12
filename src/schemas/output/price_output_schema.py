price_output_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {"type": "string"},
    "object": {"type": "string"},
    "active": {"type": "boolean"},
    "billing_scheme": {"type": "string"},
    "created": {"type": "integer"},
    "currency": {"type": "string"},
    "livemode": {"type": "boolean"},
    "lookup_key": {"type": ["string", "null"]},
    "metadata": {"type": "object"},
    "nickname": {"type": ["string", "null"]},
    "product": {"type": "string"},
    "recurring": {"type": ["object", "null"]},
    "tax_behavior": {"type": ["string", "null"]},
    "tiers_mode": {"type": ["string", "null"]},
    "transform_quantity": {"type": ["object", "null"]},
    "type": {"type": "string"},
    "unit_amount": {"type": ["integer", "null"]},
    "unit_amount_decimal": {"type": ["string", "null"]}
  },
  "required": [
    "id",
    "object",
    "active",
    "billing_scheme",
    "created",
    "currency",
    "livemode",
    "metadata",
    "product",
    "type",
    "unit_amount",
    "unit_amount_decimal"
  ]
}
price_list_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "object": {"type": "string"},
    "url": {"type": "string"},
    "has_more": {"type": "boolean"},
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "object": {"type": "string"},
          "active": {"type": "boolean"},
          "billing_scheme": {"type": "string"},
          "created": {"type": "integer"},
          "currency": {"type": "string"},
          "custom_unit_amount": {"type": ["number", "null"]},
          "livemode": {"type": "boolean"},
          "lookup_key": {"type": ["string", "null"]},
          "metadata": {"type": "object"},
          "nickname": {"type": ["string", "null"]},
          "product": {"type": "string"},
          "recurring": {
            "type": ["object", "null"],
            "properties": {
              "interval": {"type": "string"},
              "interval_count": {"type": "integer"},
              "trial_period_days": {"type": ["integer", "null"]},
              "usage_type": {"type": "string"}
            },
            "required": ["interval", "interval_count", "trial_period_days", "usage_type"]
          },
          "tax_behavior": {"type": ["string", "null"]},
          "tiers_mode": {"type": ["string", "null"]},
          "transform_quantity": {"type": ["object", "null"]},
          "type": {"type": "string"},
          "unit_amount": {"type": ["integer", "null"]},
          "unit_amount_decimal": {"type": ["string", "null"]}
        },
        "required": [
          "id", "object", "active", "billing_scheme", "created", "currency",
          "custom_unit_amount", "livemode", "lookup_key", "metadata", "nickname",
          "product", "recurring", "tax_behavior", "tiers_mode", "transform_quantity",
          "type", "unit_amount", "unit_amount_decimal"
        ]
      }
    }
  },
  "required": ["object", "url", "has_more", "data"]
}
