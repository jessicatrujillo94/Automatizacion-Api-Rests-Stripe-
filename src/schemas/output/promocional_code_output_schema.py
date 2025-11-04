promocional_code_output_schema = {
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
    "code": {
      "type": "string"
    },
    "promotion": {
      "type": "object",
      "properties": {
        "type": {
          "type": "string"
        },
        "coupon": {
          "type": "string"
        }
      },
      "required": [
        "type",
        "coupon"
      ]
    },
    "created": {
      "type": "integer"
    },
    "customer": {
      "type": "null"
    },
    "expires_at": {
      "type": "null"
    },
    "livemode": {
      "type": "boolean"
    },
    "max_redemptions": {
      "type": "null"
    },
    "metadata": {
      "type": "object"
    },
    "restrictions": {
      "type": "object",
      "properties": {
        "first_time_transaction": {
          "type": "boolean"
        },
        "minimum_amount": {
          "type": "null"
        },
        "minimum_amount_currency": {
          "type": "null"
        }
      },
      "required": [
        "first_time_transaction",
        "minimum_amount",
        "minimum_amount_currency"
      ]
    },
    "times_redeemed": {
      "type": "integer"
    }
  },
  "required": [
    "id",
    "object",
    "active",
    "code",
    "promotion",
    "created",
    "customer",
    "expires_at",
    "livemode",
    "max_redemptions",
    "metadata",
    "restrictions",
    "times_redeemed"
  ]
}