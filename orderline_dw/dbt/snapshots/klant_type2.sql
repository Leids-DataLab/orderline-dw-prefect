{% snapshot klant_type2 %}

{{
    config(
        target_schema='snapshots',
        unique_key='klantnummer',
        strategy='check',
        check_cols=['woonplaats']
    )
}}

SELECT
    klantnummer,
    woonplaats
FROM {{ source('orderline_staging', 'klant') }} -- Verwijzing naar de bron- of stagingmodel van Klant

{% endsnapshot %}
