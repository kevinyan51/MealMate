import React, { useEffect, useState } from 'react';
const FAKE_DATA = [
  {
    id: 1,
    name: 'Chicken',
    description: 'this is chicken',
    ingredients: 'chicken, salt, pepper',
    chef: 'John',
    price: 10.0,
    image:
      'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thespruceeats.com%2Fchi',
  },
  {
    id: 1,
    name: 'Chicken',
    description: 'this is chicken',
    ingredients: 'chicken, salt, pepper',
    chef: 'John',
    price: 10.0,
    image:
      'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thespruceeats.com%2Fchi',
  },
  {
    id: 1,
    name: 'Chicken',
    description: 'this is chicken',
    ingredients: 'chicken, salt, pepper',
    chef: 'John',
    price: 10.0,
    image:
      'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thespruceeats.com%2Fchi',
  },
  {
    id: 1,
    name: 'Chicken',
    description: 'this is chicken',
    ingredients: 'chicken, salt, pepper',
    chef: 'John',
    price: 10.0,
    image:
      'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thespruceeats.com%2Fchi',
  },
];

const Box = () => {
  const [box, setBox] = useState({});

  const getAllMeals = async () => {
    const url = 'http://localhost:8000/api/meals/';
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      return data;
    }
    console.log('error getting all meals');
    return [];
  };
  const handleAdd = (mealId) => {
    const newBox = { ...box };
    let meals = [...newBox.meals];
    meals = meals.map((meal) => {
      meal = { ...meal };
      if (meal.meal_id === mealId) {
        meal.quantity += 1;
      }
      return meal;
    });
    setBox({ ...newBox, meals });
  };
  const handleRemove = (mealId) => {
    const newBox = { ...box };
    let meals = [...newBox.meals];
    meals = meals.map((meal) => {
      meal = { ...meal };
      if (meal.meal_id === mealId) {
        if (meal.quantity > 0) meal.quantity -= 1;
      }
      return meal;
    });
    setBox({ ...newBox, meals });
  };

  const [userId, setUserId] = useState(null);
  const [boxId, setBoxId] = useState(null);

  const getUserBox = async () => {
    if (!userId) setUserId(1);
    const url = `http://localhost:8000/api/users/${userId || 1}/box_id/`;
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setBoxId(data);
      await getOneBox(data);
    }
  };
  useEffect(() => {
    getUserBox();
  }, []);

  const getOneBox = async () => {
    const url = `http://localhost:8000/api/boxes/${boxId}/`;
    const response = await fetch(url);
    const allMeals = await getAllMeals();

    if (response.ok) {
      const data = await response.json();
      data.meals = allMeals.map((meal) => {
        const mealInBox = data.meals.find(
          (mealInBox) => mealInBox.meal_id === meal.meal_id
        );
        if (mealInBox) {
          return { ...meal, quantity: mealInBox.quantity };
        }
        return { ...meal, quantity: 0 };
      });
      setBox(data);
    }
  };
  const saveBox = async () => {
    const url = `http://localhost:8000/api/boxes/${boxId}/`;
    let meals = [...box.meals.filter((meal) => meal.quantity > 0)];
    const response = await fetch(url, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ ...box, meals }),
    });
    if (response.ok) {
      return console.log('success');
    }
    console.log('error');
  };

  useEffect(() => {
    if (boxId) getOneBox();
  }, [boxId]);

  return (
    <div>
      {box?.meals?.map((meal) => {
        return (
          <div
            key={meal.meal_id}
            style={{ border: '1px solid', margin: 10, padding: 10 }}
          >
            <div>{meal.name}</div>
            <img src={meal.picture_url} alt={meal.name} width={200} />
            <div style={{ display: 'flex', marginTop: 10 }}>
              <button onClick={() => handleAdd(meal.meal_id)}>add</button>
              <div style={{ marginLeft: 10, marginRight: 10 }}>
                {meal.quantity || 0}
              </div>
              <button
                disabled={meal.quantity <= 0}
                onClick={() => handleRemove(meal.meal_id)}
              >
                remove
              </button>
            </div>
          </div>
        );
      })}
      <div>
        <button onClick={saveBox}>save box</button>
        <button>order now</button>
      </div>
    </div>
  );
};

export default Box;
