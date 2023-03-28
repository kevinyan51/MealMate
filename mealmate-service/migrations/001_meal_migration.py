steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE meal (
            meal_id serial not null primary key,
            meal_name varchar(100) not null,
            picture_url varchar(5000) not null,
            description varchar(5000) not null,
            instructions varchar(1000) not null,
            ingredients varchar(5000) not null,
            subscriber_id int null,
            chef_id int null
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE meal;
        """
    ],

]
