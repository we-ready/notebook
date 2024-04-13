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


def format_q2_row(colWidth, textArr) -> None:
    """ Print one row with specific format.

    Parameters
    ----------
    colWidth
    textArr

    Returns
    -------
    None

    """

    print(f"{textArr[0]:<{colWidth[0]}} {textArr[1]:<{colWidth[1]}} {textArr[2]:<{colWidth[2]}} {textArr[3]:<{colWidth[3]}} {textArr[4]:<{colWidth[4]}} {textArr[5]}")



def parse_item(item, keyword):
    arr = item.split(f" =={keyword}== ")
    if len(arr) == 1:
        return item
    else:
        return arr


def parse_tree_node(node, keyword):
    newItems = []
    # print('parse tree node: ', node, keyword)
    for item in node['items']:
        newItem = parse_item(item, keyword)
        if newItem != item:
            newItems.append({
                "type": keyword,
                "level": node['level'] + 1,
                "items": newItem
            })
        else:
            newItems.append(item)
    node['items'] = newItems


def parse_tree(treeRoot):
    parse_tree_node(treeRoot, 'OR')
    if isinstance(treeRoot['items'][0], str):
        parse_tree_node(treeRoot, 'AND')
        return

    for node in treeRoot['items']:
        if type(node) != 'str':
            parse_tree_node(node, 'AND')


def print_tree_node(node):
    indentation = ''.join(['\t'] * node['level'])
    indentation_1 = ''.join(['\t'] * (node['level'] - 1))

    for index, item in enumerate(node['items']):
        # print("item:", item, type(item))
        if isinstance(item, str):
            print(f"{indentation}{item}")
        else:
            print_tree_node(item)

        if index < (len(node['items']) - 1) and node['type'] is not None:
            print(f"{indentation_1}{node['type']}")

def print_requirements(text):
    treeRoot = {
        "type": None,
        "level": 1,
        "items": [text]
    }
    parse_tree(treeRoot)
    print_tree_node(treeRoot)

OPSITE_DIRECTION = {
    "pre": "post",
    "post": "pre",
}
def track_evolution(pokemon, field, cur):
    if field != 'pre' and field != 'post':
        print('field error')
        return
    
    qry = f"""
      select *
      from evolution_all_in_one_requirements
      where {field}='{pokemon}';
    """
    cur.execute(qry)
    rows = cur.fetchall()
    if len(rows) == 0:
        print(f"\n'{pokemon}' doesn't have any {OPSITE_DIRECTION[field]}-evolutions.")
        return

    for row in rows:
        pre, post, requirements = row
        if field == 'pre':
            print(f"\n'{pre}' can evolve into '{post}' when the following requirements are satisfied:")
        else:
            print(f"\n'{post}' can evolve from '{pre}' when the following requirements are satisfied:")
        print_requirements(requirements)

        if field == 'post':
            track_evolution(pre, field, cur)
        elif field == 'pre':
            track_evolution(post, field, cur)
        
        print("")
