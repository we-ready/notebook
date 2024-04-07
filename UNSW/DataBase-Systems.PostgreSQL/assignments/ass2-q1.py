def main(db):
    if len(sys.argv) != 1:
        print(USAGE)
        return 1

    # TODO: your code here

    qryLocation = """
        select * 
        from game_location_count
    """
    qryPokemon = """
        select * 
        from game_pokemon_count
    """

    cur = db.cursor()
    dict = {}

    cur.execute(qryLocation)
    locationRows = cur.fetchall()
    cur.execute(qryPokemon)
    pokemonRows = cur.fetchall()

    # print(locationRows)
    # print(pokemonRows)

    for row in locationRows:
        # print(row)
        region, game, locationCount = row
        if region not in dict:
          dict[region] = {}
        dict[region][game] = [locationCount]

    for row in pokemonRows:
        # print(row)
        region, game, pokemonCount = row
        # print(dict[region][game])
        if region not in dict:
          dict[region] = {}
        if game not in dict[region]:
          dict[region][game] = [0, pokemonCount]
        else:
          dict[region][game] = [dict[region][game][0], pokemonCount]

    # print(dict)
    
    headRegion="Region"
    headGame="Game"
    headPokemon="#Pokemon"
    headLocation="#Locations"
    print(f"{headRegion:<6} {headGame:<17} {headPokemon:<8} {headLocation:<10}")

    for region in dict:
      for game in dict[region]:
        print(f"{region:<6} {game:<17} {dict[region][game][0]:<8} {dict[region][game][1]:<10}")
