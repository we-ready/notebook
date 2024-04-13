import sys
import psycopg2
import math
import helpers


### Constants
USAGE = f"Usage: {sys.argv[0]} <Game> <Attacking Pokemon> <Defending Pokemon>"


def main(db):
    ### Command-line args
    if len(sys.argv) != 4:
        print(USAGE)
        return 1
    game_name = sys.argv[1]
    attacking_pokemon_name = sys.argv[2]
    defending_pokemon_name = sys.argv[3]

    # TODO: your code here

    cleanNameA = helpers.clean(attacking_pokemon_name)
    cleanNameD = helpers.clean(defending_pokemon_name)
    cleanNameG = helpers.clean(game_name)
    cur = db.cursor()

    qryGame = f"""
        select id from games where name='{cleanNameG}'
    """
    cur.execute(qryGame)
    gmRows = cur.fetchall()
    if len(gmRows) == 0:
        print(f"Game \"{cleanNameG}\" does not exist")
        return

    qryPokemonA = f"""
        select id, first_type, second_type from pokemon where name='{cleanNameA}'
    """
    cur.execute(qryPokemonA)
    pkRowsA = cur.fetchall()
    if len(pkRowsA) == 0:
        print(f"Pokemon \"{cleanNameA}\" does not exist")
        return

    qryPokemonD = f"""
        select id, first_type, second_type from pokemon where name='{cleanNameD}'
    """
    cur.execute(qryPokemonD)
    pkRowsD = cur.fetchall()
    if len(pkRowsD) == 0:
        print(f"Pokemon \"{cleanNameD}\" does not exist")
        return

    qryGamePokemonA = f"""
        select game, pokemon from game_pokemon where game='{cleanNameG}' and pokemon='{cleanNameA}'
    """
    cur.execute(qryGamePokemonA)
    gpRowsA = cur.fetchall()
    if len(gpRowsA) == 0:
        print(f"Pokemon \"{cleanNameA}\" is not in \"{cleanNameG}\"")
        return

    qryGamePokemonD = f"""
        select game, pokemon from game_pokemon where game='{cleanNameG}' and pokemon='{cleanNameD}'
    """
    cur.execute(qryGamePokemonD)
    gpRowsD = cur.fetchall()
    if len(gpRowsD) == 0:
        print(f"Pokemon \"{cleanNameD}\" is not in \"{cleanNameG}\"")
        return

    qryTypeEffectiveness = f"""
        select attacking, defending, multiplier from type_effectiveness
    """
    cur.execute(qryTypeEffectiveness)
    typeEffectRows = cur.fetchall()

    dict = {}
    for row in typeEffectRows:
        attacking, defending, multiplier = row
        if attacking not in dict:
            dict[attacking] = {}
        dict[attacking][defending] = multiplier
    
    qryMoves = f"""
        select name, type, power, requirements from Move_Power('{cleanNameA}', '{cleanNameG}')
    """
    cur.execute(qryMoves)
    moveRows = cur.fetchall()
    if len(moveRows) == 0:
        print(f"No moves found for \"{cleanNameA}\" against \"{cleanNameD}\" in \"{cleanNameG}\"")
        return

    newMoveRows = []
    for row in moveRows:
        name, type, power, requirements = row
        
        newPower = power
        if type == pkRowsA[0][1] or type == pkRowsA[0][2]:
            newPower = math.floor(1.5 * newPower)
        if type in dict:
            if pkRowsD[0][1] in dict[type]:
                newPower = math.floor(newPower * dict[type][pkRowsD[0][1]] / 100)
            if pkRowsD[0][2] in dict[type]:
                newPower = math.floor(newPower * dict[type][pkRowsD[0][2]] / 100)

        newMoveRows.append((name, newPower, requirements))
    
    sortedRows = sorted(newMoveRows, key=lambda x: x[1], reverse=True)
    print(f"If \"{cleanNameA}\" attacks \"{cleanNameD}\" in \"{cleanNameG}\" it's available moves are:")
    for row in sortedRows:
        name, power, requirements = row
        print(f"\t{name}")
        print(f"\t\twould have a relative power of {power}")
        print(f"\t\tand can be learnt from {requirements}")

    print("")
