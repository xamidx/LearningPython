print(
    'NO' if
    set(
        [int(e) for e in input()]
    ).isdisjoint(
        [int(e) for e in input()]
    )
    else 'YES'
)
