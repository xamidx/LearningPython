print(
    *sorted(
        set(
            [int(e) for e in input().split()]
        ).intersection(
            [int(e) for e in input().split()]
        )
    )
)
