# from helpers import format_q2_row
# from helpers import clean
import helpers

def main(db):
    if len(sys.argv) != 2:
        print(USAGE)
        return 1

    pokemon_name = sys.argv[1]

    # TODO: your code here

    cleanName = helpers.clean(pokemon_name)
    cur = db.cursor()

    qryPokemon = f"""
        select id from pokemon where name='{cleanName}'
    """
    cur.execute(qryPokemon)
    pkRows = cur.fetchall()
    if len(pkRows) == 0:
        print(f"Pokemon \"{cleanName}\" does not exist")
        return

    qryEncounter = f"""
        select occurs_with from encounters where occurs_with={pkRows[0][0]}
    """
    cur.execute(qryEncounter)
    ecRows = cur.fetchall()
    if len(ecRows) == 0:
        print(f"Pokemon \"{cleanName}\" is not encounterable in any game")
        return

    qry = f"""
        select * from pokemon_encounter('{cleanName}')
    """
    cur.execute(qry)
    rows = cur.fetchall()
    # print(rows)

    titleArr = ['Game', 'Location', 'Rarity', 'MinLevel', 'MaxLevel', 'Requirements']
    colWidth = [len(titleArr[0]), len(titleArr[1]), len(titleArr[2]), len(titleArr[3]), len(titleArr[4])]
    for row in rows:
        for i in range(0,5):
            if len(str(row[i])) > colWidth[i]:
                colWidth[i] = len(str(row[i]))
    for i in range(0,5):
        colWidth[i] = colWidth[i] + 1

    helpers.format_q2_row(colWidth, titleArr)
    prevRow = ()
    for row in rows:
        # print(row)
        if (prevRow == row):
            continue
        game, location, Rarity, levelMin, levelMax, requirements = row
        helpers.format_q2_row(colWidth, [game, location, Rarity, str(levelMin), str(levelMax), requirements])
        prevRow = row
