import pandas as pd

# Load extracted text
text_file = "extracted_text.txt"

with open(text_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Process text into a structured format
structured_data = [line.strip().split("\t") for line in lines if line.strip()]

# Convert to DataFrame
df = pd.DataFrame(structured_data)

# Save as Excel file
excel_file = "research_tracker.xlsx"
df.to_excel(excel_file, index=False, header=False)

print(f"Excel file saved as {excel_file}")
