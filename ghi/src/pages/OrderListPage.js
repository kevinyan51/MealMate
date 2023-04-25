import React, { useState, useEffect } from 'react';
import OrderDetail from '../components/OrderDetail';
import { Box, IconButton, Typography, Button, Divider } from '@mui/material';
import {
  Home as HomeIcon,
  CheckCircle as CheckCircleIcon,
  ShoppingCart as ShoppingCartIcon,
  RestaurantMenu as RestaurantMenuIcon,
  AttachMoney as AttachMoneyIcon,
  Shop,
} from '@mui/icons-material';
import { COLORS } from '../utils/constants';
const TopRowIcons = ({ infoArray }) => {
  return (
    <Box sx={{ display: 'flex', flex: 1, justifyContent: 'space-around' }}>
      {infoArray.map(({ icon, text, number, bgcolor }) => (
        <Box sx={{ display: 'flex', alignItems: 'center' }} key={text}>
          <Button
            sx={{
              borderRadius: 4,
              mr: 2,
              height: 50,
              width: 50,
              bgcolor: bgcolor,
              '&:hover': {
                bgcolor: bgcolor,
              },
            }}
          >
            {icon()}
          </Button>
          <Box sx={{ display: 'flex', flexDirection: 'column' }}>
            <Typography variant="caption">{text}</Typography>
            <Typography variant="h6" sx={{ fontWeight: 900 }}>
              {number}
            </Typography>
          </Box>
        </Box>
      ))}
    </Box>
  );
};
const OrderList = ({ orders, selectedOrderId, setSelectedOrderId }) => {
  const colorMapping = {
    pending: COLORS.orange,
    completed: COLORS.lightGreen,
    cancelled: COLORS.red,
  };
  return (
    <Box sx={{ flex: 1 }}>
      <Typography
        variant="h5"
        sx={{ fontWeight: 400, mt: 3, mb: 3, fontWeight: 900 }}
      >
        My Order History
      </Typography>
      <table width="100%">
        <thead>
          <tr>
            <th style={{ paddingBottom: 20, fontSize: 12 }}>Order ID</th>
            <th style={{ paddingBottom: 20, fontSize: 12 }}># Meals</th>
            <th style={{ paddingBottom: 20, fontSize: 12 }}>Date</th>
            <th style={{ paddingBottom: 20, fontSize: 12 }}>Total</th>
            <th style={{ paddingBottom: 20, fontSize: 12 }}>Status</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((s) => {
            const dt = new Date(s.order_created_at);
            const date = dt.toISOString().split('T')[0];
            const time = dt.toLocaleTimeString();
            return (
              <tr
                key={s.order_id}
                style={{
                  height: 100,
                  borderBottom: '1px solid rgba(0, 0, 0, 0.1)',
                  backgroundColor:
                    selectedOrderId === s.order_id
                      ? COLORS.lightGrayBg
                      : 'white',
                }}
                onClick={() => {
                  setSelectedOrderId(s.order_id);
                }}
              >
                <td style={{ paddingLeft: 20 }}>
                  <a href={`/my-orders/${s.order_id}`}>{s.order_id}</a>
                </td>
                <td>
                  <Box>
                    <Typography>{s.num_meals}</Typography>
                    {s.num_meals >= 20 && (
                      <Typography variant="caption" color="gray">
                        free shipping
                      </Typography>
                    )}
                  </Box>
                </td>
                <td>
                  <Box>
                    <Typography>{date}</Typography>
                    <Typography variant="caption" color="gray">
                      {time}
                    </Typography>
                  </Box>
                </td>
                <td>
                  <Box>
                    <Typography>${s.total_price.toFixed(2)}</Typography>
                    <Typography variant="caption" color="gray">
                      saved ${(16 * s.num_meals - s.total_price).toFixed(2)}
                    </Typography>
                  </Box>
                </td>
                <td>
                  <Button
                    variant="contained"
                    sx={{
                      pt: 0,
                      pb: 0,
                      color: 'white',
                      fontWeight: 700,
                      borderRadius: 3,
                      bgcolor: colorMapping[s.order_status],
                      boxShadow: 'none',
                    }}
                  >
                    {s.order_status}
                  </Button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </Box>
  );
};
const OrderListPage = () => {
  const [userId, setUserId] = useState(15);
  const [orders, setOrders] = useState([]);
  // const {
  //   user: { id: userId },
  // } = useAuth();
  const fetchUserOrders = async () => {
    const url = `${process.env.REACT_APP_MEALMATE_API_HOST}/api/users/${userId}/orders`;
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
  const [selectedOrderId, setSelectedOrderId] = useState(orders[0]?.order_id);
  const [ordersInfo, setOrdersInfo] = useState([]);
  useEffect(() => {
    if (orders.length > 0) {
      setSelectedOrderId(orders[0]?.order_id);
      setOrdersInfo([
        {
          icon: () => <ShoppingCartIcon sx={{ color: 'white' }} />,
          text: 'Number of Orders',
          number: orders.length,
          bgcolor: COLORS.lightGreen,
        },
        {
          icon: () => <RestaurantMenuIcon sx={{ color: 'white' }} />,
          text: 'Meals Ordered',
          number: orders.reduce((acc, cur) => acc + cur.num_meals, 0),
          bgcolor: COLORS.orange,
        },
        {
          icon: () => <AttachMoneyIcon sx={{ color: 'white' }} />,
          text: 'Total Savings',
          number: `$${
            orders.reduce((acc, cur) => acc + cur.num_meals, 0) *
            (16 - 9.99).toFixed(2)
          }`,
          bgcolor: COLORS.red,
        },
      ]);
    }
  }, [orders]);
  return (
    <Box sx={{ p: 7 }}>
      <Box sx={{ display: 'flex' }}>
        <Box
          sx={{
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <div
            style={{
              margin: 30,
              marginTop: 10,
              backgroundImage: `url(https://cdn.dribbble.com/users/2417352/screenshots/16024017/media/28f178c6a47b54701718232f95eb5099.jpg)`,
              backgroundPosition: 'center',
              backgroundSize: 'auto 125%',
              backgroundRepeat: 'no-repeat',
              borderRadius: '50%',
              height: 180,
              width: 180,
            }}
          ></div>
          <Box sx={{ display: 'flex' }}>
            <Box sx={{ display: 'flex', alignItems: 'center' }}>
              <IconButton>
                <HomeIcon />
              </IconButton>
              <Typography variant="caption">Main street #12</Typography>
            </Box>
            <Box sx={{ display: 'flex', alignItems: 'center', ml: 2 }}>
              <IconButton>
                <CheckCircleIcon sx={{ color: COLORS.lightGreen }} />
              </IconButton>
              <Typography variant="caption">Verified Account</Typography>
            </Box>
          </Box>
        </Box>
        <TopRowIcons infoArray={ordersInfo} />
      </Box>
      <Divider color={COLORS.lightGrayBg} sx={{ mt: 3 }} />
      <Box sx={{ display: 'flex', alignItems: 'start', pt: 0 }}>
        <OrderList
          orders={orders}
          selectedOrderId={selectedOrderId}
          setSelectedOrderId={setSelectedOrderId}
        />
        <OrderDetail
          order={orders.find((el) => el.order_id === selectedOrderId)}
          hasShadow={false}
          bgcolor={COLORS.lightGrayBg}
        />
      </Box>
    </Box>
  );
};
export default OrderListPage;
