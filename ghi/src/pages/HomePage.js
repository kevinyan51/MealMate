import React, { useEffect } from 'react';
import { Box, CircularProgress } from '@mui/material';
import { useToken } from '../components/Auth';
import ChefHome from '../components/ChefHome';
import SubscriberHome from '../components/SubscriberHome';

const HomePage = () => {
  const { user } = useToken();

  return (
    <Box>
      {user && user.role_id === 2 && <ChefHome />}
      {user && user.role_id === 1 && <SubscriberHome />}
      {!user && <CircularProgress />}
    </Box>
  );
};

export default HomePage;
