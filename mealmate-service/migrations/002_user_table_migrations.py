steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            user_id serial not null primary key,
            first_name varchar(100) not null,
            last_name varchar(100) not null,
            username varchar(15) not null unique,
            email varchar(50) not null unique,
            hashed_password varchar(200) not null,
            picture_url varchar(5000) not null,
            is_subscriber bool default false,
            is_chef bool default false
            );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """
    ],
]
