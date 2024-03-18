SELECT
    NEWID() AS productId,
    *
FROM {{ ref('product_t1') }}
