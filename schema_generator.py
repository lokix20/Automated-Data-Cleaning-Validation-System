def create_column_schema(column_name, semantic_type, pii):
    """
    Create metadata describing one column.
    """
    field = {
        "name": column_name,
        "semantic_type": semantic_type,
        "pii": pii
    }

    # Expected rules
    if semantic_type == "EMAIL":
        field["expected_format"] = "valid email address"
    elif semantic_type == "PHONE":
        field["expected_format"] = "Indian phone number"
    elif semantic_type == "DATE":
        field["expected_format"] = "valid date"
    elif column_name == "performance_score":
        field["expected_range"] = {
            "min": 1,
            "max": 5
        }
    elif column_name in ["salary", "absenteeism_days"]:
        field["expected_range"] = {
            "min": 0
        }

    return field
