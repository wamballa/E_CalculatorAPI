import openpyxl

# Load the Excel file
file_path = "D:\Documents\ChristaAPI\Payback_Tool.xlsx"  # Replace with your Excel file path
workbook = openpyxl.load_workbook(file_path, data_only=False)  # Ensure formulas are not evaluated
sheet = workbook.active  # Load the first sheet (adjust if needed)

# Create a CSV to store extracted data
with open("extracted_logic.csv", "w") as file:
    file.write("Cell,Value,Formula\n")  # Header
    for row in sheet.iter_rows():
        for cell in row:
            cell_value = cell.value
            cell_formula = cell.value if isinstance(cell.value, str) and cell.value.startswith('=') else None
            file.write(f"{cell.coordinate},{cell_value},{cell_formula}\n")

print("Extraction complete. Check 'extracted_logic.csv' for the results.")
