coupon_output_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "object": {"type": "string", "enum": ["coupon"]},
        "amount_off": {"type": ["number", "null"]},
        "created": {"type": "integer"},
        "currency": {"type": ["string", "null"]},
        "duration": {"type": "string", "enum": ["once", "repeating", "forever"]},
        "duration_in_months": {"type": ["integer", "null"]},
        "livemode": {"type": "boolean"},
        "max_redemptions": {"type": ["integer", "null"]},
        "metadata": {"type": "object"},
        "name": {"type": ["string", "null"]},
        "percent_off": {"type": ["number", "null"]},
        "redeem_by": {"type": ["integer", "null"]},
        "times_redeemed": {"type": "integer"},
        "valid": {"type": "boolean"},
    },
    "required": [
        "id",
        "object",
        "created",
        "duration",
        "livemode",
        "metadata",
        "times_redeemed",
        "valid",
    ],
}

coupon_list_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "object": {"type": "string"},
        "url": {"type": "string"},
        "has_more": {"type": "boolean"},
        "data": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "object": {"type": "string"},
                        "amount_off": {"type": "null"},
                        "created": {"type": "integer"},
                        "currency": {"type": "null"},
                        "duration": {"type": "string"},
                        "duration_in_months": {"type": "integer"},
                        "livemode": {"type": "boolean"},
                        "max_redemptions": {"type": "null"},
                        "metadata": {"type": "object"},
                        "name": {"type": "null"},
                        "percent_off": {"type": "number"},
                        "redeem_by": {"type": "null"},
                        "times_redeemed": {"type": "integer"},
                        "valid": {"type": "boolean"},
                    },
                    "required": [
                        "id",
                        "object",
                        "amount_off",
                        "created",
                        "currency",
                        "duration",
                        "duration_in_months",
                        "livemode",
                        "max_redemptions",
                        "metadata",
                        "name",
                        "percent_off",
                        "redeem_by",
                        "times_redeemed",
                        "valid",
                    ],
                }
            ],
        },
    },
    "required": ["object", "url", "has_more", "data"],
}

coupon_deleted_output_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "object": {
            "type": "string",
            "enum": ["coupon"]
        },
        "deleted": {
            "type": "boolean",
            "enum": [True]
        }
    },
    "required": ["id", "object", "deleted"]
}
