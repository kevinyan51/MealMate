# flake8: noqa
steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE boxes (
            id serial not null primary key,
            subscriber_id int references users(id) not null
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE boxes;
        """,
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE box_meals (
            id serial not null primary key,
            box_id int references boxes(id) not null,
            meal_id int references meals(id) not null,
            quantity int not null
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE box_meals;
        """,
    ],
]
