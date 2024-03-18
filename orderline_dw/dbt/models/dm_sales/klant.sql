SELECT
    NEWID() AS klantId,
    *
FROM {{ ref('klant_t1') }}
