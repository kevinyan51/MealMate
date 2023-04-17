import React, { useState, useEffect } from 'react';
import OrderDetail from '../components/OrderDetail';
import { useParams } from 'react-router-dom';

const OrderDetailPage = () => {
  const { orderId } = useParams();
  const [order, setOrder] = useState({});
  const loadOrder = async () => {
    const url = `http://localhost:8000/api/orders/${orderId ?? 3}`;
    const response = await fetch(url);
    if (response.ok) {
      const data = await response.json();
      setOrder(data);
    }
  };
  useEffect(() => {
    loadOrder();
  }, []);

  return <OrderDetail order={order} />;
};

export default OrderDetailPage;
