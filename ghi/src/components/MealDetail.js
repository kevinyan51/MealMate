import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, Col, Container, Modal, Row } from 'react-bootstrap';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faTrash, faPen } from '@fortawesome/free-solid-svg-icons';
import { Box, Grid } from '@mui/material';
// import {
//   faSeedling,
//   faPepperHot,
//   faCheese,
//   faTrophy,
//   faListAlt,
// } from '@fortawesome/free-solid-svg-icons';
import Rating from './Rating';
import { Typography } from '@mui/material';
import ButtonModal from './ButtonModal';
import MealCard from './MealCard';
import { useParames } from 'react-router-dom';

const MealDetail = ({ mealId }) => {
  const navigate = useNavigate();
  const [meal, setMeal] = useState({});
  const mealUrl = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/meals/${mealId}`;
  const editMeal = () => {
    navigate(`/meals/${mealId}/edit`);
  };

  const deleteMeal = async () => {
    await fetch(
      `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/meals/${mealId}`,
      {
        method: 'DELETE',
      }
    );
    navigate(`/meals`);
  };
  const modalContent = {
    edit: {
      openerText: 'edit',
      confirmButtonText: 'Edit',
      title: 'Edit Meal',
      content:
        'If you edit this meal, any changes upon submission will be visible to all users.',
      confirmAction: editMeal,
      openerProps: {
        variant: 'outlined',
        sx: { fontWeight: 900 },
        color: 'primary',
      },
    },
    delete: {
      openerText: 'delete',
      confirmButtonText: 'Delete',
      title: 'Delete Meal',
      content:
        'Are you sure you want to delete the meal? This will permanently remove the meal.',
      confirmAction: deleteMeal,
      openerProps: {
        variant: 'contained',
        sx: { fontWeight: 900 },
        color: 'error',
      },
    },
  };

  const fetchMeal = async () => {
    const response = await fetch(mealUrl);
    if (!response.ok) {
      throw new Error('Error getting meal');
    }
    const data = await response.json();
    setMeal(data);
  };
  const [chefMeals, setChefMeals] = useState([]);

  useEffect(() => {
    fetchMeal();
  }, [mealId]);

  const fetchChefMeals = async (chefId) => {
    const response = await fetch(
      `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/users/${chefId}/meals`
    );
    if (!response.ok) {
      throw new Error('Error getting chef meals');
    }
    const data = await response.json();
    // console.log('meals', data);
    let cMeals = [...data.filter((m) => m.meal_id != mealId)];
    setChefMeals(cMeals.length > 5 ? cMeals.slice(0, 5) : cMeals);
  };

  useEffect(() => {
    if (meal && meal?.chef_id) {
      fetchChefMeals(meal.chef_id);
    }
  }, [meal]);

  return (
    <Container style={{ paddingTop: 50 }}>
      <Card className="mb-3">
        <Card.Header className="d-flex justify-content-between align-items-center">
          <div>
            <Card.Title as="h1" className="display-5">
              {meal.name}
            </Card.Title>
            <Card.Subtitle>{meal.name2}</Card.Subtitle>
          </div>
          <Box sx={{ display: 'flex' }}>
            <ButtonModal {...modalContent.edit} />
            <Box m={2}></Box>
            <ButtonModal {...modalContent.delete} />
          </Box>
        </Card.Header>

        <Box sx={{ display: 'flex' }}>
          <Box
            sx={{
              p: 4,
              flex: 1,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'flex-start',
            }}
          >
            <Card.Img
              src={meal.picture_url}
              style={{ width: '550px' }}
              alt="meal"
            />
            <Typography variant="h3" mt={2} mb={2}>
              Meal Average Rating:
            </Typography>
            <Rating
              name="read-only"
              value={meal.avg_rating || (4.5).toFixed(1)}
              precision={0.5}
              readOnly
            />
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
            <Typography variant="h5" alignSelf={'flex-start'} sx={{ m: 2 }}>
              Description:
            </Typography>
            <Typography m={2}>{meal.description}</Typography>
            <Typography variant="h5" alignSelf={'flex-start'} sx={{ m: 2 }}>
              Ingredients:
            </Typography>
            <Typography m={2}>{meal.ingredients}</Typography>
          </Box>
          <Box sx={{ flex: 1, p: 2 }}>
            <Typography variant="h5" mt={3} mb={3}>
              Meals You Might Like
            </Typography>
            <Grid container spacing={2}>
              {chefMeals.map((meal) => (
                <Grid item xs={12} sm={6} key={meal.meal_id}>
                  <MealCard
                    meal={meal}
                    simpleCard={true}
                    setShowModal={() => navigate('/meals/' + meal.meal_id)}
                  />
                </Grid>
              ))}
            </Grid>
          </Box>
        </Box>
        <Card.Footer>
          <small className="text-muted">${meal.price}</small>
        </Card.Footer>
      </Card>
    </Container>
  );
};

export default MealDetail;

// const EditDeleteButtons = ({ mealId }) => {
//   const navigate = useNavigate();

//   const editMeal = () => {
//     navigate(`/meals/${mealId}/edit`);
//   };

//   const deleteMeal = async () => {
//     await fetch(`${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/meals/${mealId}`, {
//       method: 'DELETE',
//     });
//     navigate(`/meals`);
//   };

//   return (
//     <div style={{ display: 'inline-block' }}>
//       <button
//         type="button"
//         className="btn btn-warning me-2"
//         data-bs-toggle="modal"
//         data-bs-target="#confirmEdit"
//       >
//         <FontAwesomeIcon icon={faPen} className="me-2" />
//         Edit
//       </button>
//       <button
//         type="button"
//         className="btn btn-danger"
//         data-bs-toggle="modal"
//         data-bs-target="#confirmDelete"
//       >
//         <FontAwesomeIcon icon={faTrash} className="me-2" />
//         Delete
//       </button>
//       <div id="confirmEdit" className="modal" tabIndex="-1">
//         <div className="modal-dialog modal-dialog-centered">
//           <div className="modal-content">
//             <div className="modal-header">
//               <h5 className="modal-title">Edit Meal</h5>
//               <button
//                 type="button"
//                 className="btn-close"
//                 data-bs-dismiss="modal"
//                 aria-label="Close"
//               ></button>
//             </div>
//             <div className="modal-body">
//               <p>
//                 If you edit this meal, any changes upon submission will be
//                 visible to all users.
//               </p>
//             </div>
//             <div className="modal-footer">
//               <button
//                 type="button"
//                 className="btn btn-secondary"
//                 data-bs-dismiss="modal"
//               >
//                 Cancel
//               </button>
//               <button
//                 onClick={editMeal}
//                 type="button"
//                 className="btn btn-danger"
//               >
//                 Edit
//               </button>
//             </div>
//           </div>
//         </div>
//       </div>
//       <div id="confirmDelete" className="modal" tabIndex="-1">
//         <div className="modal-dialog modal-dialog-centered">
//           <div className="modal-content">
//             <div className="modal-header">
//               <h5 className="modal-title">Delete Meal</h5>
//               <button
//                 type="button"
//                 className="btn-close"
//                 data-bs-dismiss="modal"
//                 aria-label="Close"
//               ></button>
//             </div>
//             <div className="modal-body">
//               <p>
//                 Are you sure you want to delete the meal? This will permanently
//                 remove the meal.
//               </p>
//             </div>
//             <div className="modal-footer">
//               <button
//                 type="button"
//                 className="btn btn-secondary"
//                 data-bs-dismiss="modal"
//               >
//                 Cancel
//               </button>
//               <button
//                 onClick={deleteMeal}
//                 type="button"
//                 className="btn btn-danger"
//               >
//                 Delete
//               </button>
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// };

{
  /* <Modal show={showModal} onHide={() => setShowModal(false)}>
        <Modal.Header closeButton>
          <Modal.Title>{meal.name}</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Card.Img
            src={meal.picture_url}
            style={{ width: '100%' }}
            alt="meal"
          />
          <div className="my-4">
            <h4 className="mb-3">Description</h4>
            <p className="fs-5">{meal.description}</p>
          </div>
          <div className="my-4">
            <h4 className="mb-3">Ingredients</h4>
            <ul className="list-group list-group-flush">{meal.ingredients}</ul>
          </div>
          <div className="my-4">
            <h4 className="mb-3">Meal Details</h4>
            <ul className="list-group list-group-flush">
              {meal.calories && (
                <li className="list-group-item">
                  <FontAwesomeIcon
                    icon={faListAlt}
                    className="text-secondary me-1"
                  />
                  {meal.calories} cal
                </li>
              )}
              {meal.is_keto && (
                <li className="list-group-item">
                  <FontAwesomeIcon
                    icon={faSeedling}
                    className="text-success me-1"
                  />
                  Keto
                </li>
              )}
              {meal.is_vegan && (
                <li className="list-group-item">
                  <FontAwesomeIcon
                    icon={faSeedling}
                    className="text-success me-1"
                  />
                  Vegan
                </li>
              )}
              {meal.is_chef_choice && (
                <li className="list-group-item">
                  <FontAwesomeIcon
                    icon={faTrophy}
                    className="text-warning me-1"
                  />
                  Chef's Choice
                </li>
              )}
              {meal.is_spicy && (
                <li className="list-group-item">
                  <FontAwesomeIcon
                    icon={faPepperHot}
                    className="text-danger me-1"
                  />
                  Spicy
                </li>
              )}
              {meal.has_cheese && (
                <li className="list-group-item">
                  <FontAwesomeIcon icon={faCheese} className="text-info me-1" />
                  Cheese
                </li>
              )}
            </ul>
          </div>
        </Modal.Body>
        <Modal.Footer>
          <small className="text-muted">${meal.price}</small>
        </Modal.Footer>
      </Modal> */
}
