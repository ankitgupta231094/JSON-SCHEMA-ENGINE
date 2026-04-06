def build_schema(fields):
    schema = {"type": "object", "properties": {}}
    for field, ftype in fields.items():
        schema["properties"][field] = {"type": ftype}
    return schema
