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
