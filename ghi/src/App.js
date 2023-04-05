import { createBrowserRouter, Outlet } from 'react-router-dom';
import './App.css';
import Nav from './components/Nav.js';
import MealDetail from './components/MealDetail.js';
import LandingPage from './pages/LandingPage.js';
import LoginPage from './pages/LoginPage.js';
import SignupPage from './pages/SignupPage.js';
import HomePage from './pages/HomePage.js';
import ErrorPage from './pages/ErrorPage.js';
import BoxEditPage from './pages/BoxEditPage.js';
import MealCreatePage from './pages/MealCreatePage.js';
import MealEditPage from './pages/MealEditPage.js';
import OrderListPage from './pages/OrderListPage.js';
import OrderDetailPage from './pages/OrderDetailPage.js';

const NavbarWrapper = () => {
  return (
    <>
      <Nav />
      <Outlet />
      <div style={{ height: 56 }}></div>
    </>
  );
};

const router = createBrowserRouter([
  {
    path: '/',
    element: <NavbarWrapper />,
    errorElement: <ErrorPage />,
    children: [
      { path: '', element: <LandingPage /> },
      { path: 'login', element: <LoginPage /> },
      { path: 'signup', element: <SignupPage /> },
      { path: 'home', element: <HomePage /> },
    ],
  },
  {
    path: '/my-box',
    element: <NavbarWrapper />,
    errorElement: <ErrorPage />,
    children: [{ path: '', element: <BoxEditPage /> }],
  },
  {
    path: '/my-orders',
    element: <NavbarWrapper />,
    errorElement: <ErrorPage />,
    children: [
      { path: '', element: <OrderListPage /> },
      { path: ':orderId', element: <OrderDetailPage /> },
    ],
  },
  {
    path: '/meals',
    element: <NavbarWrapper />,
    errorElement: <ErrorPage />,
    children: [
      { path: 'new', element: <MealCreatePage /> },
      { path: ':mealId', element: <MealDetail /> },
      { path: ':mealId/edit', element: <MealEditPage /> },
    ],
  },
]);

export default router;

// function App() {
//   return (
//     <BrowserRouter>
//       <Nav />
//       <div style={{ height: 56 }}></div>
//       <div className="container">
//         <Routes>
//           <Route path="/" element={<MainPage />} />
//           <Route path="/users">
//             <Route path="login" element={<LoginForm />} />
//             <Route path="signup" element={<SignupForm />} />
//           </Route>
//           <Route path="/meals">
//             <Route path="" element={<MealList />} />
//             <Route path="new" element={<MealCreateForm />} />
//             <Route path=":mealId" element={<MealDetail />} />
//           </Route>
//           <Route path="/orders">
//             <Route path=":mealId" element={<MealDetail />} />
//             <Route path=":userId" element={<UserOrderDetail />} />
//           </Route>
//         </Routes>
//       </div>
//       <footer className="fixed-bottom">
//         <div className="d-flex justify-content-center align-items-center p-2 bg-danger bg-opacity-25 text-muted">
//           Created with
//           <i
//             className="fa fa-heart-o ms-2 me-2"
//             style={{ fontSize: '1rem', color: 'red' }}
//           ></i>
//           by the Culinary Coders. All rights reserved.
//         </div>
//       </footer>
//     </BrowserRouter>
//   );
// }
// export default App;
