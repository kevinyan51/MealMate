import React from 'react';
import MealDetail from '../components/MealDetail';
import { useParams } from 'react-router-dom';

const SubscriberMealDetailPage = () => {
  const { mealId } = useParams();
  return (
    <div>
      <MealDetail mealId={mealId} />
    </div>
  );
};

export default SubscriberMealDetailPage;
