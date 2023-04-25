import React, { useState } from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import RestaurantIcon from '@mui/icons-material/Restaurant';
import { useNavigate } from 'react-router-dom';
import { useToken } from './Auth';

const pages = [
  'home',
  'my box',
  // 'meals',
  'my orders',
  'order detail',
  'new meal',
  'edit meal',
  'meal detail',
];
const pagesToRoutes = {
  login: '/login',
  signup: '/signup',
  home: '/home',
  'my box': '/my-box',
  // meals: '/meals',
  'my orders': '/my-orders',
  'order detail': '/my-orders/1',
  'new meal': '/meals/new',
  'edit meal': '/meals/1/edit',
  'meal detail': '/meals/1',
};
const settings = ['Profile', 'Dashboard', 'Logout'];

const Nav = () => {
  const { logout, user } = useToken();
  const [anchorElUser, setAnchorElUser] = useState(null);
  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseUserMenu = (item) => {
    setAnchorElUser(null);
    if (item == 'Logout') {
      console.log('logging out');
      navigate('/');
      logout();
    } else if (item === 'Profile') {
      navigate('/profile');
    } else if (item === 'Dashboard') {
      navigate('/dashboard');
    }
  };

  const navigate = useNavigate();

  return (
    <AppBar position="sticky" sx={{ height: 64 }}>
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <RestaurantIcon sx={{ display: 'flex', mr: 1 }} />
          <Typography variant="h6" noWrap sx={{ ml: 2, mr: 2, color: 'white' }}>
            MEALMATE
          </Typography>

          <Box sx={{ flexGrow: 1, display: 'flex' }}>
            {' '}
            {pages.map((page) => (
              <Button
                key={page}
                onClick={() => navigate(pagesToRoutes[page])}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                {page}
              </Button>
            ))}
          </Box>

          {user && (
            <Box sx={{ flexGrow: 0 }}>
              <Tooltip title="Open settings">
                <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                  <Avatar alt="MealMate" src={user?.picture_url} />
                </IconButton>
              </Tooltip>
              <Menu
                sx={{ mt: '45px' }}
                id="menu-appbar"
                anchorEl={anchorElUser}
                anchorOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                open={Boolean(anchorElUser)}
                onClose={handleCloseUserMenu}
              >
                {settings.map((setting) => (
                  <MenuItem
                    key={setting}
                    onClick={(_) => handleCloseUserMenu(setting)}
                  >
                    <Typography textAlign="center">{setting}</Typography>
                  </MenuItem>
                ))}
              </Menu>
            </Box>
          )}
          {!user && (
            <Box sx={{ display: 'flex' }}>
              {['signup', 'login'].map((page) => (
                <Button
                  key={page}
                  onClick={() => navigate(pagesToRoutes[page])}
                  sx={{ my: 2, color: 'white', display: 'block' }}
                >
                  {page}
                </Button>
              ))}
            </Box>
          )}
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default Nav;
