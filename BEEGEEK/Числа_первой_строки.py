print(
    *sorted(
        set(
            [int(e) for e in input().split()]
        ).difference(
            [int(e) for e in input().split()]
        )
    )
)
