select id, name, first_type, second_type from pokemon;
select attacking, defending, multiplier from type_effectiveness;

-------- moves

select count(*) from learnable_moves;
count = 1262002

learnt_by learnt_in learnt_when learns
learnt_by - pokemon(id)
learnt_in - games(id)
learnt_when - requirements(id)
learns - moves(id)

select count(*) from moves;
count = 915

id  name  effect  of_type category  power accuracy  base_power_points
id - integer PRIMARY KEY
name - text UNIQUE
effect - text
of_type - types(id)
category - move_categories
power - statistic (byte, >=1, <=255)
accuracy - probability (percentage, >=0, <=100)
base_power_points - integer

\dT+ move_categories
{Physical,Special,Status}

select count(*) from types;
count = 18

id  name
id - integer PRIMARY KEY
name - text UNIQUE

select count(*) from type_effectiveness ;
count = 120

attacking defending multiplier
UNIQUE(attacking, defending)
attacking - type(id)
defending - type(id)
multiplier - percentage



-------- evolutions & evolution_requirements & requirements

select count(*) from evolutions;
count = 535

id  pre_evolution   post_evolution
id - integer PRIMARY KEY
pre_evolution - pokemon(id)
post_evolution - pokemon(id)


select count(*) from evolution_requirements;
count = 650

evolution requirement inverted
evolution - evolution(id)
requirement - requirements(id)
inverted - boolean
PRIMARY KEY (evolution, requirement)


select count(*) from requirements;
count = 830

id  assertion
id - integer PRIMARY KEY
assertion - text UNIQUE


------------- games

select count(*) from games;
count = 39

select * from games;
id  name  region
id - integer PRIMARY KEY
name - UNIQUE
region - regions: type enum ('Kanto', 'Johto', ...)
'Kanto': 关都地区

\dT
SELECT enum_range(null::regions);

--------------- locations
select count(*) from locations;
count = 3542

select * from locations;
id  name  appears_in
id - integer PRIMARY KEY
name - text ('Route XX', 'Berry Forest', 'Bond Bridge', ...)
appears_in - games(id)
UNIQUE(name, appears_in)

--------------- pokedex
select count(*) from pokedex;
count = 11819

select * from pokedex;
national_id  game  regional_id
national_id - pokemon(id)
game - games(id)
regional_id - integer
UNIQUE(national_id, game)
