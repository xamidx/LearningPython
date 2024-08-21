print(
    'YES' if
    set(
        [int(e) for e in input()]
    ).issuperset(
        set(
            [int(e) for e in input()]
        )
    )
    else 'NO'
)
