SELECT
    NEWID() AS klantId,
    *
FROM {{ ref('klant_scd_type1_type2') }}
