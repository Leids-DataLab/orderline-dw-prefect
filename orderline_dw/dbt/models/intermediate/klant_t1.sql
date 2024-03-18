SELECT
    klantnummer,
    geboortedatum,
    woonplaats
FROM {{ source('orderline_staging', 'klant') }};
