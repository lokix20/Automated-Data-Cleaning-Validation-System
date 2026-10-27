def detect_pii(column_name, semantic_type):
    """
    Determine whether a column contains personally identifiable information.
    """
    name = column_name.lower()

    if semantic_type == "EMAIL":
        return True

    if semantic_type == "PHONE":
        return True

    if name in ["name", "full_name", "employee_name"]:
        return True

    return False
