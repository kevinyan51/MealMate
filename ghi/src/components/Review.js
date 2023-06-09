import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box';
import Rating from '@mui/material/Rating';
import FavoriteIcon from '@mui/icons-material/Favorite';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import Typography from '@mui/material/Typography';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';
import Avatar from '@mui/material/Avatar';
import { grey } from '@mui/material/colors';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import { useToken } from '../components/Auth.js';
// import LandingPage from '../pages/LandingPage.js';

const RatingInput = styled(Rating)({
  '& .MuiRating-iconFilled': {
    color: '#ff6d75',
  },
  '& .MuiRating-iconHover': {
    color: '#ff3d47',
  },
});

const RatingDisplayCard = ({ review }) => {
  return (
    <Card
      sx={{
        maxWidth: 345,
        boxShadow: '1px 1px 1px 0px rgba(0,0,0,0.1)',
        borderRadius: 3,
        height: 300,
        mb: 5,
        p: 2,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        alignItems: 'center',
      }}
      elevation={0}
    >
      <CardHeader
        avatar={
          <Avatar
            // sx={{ bgcolor: grey[500] }}
            aria-label="review-avatar"
            alt={
              review.reviewer_first_name[0] + ' ' + review.reviewer_last_name[0]
            }
            src={review.picture_url}
          />
        }
        // title={
        //   review.reviewer_first_name + ' ' + review.reviewer_last_name[0] + '.'
        // }
        // subheader={review.updated_at.split('T')[0]}
      />
      <RatingInput
        defaultValue={2}
        size="small"
        getLabelText={(value) => `${value} Heart${value !== 1 ? 's' : ''}`}
        precision={1}
        icon={<FavoriteIcon fontSize="inherit" />}
        emptyIcon={<FavoriteBorderIcon fontSize="inherit" />}
        value={review.rating}
        readOnly
      />
      <CardContent>
        <Typography
          variant="body2"
          sx={{ fontStyle: 'oblique', fontFamily: 'Helvetica Neue' }}
        >
          {'" ' + review.comment + ' "'}
        </Typography>
      </CardContent>
      <Typography fontWeight="bold">
        {review.reviewer_first_name + ' ' + review.reviewer_last_name[0] + '.'}
      </Typography>
      <Typography sx={{ color: grey[500] }} variant="body2">
        {review.updated_at.split('T')[0]}
      </Typography>
    </Card>
  );
};

const RatingInputCard = ({ rating, setRating, user, mealId }) => {
  const [review, setReview] = useState('');
  const postReview = async () => {
    // FIXME ADD REVIEW POSTING FUNCTIONALITY
    const postReviewUrl = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/reviews`;
    const payload = {
      subscriber_id: user.id,
      meal_id: mealId,
      rating: rating,
      comment: review,
    };
    console.log('payload', payload);
    const response = await fetch(postReviewUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });
    if (response.ok) {
      const data = await response.json();
      console.log(data);
      setReview('');
    }
    // class ReviewIn(BaseModel):
    // subscriber_id: Optional[int]
    // meal_id: Optional[int]
    // rating: Optional[int]
    // comment: Optional[str]

    alert('review posted');
    setReview('');
  };
  return (
    <Box
      sx={{
        '& > legend': { mt: 2 },
      }}
      mb={8}
    >
      <Typography component="legend" variant="h6" fontWeight="bold" mb={2}>
        Your reviews
      </Typography>
      <RatingInput
        // name="customized-color"
        defaultValue={2}
        size="large"
        getLabelText={(value) => `${value} Heart${value !== 1 ? 's' : ''}`}
        precision={1}
        icon={<FavoriteIcon fontSize="inherit" />}
        emptyIcon={<FavoriteBorderIcon fontSize="inherit" />}
        value={rating}
        onChange={(event, newValue) => {
          setRating(newValue);
        }}
      />
      <Box
        component="form"
        sx={{
          '& > :not(style)': { m: 1, width: '25ch' },
        }}
        noValidate
        autoComplete="off"
      >
        <TextField
          id="standard-basic"
          label="Share your experience here..."
          variant="standard"
          value={review}
          onChange={(event) => {
            setReview(event.target.value);
          }}
          onKeyDown={(event) => {
            if (event.key === 'Enter') {
              event.preventDefault();
              postReview();
            }
          }}
        />
      </Box>
    </Box>
  );
};

const Review = () => {
  const { user } = useToken();
  const [rating, setRating] = useState(0);
  const [reviews, setReviews] = useState([]);
  const { mealId } = useParams();
  const loadReviews = async () => {
    const response = await fetch(
      `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/meals/${
        mealId ?? 7
      }/reviews`
    );
    if (response.ok) {
      const data = await response.json();
      setReviews(data.sort((a, b) => Math.random() - Math.random()));
    }
  };
  useEffect(() => {
    loadReviews();
  }, [mealId]);
  return (
    <Box
      sx={{
        flexGrow: 1,
        bgcolor: '#fafafa',
      }}
      align="center"
    >
      <Typography variant="h4" fontWeight="bold" align="center" p={5}>
        {!user && 'See how subscribers like this meal'}
        {user?.role_id === 1 && 'See how other subscribers like this meal'}
        {user?.role_id === 2 && 'See how your subscribers like this meal'}
      </Typography>
      {user?.role_id === 1 && (
        <RatingInputCard
          rating={rating}
          setRating={setRating}
          user={user}
          mealId={mealId}
        />
      )}
      <Grid
        container
        // spacing={{ xs: 2, sm: 2, md: 3 }}
        // sx={{ display: 'flex', justifyContent: 'center' }}
      >
        {reviews?.map((rvw) => (
          <Grid item xs={12} sm={6} md={4} key={rvw.id}>
            <RatingDisplayCard review={rvw} />
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default Review;
