import React, { useEffect, useState } from 'react';
import MealCreatePage from './MealCreatePage';
import { useParams } from 'react-router-dom';

const MealEditPage = () => {
  const [meal, setMeal] = useState(null);
  const { mealId } = useParams();
  const editMeal = async (mealIn) => {
    const mealUrl = `http://localhost:8000/api/meals/${mealId}/`;
    const res = await fetch(mealUrl, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(mealIn),
    });
    const data = await res.json();
    console.log(data);
  };
  const fetchMeal = async () => {
    const mealUrl = `http://localhost:8000/api/meals/${mealId}/`;
    const res = await fetch(mealUrl);
    const meal = await res.json();
    setMeal(meal);
  };
  useEffect(() => {
    fetchMeal();
  }, []);
  return (
    <MealCreatePage
      title="Edit Meal"
      buttonText="Edit Meal"
      mealIn={meal}
      buttonAction={editMeal}
    />
  );
};

export default MealEditPage;
