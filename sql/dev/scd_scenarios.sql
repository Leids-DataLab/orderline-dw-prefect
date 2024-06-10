-- Increment 1
UPDATE oltp.klant
SET [woonplaats] = 'Amsterdam',
    [geboortedatum] = '1999-11-12'
WHERE [klantnummer] = '11996';

-- Increment 2
UPDATE oltp.klant
SET [woonplaats] = 'Leiden'
WHERE [klantnummer] = '11996';

-- Increment 3
-- Geen aanpassing

-- Terug naar origineel
UPDATE oltp.klant
SET [woonplaats] = 'Utrecht',
    [geboortedatum] = '1951-11-12'
WHERE [klantnummer] = '11996';
