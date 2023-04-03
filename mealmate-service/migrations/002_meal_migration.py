steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE meals (
            id SERIAL NOT NULL PRIMARY KEY,
            chef_id int references users(id) NOT NULL,
            name VARCHAR(100) NOT NULL default 'Un-named Meal',
            name2 VARCHAR(100) NOT NULL default 'with Plain Bread or Rice',
            created_at TIMESTAMP not null default now(),
            updated_at TIMESTAMP not null default now(),
            picture_url TEXT NOT NULL default 'https://png.pngtree.com/element_our/20200702/ourmid/pngtree-vector-illustration-knife-and-fork-western-food-plate-image_2283844.jpg',
            description TEXT NOT NULL default 'No description provided',
            instructions TEXT NOT NULL default 'No instructions provided',
            ingredients TEXT NOT NULL default 'No ingredients provided',
            calories INT NOT NULL default 600,
            is_keto BOOLEAN NOT NULL default false,
            is_vegan BOOLEAN NOT NULL default false,
            is_chef_choice BOOLEAN NOT NULL default false,
            is_spicy BOOLEAN NOT NULL default false,
            has_cheese BOOLEAN NOT NULL default false,
            price DECIMAL NOT NULL default 9.99
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE meals;
        """,
    ],
]
