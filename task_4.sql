-- Use the alx_book_store database, as expected by the checker
USE alx_book_store;

-- Query the information_schema to get the full description of the 'books' table
SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'books'
ORDER BY
    ORDINAL_POSITION;
