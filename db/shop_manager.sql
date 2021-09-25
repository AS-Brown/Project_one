DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS suppliers;

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255)
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    buying_cost FLOAT,
    sell_price FLOAT,
    stock_count INT,
    type_of_product VARCHAR(255),
    supplier_id INT REFERENCES suppliers(id)
);