import React from 'react';

const OrderDetailPage = () => {
  const fetchOrder = async () => {
    const orderId = 1;
    const url = `http://localhost:3000/api/orders/${orderId}`;
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  };
  return <div>OrderDetailPage</div>;
};

export default OrderDetailPage;
