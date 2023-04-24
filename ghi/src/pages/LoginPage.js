import React, { useState, useEffect } from 'react';
import { useToken } from '../components/Auth';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const { login, token } = useToken();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      console.log('herer');
      const response = await login({ username, password });
      console.log('login data', response);
      localStorage.setItem('token', response.token);
      window.location.href = '/';

      setErrorMessage('');
    } catch (error) {
      setErrorMessage('Cannot login');
    }
  };

  useEffect(() => {
    const localToken = localStorage.getItem('token');
    if (localToken) {
      // redirect to home page
      window.location.href = '/';
    }
  }, [token]);

  return (
    <div>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
      {errorMessage && <p>{errorMessage}</p>}
    </div>
  );
}

export default Login;
