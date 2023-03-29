steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE meals (
            id SERIAL NOT NULL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            created_at timestamp not null default now(),
            updated_at timestamp not null default now(),
            picture_url VARCHAR(5000) NOT NULL,
            description VARCHAR(5000) NOT NULL,
            instructions VARCHAR(5000) NOT NULL,
            ingredients VARCHAR(5000) NOT NULL,
            chef_id int references users(id) NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE meals;
        """,
    ],
]
