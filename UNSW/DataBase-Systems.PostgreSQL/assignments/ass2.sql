CREATE OR REPLACE VIEW game_location_count AS
  SELECT
    gm.region, gm.name,
    COUNT(lc.id) AS location_count
  FROM games gm
  LEFT JOIN locations lc ON lc.appears_in=gm.id
  GROUP BY gm.region, gm.name
  ORDER BY region, name
;

CREATE OR REPLACE VIEW game_pokemon_count AS
  SELECT
    gm.region, gm.name,
    COUNT(pd.national_id) AS pokemon_count
  FROM games gm
  LEFT JOIN pokedex pd ON pd.game=gm.id
  GROUP BY gm.region, gm.name
  ORDER BY region, name
;



-- local debug

SELECT
  gm.*,
  pd.national_id
  -- gm.region, gm.name,
  -- COUNT(lc.id) AS location_count
FROM games gm
LEFT JOIN pokedex pd ON pd.game=gm.id
-- GROUP BY gm.region, gm.name
ORDER BY region, name, national_id
;


SELECT *
FROM pokedex
;

SELECT
  -- gm.*,
  gm.region, gm.name,
  lc.id AS location_id,
  lc.name AS location_name
FROM games gm
LEFT JOIN locations lc ON lc.appears_in=gm.id
ORDER BY region, name, location_id
;



SELECT id, name
FROM pokemon
;

SELECT *
FROM locations
;
