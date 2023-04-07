import React from 'react';
import { Box, Divider, Typography } from '@mui/material';

const MealItem = ({ meal }) => {
  return (
    <Box sx={{ borderRadius: 2, maxWidth: 500 }}>
      <Box sx={{ display: 'flex' }}>
        <Box sx={{ flex: 2 }}>
          <Typography variant="h6">{meal.meal_name}</Typography>
          {meal.meal_name2 && (
            <Typography variant="caption">{meal.meal_name2}</Typography>
          )}
          <Typography sx={{ mt: 2 }} variant="body1">
            $ {meal.meal_price}
          </Typography>
        </Box>
        <div
          style={{
            backgroundImage: `url(${meal.meal_picture_url})`,
            width: 80,
            height: 60,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            backgroundRepeat: 'no-repeat',
          }}
        ></div>
      </Box>
      <Divider color="primary" sx={{ mt: 4 }} />
    </Box>
  );
};

const OrderItem = ({ order }) => {
  return (
    <Box
      sx={{
        m: 2,
        p: 4,
        borderRadius: 2,
        boxShadow: '1px 1px 10px 3px rgba(0,0,0,0.1)',
        maxWidth: 500,
      }}
    >
      <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
        <Typography variant="caption">Order#: {order.order_id}</Typography>
        <Typography variant="caption">
          {order.order_created_at.split('T')[0]}
        </Typography>
      </Box>
      <Typography variant="caption" alignSelf={'center'} sx={{ mt: 2 }}>
        Status:{' '}
        {order.order_status_id == 2
          ? 'Completed'
          : order.order_status_id == 1
          ? 'Pending'
          : 'Cancelled'}
      </Typography>
      <Divider color="primary" sx={{ m: 2 }} />
      {order?.meals?.map((meal) => (
        <Box sx={{ pl: 4, pt: 2, pb: 2 }}>
          <MealItem meal={meal} />
        </Box>
      ))}
    </Box>
  );
};

export default OrderItem;
