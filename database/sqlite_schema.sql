CREATE TABLE IF NOT EXISTS stores (
    store_id TEXT PRIMARY KEY,
    store_name TEXT,
    region TEXT,
    city TEXT,
    store_type TEXT
);

CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    sub_category TEXT,
    base_price REAL
);

CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    customer_segment TEXT,
    signup_date TEXT,
    preferred_channel TEXT,
    city TEXT
);

CREATE TABLE IF NOT EXISTS sales_transactions (
    order_id TEXT,
    order_date TEXT,
    store_id TEXT,
    product_id TEXT,
    customer_id TEXT,
    sales_channel TEXT,
    units_sold INTEGER,
    unit_price REAL,
    discount_pct REAL,
    payment_status TEXT,
    delivery_status TEXT
);

CREATE TABLE IF NOT EXISTS returns (
    return_id TEXT PRIMARY KEY,
    order_id TEXT,
    return_date TEXT,
    return_reason TEXT
);
