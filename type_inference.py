def infer_column_type(column_name, series):
    """
    Infer the semantic type of a dataset column.
    """
    name = column_name.lower()

    # ID detection
    if "id" in name:
        return "ID"

    # Email detection
    if "email" in name:
        return "EMAIL"

    # Phone detection
    if "phone" in name or "mobile" in name:
        return "PHONE"

    # Date detection
    if "date" in name:
        return "DATE"

    # Numeric columns
    if series.dtype in ["int64", "float64"]:
        return "NUMERIC"

    # Default
    return "TEXT"
