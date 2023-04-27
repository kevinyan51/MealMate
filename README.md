# Intended market

We are targeting both chefs and people who are interested in pre-made microwave meals. In our website users can either become a subscriber who can order meals prepared by our gourmet chefs or they can become a chef and sell their own meals. The chef's meals are then reviewed by users and ranked in order to see the best handcrafted meals by the chef.

## Functionality

- Non logged in users arrive at a landing page that prompts them to either sign in or “get started” which is the phrase used to select create an account
- Upon signup, users can either choose to become a chef or a subscriber.
- Subscribers are assigned a box on signup which contains every meal that has been created.
- Subscribers on sign in are redirected to the box page.
- Subscribers can then edit their box based on which meals they would like and also the quantity.
- The meals themselves have further indications depending on their dietary needs.
- They can click on meal details by selecting the button with three dots. Once selected it gives a detailed description of the meal and also the ingredients. On the side of this detailed description there are more recommended meals.
Below this are reviews from users about the selected meals.
- The subscriber can then save their box after their desired meal and respective quantities are selected.
- The subscribers can also click on my orders to check out their previous orders and the status of their orders. When they click on an individual order they can see the contents of a box they previously made.
- If a user signs up as a chef they have the option of adding a new meal.
- When adding a meal the chef has the ability to add a meal using their chef id, can add a name for a meal, add a subtitle for the meal, add a picture url of the meal, the calores, a description of the meal, the instructions for cooking the meal, the ingredients of the meal, the dietary labels there meal has or contains, and finally the price of the meal
- Both users have a profile button when selecting their avatar on the right hand side of the website. In this section it shows basic account information described on the signup portion. They also have to the ability to change there avatars and also update the account information.

## Project Initialization

- To fully enjoy this application on your local machine, please make sure to follow these steps:
- Clone the repository down to your local machine
- CD into the new project directory
- Run docker volume create postgres-data
- Run docker compose build
- Run docker compose up
- Optional for preloaded data:
In the docker container ‘mealmate-service-1’, run python -m load_data



# APIs

## Meals

## Method: POST, GET, GET, PUT, DELETE,

## Path: /api/meals/

## POST: Input:
{
  "name": string,
  "name2": string,
  "picture_url": string,
  "description": string,
  "instructions": string,
  "ingredients": string,
  "chef_id": int,
  "calories": int,
  "is_keto": bool,
  "is_vegan": bool,
  "Is_chef_choice": bool,
  "is_spicy": bool,
  "has_cheese": bool,
  "price": float/int,
}
Output:
{
  “id”: int,
  "name": string,
  "name2": string,
  "picture_url": string,
  "description": string,
  "instructions": string,
  "ingredients": string,
  "chef_id": int,
  "calories": int,
  "is_keto": bool,
  "is_vegan": bool,
  "Is_chef_choice": bool,
  "is_spicy": bool,
  "has_cheese": bool,
  "price": float/int,
}
Creating a meal saves each of these fields and passes in an id. It will add a meal and allows the subscriber to select its quantity in their box so the subscriber can order. The id helps identify the meal for when subscribers want to view the details of the respective meal.

## Path: /api/meals/<int:pk>/
## GET: Input:
{
“Id”: int
}
Output:
{
  “id”: int,
  "name": string,
  "name2": string,
  "picture_url": string,
  "description": string,
  "instructions": string,
  "ingredients": string,
  "chef_id": int,
  "calories": int,
  "is_keto": bool,
  "is_vegan": bool,
  "Is_chef_choice": bool,
  "is_spicy": bool,
  "has_cheese": bool,
  "price": float/int,
}
Additionally a get request at:
Path: /api/meals/
Will have the output of each meal that exists within the database.

## Users

## Method: GET, POST, PUT, DELETE


## Path: /api/users, /api/users/<int:pk>
Input:
{
  "first_name": string,
  "last_name": string,
  “username”: string,
  "email": string,
  "password": string,
  "role_id”: int,
}
Output:
{
  "first_name": string,
  "last_name": string,
  “username”: string,
  "email": string,
  "password": string,
  "role_id”: int,
}
The Users API will create, or delete an account for a user on the Meal Mate website. Users will need to enter in all of the information listed to create an account. The role_id int field will be to determine whether an account has access to chefs or subscribers pages.


