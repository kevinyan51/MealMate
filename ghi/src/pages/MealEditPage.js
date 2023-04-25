import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import MealCreatePage from './MealCreatePage';
import { useParams } from 'react-router-dom';

const MealEditPage = () => {
  const [meal, setMeal] = useState(null);
  const { mealId } = useParams();
  const navigate = useNavigate();
  const editMeal = async (mealIn) => {
    const mealUrl = `${process.env.REACT_APP_USER_API_HOST}/api/meals/${mealId}/`;
    const response = await fetch(mealUrl, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(mealIn),
    });
    if (response.ok) {
      const meal = await response.json();
      navigate(`/meals/${meal.id}`);
    } else {
      // console.log('Error updating meal');
      navigate('/meals');
    }
  };
  const fetchMeal = async () => {
    const mealUrl = `${process.env.REACT_APP_USER_API_HOST}/api/meals/${mealId}/`;
    const response = await fetch(mealUrl);
    if (response.ok) {
      const meal = await response.json();
      setMeal(meal);
    }
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
