SELECT
    bestelling.bestellingnummer as bestellingnummer,
    bestelling.bestelmoment as bestelmoment,
    bestellingregel.aantal as aantal,
    bestellingregel.bedrag as bedrag,
    klant.klantId as klantId,
    product.productId as productId,
    DatumDimensie.datumId as datumId            
FROM {{ source('orderline_staging', 'bestelling') }} as bestelling
LEFT JOIN {{ source('orderline_staging', 'bestellingregel') }} as bestellingregel
    ON bestelling.bestellingnummer = bestellingregel.bestellingnummer
LEFT JOIN {{ ref("klant") }} as klant
    ON bestelling.klantnummer = klant.klantnummer
LEFT JOIN {{ ref('product') }} as product
    ON bestellingregel.productCode = product.code
LEFT JOIN {{ ref('DatumDimensie') }} as DatumDimensie
    ON CAST(bestelling.bestelmoment AS DATE) = DatumDimensie.datum
