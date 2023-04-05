import * as React from 'react';
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

const pages = [
  'login',
  'signup',
  'home',
  'my box',
  'meals',
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
  'my orders': '/my-orders',
  'order detail': '/my-orders/1',
  'new meal': '/meals/new',
  'edit meal': '/meals/1/edit',
  'meal detail': '/meals/1',
};
const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];

const Nav = () => {
  const [anchorElUser, setAnchorElUser] = React.useState(null);

  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const navigate = useNavigate();

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <RestaurantIcon sx={{ display: { xs: 'none', md: 'flex' }, mr: 1 }} />
          <Typography variant="h6" noWrap sx={{ ml: 2, mr: 2, color: 'white' }}>
            MEALMATE
          </Typography>

          <Box sx={{ flexGrow: 1, display: 'flex' }}>
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

          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
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
                <MenuItem key={setting} onClick={handleCloseUserMenu}>
                  <Typography textAlign="center">{setting}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default Nav;
