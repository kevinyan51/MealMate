import React from 'react';
import { Box, Divider, Typography } from '@mui/material';
import male_chef from '../assets/images/male_chef.png';


const OrderItem = ({ meal }) => {
  return (
    <Box sx={{ borderRadius: 2, maxWidth: 700 }}>
      <Box sx={{ display: 'flex' }}>
        <div
          style={{
            flex: 1,
            backgroundImage: `url(${meal.meal_picture_url})`,
            width: 90,
            height: 90,
            borderRadius: 10,
            boxShadow: '1px 1px 10px 3px rgba(0,0,0,0.1)',
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            backgroundRepeat: 'no-repeat',
            marginRight: 10,
          }}
        ></div>
        <Box sx={{ flex: 3, ml: 3 }}>
          <Typography variant="h6">{meal.meal_name}</Typography>
          {meal.meal_name2 && (
            <Typography variant="caption" color="gray">
              {meal.meal_name2}
            </Typography>
          )}
          <Typography sx={{ mt: 2 }} variant="body1">
            $ {meal.meal_price}
          </Typography>
        </Box>
        <Box sx={{ flex: 1, ml: 3 }}>
          <Typography variant="h6">
            {meal.quantity} {meal.quantity > 1 ? 'items' : 'item'}
          </Typography>
        </Box>
      </Box>
      <Divider color="primary" sx={{ mt: 4 }} />
    </Box>
  );
};

const OrderDetail = ({ order, hasShadow = false, bgcolor = 'white' }) => {
  return (
    <Box
      sx={{
        display: 'flex',
        m: hasShadow ? 2 : 0,
        p: 4,
        borderRadius: hasShadow ? 2 : 0,
        boxShadow: hasShadow ? '1px 1px 10px 3px rgba(0,0,0,0.1)' : 'none',
        bgcolor: bgcolor,
        // width: '100%',
      }}
    >
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          // justifyContent: 'space-between',
          width: '50%',
        }}
      >
        <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
          <Typography variant="caption">Order#: {order?.order_id}</Typography>
          <Typography variant="caption">
            {order?.order_created_at?.split('T')[0]}
          </Typography>
        </Box>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', mt: 0.5 }}>
          <Typography variant="caption">
            Order Total: ${order?.total_price?.toFixed(2)}
          </Typography>
        </Box>
        <Typography variant="caption" sx={{ mt: 2 }}>
          Status: {order?.order_status}
        </Typography>
        <Divider color="primary" sx={{ m: 2 }} />
        {order?.meals?.map((meal, idx) => (
          <Box key={idx} sx={{ pl: 4, pt: 2, pb: 2 }}>
            <OrderItem meal={meal} />
          </Box>
        ))}
      </Box>
    </Box>
  );
};

export default OrderDetail;
