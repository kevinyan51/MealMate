import React from 'react';

const MealForm = ({ meal, isCreate, handleSubmit, handleValChange }) => {
  return (
    <>
      <form Onsubmit = {handleSubmit}>
        <input value={} name={} onChange={} />
        <button type='submit'>{isCreate? 'Create' : 'Update'}</button>
      </form>
    </>
  );
};

export default MealForm;































    <form onSubmit={handleSubmit}>
      <input value={meal.name} name={'name'} onChange={handleValChange} />
      <button type="submit">{isCreate ? 'create meal' : 'update meal'}</button>
    </form>