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

CREATE OR REPLACE VIEW encounter_assertions AS
  SELECT
    encounter, string_agg(assertion, ', ') AS assertions
  FROM
  (
    SELECT
      er.encounter,
      CASE er.inverted
        WHEN true THEN CONCAT('NOT ', rq.assertion)
        ELSE CONCAT('BE ', rq.assertion)
      END AS assertion
    FROM encounter_requirements er
    LEFT JOIN requirements rq ON rq.id=er.requirement
  )
  GROUP BY encounter
;

CREATE OR REPLACE FUNCTION Pokemon_Encounter(PokemonName TEXT)
  RETURNS TABLE (region TEXT, game TEXT, location TEXT, rate TEXT, level_min INTEGER, level_max INTEGER, assertions TEXT)
  AS $$

    SELECT
      gm.region::TEXT, gm.name::TEXT AS game, 
      lc.name::TEXT AS location,
      -- ec.rarity,
      CASE
        WHEN ec.rarity >= 21 THEN 'Common'
        WHEN ec.rarity >= 6 AND ec.rarity <= 20 THEN 'Uncommon'
        WHEN ec.rarity >= 1 AND ec.rarity <= 5 THEN 'Rare'
        ELSE 'Limited'
      END AS rate,
      -- ec.levels,
      (ec.levels).MIN AS level_min,
      (ec.levels).MAX AS level_max,
      -- pk.name AS pokemon_name,
      -- ec.id
      ea.assertions
    FROM encounters ec
    LEFT JOIN pokemon pk ON pk.id=ec.occurs_with
    LEFT JOIN locations lc ON lc.id=ec.occurs_at
    LEFT JOIN games gm ON gm.id=lc.appears_in
    LEFT JOIN encounter_assertions ea ON ea.encounter=ec.id
    WHERE pk.name = PokemonName
    ORDER BY region, game, location, rarity, level_min, level_max
  
  $$ LANGUAGE SQL
;




-- local debug



SELECT *
FROM requirements
;



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
