import React, { useState } from 'react';
import ChefMealDetailPage from './ChefMealDetailPage.js';
import SubscriberMealDetailPage from './SubscriberMealDetailPage.js';
import Review from '../components/Review.js';
import { useToken } from '../components/Auth.js';

const MealDetailPage = () => {
  const { user } = useToken();
  return (
    <>
      {user?.role_id === 2 ? (
        <ChefMealDetailPage />
      ) : (
        <SubscriberMealDetailPage />
      )}
      <Review />
    </>
  );
};

export default MealDetailPage;
