import { useSelector } from 'react-redux';
import { Outlet, Navigate } from 'react-router-dom';

const PrivateRoute = () => {
  const isLogin = useSelector((state) => state.user.isLogin);
  return isLogin ? <Outlet /> : <Navigate to="/login" />;
};

export default PrivateRoute;
