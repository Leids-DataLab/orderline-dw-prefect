{{ config(materialized=var('sales_materialization')) }}

SELECT
    *
FROM {{ ref('sales_t1') }}
{% if is_incremental() %}
    WHERE bestelmoment > (SELECT MAX(bestelmoment) FROM {{ this }})
{% endif %}

