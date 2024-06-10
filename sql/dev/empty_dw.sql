TRUNCATE TABLE staging.klant;
TRUNCATE TABLE staging.productcategorie;
TRUNCATE TABLE staging.productsubcategorie;
TRUNCATE TABLE staging.product;
TRUNCATE TABLE staging.bestelling;
TRUNCATE TABLE staging.bestellingregel;

TRUNCATE TABLE dbt_dm.klant
TRUNCATE TABLE dbt_dm.product
TRUNCATE TABLE dbt_dm.sales
TRUNCATE TABLE snapshots.klant_type2

DROP TABLE staging.klant;
DROP TABLE staging.productcategorie;
DROP TABLE staging.productsubcategorie;
DROP TABLE staging.product;
DROP TABLE staging.bestelling;
DROP TABLE staging.bestellingregel;

DROP TABLE dbt_dm.klant
DROP TABLE dbt_dm.product
DROP TABLE dbt_dm.sales
DROP TABLE snapshots.klant_type2

DROP VIEW dbt.klant_scd_type1_type2
DROP VIEW dbt.klant_type1
DROP VIEW dbt.product_t1
DROP VIEW dbt.sales_t1
