import React from 'react';
import ChefMealDetailPage from './ChefMealDetailPage.js';
import SubscriberMealDetailPage from './SubscriberMealDetailPage.js';

const MealDetailPage = () => {
  return (
    <>
      {/* if user role is chef, show this component */}
      <ChefMealDetailPage />
      {/* elif user role is subscriber, show this instead */}
      <SubscriberMealDetailPage />
    </>
  );
};

export default MealDetailPage;
