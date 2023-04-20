# flake8: noqa
steps = [
    [
        # "Up" SQL statement
        """
        CREATE OR REPLACE FUNCTION update_updated_at_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = now();
            RETURN NEW;
        END;
        $$ language 'plpgsql';
        """,
        # "Down" SQL statement
        """
        DROP FUNCTION update_updated_at_column;
        """,
    ],
    [
        # "Up" SQL statement
        """
        CREATE TRIGGER update_users_modtime
        BEFORE UPDATE ON users
        FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """,
        # "Down" SQL statement
        """
        DROP TRIGGER update_users_modtime ON users;
        """,
    ],
    [
        # "Up" SQL statement
        """
        CREATE TRIGGER update_meals_modtime
        BEFORE UPDATE ON meals
        FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """,
        # "Down" SQL statement
        """
        DROP TRIGGER update_meals_modtime ON meals;
        """,
    ],
    [
        # "Up" SQL statement
        """
        CREATE TRIGGER update_orders_modtime
        BEFORE UPDATE ON orders
        FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """,
        # "Down" SQL statement
        """
        DROP TRIGGER update_orders_modtime ON orders;
        """,
    ],
    [
        # "Up" SQL statement
        """
        CREATE TRIGGER update_reviews_modtime
        BEFORE UPDATE ON reviews
        FOR EACH ROW
        EXECUTE PROCEDURE update_updated_at_column();
        """,
        # "Down" SQL statement
        """
        DROP TRIGGER update_reviews_modtime ON reviews;
        """,
    ],
]