## Orders

## Method: POST, DELETE,GET,GET,GET,GET
## Path: /api/users/{user_id}/orders,
Input:
{
  "userr_id": int,
  “order_status”: str
}
Output:
{
  "order_id": int,
  "order_status": str,
  "order_created_at": datetime,
  "order_updated_at": datetime,
  “subscriber_id”: int,
  “num_meals”: int,
  “total_price”: float,
  “meals”: List,

}

This gets the orders by subscriber.

## Path: /api/orders
Input:
{
}
Output:
{
  "order_id": int,
  "order_status": str,
  "order_created_at": datetime,
  "order_updated_at": datetime,
  “subscriber_id”: int,
  “num_meals”: int,
  “total_price”: float,
  “meals”: List,

}

This gets all the orders.
Path: /api/orders
Input:
{
  “box_id”: int
}
Output:
{
  "order_id": int,
  "order_status": str,
  "order_created_at": datetime,
  "order_updated_at": datetime,
  “subscriber_id”: int,
  “num_meals”: int,
  “total_price”: float,
  “meals”: List,

}

This creates an order
## Path: /api/orders/{order_id}
Input:
{
  “order_id”: int
}
Output:
{
  "order_id": int,
  "order_status": str,
  "order_created_at": datetime,
  "order_updated_at": datetime,
  “subscriber_id”: int,
  “num_meals”: int,
  “total_price”: float,
  “meals”: List,

}

This gets one order.

## Path: /api/users/{user_id}/orders/meals/{meal_id}
Input:
{
  “meal_id”: int,
  “Subscriber_id”: int
}
Output:
{
 ‘true’ or ‘false’
}




## Reviews

## Method: GET, POST, GET,  PUT, DELETE,
## Path: /api/reviews/, /api/reviews/<int:pk>
Input:
{
  "subscriber_id”: int,
  "meal_id": int,
  "rating": int,
  "comment": str
}
Output:
{
  "id”: int,
  "review_status": str,
  "subscriber_id": int,
  "comment": str,
  “meal_id”:int,
  “created_at”: datetime,
  “updated_at”: datetime,
  “Rating”: int,
  “comment”: str,
  “reviewer_first_name”: str,
  “reviewer_last_name”: str,
  “Picture_url” : str
}

This creates a review.


## Get reviews by subscriber:

## Path: /api/users/{user_id}/reviews/

Input:
{
“User_id”: int,
}
Output:
{
  "id”: int,
  "review_status": str,
  "subscriber_id": int,
  "comment": str,
  “meal_id”:int,
“created_at”: datetime,
“updated_at”: datetime,
“Rating”: int,
“comment”: str,
“reviewer_first_name”: str,
“reviewer_last_name”: str,
“Picture_url” : str
}

This will get all the reviews by an individual subscriber



## Get reviews by Meal:

## Path: /api/meals/{meal_id}/reviews/

input:
{
“meal_id”: int,
}

Output:
{
  "id”: int,
  "review_status": str,
  "subscriber_id": int,
  "comment": str,
  “meal_id”:int,
  “created_at”: datetime,
  “updated_at”: datetime,
  “rating”: int,
  “comment”: str,
  “reviewer_first_name”: str,
  “reviewer_last_name”: str,
  “picture_url” : str
}
This will get all the reviews by all users foran individual meal

## Boxes

## Method: GET,PUT
## Path: /api/boxes}/{box_id}/
{
  "box_id": int,
  "subscriber_id": int,
  "subscriber_first_name": "string",
  "subscriber_last_name": "string",
  "meals": [
    {
      "meal_id": int,
      "status_id": int,
      "chef_id": int,
      "name": "string",
      "name2": "string",
      "created_at": "datetime",
      "updated_at": "datetime",
      "picture_url": "string",
      "description": "string",
      "instructions": "string",
      "ingredients": "string",
      "calories": int,
      "is_keto": bool,
      "is_vegan": bool,
      "is_chef_choice": bool,
      "is_spicy": bool,
      "Has_cheese": bool,
      "price":  int,
      "chef_first_name": "string",
      "chef_last_name": "string",
      "chef_picture_url": "string",
      "quantity":  int
    }
  ]
}
This allow users to edit and create there box


#WireFrame:

[wireframe.png]
