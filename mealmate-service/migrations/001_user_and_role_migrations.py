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
        CREATE TABLE statuses (
            id serial not null primary key,
            name varchar(100) not null unique
        );

        INSERT INTO statuses (name) 
        VALUES ('pending'), ('completed'), ('cancelled'), ('delivered'), ('deleted'), ('active');
        """,
        # "Down" SQL statement
        """
        DROP TABLE statuses;
        """,
    ],
    [
        # "Up" SQL statement
        # chef default avatar: https://static.thenounproject.com/png/2053062-200.png
        """
        CREATE TABLE users (
            id serial not null primary key,
            status_id INT REFERENCES statuses(id) NOT NULL default 6,
            role_id int references roles(id) not null,
            first_name varchar(100) not null default 'Anonymous',
            last_name varchar(100) not null default 'Doe',
            username varchar(15) not null unique,
            email varchar(50) not null unique,
            hashed_password varchar(200) not null,
            created_at timestamp not null default now(),
            updated_at timestamp not null default now(),
            picture_url TEXT not null default 'https://static.vecteezy.com/system/resources/previews/007/319/933/original/black-avatar-person-icons-user-profile-icon-vector.jpg'
            );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """,
    ],
]
