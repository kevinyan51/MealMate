import React, { useState, useEffect } from 'react';
import OrderItem from '../components/OrderItem';

const OrderListPage = () => {
  const [userId, setUserId] = useState(1);
  const [orders, setOrders] = useState([]);
  // const {
  //   user: { id: userId },
  // } = useAuth();
  const fetchUserOrders = async () => {
    const url = `http://localhost:8000/api/users/${userId}/orders`;
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setOrders(data);
      console.log(data);
    }
  };
  useEffect(() => {
    fetchUserOrders();
  }, []);
  return (
    <div>
      {/* <h1>{orders.length > 0 ? 'got data' : 'no data'}</h1> */}
      {orders.map((order) => (
        <OrderItem key={order.order_id} order={order} />
      ))}
    </div>
  );
};

export default OrderListPage;
