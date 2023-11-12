import tabula

# Specify the PDF file path
pdf_file = "path to the pdf file"

# Extract tables from the PDF
tables = tabula.read_pdf(pdf_file, pages="all")

# Filter tables with keywords "consolidated" and "statement" and print them
for i, table in enumerate(tables):
    # Convert the table data to a string for keyword search
    table_text = table.to_string()
    if "consolidated" in table_text.lower() and "statement" in table_text.lower():
        print(f"Table {i + 1}:")
        print(table)
        print("\n" + "=" * 50 + "\n")  # Separation line

# Example: Print the number of filtered tables
filtered_table_count = sum(
    1
    for table in tables
    if "consolidated" in table.to_string().lower() and "statement" in table.to_string().lower()
)
print(f"Found {filtered_table_count} tables with keywords 'consolidated' and 'statement'.")
