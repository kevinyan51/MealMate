import React, { useState, useEffect } from 'react';
import { Box, Button, Typography } from '@mui/material';
import male_chef from '../assets/images/male_chef.png';

const MealCreatePage = ({
  title = 'Create a New Meal',
  buttonText = 'Create Meal',
  mealIn = null,
  buttonAction = null,
}) => {
  const [chef, setChef] = useState('');
  const [name, setName] = useState('');
  const [name2, setName2] = useState('');
  const [picture_url, setPicture_URL] = useState('');
  const [description, setDescription] = useState('');
  const [instruction, setInstruction] = useState('');
  const [ingredient, setIngredient] = useState('');
  const [calorie, setCalorie] = useState('');
  const [keto, setKeto] = useState('');
  const [vegan, setVegan] = useState('');
  const [choice, setChoice] = useState('');
  const [spicy, setSpicy] = useState('');
  const [cheese, setCheese] = useState('');
  const [price, setPrice] = useState(9.99);

  useEffect(() => {
    if (mealIn) {
      setChef(mealIn.chef_id);
      setName(mealIn.name);
      setName2(mealIn.name2);
      setPicture_URL(mealIn.picture_url);
      setDescription(mealIn.description);
      setInstruction(mealIn.instructions);
      setIngredient(mealIn.ingredients);
      setCalorie(mealIn.calories);
      setKeto(mealIn.is_keto);
      setVegan(mealIn.is_vegan);
      setChoice(mealIn.is_chef_choice);
      setSpicy(mealIn.is_spicy);
      setCheese(mealIn.has_cheese);
      setPrice(mealIn.price);
    }
  }, [mealIn]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {};
    data.chef_id = chef;
    data.name = name;
    data.name2 = name2;
    data.picture_url = picture_url;
    data.description = description;
    data.instructions = instruction;
    data.ingredients = ingredient;
    data.calories = calorie;
    data.is_keto = keto;
    data.is_vegan = vegan;
    data.is_chef_choice = choice;
    data.is_spicy = spicy;
    data.has_cheese = cheese;
    data.price = price;
    if (buttonAction) {
      return buttonAction(data);
    }
    const mealUrl = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/meals/`;
    const fetchConfig = {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
      },
    };
    const response = await fetch(mealUrl, fetchConfig);
    if (response.ok) {
      const newMeal = await response.json();
      setChef('');
      setName('');
      setName2('');
      setPicture_URL('');
      setDescription('');
      setInstruction('');
      setIngredient('');
      setCalorie('');
      setKeto('');
      setVegan('');
      setChoice('');
      setSpicy('');
      setCheese('');
      setPrice(9.99);
    }
  };

  return (
    <Box sx={{ display: 'flex', height: '100%' }}>
      <Box
        sx={{
          flex: 1,
          flexGrow: 1,
          height: 'calc(100vh - 64px)',
          width: '100%',
          bgcolor: '#FEE2CA',
          justifyContent: 'center',
          position: 'relative',
          p: 10,
          backgroundImage: `url(${male_chef})`,
          backgroundPosition: 'center',
          backgroundSize: 'cover',
          backgroundRepeat: 'no-repeat',
        }}
      >
        <Typography
          variant="h1"
          sx={{
            mt: 2,
            mb: 6,
            bgcolor: 'rgba(255, 255, 255, 0.3)',
            p: 2,
          }}
        >
          Share Your Passion for Cooking with the World
        </Typography>
        <Typography
          variant="h3"
          sx={{
            mt: 2,
            mb: 6,
            bgcolor: 'rgba(255, 255, 255, 0.3)',
            p: 2,
          }}
        >
          Create a Meal that Will Make Your Subscribers Smile!
        </Typography>

        {/* <img
          src={male_chef}
          style={{
            width: '40vw',
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            zIndex: 0,
          }}
        /> */}
        {/* <video
          style={{
            zIndex: '-1',
            width: '400px',
            marginTop: '3vh',
          }}
          autoPlay
          muted
          src={video}
          alt="female chef cooking"
          loop
        ></video> */}
      </Box>
      <Box
        sx={{
          flex: 1,
          p: 4,
          maxHeight: 'calc(100vh - 64px)',
          overflow: 'scroll',
        }}
      >
        <Box>
          <Box>
            <form
              onSubmit={
                buttonAction
                  ? (e) => {
                      e.preventDefault();
                      const data = {};
                      data.chef_id = chef;
                      data.name = name;
                      data.name2 = name2;
                      data.picture_url = picture_url;
                      data.description = description;
                      data.instructions = instruction;
                      data.ingredients = ingredient;
                      data.calories = calorie;
                      data.is_keto = keto;
                      data.is_vegan = vegan;
                      data.is_chef_choice = choice;
                      data.is_spicy = spicy;
                      data.has_cheese = cheese;
                      data.price = price;
                      buttonAction(data);
                    }
                  : handleSubmit
              }
            >
              <Typography variant="h3" sx={{ mt: 2, mb: 2 }}>
                {title}
                {/* Create a New Meal */}
              </Typography>
              <Typography
                variant="body2"
                sx={{
                  mt: 2,
                  mb: 2,
                  color: 'text.secondary',
                }}
              >
                These information below are required to create a new meal to
                display to subscribers.
              </Typography>
              <Box className="form-floating mb-3">
                <input
                  value={chef}
                  onChange={(event) => setChef(event.target.value)}
                  id="chef_id"
                  placeholder="chef_id"
                  required
                  type="text"
                  className="form-control"
                />
                <label>Chef ID</label>
              </Box>
              <Box className="form-floating mb-3">
                <input
                  value={name}
                  onChange={(event) => setName(event.target.value)}
                  id="name"
                  placeholder="name"
                  required
                  type="text"
                  className="form-control"
                />
                <label>Meal Name</label>
              </Box>
              <Box className="form-floating mb-3">
                <input
                  value={name2}
                  onChange={(event) => setName2(event.target.value)}
                  id="name2"
                  placeholder="name2"
                  required
                  type="text"
                  className="form-control"
                />
                <label>Meal Subtitle</label>
              </Box>
              <Box className="form-floating mb-3">
                <input
                  onChange={(event) => setPicture_URL(event.target.value)}
                  value={picture_url}
                  placeholder="picture_url"
                  required
                  type="text"
                  name="picture_url"
                  id="picture_url"
                  className="form-control"
                />
                <label htmlFor="picture_url">Picture URL</label>
              </Box>
              <Box className="form-floating mb-3">
                <input
                  onChange={(event) => setCalorie(event.target.value)}
                  value={calorie}
                  id="calories"
                  placeholder="calories"
                  required
                  type="number"
                  className="form-control"
                />
                <label>Calories</label>
              </Box>
              <Box className="form-floating mb-3">
                <textarea
                  onChange={(event) => setDescription(event.target.value)}
                  value={description}
                  className="form-control"
                  id="description"
                  name="description"
                  rows="15"
                ></textarea>
                <label className="form-label">Description</label>
              </Box>
              <Box className="form-floating mb-3">
                <textarea
                  onChange={(event) => setInstruction(event.target.value)}
                  value={instruction}
                  className="form-control"
                  id="instructions"
                  name="instructions"
                  rows="15"
                ></textarea>
                <label className="form-label">Instructions</label>
              </Box>
              <Box className="form-floating mb-3">
                <textarea
                  onChange={(event) => setIngredient(event.target.value)}
                  value={ingredient}
                  className="form-control"
                  id="ingredients"
                  name="ingredients"
                  rows="15"
                ></textarea>
                <label className="form-label">Ingredients</label>
              </Box>

              <Box className="form-check form-switch mb-3">
                <input
                  checked={keto}
                  onChange={(event) => setKeto(event.target.checked)}
                  id="is_keto"
                  type="checkbox"
                  className="form-check-input"
                />
                <label className="form-check-label" htmlFor="is_keto">
                  Keto
                </label>
              </Box>
              <Box className="form-check form-switch mb-3">
                <input
                  checked={vegan}
                  onChange={(event) => setVegan(event.target.checked)}
                  id="is_vegan"
                  type="checkbox"
                  className="form-check-input"
                />
                <label className="form-check-label" htmlFor="is_vegan">
                  Vegan
                </label>
              </Box>
              <Box className="form-check form-switch mb-3">
                <input
                  checked={choice}
                  onChange={(event) => setChoice(event.target.checked)}
                  id="is_chef_choice"
                  type="checkbox"
                  className="form-check-input"
                />
                <label className="form-check-label" htmlFor="is_chef_choice">
                  Chef Choice
                </label>
              </Box>
              <Box className="form-check form-switch mb-3">
                <input
                  checked={spicy}
                  onChange={(event) => setSpicy(event.target.checked)}
                  id="is_spicy"
                  type="checkbox"
                  className="form-check-input"
                />
                <label className="form-check-label" htmlFor="is_spicy">
                  Spicy
                </label>
              </Box>
              <Box className="form-check form-switch mb-3">
                <input
                  checked={cheese}
                  onChange={(event) => setCheese(event.target.checked)}
                  id="has_cheese"
                  type="checkbox"
                  className="form-check-input"
                />
                <label className="form-check-label" htmlFor="has_cheese">
                  Has Cheese
                </label>
              </Box>
              <Box className="form-floating mb-3">
                <input
                  value={price}
                  onChange={(event) => setPrice(event.target.value)}
                  id="has_cheese"
                  placeholder="has_cheese"
                  type="number"
                  className="form-control"
                />
                <label>Price</label>
              </Box>
              <Button
                variant="contained"
                sx={{
                  color: 'white',
                  fontWeight: 700,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                }}
                type="submit"
              >
                <Typography variant="h6">{buttonText}</Typography>
              </Button>
            </form>
          </Box>
        </Box>
      </Box>
    </Box>
  );
};

export default MealCreatePage;
