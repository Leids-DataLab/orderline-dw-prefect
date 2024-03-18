--
-- Wijzingen in OLTP
--

-- Bestelling erbij
INSERT INTO oltp.bestelling ([bestellingnummer], [bestelmoment], [klantnummer]) VALUES ('2009231717979', GETDATE(), '11996');
INSERT INTO oltp.bestellingregel ([bestellingnummer], [bestellingRegelnummer], [aantal], [bedrag], [productCode]) VALUES ('2009231717979', 1, 1, 599.00, '0301046');

-- Klant erbij
INSERT INTO oltp.klant ([klantnummer], [initialen], [voornaam], [achternaam], [geboortenaam], [achternaamPartner], [gender], [geboortedatum], [straat], [huisnummer], [huisnummertoevoeging], [postcode], [woonplaats], [provincie], [email], [telefoonnummer], [rating], [latitude], [longitude])
VALUES ('K0001', 'J.D.', 'John', 'Doe', 'Doe', NULL, 'M', '1990-05-15', '123 Main Street', 123, 'A', '12345', 'New York', 'New York', 'johndoe@email.com', '123-456-7890', '5 stars', 40.7128, -74.0060);

-- Update klant 11996
UPDATE oltp.klant
SET [woonplaats] = 'Amsterdam',
    [geboortedatum] = '1999-11-12'
WHERE [klantnummer] = '11996';

--
-- Terug naar origineel OLTP
--

-- Klant verwijderen
DELETE FROM oltp.klant WHERE [klantnummer] = 'K0001';

-- Klantgegevens herstellen
UPDATE oltp.klant
SET [woonplaats] = 'Leiden',
    [geboortedatum] = '1951-11-12'
WHERE [klantnummer] = '11996';

-- Bestelling verwijderen
DELETE FROM oltp.bestellingregel WHERE [bestellingnummer] = '2009231717979';
DELETE FROM oltp.bestelling WHERE [bestellingnummer] = '2009231717979';

