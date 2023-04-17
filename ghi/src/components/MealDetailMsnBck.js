import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Box from '@mui/material/Box';
import Rating from '@mui/material/Rating';
import Typography from '@mui/material/Typography';
import Avatar from '@mui/material/Avatar';
import { grey } from '@mui/material/colors';
import ListAltIcon from '@mui/icons-material/ListAlt';

const MealDetail = () => {
  const [meal, setMeal] = useState({});
  const id = useParams().mealId;
  const mealUrl = `http://localhost:8000/api/meals/${id}/`;

  const fetchMeal = async () => {
    const response = await fetch(mealUrl);
    if (response.ok) {
      const data = await response.json();
      setMeal(data);
    } else {
      throw new Error('error getting Meal');
    }
  };

  useEffect(() => {
    fetchMeal();
  }, []);

  return (
    <div className="container">
      <div className="card mb-3">
        <div className="card-header">
          <h1 className="card-title display-5">{meal.name}</h1>
          <h4 className="card-subtitle">{meal.name2}</h4>
        </div>
        <img
          className="card-img-top"
          src={meal.picture_url}
          style={{ width: '550px', height: '325px' }}
          alt="meal"
        />
        <div className="card-body">
          <ul className="list-group list-group-flush">
            {meal.calories && (
              <li className="list-group-item">{meal.calories} calories</li>
            )}
            {meal.is_keto && <li className="list-group-item">Keto</li>}
            {meal.is_vegan && <li className="list-group-item">Vegan</li>}
            {meal.is_chef_choice && (
              <li className="list-group-item">Chef's Choice</li>
            )}
            {meal.is_spicy && <li className="list-group-item">Spicy</li>}
            {meal.has_cheese && <li className="list-group-item">Cheese</li>}
          </ul>
          <small className="text-muted">
            by {meal.first_name} {meal.last_name}
          </small>
          <div className="card-footer">
            <small className="text-muted">${meal.price}</small>
          </div>
        </div>
      </div>

      <div className="card-body">
        <div className="row">
          <div className="col-sm-6">
            <p className="card-text">
              <small className="text-muted">
                by {meal.first_name} {meal.last_name}
              </small>
            </p>
            <ul className="list-group list-group-flush">...</ul>
          </div>
          <div className="col-sm-6">
            <div className="text-end">
              <Rating
                name="read-only"
                value={meal.rating}
                precision={0.5}
                readOnly
              />
            </div>
          </div>
        </div>
      </div>

      <div className="card">
        <p className="card-text"> {meal.description} </p>
        <p className="card-text"> {meal.ingredients} </p>
      </div>
    </div>
  );
};

export default MealDetail;
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Box from '@mui/material/Box';
import Rating from '@mui/material/Rating';
import Typography from '@mui/material/Typography';
import Avatar from '@mui/material/Avatar';
import { grey } from '@mui/material/colors';
import ListAltIcon from '@mui/icons-material/ListAlt';

const MealDetail = () => {
  const [meal, setMeal] = useState({});
  const id = useParams().mealId;
  const mealUrl = `http://localhost:8000/api/meals/${id}/`;

  const fetchMeal = async () => {
    const response = await fetch(mealUrl);
    if (response.ok) {
      const data = await response.json();
      setMeal(data);
    } else {
      throw new Error('error getting Meal');
    }
  };

  useEffect(() => {
    fetchMeal();
  }, []);

  return (
    <div className="container">
      <div className="card mb-3">
        <div className="card-header">
          <h1 className="card-title display-5">{meal.name}</h1>
          <h4 className="card-subtitle">{meal.name2}</h4>
        </div>
        <img
          className="card-img-top"
          src={meal.picture_url}
          style={{ width: '550px', height: '325px' }}
          alt="meal"
        />
        <div className="card-body">
          <ul className="list-group list-group-flush">
            {meal.calories && (
              <li className="list-group-item">{meal.calories} calories</li>
            )}
            {meal.is_keto && <li className="list-group-item">Keto</li>}
            {meal.is_vegan && <li className="list-group-item">Vegan</li>}
            {meal.is_chef_choice && (
              <li className="list-group-item">Chef's Choice</li>
            )}
            {meal.is_spicy && <li className="list-group-item">Spicy</li>}
            {meal.has_cheese && <li className="list-group-item">Cheese</li>}
          </ul>
          <small className="text-muted">
            by {meal.first_name} {meal.last_name}
          </small>
          <div className="card-footer">
            <small className="text-muted">${meal.price}</small>
          </div>
        </div>
      </div>

      <div className="card-body">
        <div className="row">
          <div className="col-sm-6">
            <p className="card-text">
              <small className="text-muted">
                by {meal.first_name} {meal.last_name}
              </small>
            </p>
            <ul className="list-group list-group-flush">...</ul>
          </div>
          <div className="col-sm-6">
            <div className="text-end">
              <Rating
                name="read-only"
                value={meal.rating}
                precision={0.5}
                readOnly
              />
            </div>
          </div>
        </div>
      </div>

      <div className="card">
        <p className="card-text"> {meal.description} </p>
        <p className="card-text"> {meal.ingredients} </p>
      </div>
    </div>
  );
};

export default MealDetail;
