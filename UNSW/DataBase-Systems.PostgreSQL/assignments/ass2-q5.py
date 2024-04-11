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
    helpers.track_evolution(cleanName, 'post', cur)
    helpers.track_evolution(cleanName, 'pre', cur)

