USE ROLE ACCOUNTADMIN;

-- Task 1
CREATE ROLE Admin;
CREATE ROLE Developer;
CREATE ROLE PII;

GRANT ROLE ADMIN to ROLE ACCOUNTADMIN;
GRANT ROLE DEVELOPER to ROLE ADMIN;
GRANT ROLE PII to ROLE ACCOUNTADMIN;

show roles;

-- Task 2
CREATE OR REPLACE WAREHOUSE assignment_wh WITH WAREHOUSE_SIZE = 'MEDIUM';

GRANT ALL PRIVILEGES ON WAREHOUSE assignment_wh TO ROLE ADMIN;

GRANT CREATE DATABASE ON ACCOUNT TO ROLE admin;

-- Task 3
USE ROLE ADMIN;

-- Task 4
CREATE DATABASE assignment_db;

-- Task 5
CREATE SCHEMA my_schema;

-- Task 6
CREATE TABLE EMPLOYEE_DATA (
    ID NUMBER,
    FIRST_NAME VARCHAR(255),
    LAST_NAME VARCHAR(255),
    EMAIL VARCHAR(255),
    DEPARTMENT VARCHAR(255),
    MOBILE_NUMBER VARCHAR(255),
    CITY VARCHAR(255),
    etl_ts timestamp default current_timestamp(),
    etl_by varchar default 'snowsight',
    file_name varchar 
);

-- Task 7
CREATE OR REPLACE FILE FORMAT my_json_format TYPE = JSON;

CREATE TABLE variant_table (variant_data variant);

COPY INTO variant_table FROM @%variant_table file_format = my_json_format;

select * from variant_table;

-- Task 8
CREATE OR REPLACE FILE FORMAT my_csv_format TYPE = 'CSV' FIELD_DELIMITER = ',' SKIP_HEADER = 1;

CREATE STAGE internal_stage file_format = my_csv_format;

CREATE STORAGE INTEGRATION s3_integration type = external_stage storage_provider = s3 enabled = true storage_aws_role_arn = 'arn:aws:iam::726476339007:role/anuj' storage_allowed_locations = ('s3://snowflake-anuj/employee.csv');

GRANT ALL ON INTEGRATION s3_integration TO ROLE admin;

DESC INTEGRATION s3_integration;

CREATE OR REPLACE 
STAGE external_stage URL = 's3://snowflake-anuj/employee.csv' 
STORAGE_INTEGRATION = s3_integration 
FILE_FORMAT = my_csv_format;

LIST @internal_stage;
LIST @external_stage;

-- Task 9
CREATE TABLE employee_internal_stage (
    ID NUMBER,
    FIRST_NAME VARCHAR(255),
    LAST_NAME VARCHAR(255),
    EMAIL VARCHAR(255),
    DEPARTMENT VARCHAR(255),
    CONTACT_NO VARCHAR(255),
    CITY VARCHAR(255),
    etl_ts timestamp default current_timestamp(),
    etl_by varchar default 'snowsight',
    file_name varchar
);

CREATE TABLE employee_external_stage (
    ID NUMBER,
    FIRST_NAME VARCHAR(255),
    LAST_NAME VARCHAR(255),
    EMAIL VARCHAR(255),
    DEPARTMENT VARCHAR(255),
    CONTACT_NO VARCHAR(255),
    CITY VARCHAR(255),
    etl_ts timestamp default current_timestamp(),
    etl_by varchar default 'snowsight',
    file_name varchar
);

COPY INTO employee_internal_stage(
    id,
    first_name,
    last_name,
    email,
    department,
    contact_no,
    city,
    file_name
)FROM (
    SELECT emp.$1, emp.$2, emp.$3, emp.$4, emp.$5, emp.$6, emp.$7, METADATA$FILENAME
    FROM @internal_stage/employee.csv.gz (file_format => my_csv_format) emp
    );
    
COPY INTO employee_external_stage(
        id,
        first_name,
        last_name,
        email,
        department,
        contact_no,
        city,
        file_name
    )
FROM
    (
        SELECT emp.$1, emp.$2, emp.$3, emp.$4, emp.$5, emp.$6, emp.$7, METADATA$FILENAME
        FROM @external_stage (file_format => my_csv_format) emp
    );

select * from employee_internal_stage limit 10;
select * from employee_external_stage limit 10;

-- Task 10
CREATE FILE FORMAT my_parquet_format TYPE = parquet;

CREATE STAGE parquet_stage file_format = my_parquet_format;

SELECT * FROM TABLE(
        INFER_SCHEMA(
            LOCATION => '@parquet_stage',
            FILE_FORMAT => 'my_parquet_format'
        )
    );
    
-- Task 11
SELECT * from @parquet_stage/employee.parquet;

-- Task 12
CREATE OR REPLACE MASKING POLICY email_mask AS (VAL string) RETURNS string -> CASE
    WHEN CURRENT_ROLE() = 'PII' THEN VAL
    ELSE '****MASK****'
END;

CREATE OR REPLACE MASKING POLICY contact_Mask AS (VAL string) RETURNS string -> CASE
        WHEN CURRENT_ROLE() = 'PII' THEN VAL
        ELSE '****MASK****'
END;

ALTER TABLE IF EXISTS employee_internal_stage MODIFY EMAIL SET MASKING POLICY email_mask;

ALTER TABLE IF EXISTS employee_external_stage MODIFY EMAIL SET MASKING POLICY email_mask;

ALTER TABLE IF EXISTS employee_internal_stage MODIFY contact_no SET MASKING POLICY contact_mask;

ALTER TABLE IF EXISTS employee_external_stage MODIFY contact_no
SET MASKING POLICY contact_mask;
    
SELECT * FROM employee_internal_stage LIMIT 10;
SELECT * FROM employee_external_stage LIMIT 10;

USE ROLE ACCOUNTADMIN;

GRANT ALL PRIVILEGES ON WAREHOUSE assignment_wh TO ROLE PII;
GRANT USAGE ON DATABASE ASSIGNMENT_DB TO ROLE PII;
GRANT USAGE ON SCHEMA ASSIGNMENT_DB.MY_SCHEMA TO ROLE PII;
GRANT SELECT ON TABLE assignment_db.my_schema.employee_internal_stage TO ROLE PII;

GRANT SELECT ON TABLE assignment_db.my_schema.employee_external_stage TO ROLE PII;

USE ROLE PII;

SELECT * FROM employee_internal_stage LIMIT 10;
SELECT * FROM employee_external_stage LIMIT 10;

USE ROLE ACCOUNTADMIN;

GRANT ALL PRIVILEGES ON WAREHOUSE assignment_wh TO ROLE DEVELOPER;
GRANT USAGE ON DATABASE ASSIGNMENT_DB TO ROLE DEVELOPER;
GRANT USAGE ON SCHEMA ASSIGNMENT_DB.MY_SCHEMA TO ROLE DEVELOPER;
GRANT SELECT ON TABLE assignment_db.my_schema.employee_internal_stage TO ROLE DEVELOPER; 

GRANT SELECT ON TABLE assignment_db.my_schema.employee_external_stage TO ROLE DEVELOPER;

USE ROLE DEVELOPER;

SELECT * FROM employee_internal_stage LIMIT 10;
SELECT * FROM employee_external_stage LIMIT 10;