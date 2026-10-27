import pandas as pd
import json
from type_inference import infer_column_type
from pii_detector import detect_pii
from schema_generator import create_column_schema

# -------------------------
# Load dataset
# -------------------------
df = pd.read_csv("data/hr_dataset.csv")

# -------------------------
# Build schema
# -------------------------
schema = {
    "dataset_name": "HR Employee Dataset",
    "rows": len(df),
    "columns": len(df.columns),
    "fields": []
}

for column in df.columns:
    # Infer semantic type
    semantic_type = infer_column_type(
        column,
        df[column]
    )

    # Detect PII
    pii = detect_pii(
        column,
        semantic_type
    )

    # Create field metadata
    field = create_column_schema(
        column,
        semantic_type,
        pii
    )

    schema["fields"].append(field)

# -------------------------
# Save schema
# -------------------------
with open("schema.json", "w") as file:
    json.dump(
        schema,
        file,
        indent=4
    )

print("Schema inference completed.")
print("Created schema.json")