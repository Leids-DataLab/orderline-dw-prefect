SELECT
    product.code as code,
    product.naam as naam,
    productsubcategorie.naam as productsubcategorieNaam,
    productcategorie.naam as productcategorieNaam
FROM {{ source('orderline_staging', 'product') }} as product
LEFT JOIN {{ source('orderline_staging', 'productsubcategorie') }} as productsubcategorie
    ON product.productsubcategorieCode = productsubcategorie.code
LEFT JOIN {{ source('orderline_staging', 'productcategorie') }} as productcategorie
    ON productsubcategorie.productcategorieCode = productcategorie.code
