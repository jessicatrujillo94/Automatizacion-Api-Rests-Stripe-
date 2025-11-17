tax_rate_output_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": { "type": "string" },
    "object": { "type": "string", "enum": ["tax_rate"] },
    "active": { "type": "boolean" },
    "country": { "type": ["string", "null"] },
    "created": { "type": "integer" },
    "description": { "type": ["string", "null"] },
    "display_name": { "type": "string" },
    "effective_percentage": { "type": "number" },
    "flat_amount": { "type": ["number", "null"] },
    "inclusive": { "type": "boolean" },
    "jurisdiction": { "type": ["string", "null"] },
    "jurisdiction_level": { "type": ["string", "null"] },
    "livemode": { "type": "boolean" },
    "metadata": { "type": "object" },
    "percentage": { "type": "number" },
    "rate_type": { "type": "string", "enum": ["percentage"] },
    "state": { "type": ["string", "null"] },
    "tax_type": { "type": ["string", "null"] }
  },
  "required": [
    "id",
    "object",
    "active",
    "created",
    "display_name",
    "inclusive",
    "livemode",
    "metadata",
    "percentage",
    "rate_type"
  ]
}
