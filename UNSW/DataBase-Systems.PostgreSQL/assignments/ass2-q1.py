# from helpers import format_q1_row
import helpers

def main(db):
    if len(sys.argv) != 1:
        print(USAGE)
        return 1

    # TODO: your code here

    qry = """
        select * 
        from ass2_q1
    """

    cur = db.cursor()
    cur.execute(qry)
    rows=cur.fetchall()

    helpers.format_q1_row("Region", "Game", "#Pokemon", "#Locations")
    for row in rows:
        region, game, locationCount, pokemonCount = row
        helpers.format_q1_row(region, game, str(pokemonCount), str(locationCount))
