# flake8: noqa
steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE reviews (
          id serial NOT NULL PRIMARY KEY,
          status_id INT REFERENCES statuses(id) NOT NULL default 6,
          subscriber_id INT REFERENCES users(id) NOT NULL,
          meal_id INT REFERENCES meals(id) NOT NULL,
          created_at TIMESTAMP NOT NULL DEFAULT now(),
          updated_at TIMESTAMP NOT NULL DEFAULT now(),
          rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
          comment TEXT NOT NULL DEFAULT 'No review available.'
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE reviews;
        """,
    ],
]
