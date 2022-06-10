attacks = {
    'rock_slide': {
        'type': 'ROCK',
        'damage': '10'
    },
}

monsters = {
    'geodude': {
        'name': 'GEODUDE',
        'type': 'ROCK',
        'health': 50,
        'attack': 1,
        'defense': 1,
        'attacks': [attacks['rock_slide']]
    },
}
