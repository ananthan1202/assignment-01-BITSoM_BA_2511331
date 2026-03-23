## ETL Decisions

### Decision 1 – Date Standardization
Problem: The raw dataset had multiple date formats such as DD/MM/YYYY, DD-MM-YYYY, and YYYY-MM-DD.

Resolution:
All dates were converted into the ISO standard format YYYY-MM-DD before inserting into the data warehouse.

### Decision 2 – Category Cleaning
Problem: Category values appeared in inconsistent formats such as "electronics", "Electronics", and "Grocery".

Resolution:
Categories were standardized to three consistent values:
Electronics, Clothing, and Groceries.

### Decision 3 – Revenue Calculation
Problem: The raw dataset only provided units_sold and unit_price.

Resolution: A revenue column was calculated during transformation using:
revenue = units_sold × unit_price.
