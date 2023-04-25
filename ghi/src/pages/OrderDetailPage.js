import React, { useState, useEffect } from 'react';
import OrderDetail from '../components/OrderDetail';
import { useParams } from 'react-router-dom';
import { Box } from '@mui/material';

const OrderDetailPage = () => {
  const { orderId } = useParams();
  const [order, setOrder] = useState({});
  const loadOrder = async () => {
    const url = `${process.env.REACT_APP_USER_API_HOST}/api/orders/${
      orderId ?? 3
    }`;
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setOrder(data);
    }
  };
  useEffect(() => {
    loadOrder();
  }, []);

  return (
    <Box
      sx={{ display: 'flex', justifyContent: 'center', position: 'relative' }}
    >
      <Box
        sx={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'flex-start',
          overflow: 'hidden',
          alignItems: 'center',
          position: 'absolute',
          right: 20,
          bottom: 100,
        }}
      >
        <video
          src="https://cdn.dribbble.com/userupload/4308814/file/original-27dcdfe3b29c9a6d02708e0ba50be957.mp4"
          autoPlay
          loop
          muted
          style={{ maxWidth: 400, opacity: 0.6 }}
        />
      </Box>
      <OrderDetail order={order} hasShadow={false} detailed_view={true} />
    </Box>
  );
};

export default OrderDetailPage;
