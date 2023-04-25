import React from 'react';
import ReactDOM from 'react-dom/client';
import { RouterProvider } from 'react-router-dom';
import './index.css';
import reportWebVitals from './reportWebVitals';
import router from './App';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { COLORS } from './utils/constants';
import myFonts from './theme/theme';
import { AuthProvider } from "./components/Auth.js";


const customTheme = createTheme({
  palette: {
    primary: {
      main: COLORS.primary,
      background: COLORS.backgroundLight,
    },
    secondary: {
      main: COLORS.secondary,
    },
    background: {
      default: COLORS.backgroundLight,
      secondary: COLORS.backgroundLight,
    },
  },
  ...myFonts,
});

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  // <React.StrictMode>
  <AuthProvider>
    <ThemeProvider theme={customTheme}>
      <RouterProvider router={router} />
    </ThemeProvider>
  </AuthProvider>
  // </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
