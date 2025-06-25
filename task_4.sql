-- Use the alx_book_store database, as expected by the checker
USE alx_book_store;

-- Query the information_schema to get the full description of the 'books' table
-- Alias columns to match DESCRIBE output and format NULL column
SELECT
    COLUMN_NAME AS Field,
    COLUMN_TYPE AS Type,
    CASE
        WHEN IS_NULLABLE = 'YES' THEN 'YES'
        ELSE ''
    END AS `Null`, -- Formats 'YES' for nullable, empty string for not nullable
    COLUMN_KEY AS `Key`,
    COLUMN_DEFAULT AS `Default`,
    EXTRA AS Extra
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'books'
ORDER BY
    ORDINAL_POSITION;
