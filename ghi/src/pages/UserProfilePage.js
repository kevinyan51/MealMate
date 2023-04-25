import React, { useEffect } from 'react';
import { useToken } from '../components/Auth';

const UserProfilePage = () => {
  const { user } = useToken();
  return (
    <div>
      <h1>User Profile Page</h1>
      <div>userid: {user?.id}</div>
      <div>username: {user?.username}</div>
      <div>user firstname: {user?.firstname}</div>
      <div>user lastname: {user?.last_name}</div>
      <div>user email: {user?.email}</div>
      <div>user picture: {user?.picture_url}</div>
    </div>
  );
};

export default UserProfilePage;
