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
