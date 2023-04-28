import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Box, } from '@mui/material';
import {  Col, Container, Row,  Carousel } from 'react-bootstrap';
import { Typography } from '@mui/material';
import { COLORS } from '../utils/constants';


const ChefDetailPage = () => {
  const [meals, setMeals] = useState([]);
  const userid = useParams().userId;

  const mealUrl = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/users/${userid}/meals/`;

  const fetchMeals = async () => {
    const response = await fetch(mealUrl);
    if (response.ok) {
      const mealData = await response.json();
      setMeals(mealData);
    } else {
      throw new Error('error getting Meals');
    }
  };

  useEffect(() => {
    fetchMeals();
  }, []);


return (
  <div>
    <div class="d-flex justify-content-center">
      <div class="mx-auto text-center" style={{ position: 'relative', marginBottom: '40px', paddingBottom: '30px' }}>
        <div style={{ paddingBottom: '30px' }}>
        <h1> Chef Profile</h1>
        </div>
        <h3>{meals[0]?.chef_first_name} {meals[0]?.chef_last_name}</h3>
        <img src={meals[0]?.chef_picture_url} alt="user profile" className="rounded-circle img-thumbnail" style={{ height: "150px", width: "150px", marginBottom: "20px" }}/>
      </div>
    </div>
    <div style={{ backgroundColor: COLORS.lightGreen , paddingTop: '20px', paddingBottom: '20px' }}>
    <Container>
      <Row className="justify-content-center">
        <Col>
          <h1 className="text-center mb-4">Meals by this chef:</h1>
          <Box display="flex" justifyContent="center">
          <Carousel className="mx-auto" indicators={false} control-prev-icon={false} control-next-icon={false}>
            {meals.map((meal) => (
              <Carousel.Item key={meal.meal_id} className="text-center">
                <div>
                  <h4>{meal.name}</h4>
                    <img src={meal.picture_url} alt={meal.name} style={{ height: "150px", width: "250px", objectFit: "cover" }} />
                  <Typography m={2}>
                    {meal.calories && (
                      <span className="badge bg-secondary me-1">
                        {meal.calories} cal
                      </span>
                    )}
                    {meal.is_keto && (
                      <span className="badge bg-success me-1">Keto</span>
                    )}
                    {meal.is_vegan && (
                      <span className="badge bg-primary me-1">Vegan</span>
                    )}
                    {meal.is_chef_choice && (
                      <span className="badge bg-warning text-dark me-1">
                        Chef's Choice
                      </span>
                    )}
                    {meal.is_spicy && (
                      <span className="badge bg-danger me-1">Spicy</span>
                    )}
                    {meal.has_cheese && (
                      <span className="badge bg-info text-dark me-1">Cheese</span>
                    )}
                  </Typography>
                </div>
              </Carousel.Item>
            ))}
          </Carousel>
        </Box>
        </Col>
      </Row>

    </Container>
    </div>
  </div>
  );
};

export default ChefDetailPage;
