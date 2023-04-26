import React, { useEffect, useState } from 'react';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
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

const BoxEditPage = () => {
  const navigate = useNavigate();
  const [box, setBox] = useState({});
  const [showModal, setShowModal] = useState(false);

  const getAllMeals = async () => {
    const url = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/meals/`;
    const response = await fetch(url).catch((e) => {
      console.log('error getting all meals', e);
    });
    if (response.ok) {
      const data = await response.json();
      return data;
    }
    console.log('error getting all meals');
    return [];
  };
  const handleAdd = (mealId) => {
    const newBox = { ...box };
    let meals = [...newBox.meals];
    meals = meals.map((meal) => {
      meal = { ...meal };
      if (meal.meal_id === mealId) {
        if (meal.quantity < 10) meal.quantity += 1;
      }
      return meal;
    });
    setBox({ ...newBox, meals });
  };
  const handleRemove = (mealId) => {
    const newBox = { ...box };
    let meals = [...newBox.meals];
    meals = meals.map((meal) => {
      meal = { ...meal };
      if (meal.meal_id === mealId) {
        if (meal.quantity > 0) meal.quantity -= 1;
      }
      return meal;
    });
    setBox({ ...newBox, meals });
  };

  const [userId, setUserId] = useState(null);
  const [boxId, setBoxId] = useState(null);

  const getUserBox = async () => {
    if (!userId) setUserId(1);
    const url = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/users/${
      userId || 1
    }/box_id/`;
    console.log('url', url);
    const response = await fetch(url).catch((e) => {
      console.log('error getting user box', e);
    });
    if (response.ok) {
      const data = await response.json();
      setBoxId(data);
      await getOneBox(data);
    }
  };
  useEffect(() => {
    getUserBox();
  }, []);
  const [selectedMeal, setSelectedMeal] = useState(null);

  const getOneBox = async () => {
    const url = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/boxes/${
      boxId || 1
    }/`;
    const response = await fetch(url).catch((e) => {
      console.log('error getting one box', e);
    });
    const allMeals = await getAllMeals();

    if (response.ok) {
      const data = await response.json();
      data.meals = allMeals.map((meal) => {
        const mealInBox = data.meals.find(
          (mealInBox) => mealInBox.meal_id === meal.meal_id
        );
        if (mealInBox) {
          return { ...meal, quantity: mealInBox.quantity };
        }
        return { ...meal, quantity: 0 };
      });
      setBox(data);
    }
  };
  const saveBox = async () => {
    const url = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/boxes/${boxId}/`;
    let meals = [...box.meals.filter((meal) => meal.quantity > 0)];
    const response = await fetch(url, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ ...box, meals }),
    }).catch((e) => {
      console.log('error saving box', e);
    });
    if (response.ok) {
      return console.log('success');
    }
    console.log('error');
  };

  useEffect(() => {
    if (boxId) getOneBox();
  }, [boxId]);

  return (
    <Box p={4}>
      <Typography variant="h1" sx={{ mb: 2 }}>
        My Meal Box
      </Typography>
      <Box mb={2} mr={2} sx={{ display: 'flex', justifyContent: 'flex-end' }}>
        <Button variant="outlined" onClick={saveBox} sx={{ mr: 2 }}>
          save box
        </Button>
        <Button variant="contained" sx={{ color: 'white' }}>
          order now
        </Button>
      </Box>
      <Grid container spacing={2}>
        {box?.meals?.map((meal) => {
          return (
            <Grid item xs={12} sm={6} md={4} lg={3} xl={3} key={meal.meal_id}>
              <MealCard
                meal={meal}
                handleAdd={handleAdd}
                handleRemove={handleRemove}
                setSelectedMeal={setSelectedMeal}
                setShowModal={setShowModal}
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
              <BModal.Title>{selectedMeal?.name}</BModal.Title>
            </BModal.Header>
            <IconButton
              onClick={() => navigate(`/meals/${selectedMeal.meal_id}`)}
            >
              <MoreVert />
            </IconButton>
          </Box>
          <BModal.Body>
            <BCard.Img
              src={selectedMeal?.picture_url}
              style={{ width: '100%' }}
              alt="selectedMeal?"
            />
            <div className="my-4">
              <h4 className="mb-3">Description</h4>
              <p className="fs-5">{selectedMeal?.description}</p>
            </div>
            <div className="my-4">
              <h4 className="mb-3">Ingredients</h4>
              <ul className="list-group list-group-flush">
                {selectedMeal?.ingredients}
              </ul>
            </div>
            <div className="my-4">
              <h4 className="mb-3">Meal Details</h4>
              <ul className="list-group list-group-flush">
                {selectedMeal?.calories && (
                  <li className="list-group-item">
                    <FontAwesomeIcon
                      icon={faListAlt}
                      className="text-secondary me-1"
                    />
                    {selectedMeal?.calories} cal
                  </li>
                )}
                {selectedMeal?.is_keto && (
                  <li className="list-group-item">
                    <FontAwesomeIcon
                      icon={faSeedling}
                      className="text-success me-1"
                    />
                    Keto
                  </li>
                )}
                {selectedMeal?.is_vegan && (
                  <li className="list-group-item">
                    <FontAwesomeIcon
                      icon={faSeedling}
                      className="text-success me-1"
                    />
                    Vegan
                  </li>
                )}
                {selectedMeal?.is_chef_choice && (
                  <li className="list-group-item">
                    <FontAwesomeIcon
                      icon={faTrophy}
                      className="text-warning me-1"
                    />
                    Chef's Choice
                  </li>
                )}
                {selectedMeal?.is_spicy && (
                  <li className="list-group-item">
                    <FontAwesomeIcon
                      icon={faPepperHot}
                      className="text-danger me-1"
                    />
                    Spicy
                  </li>
                )}
                {selectedMeal?.has_cheese && (
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
            <small className="text-muted">${selectedMeal?.price}</small>
          </BModal.Footer>
        </Box>
      </Modal>
    </Box>
  );
};

export default BoxEditPage;
