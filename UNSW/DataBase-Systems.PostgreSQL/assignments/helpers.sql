CREATE OR REPLACE VIEW ass2_q1 AS
  SELECT
    gm.region, gm.name,
    lc.count AS locations_count,
    pc.count AS pokemon_count
  FROM games gm
  LEFT JOIN
  (
    SELECT appears_in AS game, count(name)
    FROM locations
    GROUP BY appears_in
    ORDER BY game
  ) lc ON lc.game=gm.id
  LEFT JOIN
  (
    SELECT game, count(national_id)
    FROM pokedex
    GROUP BY game
    ORDER BY game
  ) pc ON pc.game=gm.id
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
        ELSE rq.assertion
      END AS assertion
    FROM encounter_requirements er
    LEFT JOIN requirements rq ON rq.id=er.requirement
  )
  GROUP BY encounter
;

CREATE OR REPLACE FUNCTION Pokemon_Encounter(PokemonName TEXT)
  RETURNS TABLE (game TEXT, location TEXT, rarity TEXT, level_min INTEGER, level_max INTEGER, requirements TEXT)
  AS $$

    SELECT
      -- gm.region,
      gm.name AS game, 
      lc.name AS location,
      -- ec.rarity,
      CASE
        WHEN ec.rarity >= 21 THEN 'Common'
        WHEN ec.rarity >= 6 AND ec.rarity <= 20 THEN 'Uncommon'
        WHEN ec.rarity >= 1 AND ec.rarity <= 5 THEN 'Rare'
        ELSE 'Limited'
      END AS rarity,
      -- ec.levels,
      (ec.levels).MIN AS level_min,
      (ec.levels).MAX AS level_max,
      -- pk.name AS pokemon_name,
      -- ec.id
      ea.assertions AS requirements
    FROM encounters ec
    LEFT JOIN pokemon pk ON pk.id=ec.occurs_with
    LEFT JOIN locations lc ON lc.id=ec.occurs_at
    LEFT JOIN games gm ON gm.id=lc.appears_in
    LEFT JOIN encounter_assertions ea ON ea.encounter=ec.id
    WHERE pk.name = PokemonName
    ORDER BY gm.region, game, location, rarity, level_min, level_max

  $$ LANGUAGE SQL
;


CREATE OR REPLACE VIEW evolution_all_in_one_requirements AS
  SELECT
    -- evx.*,
    pk0.name AS pre,
    pk1.name AS post,
    evx.requirements
  FROM
  (
    SELECT
      pre_evolution, post_evolution,
      string_agg(requirements, ' ==OR== ') as requirements
    FROM
    (
      SELECT
        evl.*,
        evr.requirements
      FROM evolutions evl
      LEFT JOIN
      (
        SELECT
          evolution,
          string_agg(assertion, ' ==AND== ') as requirements
        FROM
        (
          SELECT
            er.evolution,
            CASE er.inverted
              WHEN true THEN CONCAT('NOT ', rq.assertion)
              ELSE rq.assertion
            END AS assertion
          FROM evolution_requirements er
          LEFT JOIN requirements rq ON rq.id = er.requirement
          ORDER BY er.evolution, er.inverted, er.requirement
        )
        GROUP BY evolution
        -- ORDER BY evolution
      ) evr ON evr.evolution=evl.id
    )
    GROUP BY pre_evolution, post_evolution
    -- ORDER BY pre_evolution, post_evolution
  ) evx
  LEFT JOIN pokemon pk0 ON pk0.id = evx.pre_evolution
  LEFT JOIN pokemon pk1 ON pk1.id = evx.post_evolution
  ORDER BY evx.pre_evolution, evx.post_evolution
;
