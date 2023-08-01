import {Navigate,createBrowserRouter} from 'react-router-dom';
import Login from "./login";
import Register from "./register";

export const router = createBrowserRouter([
    {
      path: '/',
      element: <Navigate to={'/login'} replace />,
    },
    {
      path: '/login',
      element: <Login />,
    },
    {
      path: '/register',
      element: <Register />,
    },
  ]);
  