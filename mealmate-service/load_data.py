from queries.pool import pool


def load_data():
    try:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into roles (name) values ('subscriber');
                    insert into roles (name) values ('chef');
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('John', 'Doe', 'johndoe', 'johndoe@gmail.com', 'password', 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGVyc29ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60', 1);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Jane', 'Doe', 'janedoe', 'janedoe@gmail.com', 'password', 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGVyc29ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60', 2);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Joe', 'Doe', 'joedoe', 'joedoe@gmail.com', 'password', 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGVyc29ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60', 1);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Jill', 'Doe', 'jilldoe', 'jilldoe@gmail.com', 'password', 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGVyc29ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=800&q=60', 2);
                    insert into statuses (name) values ('pending');
                    insert into statuses (name) values ('completed');
                    insert into statuses (name) values ('cancelled');
                    insert into meals (name, description, picture_url, chef_id, instructions, ingredients) values ('Chicken Parm', 'Chicken Parmesan is a dish of chicken cutlet, topped with tomato sauce and melted cheese, usually mozzarella. It is a common dish in Italian-American cuisine.', 'https://media.istockphoto.com/id/1308223808/photo/grilled-salmon-fillet-and-fresh-vegetable-salad-mediterranean-diet.jpg?b=1&s=170667a&w=0&k=20&c=3Hqmj_jGcF6m2Tj4Cb_Sek0GMSM2AuEUk6LcHNrf7kc=', 2, 'instructions', 'ingredients');
                    insert into meals (name, description, picture_url, chef_id, instructions, ingredients) values ('Fish Parm', 'Chicken Parmesan is a dish of chicken cutlet, topped with tomato sauce and melted cheese, usually mozzarella. It is a common dish in Italian-American cuisine.', 'https://media.istockphoto.com/id/1308223808/photo/grilled-salmon-fillet-and-fresh-vegetable-salad-mediterranean-diet.jpg?b=1&s=170667a&w=0&k=20&c=3Hqmj_jGcF6m2Tj4Cb_Sek0GMSM2AuEUk6LcHNrf7kc=', 2, 'instructions', 'ingredients');
                    insert into meals (name, description, picture_url, chef_id, instructions, ingredients) values ('Crab Parm', 'Chicken Parmesan is a dish of chicken cutlet, topped with tomato sauce and melted cheese, usually mozzarella. It is a common dish in Italian-American cuisine.', 'https://media.istockphoto.com/id/1308223808/photo/grilled-salmon-fillet-and-fresh-vegetable-salad-mediterranean-diet.jpg?b=1&s=170667a&w=0&k=20&c=3Hqmj_jGcF6m2Tj4Cb_Sek0GMSM2AuEUk6LcHNrf7kc=', 2, 'instructions', 'ingredients');
                    insert into meals (name, description, picture_url, chef_id, instructions, ingredients) values ('Beef Parm', 'Chicken Parmesan is a dish of chicken cutlet, topped with tomato sauce and melted cheese, usually mozzarella. It is a common dish in Italian-American cuisine.', 'https://media.istockphoto.com/id/1308223808/photo/grilled-salmon-fillet-and-fresh-vegetable-salad-mediterranean-diet.jpg?b=1&s=170667a&w=0&k=20&c=3Hqmj_jGcF6m2Tj4Cb_Sek0GMSM2AuEUk6LcHNrf7kc=', 2, 'instructions', 'ingredients');

                    insert into boxes (user_id) values (1);
                    insert into boxes (user_id) values (3);

                    insert into box_meals (box_id, meal_id, quantity) values (1, 1, 1);
                    insert into box_meals (box_id, meal_id, quantity) values (1, 2, 1);
                    insert into box_meals (box_id, meal_id, quantity) values (2, 3, 1);
                    insert into box_meals (box_id, meal_id, quantity) values (2, 4, 1);
                    insert into orders (user_id, status_id) values (1, 1);
                    insert into orders (user_id, status_id) values (3, 2);
                    insert into order_meals (order_id, meal_id, quantity) values (1, 1, 1);
                    insert into order_meals (order_id, meal_id, quantity) values (1, 2, 1);
                    insert into order_meals (order_id, meal_id, quantity) values (1, 3, 1);
                    insert into order_meals (order_id, meal_id, quantity) values (2, 2, 1);
                    insert into order_meals (order_id, meal_id, quantity) values (2, 3, 1);
                    insert into order_meals (order_id, meal_id, quantity) values (2, 4, 1);
                    """
                )
                print("***********Data loaded************")
    except Exception as e:
        print(e)
        return {"message": "Data not loaded"}


if __name__ == "__main__":
    load_data()
