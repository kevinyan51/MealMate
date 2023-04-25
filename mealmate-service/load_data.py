# flake8: noqa
from queries.pool import pool


def load_data():
    try:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    insert into roles (name) values ('subscriber');
                    insert into roles (name) values ('chef');

                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('John', 'Doe', 'johndoe', 'johndoe@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://images.unsplash.com/photo-1527980965255-d3b416303d12?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8YXZhdGFyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=900&q=60', 1);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Jane', 'Doe', 'janedoe', 'janedoe@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://districtfray.com/wp-content/uploads/2023/03/Ria-Montes-Headshot1-1.jpg', 2);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Joe', 'Doe', 'joedoe', 'joedoe@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://images.unsplash.com/photo-1599566150163-29194dcaad36?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8YXZhdGFyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=900&q=60', 1);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Jill', 'Doe', 'jilldoe', 'jilldoe@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://i.pinimg.com/736x/cd/a2/a2/cda2a2c9e23b631814dda8ea5ea4e073--corporate-headshots-headshot-ideas.jpg', 2);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Mike', 'Williams', 'mikewilliams', 'mikewilliams@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8dXNlcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=700&q=60', 1);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Peter', 'Lee', 'peterlee', 'peterlee@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://i.pinimg.com/236x/a5/4e/e3/a54ee32ff16ae7e3c298eaca2bb6a825.jpg', 2);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Stephanie', 'Green', 'stephaniegreen', 'stephaniegreen@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://images.unsplash.com/photo-1580489944761-15a19d654956?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8YXZhdGFyfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=700&q=60', 1);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Amy', 'Smith', 'amysmith', 'amysmith@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/65X4LYTHFNBTJLY3R45NPSWO7I.jpg', 2);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Karen', 'Brown', 'karenbrown', 'karenbrown@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://images.unsplash.com/photo-1544725176-7c40e5a71c5e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Nnx8YXZhdGFyc3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=700&q=60', 1);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Ryan', 'Johnson', 'ryanjohnson', 'ryanjohnson@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://static8.depositphotos.com/1377527/955/i/450/depositphotos_9551898-stock-photo-head-shot-of-chef.jpg', 2);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Carol', 'Jones', 'caroljones', 'caroljones@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fGZlbWFsZSUyMGF2YXRhcnxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=700&q=60', 1);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Tina', 'Davis', 'tinadavis', 'tinadavis', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://images.unsplash.com/photo-1591980896142-4e36328411ec?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1974&q=80', 1);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Diane', 'Miller', 'dianemiller', 'dianemiller', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://images.unsplash.com/photo-1569913486515-b74bf7751574?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MzV8fGF2YXRhcnN8ZW58MHx8MHx8&auto=format&fit=crop&w=700&q=60', 1);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Bari', 'Watson', 'bariwatson', 'bariwatson@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://images.unsplash.com/photo-1603415526960-f7e0328c63b1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8dXNlciUyMHByb2ZpbGV8ZW58MHx8MHx8&auto=format&fit=crop&w=700&q=60', 1);
                    insert into users (first_name, last_name, username, email, hashed_password, picture_url, role_id) values ('Linda', 'Moore', 'lindamoore', 'lindamoore@gmail.com', '$2b$12$ncm1yaRChhlSs1Q7dvsv1.ZNXVqzDlRdQkfgG5Fo8NCnnhLIWmeV2', 'https://media.istockphoto.com/id/1438289500/photo/portrait-of-pretty-african-american-girl-looking-at-camera-smiling-and-laughing-human.jpg?s=612x612&w=0&k=20&c=DkfJZQt3upPGtWsNGUfFB0YKa9_xxpbx2gtwcLln_0U=', 1);

                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values 
                    (2, 9.99, 'Pesto Salmon', 'with Creamed Spinach & Tomato Butter Haricots Verts', 700, true, false, true, false, false, 'https://img.hellofresh.com/w_1200,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/640b6cea8fbd1f824e04997b-2071566c.jpg','Get your greens—and all of the feel-good benefits that go along with them—with this pescatarian dish. Here, oven-roasted salmon is served on a bed of velvety creamed spinach made with cream cheese, Parmesan, onions, and garlic. A blanket of vibrant kale pesto adds another layer of green goodness on top. For textural contrast, crisp haricots verts (aka slender green beans) with sun-dried tomato and basil butter complete the meal.','Ingredients: Salmon, Spinach, Haricots Verts, Cream Cheese (Pasteurized Milk And Cream, Cheese Culture, Salt, Guar Gum, Carob Bean Gum, Xanthan Gum), Olive Pomace Oil, Onions, Unsalted Butter (Pasteurized Cream, Natural Flavorings), Shredded Parmesan Cheese (Parmesan Cheese (Pasteurized Part-Skim Milk, Cheese Culture, Salt, Enzymes), Powdered Cellulose To Prevent Caking, Natamycin To Protect Flavor), Garlic, Grated Parmesan Cheese ((Parmesan Cheese (Pasteurized Cow’S Milk, Cheese Culture, Salt, Enzymes), Water, Milk Protein, Modified Food Starch, Palm Oil Blend, Salt, Disodium Phosphate, Citric Acid, Xanthan Gum), And Calcium Propionate (Preservative)), Almonds, Baby Kale, Basil, Spinach, Sun-Dried Tomatoes (Sun-Dried Tomatoes, Salt), Sea Salt, Granulated Garlic'); 
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values
                    (4, 8.99, 'Chicken Tikka Masala', 'with Basmati Rice, Chickpeas & Curry Cauliflower', 490, false, false, true, true, true, 'https://img.hellofresh.com/w_1200,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/640b7b6fe0314bf19203476d-3ea62b2b.jpg', 'Classic Indian-inspired flavors are on full display with this creamy chicken dish. Tender marinated chicken is slathered in our fragrant tikka masala sauce that has chock-full of spices, heavy cream, and cream cheese. It’s garnished with scallions and cilantro and served alongside seasoned basmati rice, masala-spiced chickpeas, and curry-spiced cauliflower florets.','Ingredients: Chicken Breast, Cauliflower, Water, Chickpeas (Prepared Chickpeas Beans, Water, Salt, Disodium Edta To Promote Color Retention), Heavy Cream, Onions, Concentrated Crushed Tomatoes (Tomatoes, Salt), Lowfat Buttermilk (Cultured Lowfat Milk, Nonfat Dry Milk, Salt, Sodium Citrate, Vitamin A Palmitate And Vitamin D3), Tomato Paste (Tomatoes, Citric Acid), Tomatoes, White Basmati Rice, Garlic, Ginger, Brown Basmati Rice, Cream Cheese (Pasteurized Milk And Cream, Cheese Culture, Salt, Guar Gum, Carob Bean Gum, Xanthan Gum), Green Onions, Olive Pomace Oil, Roasted Chicken Stock Base (Chicken Stock, Roasted Chicken Stock, Mirepoix Stock (Made Of Carrot, Celery And Onion Stocks, Dried Chicken Stock, Salt, Gelatin, Water, White Wine)), Plain Greek Yogurt (Pasteurized Cow’S And Goat’S Milk, Skim Milk, Milk Protein Concentrate, Cream, Contains Active Cultures Including L. Acidophilus, B. Lactis), Cilantro, Cumin Seeds, Sea Salt, Coriander, Curry Powder (Coriander, Fenugreek, Fennel, Mustard, Turmeric, Cumin, Black Pepper, Bay Leaves, Celery Seed, Nutmeg, Cloves, Onion, Red Pepper, Ginger, Chile Powder, Cinnamon, Cardamon, Salt), Turmeric, Paprika (Paprika And Silicon Dioxide (Added To Make Free Flowing)), Chili Powder (Chili Pepper, Spices, Salt, Garlic Powder), Black Pepper, Cinnamon, Cloves, Nutmeg, Ground Fennel, Ground Bay Leaves, Fenugreek Leaves');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values
                    (6, 11.99, 'Spicy Sweet Potatoes & Peanut Sauce','with Coconut Rice & Miso-Roasted Green Beans', 660, false, true, true, true, false, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/641891d2b786533ae4097582-65d3880d.jpg', 'Sweet, savory, and spicy flavors are on full display in this Indonesian-inspired vegan dish. We start with tender roasted sweet potatoes and drape them in a traditional satay sauce made with peanut butter, ginger, garlic, lime juice, and sambal chili sauce for a spicy kick. It’s all piled over coconut basmati rice, and garnished with toasted peanuts that are spiced with gogucharu (Korean chili flakes). On the side there’s green beans, roasted with red miso, sesame, and roasted garlic for a hit of umami.','Ingredients: Sweet Potatoes, Green Beans, Water, Brown Basmati Rice, Peanut Butter, Garlic, Ginger, Roasted Peanuts, Olive Pomace Oil, Unsweetened Coconut Milk (Coconut, Water, Guar Gum), Cilantro, Blue Agave Nectar, Lime Juice, Coconut Aminos (Organic Coconut Nectar, Organic Pure Coconut Blossom Sap, Natural Unrefined Sea Salt (Less Than 2%)), Red Miso Paste (Filtered Water, Cultured Rice, Organic Whole Soy Beans, Sea Salt), Toasted Sesame Oil, Gochugaru Chile Flakes, Desiccated Coconut, Sambal Oelek Chili Paste (Red Chili Peppers, Salt, Distilled Vinegar, Xanthan Gum), Ground Kaffir Lime Leaves, Sea Salt, Black Sesame Seeds, Toasted Sesame Seeds');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values
                    (8, 10.99, 'Spicy Poblano Beef Bowl','with Roasted Broccoli Rice & Scallion Sour Cream', 580, true, false, true, true, true, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/641ded0391433a6f540a71f2-2428ca5e.jpg','Enjoy spicy, bold flavors in this simple yet satisfying keto bowl. We start by simmering ground beef with cumin, chili powder, and cayenne, kick it up even more with jalapeño and poblano peppers, then sprinkle on some cheddar cheese. We’ve also added a side of broccoli “rice“ for a boost of veggies, and a drizzle of scallion sour cream to cool things off.','Ingredients: Ground Beef, Riced Broccoli, Poblano Peppers, Tomato Sauce (Tomatoes, Tomato Puree, Salt, Red Pepper, Dehydrated Bell Peppers, Dehydrated Onion, Dehydrated Garlic, Onion Powder, Garlic Powder, Spice Extractive, Citric Acid, Natural Flavoring), Sour Cream (Cultured Cream), Shredded Cheddar Cheese (Pasteurized Milk, Cheese Cultures, Salt, Enzymes, Annatto Vegetable Color, Anti-Caking Agent (Potato Starch, Powdered Cellulose, Corn Starch, Natamycin)), Sliced Jalapeño Peppers (Jalapeño Peppers, Water, Distilled Vinegar, Salt, Calcium Chloride, Garlic Powder, Sodium Benzoate, Riboflavin), Unsalted Butter (Pasteurized Cream, Natural Flavorings), Green Onions, Roasted Garlic Oil (Olive Pomace Oil, Garlic), Granulated Onion, Chili Powder (Chili Pepper, Spices, Salt, Garlic Powder), Paprika (Paprika And Silicon Dioxide (Added To Make Free Flowing)), Cumin, Sea Salt, Granulated Garlic, Black Pepper, Cayenne Pepper');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values
                    (10, 9.99, 'Garlic Rosemary Pork Chop', 'with Creamy Parmesan Brussels & Garlic Broccoli', 590, true, false, true, false, true, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/garlic-rosemary-pork-chop-w14-b79606d1.jpg', 'This indulgent dish features a garlic-rosemary grilled pork chop that has been brined with apple cider vinegar for extra tenderness. It pairs beautifully with the two vegetable sides: roasted Brussels sprouts enriched with Parmesan cream and soft garden herb cheese plus garlicky broccoli florets topped with lemon garlic butter.','Ingredients: Pork Chop, Broccoli, Brussels Sprouts, Heavy Cream, Neufchatel Cheese (Pasteurized Milk And Cream, Skim Milk, Cheese Culture, Salt, Guar Gum, Carob Bean Gum, Xanthan Gum), Unsalted Butter (Pasteurized Cream, Natural Flavorings), Grated Parmesan Cheese ((Parmesan Cheese (Pasteurized Cow’S Milk, Cheese Culture, Salt, Enzymes), Water, Milk Protein, Modified Food Starch, Palm Oil Blend, Salt, Disodium Phosphate, Citric Acid, Xanthan Gum), And Calcium Propionate (Preservative)), Olive Pomace Oil, Garlic, Sea Salt, Granulated Onion, Toasted Garlic Powder, Granulated Garlic, Apple Cider Vinegar, Thyme, Sage, Black Pepper, Toasted Minced Garlic, Rosemary, Lemon Powder (Citric Acid, Natural Lemon Flavor), Dried Parsley, Dried Dill Weed, Smoked Black Pepper (Pepper, Smoke Flavor), Dried Chives, Dried Thyme');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values
                    (2, 8.99, 'Indian Butter Chicken','with Cilantro Lime Cauliflower Rice',630, true, false, true, false, false, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/641deee7d8a9d25cb708914f-5d54396f.jpg','This Indian-inspired meal begins with a tender bed of cauliflower “rice” enhanced with cilantro, lime juice, and garlic. It’s topped with juicy garam masala-spiced chicken, then swirled in a rich tomato-based sauce made with butter, heavy cream, cumin, coriander, chili powder and even more aromatic masala spices.','Ingredients: Chicken Breast, Riced Cauliflower, Crushed Tomatoes (Tomatoes, Tomato Puree, Less Than 2% Salt, Citric Acid), Heavy Cream, Unsalted Butter (Pasteurized Cream, Natural Flavorings), Olive Pomace Oil, Onions, Water, Roasted Garlic Oil (Olive Pomace Oil, Garlic), Plain Greek Yogurt (Pasteurized Cow’S And Goat’S Milk, Skim Milk, Milk Protein Concentrate, Cream, Contains Active Cultures Including L. Acidophilus, B. Lactis), Cilantro, Green Onions, Ginger, Garlic, Whole Milk (Pasteurized Milk, Vitamin D3), Sea Salt, Monkfruit Sweetener (Erythritol, Monk Fruit Extract), Cumin, Lime Juice, Chili Powder (Chili Pepper, Spices, Salt, Garlic Powder), Coriander, Turmeric, Black Pepper, Lime Powder (Citric Acid, Natural Lime Flavor), Cinnamon, Fenugreek Leaves, Smoked Black Pepper (Pepper, Smoke Flavor), Cloves, Nutmeg, Ground Fennel');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values
                    (4, 11.99, 'Shredded Chicken Taco Bowl','with Roasted Corn Salsa & Cilantro Lime Sour Cream',530,false, false, true, false, false, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/641e6043383e0665f80afd5e-c7176d1e.jpg','Packed with savory Mexican-style flavors, each element of this dish comes together to form one exciting bowl. Juicy shredded chicken, seasoned with our house-made taco seasoning, is served over black beans and brown rice. It’s all accented with a roasted corn salsa made with spicy poblanos, red bell peppers, cilantro, paprika, cumin, and chili powder. The meal is finished with a creamy cilantro sour cream, perfect for drizzling over the top.','Ingredients: Chicken Breast, Yellow Sweet Corn, Water, Long Grain Parboiled Brown Rice, Sour Cream (Cultured Cream), Black Beans, Shredded Cheddar Cheese (Pasteurized Milk, Cheese Cultures, Salt, Enzymes, Annatto Vegetable Color, Anti-Caking Agent (Potato Starch, Powdered Cellulose, Corn Starch, Natamycin)), Cilantro, Poblano Peppers, Red Onions, Red Bell Peppers, Green Onions, Olive Oil, Chili Powder (Chili Pepper, Spices, Salt, Garlic Powder), Roasted Chicken Stock Base (Chicken Stock, Roasted Chicken Stock, Mirepoix Stock (Made Of Carrot, Celery And Onion Stocks, Dried Chicken Stock, Salt, Gelatin, Water, White Wine)), Lime Juice, Jalapeño Peppers, Sea Salt, Cumin, Paprika (Paprika And Silicon Dioxide (Added To Make Free Flowing)), Black Pepper, Garlic, Granulated Garlic, Crushed Red Pepper Flakes, Granulated Onion, Dried Oregano');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values
                    (6, 10.99, 'Tomato & Roasted Vegetable Risotto', 'with Zucchini, Bell Peppers & Toasted Pine Nuts', 440, false, true, true, false, false, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/641e69c2deca2fd86f0d0421-8939fc94.jpg','Any time is a good time to savor this elegant vegan risotto. Arborio rice, red onions, and garlic are simmered in red wine, low and slow until creamy and tender, then sprinkled with basil and nutritional yeast to add a “cheesy” note. On the side: a vibrant mix of roasted bell peppers, zucchini, and cherry tomatoes, plus a serving of toasted pine nuts, which adds a light nutty crunch.','Ingredients: Water, Arborio Rice, Zucchini, Red Bell Peppers, Grape Tomatoes, Pine Nuts, Crushed Tomatoes (Tomatoes, Tomato Puree, Less Than 2% Salt, Citric Acid), Red Onions, Cabernet Sauvignon Wine (Grapes, Sulfites), Olive Pomace Oil, Nutritional Yeast Flakes (Dried Yeast, Niacin, Pyridoxine Hydrochloride (B6), Riboflavin, Thiamine Hydrochloride, (Thiamine), Folic Acid, Cobalamin (B12)), Sea Salt, Garlic, Basil, Black Pepper');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values
                    (8, 9.99, 'Garlic Pork Tenderloin', 'with Asiago Cauliflower Mash & Pesto Green Beans', 700, true, false, false, false, true, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/642b21ea3305168f5b0f2724-5f7d493f.jpg', 'To infuse pork tenderloin with as much flavor as possible, our chefs marinate it with plenty of garlic, lemon, and herbs, before grilling and slicing it. They then top the pork with a garlic butter sauce and serve it over a creamy cauliflower mash blended with sharp, nutty Asiago cheese. For the side veg, they offer roasted green beans and red bell pepper slices garnished with a classic pesto made with pine nuts and Parmesan cheese.', 'Ingredients: Pork Tenderloin, Green Beans, Riced Cauliflower, Unsalted Butter (Pasteurized Cream, Natural Flavorings), Red Bell Peppers, Olive Oil, Water, Garlic, Cream Cheese (Pasteurized Milk And Cream, Cheese Culture, Salt, Guar Gum, Carob Bean Gum, Xanthan Gum), Shredded Asiago Cheese (Pasteurized Cow’s Milk, Cheese Cultures, Salt, Enzymes, Natamycin (A Natural Mold Inhibitor)), Lemon Juice, Whole Milk (Pasteurized Milk, Vitamin D3), Pine Nuts, Grated Parmesan Cheese ((Parmesan Cheese (Pasteurized Cow’s Milk, Cheese Culture, Salt, Enzymes), Water, Milk Protein, Modified Food Starch, Palm Oil Blend, Salt, Disodium Phosphate, Citric Acid, Xanthan Gum), And Calcium Propionate (Preservative)), Basil, Spinach, Sea Salt, Roasted Chicken Stock Base (Chicken Stock, Roasted Chicken Stock, Mirepoix Stock (Made Of Carrot, Celery And Onion Stocks, Dried Chicken Stock, Salt, Gelatin, Water, White Wine)), Black Pepper, Granulated Garlic, Dried Chives, Granulated Onion, Toasted Garlic Powder, Dried Parsley, White Pepper, Xanthan Gum, Dried Oregano, Granulated Green Onion');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values 
                    (10, 8.99, 'White Cheddar Chicken', 'with Broccoli-Parmesan "Grits", Roasted Green Beans & Sliced Almonds', 650, true, false, false, false, true, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/642b14b5533641d8290f0307-0527cf05.jpg','A comfort classic gets a modern upgrade in this flavor-packed meal. Marinated chicken is grilled until juicy, topped with a slice of white cheddar cheese, and served over creamy broccoli cheddar grits. On the side, there’s roasted chili green beans topped with garlic chili butter for a little extra decadence and toasted almonds for crunch.','Ingredients: Chicken Breast, Green Beans, Riced Broccoli, Sharp White Cheddar Cheese (Cultured Pasteurized Milk, Salt, Enzymes), Heavy Cream, Olive Pomace Oil, Shredded Medium White Cheddar Cheese (Cultured Milk, Salt, Enzymes, Anti-Caking Agents (Potato Starch, Powdered Cellulose, Natamycin)), Cream Cheese (Pasteurized Milk And Cream, Cheese Culture, Salt, Guar Gum, Carob Bean Gum, Xanthan Gum), Almonds, Unsalted Butter (Pasteurized Cream, Natural Flavorings), Lowfat Buttermilk (Cultured Lowfat Milk, Nonfat Dry Milk, Salt, Sodium Citrate, Vitamin A Palmitate And Vitamin D3), Onions, Green Onions, Sea Salt, Granulated Garlic, Black Pepper, Toasted Minced Garlic, Toasted Onion Powder, Granulated Onion, Rosemary, Dried Chives, Gochugaru Chile Flakes, Guajillo Chile Powder, Thyme');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values 
                    (2, 11.99, 'Sun-Dried Tomato Chicken', 'with Zucchini Noodles', 640, true, false, false, false, true, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/642b147bdf29d37ebb026627-98b6a896.jpg','All the comforting flavors of a home-cooked meal, but without any of the fuss. We start with a fire-grilled chicken breast, seasoned with basil, oregano, and garlic and nestle it in a delectable sun-dried tomato cream sauce made with Parmesan and spinach. It’s served with tender zucchini noodles, perfect for lapping up every bit of the sauce.','Ingredients: Chicken Breast, Zucchini, Heavy Cream, Olive Pomace Oil, Onions, Grated Parmesan Cheese ((Parmesan Cheese (Pasteurized Cow’S Milk, Cheese Culture, Salt, Enzymes), Water, Milk Protein, Modified Food Starch, Palm Oil Blend, Salt, Disodium Phosphate, Citric Acid, Xanthan Gum), And Calcium Propionate (Preservative)), Spinach, Sun-D, Dried Tomatoes In Olive Oil, Garlic, Sea Salt, Black Pepper, Dried Oregano, Dried Basil, Dried Parsley, Dried Thyme, Dried Rosemary, Dried Marjoram, Dried Sage, Dried Tarragon, Dried Fennel, Dried Celery Seed, Dried Bay Leaf, Dried Lavender, Dried Lemon Peel, Dried Orange Peel, Dried Lime Peel, Dried Grapefruit Peel, Dried Coriander, Dried Cumin, Dried Mustard Seed, Dried Ginger, Dried Turmeric, Dried Nutmeg, Dried Cloves, Dried Allspice, Dried Cinnamon, Dried Cardamom, Dried Black Pepper, Dried Red Pepper, Dried Cayenne Pepper, Dried Anise, Dried Fenugreek, Dried Caraway Seed, Dried Dill Seed, Dried Fennel Seed, Dried Poppy Seed, Dried Sesame Seed, Dried Cilantro, Dried Chives, Dried Garlic, Dried Onion, Dried Parsley, Dried Basil, Dried Thyme, Dried Rosemary, Dried Marjoram, Dried Sage, Dried Tarragon, Dried Fennel');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values 
                    (4, 10.99, 'Goat Cheese & Romesco Baked Chicken', 'with Lemon Basil Broccoli', 600, true, false, false, false, true, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/642b219e8d245f257b0ff63b-6d7af19e.jpg', 'Tonight’s hearty dish begins with a bright and complex romesco sauce, made with fire-roasted red peppers and tomatoes, which serves as a bed for a juicy Italian-seasoned chicken breast. The chicken is topped with a creamy spread of goat cheese, heavy cream, Parmesan, and walnuts for a touch of creamy crunch in every bite. Roasted broccoli florets, topped with rich lemon-basil butter, add fresh, bright flavors on the side.', 'Ingredients: Chicken Breast, Broccoli, Water, Unsalted Butter (Pasteurized Cream, Natural Flavorings), Fire Roasted Diced Tomatoes (Tomatoes, Tomato Juice, Sea Salt, Calcium Chloride, Citric Acid), Fire Roasted Red Peppers (Roasted Peppers, Water, Sea Salt, Citric Acid), Walnuts, Goat Cheese (Whole Pasteurized Goat Milk, Salt, Cheese Culture, Enzymes), Cream Cheese (Pasteurized Milk And Cream, Cheese Culture, Salt, Guar Gum, Carob Bean Gum, Xanthan Gum), Roasted Garlic Oil (Olive Pomace Oil, Garlic), Heavy Cream, Olive Pomace Oil, Granulated Garlic, Red Wine Vinegar, Grated Parmesan Cheese ((Parmesan Cheese (Pasteurized Cow’S Milk, Cheese Culture, Salt, Enzymes), Water, Milk Protein, Modified Food Starch, Palm Oil Blend, Salt, Disodium Phosphate, Citric Acid, Xanthan Gum), And Calcium Propionate (Preservative)), Parsley, Garlic, Sea Salt, Lemon Powder (Citric Acid, Natural Lemon Flavor), Black Pepper, Dried Basil, Granulated Onion, Italian Seasoning (Marjoram, Thyme, Rosemary, Savory, Sage, Oregano, Basil), Smoked Paprika, Crushed Red Pepper Flakes, Cayenne Pepper');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values 
                    (6, 9.99, 'Pimento Cheese Chicken Breast', 'with Garlic Spinach & Creamed Zucchini', 620, true, false, false, false, true, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/64024035caf1ded06303d2ad-9e00fae3.jpg', 'Pimento cheese is a southern party staple, usually paired with crackers or spread between slices of white bread. Here, the dip takes new shape in the form of a satisfying square meal. This version—made with avocado mayo, cream cheese, cheddar, and diced red peppers—sits below garlicky steamed spinach and smoky grilled chicken. Creamed zucchini rounds out the dish.', 'Ingredients: Chicken Breast, Zucchini, Spinach, Cream Cheese (Pasteurized Milk And Cream, Cheese Culture, Salt, Guar Gum, Carob Bean Gum, Xanthan Gum), Shredded Cheddar Cheese (Pasteurized Milk, Cheese Cultures, Salt, Enzymes, Annatto Vegetable Color, Anti-Caking Agents (Potato Starch, Powdered Cellulose, Corn Starch)), Heavy Cream, Olive Oil, Avocado Oil Mayonnaise (Avocado Oil, Organic Certified Humane Free Range Egg Yolks, Water, Distilled Vinegar, Salt, Lime Juice Concentrate, Citric Acid, Lime Oil), Diced Red Peppers (Red Sweet Pepper, Water, Citric Acid), Garlic, Onions, Granulated Onion, Granulated Garlic, Blanched Almond Flour, Shredded Parmesan Cheese (Parmesan Cheese (Pasteurized Part-Skim Milk, Cheese Culture, Salt, Enzymes), Powdered Cellulose To Prevent Caking, Natamycin To Protect Flavor), Smoked Paprika, Sea Salt, Smoked Black Pepper (Pepper, Smoke Flavor), Black Pepper, Cayenne Pepper');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values 
                    (8, 8.99, 'Fiesta Grilled Chicken', 'with Hominy-Tomato Sauce & Elote-Style Squash', 420, false, false, false, false, true, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/642b2465b5081feedb0aea0a-dc11541b.jpg', 'Corn abounds in this meal inspired by flavors found South of the border. Grilled chicken marinated with cumin and chili is paired with a salad of roasted corn, black beans, and cilantro. For a tomato and corn “sauce,“ diced tomatoes are simmered with onion, garlic, and Mexican spices, then rounded out with a touch of cream. Crushed tostadas add texture to a base of hominy, a large white-kernel corn. Lastly, a side of zucchini get elote-style toppings with a chili-lime seasoning and crumbled queso fresco.', 'Ingredients: Chicken Breast, Zucchini, Diced Tomatoes (Tomatoes, Tomato Juice, Salt, Calcium Chloride, Citric Acid), Hominy (Hominy, Water, Salt), Black Beans (Prepared Black Beans, Water)');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values
                    (10, 11.99, 'Garlic Butter Shrimp & Creamed Kale', 'with Zucchini-Pepper-Onion Medley', 520, true, false, false, false, true, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/642b22d1f96531831e0afb52-56cccd0d.jpg', 'Our chefs have prepared a meal to remember with this ultra-luxe seafood dish. Succulent shrimp are marinated in garlic and savory Italian spices, and then roasted until tender and juicy. They’re drizzled with a rich onion-garlic butter sauce and served with a side of creamy creamed kale. A zucchini-pepper-onion medley rounds out the meal.', 'Ingredients: Shrimp, Zucchini, Kale, Butter (Cream, Salt), Garlic, Onions, Granulated Onion, Granulated Garlic, Blanched Almond Flour, Shredded Parmesan Cheese (Parmesan Cheese (Pasteurized Part-Skim Milk, Cheese Culture, Salt, Enzymes), Powdered Cellulose To Prevent Caking, Natamycin To Protect Flavor), Heavy Cream, Olive Oil, Sea Salt, Smoked Black Pepper (Pepper, Smoke Flavor), Black Pepper, Cayenne Pepper');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values 
                    (2, 10.99, 'Bacon-Ranch Butter Shredded Chicken', 'with Garlic Kale & Sour Cream & Onion Haricots Verts', 770, true, false, true, false, false, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/bacon-ranch-butter-shredded-chicken-w14-66014c8c.jpg', 'For this meal, our chefs brined and marinated chicken thighs in a blend of olive oil, garlic, and herbs, then cooked them until fall-apart tender. Once shredded, the meat is piled on top of garlicky ranch-seasoned kale and dolloped with tangy bacon ranch butter. A side of steamed haricots verts is served with a creamy french onion sauce.', 'Ingredients: Chicken Thighs, Haricots Verts, Kale, Olive Pomace Oil, Unsalted Butter (Pasteurized Cream, Natural Flavorings), Nitrite/Nitrate-Free Uncured Bacon (Pork, Water, Salt, Celery Powder, Cherry Baste Aid), Neufchatel Cheese (Pasteurized Milk And Cream, Skim Milk, Cheese Culture, Salt, Guar Gum, Carob Bean Gum, Xanthan Gum), Sour Cream (Cultured Cream), Water, Whole Milk (Pasteurized Milk, Vitamin D3), Garlic, Sunflower Seeds, Roasted Chicken Stock Base (Chicken Stock, Roasted Chicken Stock, Mirepoix Stock (Made Of Carrot, Celery And Onion Stocks, Dried Chicken Stock, Salt, Gelatin, Water, White Wine)), Grated Parmesan Cheese ((Parmesan Cheese (Pasteurized Cow’S Milk, Cheese Culture, Salt, Enzymes), Water, Milk Protein, Modified Food Starch, Palm Oil Blend, Salt, Disodium Phosphate, Citric Acid, Xanthan Gum), And Calcium Propionate (Preservative)), Red Wine Vinegar, Sea Salt, Dried Onion Flakes, Granulated Garlic, Black Pepper, Roasted Garlic Oil (Olive Pomace Oil, Garlic), Toasted Onion Powder, Toasted Garlic Powder, Granulated Onion, Dried Parsley, Dried Dill Weed, Dried Chives');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values 
                    (4, 9.99, 'Lebanese Chicken & Quinoa Bowl', 'with Asparagus-Pepper Tabbouleh & Lemon Dressing', 540, false, false, false, false, false, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/lebanese-chicken-quinoa-bowl-w14-c9ed0ee1.jpg', 'This light and summery meal is packed with fragrant Mediterranean spices. Red bell peppers, onions, garlic, and fennel are sautéed until tender, and then stirred into tender white quinoa, which serves as a base for chicken breast bites seasoned with basil, oregano, and thyme. It’s served with our take on tabbouleh, made with hemp seeds instead of bulgur, and sautéed asparagus, bell peppers, and parsley. There’s also a bright lemon dressing to top it all off.', 'Ingredients: Chicken Breast, Quinoa, Asparagus, Red Bell Pepper, Hemp Seeds, Parsley, Olive Pomace Oil, Lemon Juice, Garlic, Lemon Zest, Lemon Oil, Sea Salt, Black Pepper, Dried Basil, Dried Oregano, Dried Thyme, Dried Parsley, Dried Fennel, Dried Rosemary, Dried Mint, Dried Marjoram, Dried Sage, Dried Tarragon, Dried Chives');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values 
                    (6, 8.99, 'Smoked Tofu Almond Stir-Fry', 'with Edamame Succotash & Soy Vinaigrette', 560, false, true, false, false, false, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/642b275acf3deac0aa0d29a6-66b39ab7.jpg', 'Every forkful of this Asian-inspired plant-based entrée contains layers of irresistible flavor and texture. Fluffy brown basmati rice cradles gingery, garlic-braised mushrooms, sesame-roasted green beans, and smoked five-spice tofu. A handful of crunchy, ginger-chili toasted almonds crowns it all. On the side, you’ll find a colorful, sesame-spiked succotash of bell peppers and edamame. A drizzle of soy vinaigrette with agave ties it all together.', 'Ingredients: Smoked Five Spice Tofu (Whole Soybeans, Calcium Sulfate, Glucono Delta- Lactone (Gdl), Water, Gluten-Free Soy Sauce, Kosher Salt, Spices (Peppercorn, Cumin, Cinnamon, Clove, Aniseed, Coriander), Shelled Edamame, Water, Green Beans, Mushrooms, Brown Basmati Rice, Green Bell Peppers, Red Bell Peppers, Toasted Sesame Oil, Almonds, Reduced Sodium Tamari (Water, Soybeans, Salt, Alcohol (To Preserve Freshness)), Red Onions, Rice Vinegar, Garlic, Ginger, Maple Syrup, Blue Agave Nectar, Green Onions, Orange Juice, Sesame Seeds, Sea Salt, Granulated Garlic, Granulated Onion, Ground Ginger, Cilantro, Toasted Sesame Seeds, Coconut Aminos (Organic Coconut Nectar, Organic Pure Coconut Blossom Sap, Natural Unrefined Sea Salt (Less Than 2%)), Toasted Garlic Powder, Toasted Onion Powder, Black Pepper, Gochugaru Chile Flakes, White Pepper, Xanthan Gum');
                    insert into meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) values 
                    (8, 11.99, 'Almond Crusted Salmon', 'with Red Pepper Cream, Green Beans & Feta Dressing', 660, true, false, false, false, true, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/642b266997220935fa0e8509-8e599982.jpg', 'Savor this luxurious keto seafood dish, featuring bold and complex flavors. An almond-crusted salmon filet sits atop a rich and creamy roasted red pepper sauce seasoned with thyme, oregano, and plenty of garlic. It’s accompanied by garlicky steamed green beans and a rich dressing made with feta, Greek yogurt, basil, garlic, and lemon.', 'Ingredients: Salmon, Green Beans, Heavy Cream, Fire Roasted Red Peppers (Roasted Peppers, Water, Sea Salt, Citric Acid), Plain Greek Yogurt (Pasteurized Cow’S And Goat’S Milk, Skim Milk, Milk Protein Concentrate, Cream, Contains Active Cultures Including L. Bulgaricus, S. Thermophilus, L. Acidophilus, L. Casei, L. Rhamnosus, L. Plantarum, Bifidus, And L. Paracasei), Feta Cheese (Pasteurized Milk, Cheese Culture, Salt, Enzymes), Basil, Lemon Juice, Garlic, Lemon Zest, Olive Pomace Oil, Sea Salt, Black Pepper, Dried Thyme, Dried Oregano, Dried Parsley, Dried Rosemary, Dried Mint, Dried Marjoram, Dried Sage, Dried Tarragon, Dried Chives');
                    INSERT INTO meals (chef_id, price, name, name2, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese, picture_url, description, ingredients) VALUES 
                    (10, 10.99, 'Peanut Buddha Bowl', 'with Cilantro Quinoa, Gochugaru-Spiced Peanuts & Sesame Broccoli', 580, false, true, false, true, false, 'https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/640243a0f1c544f7540f82dc-1d24fd99.jpg', 'This Buddha bowl starts with quinoa topped with sesame-roasted broccoli and toasted peanuts coated with gochugaru (Korean chili flakes). They’re served with red and green bell peppers, garlic, and cilantro. A satay-style peanut sauce is perfect for drizzling over the top.', 'Sweet Potatoes, Broccoli, Green Bell Peppers, Water, Quinoa, Red Bell Peppers, Peanut Butter, Peanuts, Garlic, Blue Agave Nectar, Red Onions, Green Onions, Olive Pomace Oil, Toasted Sesame Oil, Lime Juice, Coconut Aminos (Organic Coconut Nectar, Organic Pure Coconut Blossom Sap, Natural Unrefined Sea Salt (Less Than 2%)), Ginger, Cilantro, Roasted Garlic Oil (Olive Pomace Oil, Garlic), Mirepoix Concentrate (Water, Sea Salt, Vegetable Stock (Carrot, Celery And Onion Stocks), Carrot Stock, Tapioca Starch, Cabbage Juice Concentrate, Celery Stock, Onion Stock, Natural Flavors, Mushroom Stock, Tomato Paste), Gochugaru Chile Flakes, Sambal Oelek Chili Paste (Red Chili Peppers, Salt, Distilled Vinegar, Xanthan Gum), Coconut Oil, Sea Salt, Jalapeño Peppers, Toasted Sesame Seeds, Granulated Garlic, Toasted Onion Powder, Lime Powder (Citric Acid, Natural Lime Flavor), Crushed Red Pepper Flakes');


                    INSERT INTO boxes (subscriber_id) VALUES 
                    (1), (3), (5), (7), (9), (11), (12), (13), (14), (15);

                    INSERT INTO box_meals (box_id, meal_id, quantity) VALUES 
                    (1, 1, 2),
                    (1, 2, 1),
                    (1, 3, 2),
                    (1, 4, 1),
                    (1, 5, 2),
                    (2, 1, 2),
                    (2, 2, 1),
                    (2, 3, 2),
                    (2, 4, 1),
                    (2, 5, 2),
                    (3, 1, 2),
                    (3, 2, 1),
                    (3, 3, 2),
                    (3, 4, 1),
                    (3, 5, 2),
                    (4, 1, 2),
                    (4, 2, 1),
                    (4, 3, 2),
                    (4, 4, 1),
                    (4, 5, 2),
                    (5, 1, 2),
                    (5, 2, 1),
                    (5, 3, 2),
                    (5, 4, 1),
                    (5, 5, 2),
                    (6, 1, 2),
                    (6, 2, 1),
                    (6, 3, 2),
                    (6, 4, 1),
                    (6, 5, 2),
                    (7, 1, 2),
                    (7, 2, 1),
                    (7, 3, 2),
                    (7, 4, 1),
                    (7, 5, 2),
                    (8, 1, 2),
                    (8, 2, 1),
                    (8, 3, 2),
                    (8, 4, 1),
                    (8, 5, 2),
                    (9, 1, 2),
                    (9, 2, 1),
                    (9, 3, 2),
                    (9, 4, 1),
                    (9, 5, 2),
                    (10, 1, 2),
                    (10, 2, 1),
                    (10, 3, 2),
                    (10, 4, 1),
                    (10, 5, 2);

                    -- Subscriber 1
                    INSERT INTO orders (subscriber_id, status_id) VALUES
                    (1, 2),
                    (1, 2),
                    (1, 1),
                    (1, 3),
                    (1, 2);

                    -- Subscriber 3
                    INSERT INTO orders (subscriber_id, status_id) VALUES
                    (3, 2),
                    (3, 2),
                    (3, 1),
                    (3, 3),
                    (3, 2);

                    -- Subscriber 5
                    INSERT INTO orders (subscriber_id, status_id) VALUES
                    (5, 3),
                    (5, 1),
                    (5, 2),
                    (5, 2),
                    (5, 1);

                    -- Subscriber 7
                    INSERT INTO orders (subscriber_id, status_id) VALUES
                    (7, 1),
                    (7, 2),
                    (7, 3),
                    (7, 1),
                    (7, 2);

                    -- Subscriber 9
                    INSERT INTO orders (subscriber_id, status_id) VALUES
                    (9, 3),
                    (9, 1),
                    (9, 2),
                    (9, 3),
                    (9, 1);

                    -- Subscriber 11
                    INSERT INTO orders (subscriber_id, status_id) VALUES
                    (11, 2),
                    (11, 3),
                    (11, 1),
                    (11, 2),
                    (11, 3);

                    -- Subscriber 12
                    INSERT INTO orders (subscriber_id, status_id) VALUES
                    (12, 1),
                    (12, 2),
                    (12, 3),
                    (12, 1),
                    (12, 2);

                    -- Subscriber 13
                    INSERT INTO orders (subscriber_id, status_id) VALUES
                    (13, 3),
                    (13, 2),
                    (13, 1),
                    (13, 3),
                    (13, 2);

                    -- Subscriber 14
                    INSERT INTO orders (subscriber_id, status_id) VALUES
                    (14, 1),
                    (14, 3),
                    (14, 2),
                    (14, 1),
                    (14, 3);

                    -- Subscriber 15
                    INSERT INTO orders (subscriber_id, status_id) VALUES
                    (15, 3),
                    (15, 2),
                    (15, 1),
                    (15, 3),
                    (15, 2);


                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES 
                    (1, 1, 5, 'The Pesto Salmon was a delight to my taste buds! The salmon was perfectly cooked, and the pesto sauce was divine.'),
                    (3, 1, 4, 'I really enjoyed the Pesto Salmon, but I wish there was more pesto sauce. The salmon was cooked perfectly.'),
                    (5, 1, 5, 'Wow! The Pesto Salmon was amazing! The salmon was cooked to perfection and the pesto sauce was heavenly.'),
                    (7, 1, 4, 'The Pesto Salmon was good, but I was hoping for more flavor. The salmon was cooked well.'),
                    (9, 1, 5, 'The Pesto Salmon was so delicious! The salmon was cooked perfectly, and the pesto sauce was absolutely amazing.'),
                    (11, 1, 4, 'The Pesto Salmon was good, but it lacked a bit of seasoning. The salmon was cooked well.'),
                    (12, 1, 5, 'I loved the Pesto Salmon! The salmon was perfectly cooked, and the pesto sauce was just the right amount of flavor.'),
                    (13, 1, 4, 'The Pesto Salmon was pretty good, but it was a bit dry. The pesto sauce was flavorful.'),
                    (14, 1, 5, 'The Pesto Salmon was one of the best meals I have ever had! The salmon was cooked to perfection, and the pesto sauce was simply delicious.'),
                    (15, 1, 4, 'I enjoyed the Pesto Salmon, but I wish there was more sauce. The salmon was cooked well.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES 
                    (1, 2, 4, 'The chicken in the tikka masala was tender and succulent. The spices were well-balanced and the sauce was creamy.'),
                    (3, 2, 5, 'Wow! This chicken tikka masala was a flavor explosion. The chicken was cooked to perfection and the sauce was heavenly.'),
                    (5, 2, 3, 'The chicken in the tikka masala was slightly dry, but the sauce was tasty and fragrant.'),
                    (7, 2, 4, 'The chicken tikka masala was good, but a little spicier than I expected.'),
                    (9, 2, 5, 'The chicken in the tikka masala was so tender and the sauce was divine. This dish is a new favorite of mine.'),
                    (11, 2, 4, 'This chicken tikka masala was good, but I prefer mine with a bit more heat.'),
                    (12, 2, 5, 'I was blown away by this chicken tikka masala! The chicken was cooked to perfection and the sauce was absolutely delicious.'),
                    (13, 2, 4, 'The chicken was a little overcooked in the tikka masala, but the sauce made up for it with its rich and bold flavors.'),
                    (14, 2, 3, 'The chicken in the tikka masala was a bit tough, and the sauce was not as flavorful as I had hoped.'),
                    (15, 2, 5, 'This chicken tikka masala was phenomenal! The chicken was tender and the sauce had just the right amount of spice and creaminess.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 3, 5, 'The combination of the sweet potatoes and the peanut sauce was perfect. I loved the way the flavors blended together.'),
                    (3, 3, 4, 'This dish was really good, but I think it could have been spicier. The peanut sauce was a nice touch.'),
                    (5, 3, 3, 'I am not a big fan of sweet potatoes, but the peanut sauce was good.'),
                    (7, 3, 5, 'This was one of the best dishes I''ve had in a while! The peanut sauce was amazing and the sweet potatoes were cooked perfectly.'),
                    (9, 3, 4, 'The sweet potatoes were a little undercooked, but the peanut sauce was really tasty.'),
                    (11, 3, 5, 'I loved the combination of the spicy sauce and the sweetness of the potatoes. This dish was amazing!'),
                    (12, 3, 3, 'The peanut sauce was good, but the sweet potatoes were a little too sweet for my taste.'),
                    (13, 3, 4, 'The peanut sauce was really good, but I think the dish could have used a little more spice.'),
                    (14, 3, 5, 'This was a great vegetarian dish! The sweet potatoes were cooked perfectly and the peanut sauce was amazing.'),
                    (15, 3, 3, 'I thought the sweet potatoes were a little overcooked, but the peanut sauce was really good.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 4, 4, 'The beef in this Spicy Poblano Beef Bowl was tender and the spiciness was just right.'),
                    (3, 4, 5, 'I absolutely loved this Spicy Poblano Beef Bowl! The beef was cooked perfectly and the flavor was amazing.'),
                    (5, 4, 3, 'The spiciness of this Spicy Poblano Beef Bowl was a bit too much for me, but the beef was still good.'),
                    (7, 4, 4, 'The beef in this Spicy Poblano Beef Bowl was good, but the spiciness overpowered the other flavors.'),
                    (9, 4, 5, 'This Spicy Poblano Beef Bowl was fantastic! The beef was tender and the spiciness was just right.'),
                    (11, 4, 4, 'I enjoyed this Spicy Poblano Beef Bowl, but I would have preferred a bit more beef.'),
                    (12, 4, 5, 'This Spicy Poblano Beef Bowl was one of the best meals I have ever had! The beef was tender and the spiciness was perfect.'),
                    (13, 4, 4, 'The beef in this Spicy Poblano Beef Bowl was flavorful and the spiciness was just right.'),
                    (14, 4, 3, 'The spiciness in this Spicy Poblano Beef Bowl was too much for me, and the beef was a bit tough.'),
                    (15, 4, 5, 'This Spicy Poblano Beef Bowl was amazing! The beef was tender and the spiciness was perfect.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 5, 4, 'The pork was juicy and well-seasoned. I loved the garlic and rosemary flavor.'),
                    (3, 5, 5, 'This pork chop was amazing! The garlic and rosemary flavor really came through and the meat was perfectly cooked.'),
                    (5, 5, 3, 'The pork was a bit dry, but the garlic and rosemary seasoning was good.'),
                    (7, 5, 4, 'The pork was flavorful, but a bit tough.'),
                    (9, 5, 5, 'This pork chop was delicious! The garlic and rosemary seasoning was perfect and the meat was tender.'),
                    (11, 5, 4, 'The pork was good, but I would have liked more garlic and rosemary flavor.'),
                    (12, 5, 5, 'This was an excellent pork chop. The garlic and rosemary seasoning was just right and the meat was tender and juicy.'),
                    (13, 5, 4, 'The pork was tender and flavorful, but the garlic and rosemary flavor was a bit too strong for me.'),
                    (14, 5, 3, 'The pork was a bit dry and the garlic and rosemary seasoning was too subtle.'),
                    (15, 5, 5, 'This pork chop was amazing! The garlic and rosemary seasoning was so flavorful and the meat was cooked to perfection.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 6, 4, 'The chicken was tender and juicy. The spices were well-balanced.'),
                    (3, 6, 5, 'I loved the Indian Butter Chicken! The chicken was cooked perfectly and the sauce was delicious.'),
                    (5, 6, 3, 'The chicken was a bit dry, but the sauce was tasty.'),
                    (7, 6, 4, 'The chicken was good, but I would have liked more spice.'),
                    (9, 6, 5, 'The Indian Butter Chicken was amazing! The chicken was so tender and the sauce was flavorful.'),
                    (11, 6, 4, 'This dish was good, but I would have preferred more sauce.'),
                    (12, 6, 5, 'The chicken was perfectly cooked and the sauce was delicious. I would definitely order this again!'),
                    (13, 6, 4, 'The spices were good, but the chicken was a little dry.'),
                    (14, 6, 3, 'The chicken was a bit tough and the sauce was lacking in flavor.'),
                    (15, 6, 5, 'This Indian Butter Chicken was fantastic! The chicken was tender and the sauce was the perfect balance of spicy and creamy.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 7, 4, 'The chicken was tender and flavorful. I enjoyed the different textures.'),
                    (3, 7, 5, 'What a bowl! The chicken was cooked to perfection and the toppings were delicious.'),
                    (5, 7, 3, 'To be honest, the chicken was a bit dry. However, the toppings were good.'),
                    (7, 7, 4, 'At first, the chicken seemed a little bland, but the rice made up for it.'),
                    (9, 7, 5, 'The chicken was tender and juicy. I loved the combination of toppings.'),
                    (11, 7, 4, 'Although the chicken was good, I would have liked more salsa.'),
                    (12, 7, 5, 'I must say, this was an excellent chicken taco bowl. The chicken was tender and the toppings were perfect.'),
                    (13, 7, 4, 'The chicken was flavorful and tender. The rice could have been a bit more moist.'),
                    (14, 7, 3, 'Honestly, the chicken was dry and the toppings were a bit bland.'),
                    (15, 7, 5, 'This chicken taco bowl was amazing! I loved the combination of tender chicken and flavorful toppings.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 8, 4, 'The risotto was cooked perfectly. The roasted vegetables added a great flavor.'),
                    (3, 8, 5, 'I loved this risotto! The tomato flavor was so rich and the veggies were perfectly roasted.'),
                    (5, 8, 3, 'To be honest, I was a little underwhelmed by this risotto. The veggies were great, but the seasoning was a bit too salty for me.'),
                    (7, 8, 4, 'Overall, I enjoyed this risotto. The tomato flavor was good, but it could have used a bit more seasoning.'),
                    (9, 8, 5, 'This risotto was simply amazing! The roasted vegetables were perfectly cooked and the tomato flavor was so rich and satisfying.'),
                    (11, 8, 4, 'The risotto was good, but I think it needed more seasoning to really make the flavors pop.'),
                    (12, 8, 5, 'I have to say, this was one of the best risottos I have ever tasted! The tomato and roasted vegetables were a perfect match.'),
                    (13, 8, 4, 'The risotto was creamy and flavorful, but I would have liked more veggies in it.'),
                    (14, 8, 3, 'Unfortunately, this risotto didn''t quite meet my expectations. The roasted vegetables were good, but the risotto itself was a bit bland.'),
                    (15, 8, 5, 'This risotto was an absolute delight! The tomato flavor was rich and satisfying, and the roasted veggies added a wonderful touch of flavor.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 9, 4, 'The pork was cooked perfectly. The garlic flavor added a great depth.'),
                    (3, 9, 5, 'I loved this pork tenderloin! The garlic flavor was so rich and the meat was perfectly cooked.'),
                    (5, 9, 3, 'To be honest, I was a little underwhelmed by this pork tenderloin. The meat was good, but the garlic flavor was a bit too strong for me.'),
                    (7, 9, 4, 'Overall, I enjoyed this pork tenderloin. The garlic flavor was good, but it could have used a bit more seasoning.'),
                    (9, 9, 5, 'This pork tenderloin was simply amazing! The garlic flavor was so rich and satisfying, and the meat was perfectly tender.'),
                    (11, 9, 4, 'The pork was good, but I think it needed more seasoning to really make the flavors pop.'),
                    (12, 9, 5, 'I have to say, this was one of the best pork tenderloins I have ever tasted! The garlic and meat were a perfect match.'),
                    (13, 9, 4, 'The pork was juicy and flavorful, but I would have liked more garlic flavor in it.'),
                    (14, 9, 3, 'Unfortunately, this pork tenderloin didn''t quite meet my expectations. The meat was good, but the garlic flavor was a bit overpowering.'),
                    (15, 9, 5, 'This pork tenderloin was an absolute delight! The garlic flavor was rich and satisfying, and the meat was cooked to perfection.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 10, 4, 'The chicken was cooked perfectly. The white cheddar added a great flavor.'),
                    (3, 10, 5, 'I loved this chicken! The white cheddar flavor was so rich and the chicken was perfectly cooked.'),
                    (5, 10, 3, 'To be honest, I was a little underwhelmed by this chicken. The white cheddar was great, but the seasoning was a bit too salty for me.'),
                    (7, 10, 4, 'Overall, I enjoyed this chicken. The white cheddar flavor was good, but it could have used a bit more seasoning.'),
                    (9, 10, 5, 'This chicken was simply amazing! The white cheddar was perfectly melted and the chicken was so tender and juicy.'),
                    (11, 10, 4, 'The chicken was good, but I think it needed more seasoning to really make the flavors pop.'),
                    (12, 10, 5, 'I have to say, this was one of the best chicken dishes I have ever tasted! The white cheddar was a perfect match.'),
                    (13, 10, 4, 'The chicken was juicy and flavorful, but I would have liked more cheese in it.'),
                    (14, 10, 3, 'Unfortunately, this chicken didn''t quite meet my expectations. The white cheddar was good, but the chicken itself was a bit bland.'),
                    (15, 10, 5, 'This chicken was an absolute delight! The white cheddar flavor was rich and satisfying, and the chicken was cooked to perfection.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 11, 4, 'The chicken was moist and tender. The sun-dried tomatoes added a nice touch of sweetness.'),
                    (3, 11, 5, 'Wow! This chicken was amazing! The sun-dried tomatoes were the perfect addition and the chicken was cooked to perfection.'),
                    (5, 11, 3, 'The chicken was a little dry for my taste, but the sun-dried tomatoes added a nice touch of flavor.'),
                    (7, 11, 4, 'The sun-dried tomato flavor was really good in this dish, but the chicken was a little overcooked.'),
                    (9, 11, 5, 'I absolutely loved this dish! The chicken was perfectly cooked and the sun-dried tomatoes added a great pop of flavor.'),
                    (11, 11, 4, 'The chicken was cooked well, but I think it needed a bit more seasoning. The sun-dried tomatoes were a nice touch.'),
                    (12, 11, 5, 'This dish was fantastic! The sun-dried tomatoes were perfectly balanced with the chicken and the seasoning was spot on.'),
                    (13, 11, 4, 'The chicken was good, but it was a little dry for my liking. The sun-dried tomatoes added a nice touch of sweetness.'),
                    (14, 11, 3, 'The chicken was a bit overcooked and dry, but the sun-dried tomatoes added a nice flavor.'),
                    (15, 11, 5, 'This dish was absolutely delicious! The chicken was moist and the sun-dried tomatoes added a perfect touch of sweetness.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 12, 5, 'This chicken was so delicious! The goat cheese and romesco sauce added the perfect amount of flavor.'),
                    (3, 12, 4, 'I enjoyed this chicken, but I think it could have used a bit more seasoning. The goat cheese and romesco sauce were a nice touch.'),
                    (5, 12, 3, 'Unfortunately, this chicken was a bit dry for my taste. The goat cheese and romesco sauce helped add some flavor, though.'),
                    (7, 12, 4, 'The chicken was cooked well, but the goat cheese and romesco sauce were a bit too rich for me.'),
                    (9, 12, 5, 'I absolutely loved this chicken! The goat cheese and romesco sauce were the perfect combination, and the chicken was cooked perfectly.'),
                    (11, 12, 4, 'Overall, I enjoyed this chicken dish. The goat cheese and romesco sauce were a unique twist on a classic dish.'),
                    (12, 12, 5, 'Wow, this chicken was amazing! The goat cheese and romesco sauce were a perfect match, and the chicken was cooked to perfection.'),
                    (13, 12, 4, 'The chicken was moist and flavorful, but I thought the goat cheese and romesco sauce overpowered the dish a bit.'),
                    (14, 12, 3, 'This chicken was just okay for me. The goat cheese and romesco sauce were a nice touch, but the chicken itself was a bit bland.'),
                    (15, 12, 5, 'This chicken was absolutely delicious! The goat cheese and romesco sauce were the perfect addition, and the chicken was cooked perfectly.');
                        
                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 13, 5, 'Wow, this chicken breast was amazing! The pimento cheese was the perfect addition to this dish.'),
                    (3, 13, 4, 'This chicken breast was pretty good, but I think it could have used a bit more seasoning. The pimento cheese added a nice touch though.'),
                    (5, 13, 3, 'I wasn''t a huge fan of this chicken breast. The pimento cheese was okay, but the chicken itself was a bit dry.'),
                    (7, 13, 4, 'The pimento cheese on this chicken breast was really good, but I think the chicken itself could have been cooked a bit better.'),
                    (9, 13, 5, 'This chicken breast was absolutely delicious! The pimento cheese was the perfect complement to the tender chicken.'),
                    (11, 13, 4, 'The pimento cheese on this chicken breast was good, but I think the chicken could have been more flavorful.'),
                    (12, 13, 5, 'I loved this chicken breast! The pimento cheese was so creamy and flavorful, and the chicken was perfectly cooked.'),
                    (13, 13, 4, 'The pimento cheese on this chicken breast was tasty, but the chicken itself was a bit too dry for my liking.'),
                    (14, 13, 3, 'Unfortunately, this chicken breast didn''t quite meet my expectations. The pimento cheese was good, but the chicken was a bit tough.'),
                    (15, 13, 5, 'This chicken breast was absolutely delicious! The pimento cheese was so creamy and flavorful, and the chicken was perfectly cooked.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 14, 4, 'The grilled chicken was cooked perfectly. The corn salsa added a great flavor.'),
                    (3, 14, 5, 'I loved this grilled chicken! The spice rub was so flavorful and the corn salsa was a perfect accompaniment.'),
                    (5, 14, 3, 'To be honest, I was a little underwhelmed by this grilled chicken. The spice rub was good, but the corn salsa didn''t add much to the dish.'),
                    (7, 14, 4, 'Overall, I enjoyed this grilled chicken. The spice rub was good, but it could have used a bit more flavor.'),
                    (9, 14, 5, 'This grilled chicken was simply amazing! The spice rub was perfect and the corn salsa added a wonderful touch of sweetness.'),
                    (11, 14, 4, 'The grilled chicken was good, but I think it needed a bit more spice to really make the flavors pop.'),
                    (12, 14, 5, 'I have to say, this was one of the best grilled chickens I have ever tasted! The spice rub was perfect and the corn salsa was a perfect match.'),
                    (13, 14, 4, 'The grilled chicken was juicy and flavorful, but I would have liked more corn salsa on the side.'),
                    (14, 14, 3, 'Unfortunately, this grilled chicken didn''t quite meet my expectations. The spice rub was good, but the chicken itself was a bit dry.'),
                    (15, 14, 5, 'This grilled chicken was an absolute delight! The spice rub was flavorful and the corn salsa added a wonderful touch of sweetness.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 15, 4, 'The shrimp was cooked perfectly. The creamed kale was a nice touch.'),
                    (3, 15, 5, 'Wow! This dish was amazing! The garlic butter shrimp was so flavorful and the creamed kale was a perfect complement.'),
                    (5, 15, 3, 'I didn''t really care for the creamed kale, but the garlic butter shrimp was tasty.'),
                    (7, 15, 4, 'The creamed kale was really good, but the garlic butter shrimp was a bit too salty for my taste.'),
                    (9, 15, 5, 'The garlic butter shrimp was delicious and the creamed kale was a unique addition that really worked well.'),
                    (11, 15, 4, 'The shrimp was a bit overcooked, but the creamed kale was really tasty.'),
                    (12, 15, 5, 'This dish was absolutely amazing! The garlic butter shrimp was perfectly cooked and the creamed kale was a perfect match.'),
                    (13, 15, 4, 'The shrimp was a bit bland, but the creamed kale had a nice flavor.'),
                    (14, 15, 3, 'The creamed kale was a bit too rich for my taste and the shrimp was a bit overcooked.'),
                    (15, 15, 5, 'I loved this dish! The garlic butter shrimp was so flavorful and the creamed kale was a perfect complement.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 16, 4, 'The shredded chicken was cooked perfectly. The bacon and ranch flavors were a great combination.'),
                    (3, 16, 5, 'This dish was absolutely delicious! The bacon and ranch flavors really worked well together and the shredded chicken was perfectly cooked.'),
                    (5, 16, 3, 'The bacon flavor was a bit overpowering for me, but the shredded chicken was good.'),
                    (7, 16, 4, 'The shredded chicken was really tasty, but I would have liked more ranch flavor.'),
                    (9, 16, 5, 'The bacon and ranch flavors were a perfect match and the shredded chicken was cooked perfectly.'),
                    (11, 16, 4, 'The chicken was a bit dry, but the bacon and ranch flavors were really good.'),
                    (12, 16, 5, 'This dish was simply amazing! The bacon and ranch flavors were perfectly balanced and the shredded chicken was cooked to perfection.'),
                    (13, 16, 4, 'The shredded chicken was good, but I would have liked more bacon flavor.'),
                    (14, 16, 3, 'I was a bit disappointed with this dish. The shredded chicken was a bit dry and the bacon and ranch flavors were overpowering.'),
                    (15, 16, 5, 'This dish was so tasty! The bacon and ranch flavors were a perfect match and the shredded chicken was cooked to perfection.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 17, 4, 'The chicken was tender and juicy. The quinoa had a great texture.'),
                    (3, 17, 5, 'Wow! This Lebanese Chicken & Quinoa Bowl was amazing. The flavors were perfectly balanced.'),
                    (5, 17, 3, 'I thought this dish was just okay. The chicken was a bit dry and the quinoa was a bit bland.'),
                    (7, 17, 4, 'The chicken in this bowl was good, but I would have liked more seasoning. The quinoa was perfectly cooked.'),
                    (9, 17, 5, 'This Lebanese Chicken & Quinoa Bowl was absolutely delicious! The flavors were so rich and satisfying.'),
                    (11, 17, 4, 'The chicken was cooked well, but I think the dish needed more vegetables. The quinoa was good.'),
                    (12, 17, 5, 'This was a great bowl! The chicken and quinoa were cooked perfectly, and the flavors were spot on.'),
                    (13, 17, 4, 'I enjoyed this dish, but I wish the chicken had been a bit more flavorful. The quinoa was good.'),
                    (14, 17, 3, 'Unfortunately, this bowl didn''t quite meet my expectations. The chicken was dry and the quinoa was bland.'),
                    (15, 17, 5, 'I loved this Lebanese Chicken & Quinoa Bowl! The chicken was tender and juicy, and the quinoa had a great texture.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 18, 4, 'The smoked tofu was so flavorful! The almonds added a nice crunch.'),
                    (3, 18, 5, 'This Smoked Tofu Almond Stir-Fry was absolutely delicious! The flavors were perfectly balanced.'),
                    (5, 18, 3, 'I wasn''t a big fan of the smoked tofu in this dish, but the almonds were good.'),
                    (7, 18, 4, 'The smoked tofu was cooked well, but I wish the dish had more vegetables. The almonds added a nice touch.'),
                    (9, 18, 5, 'This stir-fry was amazing! The smoked tofu and almonds were a perfect match.'),
                    (11, 18, 4, 'The smoked tofu had a great flavor, but the dish was a bit too spicy for my taste. The almonds were good.'),
                    (12, 18, 5, 'I loved this Smoked Tofu Almond Stir-Fry! The flavors were so unique and delicious.'),
                    (13, 18, 4, 'The smoked tofu was good, but I wish there had been more vegetables in the dish. The almonds were a nice touch.'),
                    (14, 18, 3, 'Unfortunately, this stir-fry wasn''t my favorite. The smoked tofu was a bit too overpowering and the almonds didn''t add much flavor.'),
                    (15, 18, 5, 'This Smoked Tofu Almond Stir-Fry was absolutely delicious! The smoked tofu had a great flavor and the almonds added a nice crunch.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 19, 4, 'The salmon was cooked to perfection. The almond crust was a nice touch.'),
                    (3, 19, 5, 'What a fantastic dish! The salmon was moist and delicious, and the almond crust was a great complement.'),
                    (5, 19, 3, 'The salmon was good, but the almond crust was a bit too heavy for my liking.'),
                    (7, 19, 4, 'The almond crust gave the salmon a nice crunch, but I think it needed a bit more seasoning.'),
                    (9, 19, 5, 'I absolutely loved this dish! The salmon was perfectly cooked and the almond crust added a wonderful texture.'),
                    (11, 19, 4, 'The salmon was good, but it could have used a bit more flavor.'),
                    (12, 19, 5, 'This was one of the best salmon dishes I have ever had! The almond crust was a great touch.'),
                    (13, 19, 4, 'The salmon was tender and flaky, but the almond crust was a bit too thick for my liking.'),
                    (14, 19, 3, 'The salmon was decent, but the almond crust didn''t really add much to the dish.'),
                    (15, 19, 5, 'This dish was amazing! The salmon was perfectly cooked and the almond crust added a great crunch.');

                    INSERT INTO reviews (subscriber_id, meal_id, rating, comment) VALUES
                    (1, 20, 4, 'The peanut sauce was really flavorful. The veggies were fresh and crunchy.'),
                    (3, 20, 5, 'This dish was absolutely delicious! The peanut sauce was so flavorful and the veggies were perfectly cooked.'),
                    (5, 20, 3, 'I thought this dish was okay. The peanut sauce was a bit too sweet for my taste.'),
                    (7, 20, 4, 'The veggies in this dish were really fresh and crunchy. The peanut sauce could have used a bit more flavor.'),
                    (9, 20, 5, 'This dish was incredible! The peanut sauce was so tasty and the veggies were perfectly cooked.'),
                    (11, 20, 4, 'The peanut sauce was good, but it could have used a bit more spice.'),
                    (12, 20, 5, 'What a wonderful dish! The peanut sauce was so flavorful and the veggies were perfectly cooked.'),
                    (13, 20, 4, 'The veggies were fresh and crunchy, but the peanut sauce was a bit too sweet for my taste.'),
                    (14, 20, 3, 'I wasn''t too impressed with this dish. The peanut sauce was too sweet for me and the veggies were just okay.'),
                    (15, 20, 5, 'This dish was amazing! The peanut sauce was so flavorful and the veggies were perfectly cooked. I would order this again in a heartbeat!');

                    """
                )

                cur.execute(
                    """
                    CREATE OR REPLACE FUNCTION generate_order_meals()
                    RETURNS void AS
                    $$
                    DECLARE
                        order_id integer;
                        meal_id integer;
                        num_records integer;
                    BEGIN
                        FOR order_id IN 1..50 LOOP
                            num_records := floor(random() * 6) + 5; -- generate a random number of records between 5 to 10
                            FOR i IN 1..num_records LOOP
                                meal_id := floor(random() * 20) + 1; -- generate a random meal_id
                                EXECUTE format('INSERT INTO order_meals (order_id, meal_id, quantity) 
                                                SELECT %s, %s, %s 
                                                WHERE NOT EXISTS (SELECT 1 FROM order_meals WHERE order_id = %s AND meal_id = %s)',
                                            order_id, meal_id, floor(random() * 5) + 1, order_id, meal_id); -- generate a random quantity between 1 to 5
                            END LOOP;
                        END LOOP;
                    END;
                    $$
                    LANGUAGE plpgsql;

                    SELECT generate_order_meals();
                    """
                )

                print("***********Data loaded************")
    except Exception as e:
        print(e)
        return {"message": "Data not loaded"}


if __name__ == "__main__":
    load_data()
