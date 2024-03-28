SELECT
    klantnummer,
    geboortedatum
FROM {{ source('orderline_staging', 'klant') }};
