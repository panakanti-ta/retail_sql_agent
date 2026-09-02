# Database Schema Reference (SQLite)

### stores
- `store_id`: TEXT (Primary Key)
- `store_name`: TEXT
- `region`: TEXT
- `city`: TEXT
- `store_type`: TEXT

### products
- `product_id`: TEXT (Primary Key)
- `product_name`: TEXT
- `category`: TEXT
- `sub_category`: TEXT
- `base_price`: REAL

### customers
- `customer_id`: TEXT (Primary Key)
- `customer_segment`: TEXT
- `signup_date`: TEXT
- `preferred_channel`: TEXT
- `city`: TEXT

### sales_transactions
- `order_id`: TEXT
- `order_date`: TEXT
- `store_id`: TEXT
- `product_id`: TEXT
- `customer_id`: TEXT
- `sales_channel`: TEXT
- `units_sold`: INTEGER
- `unit_price`: REAL
- `discount_pct`: REAL
- `payment_status`: TEXT
- `delivery_status`: TEXT

### returns
- `return_id`: TEXT (Primary Key)
- `order_id`: TEXT
- `return_date`: TEXT
- `return_reason`: TEXT
