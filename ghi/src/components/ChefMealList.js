import React, { useEffect, useState } from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Modal from '@mui/material/Modal';
import { Card as BCard, Modal as BModal } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import {
  faSeedling,
  faPepperHot,
  faCheese,
  faTrophy,
  faListAlt,
} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import MealCard from '../components/MealCard';
import { IconButton, Typography } from '@mui/material';
import { MoreVert } from '@mui/icons-material';
import { useToken } from '../components/Auth';

const ChefMealList = () => {
  const { user } = useToken();
  const navigate = useNavigate();
  const [showModal, setShowModal] = useState(false);
  const [meals, setMeals] = useState([]);
  const [meal, setMeal] = useState({});

  const getChefAllMeals = async () => {
    const url = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/users/${user?.id}/meals`;
    const response = await fetch(url).catch((e) => {
      // console.log('error getting all meals', e);
    });
    if (response.ok) {
      const data = await response.json();
      console.log('data', data);
      setMeals(data);
    }
    // console.log('error getting all meals');
    return [];
  };

  useEffect(() => {
    getChefAllMeals();
  }, []);

  return (
    <Box p={4}>
      <Typography variant="h1" sx={{ mb: 2 }}>
        All Meals Created By You As A Chef
      </Typography>
      <Grid container spacing={2}>
        {meals?.map((m) => {
          return (
            <Grid item xs={12} sm={6} md={4} lg={3} xl={3} key={m.meal_id}>
              <MealCard
                meal={m}
                // handleAdd={handleAdd}
                // handleRemove={handleRemove}
                setSelectedMeal={setMeal}
                setShowModal={setShowModal}
                simpleCard={true}
              />
            </Grid>
          );
        })}
      </Grid>
      <Modal open={showModal} onClose={() => setShowModal(false)}>
        <Box
          sx={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            bgcolor: 'background.paper',
            backgroundColor: 'transparent',
            boxShadow: 24,
            p: 4,
            backgroundColor: 'white',
            opacity: 0.95,
            maxHeight: '90vh',
            overflow: 'scroll',
          }}
        >
          <Box
            sx={{
              mb: 1,
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
            }}
          >
            <BModal.Header>
              <BModal.Title>{meal?.name}</BModal.Title>
            </BModal.Header>
            <IconButton onClick={() => navigate(`/meals/${meal.meal_id}`)}>
              <MoreVert />
            </IconButton>
          </Box>
          <BModal.Body>
            <BCard.Img
              src={meal?.picture_url}
              style={{ width: '100%' }}
              alt="meal?"
            />
            <div className="my-4">
              <h4 className="mb-3">Description</h4>
              <p className="fs-5">{meal?.description}</p>
            </div>
            <div className="my-4">
              <h4 className="mb-3">Ingredients</h4>
              <ul className="list-group list-group-flush">
                {meal?.ingredients}
              </ul>
            </div>
            <div className="my-4">
              <h4 className="mb-3">Meal Details</h4>
              <ul className="list-group list-group-flush">
                {meal?.calories && (
                  <li className="list-group-item">
                    <FontAwesomeIcon
                      icon={faListAlt}
                      className="text-secondary me-1"
                    />
                    {meal?.calories} cal
                  </li>
                )}
                {meal?.is_keto && (
                  <li className="list-group-item">
                    <FontAwesomeIcon
                      icon={faSeedling}
                      className="text-success me-1"
                    />
                    Keto
                  </li>
                )}
                {meal?.is_vegan && (
                  <li className="list-group-item">
                    <FontAwesomeIcon
                      icon={faSeedling}
                      className="text-success me-1"
                    />
                    Vegan
                  </li>
                )}
                {meal?.is_chef_choice && (
                  <li className="list-group-item">
                    <FontAwesomeIcon
                      icon={faTrophy}
                      className="text-warning me-1"
                    />
                    Chef's Choice
                  </li>
                )}
                {meal?.is_spicy && (
                  <li className="list-group-item">
                    <FontAwesomeIcon
                      icon={faPepperHot}
                      className="text-danger me-1"
                    />
                    Spicy
                  </li>
                )}
                {meal?.has_cheese && (
                  <li className="list-group-item">
                    <FontAwesomeIcon
                      icon={faCheese}
                      className="text-info me-1"
                    />
                    Cheese
                  </li>
                )}
              </ul>
            </div>
          </BModal.Body>
          <BModal.Footer>
            <small className="text-muted">${meal?.price}</small>
          </BModal.Footer>
        </Box>
      </Modal>
    </Box>
  );
};

export default ChefMealList;
