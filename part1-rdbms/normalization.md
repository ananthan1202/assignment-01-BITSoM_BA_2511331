## Anomaly Analysis

### Insert Anomaly
If we want to add a new product (e.g., "Keyboard") but no order exists, we cannot insert it because order_id is required in the table.

### Update Anomaly
Customer "Priya Sharma" appears in multiple rows. If her city changes from "Delhi" to "Mumbai", we must update multiple rows. Missing one row causes inconsistency.

### Delete Anomaly
If we delete the last order of customer "Rohan Mehta", we also lose his customer details like email and city.

## Normalisation Justification 
The dataset contains repeated customer, product, and sales representative information in multiple rows. This leads to redundancy and inconsistencies. By normalising into seperate tables (customers, products, orders etc) we reduce duplication and ensure data integrity.Updates become easier and safer, and storage is optimized.