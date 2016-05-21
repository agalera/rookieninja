from rookieninja.modules.db import Mongo


def get_stats(calculated=False):
    stats = list(Mongo.stats_eve.find())
    if not calculated:
        return stats
    result = {'players': 0, 'fleets': 0}
    for stat in stats:
        result['fleets'] += stat['fleets']
        result['players'] += stat['players']
    return result
