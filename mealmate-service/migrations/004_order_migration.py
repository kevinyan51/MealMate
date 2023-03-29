steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE orders (
          id serial NOT NULL PRIMARY KEY,
          status_id INT REFERENCES statuses(id) NOT NULL,
          user_id INT REFERENCES users(id) NOT NULL,
          created_at TIMESTAMP NOT NULL default now(),
          updated_at TIMESTAMP NOT NULL default now()
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE orders;
        """,
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE order_meals (
          id serial NOT NULL PRIMARY KEY,
          order_id INT REFERENCES orders(id) NOT NULL,
          meal_id INT REFERENCES meals(id) NOT NULL,
          quantity INT NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE order_meals;
        """,
    ],
]
