import re

def clean(s: str) -> str:
    """
    Clean user input
    remove leading and trailing whitespace
    convert to title case (first letter of each word is uppercase, the rest are lowercase)
    squish multiple whitespace characters into a single space
    """
    return re.sub(r'\s+', ' ', s.strip().title())


def format_q1_row(region: str, game: str, pokemonCount: str, locationCount: str) -> None:
    """ Print one row with specific format.

    Parameters
    ----------
    region
    game
    pokemonCount
    locationCount

    Returns
    -------
    None

    """

    print(f"{region:<6} {game:<17} {pokemonCount:<8} {locationCount:<10}")


def format_q2_row(game: str, location: str, Rarity: str, minLevel: str, maxLevel: str, requirements: str) -> None:
    """ Print one row with specific format.

    Parameters
    ----------
    game
    location
    Rarity
    minLevel
    maxLevel
    requirements

    Returns
    -------
    None

    """

    print(f"{game:<18} {location:<27} {Rarity:<9} {minLevel:<9} {maxLevel:<9} {requirements}")



def print_requirements(text):
    arr = text.split('==AND==')
    if len(arr) == 1:
        print(arr[0])
        return
    for t in arr:
        if t == '==AND==':
            print('AND')
        else:
            print_requirements(f"    {t}")

def print_evolution_requirements(pre, post, text):
    print(f"'{pre}' can evolve into '{post}' when the following requirements are satisfied:")
    print_requirements(text)
    
def track_evolution(pokemon, field, cur):
    qry = f"""
      select *
      from evolution_all_in_one_requirements
      where {field}='{pokemon}';
    """
    cur.execute(qry)
    rows = cur.fetchall()
    if len(rows) == 0:
        print(f"'{pokemon}' does not have any {field}-evolutions")
        return

    for row in rows:
        pre, post, requirements = row
        print_evolution_requirements(pre, post, requirements)
        if field == 'post':
            track_evolution(pre, field, cur)
        elif field == 'pre':
            track_evolution(post, field, cur)
    
    print("")
