import React from 'react';
import MealDetail from '../components/MealDetail';
import { useParams } from 'react-router-dom';

const ChefMealDetailPage = () => {
  const { mealId } = useParams();

  return (
    <div>
      <MealDetail mealId={mealId} />
    </div>
  );
};

export default ChefMealDetailPage;
