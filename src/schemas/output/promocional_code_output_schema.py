promocional_code_output_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "object": { "type": "string", "enum": ["promotion_code"] },
    "active": { "type": "boolean" },
    "code": { "type": "string" },
    "coupon": {
      "type": "object",
      "properties": {
        "id": { "type": "string" },
        "object": { "type": "string", "enum": ["coupon"] },
        "amount_off": { "type": ["number", "null"] },
        "created": { "type": "integer" },
        "currency": { "type": ["string", "null"] },
        "duration": { "type": "string" },
        "duration_in_months": { "type": ["integer", "null"] },
        "livemode": { "type": "boolean" },
        "max_redemptions": { "type": ["integer", "null"] },
        "metadata": { "type": "object" },
        "name": { "type": ["string", "null"] },
        "percent_off": { "type": ["number", "null"] },
        "redeem_by": { "type": ["integer", "null"] },
        "times_redeemed": { "type": "integer" },
        "valid": { "type": "boolean" }
      },
      "required": [
        "id",
        "object",
        "created",
        "duration",
        "livemode",
        "metadata",
        "times_redeemed",
        "valid"
      ]
    },
    "created": { "type": "integer" },
    "customer": { "type": ["string", "null"] },
    "expires_at": { "type": ["integer", "null"] },
    "livemode": { "type": "boolean" },
    "max_redemptions": { "type": ["integer", "null"] },
    "metadata": { "type": "object" },
    "restrictions": {
      "type": "object",
      "properties": {
        "first_time_transaction": { "type": "boolean" },
        "minimum_amount": { "type": ["integer", "null"] },
        "minimum_amount_currency": { "type": ["string", "null"] }
      },
      "required": ["first_time_transaction"]
    },
    "times_redeemed": { "type": "integer" }
  },
  "required": [
    "id",
    "object",
    "active",
    "code",
    "coupon",
    "created",
    "livemode",
    "metadata",
    "restrictions",
    "times_redeemed"
  ]
}
list_promocional_code_output_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "object": { "type": "string", "enum": ["list"] },
    "data": {
      "type": "array",
      "items": promocional_code_output_schema
    },
    "has_more": { "type": "boolean" },
    "url": { "type": "string" }
  },
  "required": ["object", "data", "has_more", "url"]
}