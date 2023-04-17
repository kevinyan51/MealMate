import React from 'react';
import {
  Box,
  Card,
  CardHeader,
  CardMedia,
  Typography,
  Button,
} from '@mui/material';
import { Avatar } from '@mui/material';
import { IconButton } from '@mui/material';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import AddIcon from '@mui/icons-material/Add';
import RemoveIcon from '@mui/icons-material/Remove';
import { COLORS } from '../utils/constants';

const Tags = ({ tags }) => {
  const tagMap = {
    is_vegan: { text: 'Vegan', color: 'white', bgcolor: COLORS.lightGreen },
    is_keto: { text: 'Keto', color: 'black', bgcolor: COLORS.orange },
    is_chef_choice: { text: 'Chef Choice', color: 'gold', bgcolor: 'black' },
    calories: {
      text: 'Calorie Smart',
      color: 'black',
      bgcolor: COLORS.biege,
    },
  };
  const isCalorieSmart = tags.calories < 550;
  const filteredTags = Object.keys(tags).filter((tag) => {
    return tag == 'calories' || tags[tag] === true;
  });
  return (
    <Box
      sx={{
        display: 'flex',
        flexWrap: 'wrap',
        position: 'absolute',
        flexDirection: 'column',
        top: 5,
        left: 5,
      }}
    >
      {filteredTags?.map((tag) => {
        if (tag === 'calories' && !isCalorieSmart) return null;
        return (
          <Box
            key={tag}
            sx={{
              boxShadow: 1,
              mr: 1,
              mb: 1,
              color: tagMap[tag].color,
              bgcolor: tagMap[tag].bgcolor,
              borderRadius: 1,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              pl: 1,
              pr: 1,
            }}
          >
            <Typography variant="caption" sx={{ fontWeight: 900 }}>
              {tagMap[tag].text}
            </Typography>
          </Box>
        );
      })}
    </Box>
  );
};

const MealCard = ({
  meal,
  handleAdd = () => null,
  handleRemove = () => null,
  setSelectedMeal = () => null,
  setShowModal = () => null,
  simpleCard = false,
}) => {
  if (!meal) return null;
  return (
    <Card
      sx={{
        maxWidth: 345,
        mb: 4,
        height: simpleCard ? 250 : 420,
        position: 'relative',
      }}
      onClick={() => {
        setSelectedMeal(meal);
        setShowModal(true);
      }}
    >
      <CardMedia
        component="img"
        height="194"
        image={meal.picture_url}
        alt="Paella dish"
      />

      {!simpleCard && (
        <CardHeader
          avatar={
            <Box sx={{ position: 'relative' }}>
              <Avatar src={meal.chef_picture_url} aria-label="recipe">
                {meal.chef_first_name?.[0] + meal.chef_last_name?.[0]}
              </Avatar>
              <Typography
                variant="caption"
                sx={{
                  position: 'absolute',
                  bottom: -12,
                  right: 0,
                  bgcolor: 'black',
                  color: 'gold',
                  borderRadius: 1,
                  pl: 1,
                  pr: 1,
                }}
              >
                chef
              </Typography>
            </Box>
          }
          action={
            <IconButton aria-label="settings">
              <MoreVertIcon />
            </IconButton>
          }
          title={
            <Box sx={{ display: 'flex' }}>
              <Typography>
                {meal.chef_first_name + ' ' + meal.chef_last_name?.[0]}
              </Typography>
            </Box>
          }
          subheader={meal.created_at.split('T')[0]}
        />
      )}
      <Box sx={{ display: 'flex', flexDirection: 'column', ml: 2 }}>
        <Box sx={{ display: 'flex', alignItems: 'center' }}>
          {meal.is_spicy && (
            <img
              style={{ marginRight: 10 }}
              height="22"
              src="https://icons.veryicon.com/png/o/food--drinks/delicious-food-3/chili-pepper.png"
            />
          )}
          <Typography variant="h7" fontWeight="bold">
            {meal?.name?.length > 30
              ? `${meal?.name?.slice(0, meal.name.lastIndexOf(' ', 30))}...`
              : meal.name}
          </Typography>
        </Box>
        <Typography variant="caption" color="gray">
          {meal?.name2?.length > 50
            ? `${meal?.name2?.slice(0, meal.name2.lastIndexOf(' ', 50))}...`
            : meal?.name2}
        </Typography>
        {!simpleCard && (
          <Typography variant="caption" color="text.secondary">
            ${meal.price}
          </Typography>
        )}
        {/* <CardContent>
                      <Typography variant="oblique" color="text.secondary">
                        {meal.description.length > 100
                          ? meal.description.slice(0, 100) + '...'
                          : meal.description}
                      </Typography>
                    </CardContent> */}
      </Box>
      {!simpleCard && (
        <Box
          mt={2}
          mb={1}
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <Button variant="contained" onClick={() => handleAdd(meal.meal_id)}>
            <AddIcon sx={{ color: 'white' }} />
          </Button>
          <Box style={{ marginLeft: 10, marginRight: 10 }}>
            <Typography variant="h6" sx={{ m: 2 }}>
              {meal.quantity || 0}
            </Typography>
          </Box>
          <Button
            variant="contained"
            onClick={() => handleRemove(meal.meal_id)}
          >
            <RemoveIcon sx={{ color: 'white' }} />
          </Button>
        </Box>
      )}
      <Tags
        tags={{
          is_keto: meal.is_keto,
          is_vegan: meal.is_vegan,
          is_chef_choice: meal.is_chef_choice,
          calories: meal.calories,
        }}
      />
    </Card>
  );
};

export default MealCard;
