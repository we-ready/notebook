def main(db):
    if len(sys.argv) != 2:
        print(USAGE)
        return 1

    pokemon_name = sys.argv[1]

    # TODO: your code here

    cur = db.cursor()

    qry = f"""
        select * from pokemon_encounter('{pokemon_name}')
    """
    cur.execute(qry)
    rows = cur.fetchall()
    # print(rows)

    print(
        f"{'Game':<18} {'Location':<18} {'Rate':<10} {'Min':>4} {'Max':>4} {'Assertions'}"
    )
    for row in rows:
        # print(row)
        _, game, location, rate, levelMin, levelMax, assertions = row
        print(
            f"{game:<18} {location:<18} {rate:<10} {levelMin:>4} {levelMax:>4} {assertions}"
        )

