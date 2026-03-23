## Anomaly Analysis

### Insert Anomaly
If we want to add a new product (e.g., "Keyboard") but no order exists, we cannot insert it because order_id is required in the table.

### Update Anomaly
Customer "Priya Sharma" appears in multiple rows. If her city changes from "Delhi" to "Mumbai", we must update multiple rows. Missing one row causes inconsistency.

### Delete Anomaly
If we delete the last order of customer "Rohan Mehta", we also lose his customer details like email and city.

## Normalisation Justification 
The argument that keeping all data in a single table is simpler is understandable from a short-term perspective, but it creates serious long-term problems. In the given "orders_flat.csv", customer, product, and sales representative details are stored together, leading to redundancy and inconsistency.

For example, the same customer (e.g., Priya Sharma from Delhi) appears in multiple rows for different orders. If her email needs to be updated, it must be changed in every row. Missing even one row results in inconsistent data, demonstrating an update anomaly. Similarly, product details such as “Laptop” or “Pen Set” are repeated across many records. If a product price changes, updating it everywhere becomes error-prone.

There are also insert and delete issues. For instance, a new product cannot be added unless there is an associated order (insert anomaly). Likewise, deleting the only order of a product may remove all information about that product (delete anomaly).

By normalizing the data into separate tables like Customers, Products, Orders, and Sales Representatives (3NF), each entity is stored only once. Relationships are maintained using keys, ensuring consistency and reducing redundancy.

While a single table may seem simpler initially, it does not scale well and increases the risk of data errors. Normalization is not over-engineering; it is a necessary practice to ensure data integrity, maintainability, and efficient database operations.