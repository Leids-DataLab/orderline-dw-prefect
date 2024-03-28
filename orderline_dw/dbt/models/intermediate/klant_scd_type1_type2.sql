SELECT
    klant_type2.klantnummer,
    klant_type2.woonplaats,
    klant_type1.geboortedatum,
    klant_type2.dbt_valid_from AS geldigVanaf,
    klant_type2.dbt_valid_to AS geldigTot,
    CAST(
        CASE
            WHEN klant_type2.dbt_valid_to IS NULL THEN 1
            ELSE 0
        END
        AS bit
    ) AS isGeldig
FROM {{ ref('klant_type2') }} AS klant_type2
LEFT JOIN {{ ref('klant_type1') }} AS klant_type1
    ON klant_type2.klantnummer = klant_type1.klantnummer
