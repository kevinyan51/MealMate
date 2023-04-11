import React, { useState, useEffect } from 'react';
import ChefMealDetailPage from './ChefMealDetailPage.js';
import SubscriberMealDetailPage from './SubscriberMealDetailPage.js';
import Review from '../components/Review.js';

const MealDetailPage = () => {
  const [role, setRole] = useState(2);
  return (
    <>
      {role === 2 ? <ChefMealDetailPage /> : <SubscriberMealDetailPage />}
      <Review />
    </>
  );
};

export default MealDetailPage;
