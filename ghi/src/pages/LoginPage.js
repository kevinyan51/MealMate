import { useState, useEffect } from 'react';
import { useToken } from '../components/Auth';
import { useNavigate } from 'react-router-dom';

function LoginPage() {
  const { login, token } = useToken();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await login(username, password);
      localStorage.setItem('token', response);
      setErrorMessage('');
    } catch (error) {
      setErrorMessage('Cannot login');
    }
  };

  useEffect(() => {
    // const token = localStorage.getItem('token');
    if (token) {
      // redirect to home page
      navigate('/');
      // window.location.href = '/';
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

export default LoginPage;
