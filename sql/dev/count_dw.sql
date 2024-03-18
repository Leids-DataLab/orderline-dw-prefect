SELECT (SELECT COUNT(*) FROM staging.klant) AS stagingKlantCount,
		(SELECT COUNT(*) FROM staging.product) AS stagingProductCount,
		(SELECT COUNT(*) FROM staging.productcategorie) AS stagingProductCategorieCount,
		(SELECT COUNT(*) FROM staging.productsubcategorie) AS stagingProductSubcategorieCount,
		(SELECT COUNT(*) FROM staging.bestelling) AS stagingBestellingCount,
		(SELECT COUNT(*) FROM staging.bestellingregel) AS stagingBestellingRegelCount;
