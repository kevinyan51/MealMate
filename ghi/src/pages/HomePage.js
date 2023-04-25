import React, { useEffect } from 'react';
import { Box, CircularProgress } from '@mui/material';
import { useToken } from '../components/Auth';
import ChefHome from '../components/ChefHome';
import SubscriberHome from '../components/SubscriberHome';
import { useNavigate } from 'react-router-dom';
import LandingPage from './LandingPage';

const HomePage = () => {
  const { user } = useToken();
  const navigate = useNavigate();
  useEffect(() => {
    if (!user) {
      navigate('/');
    }
  }, [user]);

  return (
    <Box>
      {user && user.role_id === 2 && <ChefHome />}
      {user && user.role_id === 1 && <SubscriberHome />}
      {!user && <LandingPage />}
    </Box>
  );
};

export default HomePage;
