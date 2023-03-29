steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE roles (
            id serial not null primary key,
            name varchar(100) not null unique
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE roles;
        """,
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id serial not null primary key,
            first_name varchar(100) not null,
            last_name varchar(100) not null,
            username varchar(15) not null unique,
            email varchar(50) not null unique,
            hashed_password varchar(200) not null,
            created_at timestamp not null default now(),
            updated_at timestamp not null default now(),
            picture_url varchar(5000) not null,
            role_id int references roles(id) not null
            );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """,
    ],
]
