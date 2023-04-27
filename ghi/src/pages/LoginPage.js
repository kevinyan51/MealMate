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
  // <div className="chefvideo-container">
  //   <div className="loginform">
  //     <form onSubmit={handleLogin}>
  //       <div className="form-group">
  //         <label>Username</label>
  //         <input
  //           type="text"
  //           id="username"
  //           value={username}
  //           onChange={(e) => setUsername(e.target.value)}
  //         />
  //       </div>
  //       <div className="form-group">
  //         <label>Password</label>
  //         <input
  //           type="password"
  //           value={password}
  //           onChange={(e) => setPassword(e.target.value)}
  //         />
  //       </div>
  //       <div className="loginbutton">
  //         <button type="submit">Login</button>
  //       </div>
  //     </form>
  //     {errorMessage && <p>{errorMessage}</p>}
  //   </div>

  <div className="container mt-5">
    <div className="row">
      <div className="col-md-3">
        <h1>Login</h1>
        <form onSubmit={handleLogin}>
          <div className="mb-3">
            <label htmlFor="username" className="form-label">
              Username
            </label>
            <input
              type="text"
              className="form-control"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label htmlFor="password" className="form-label">
              Password
            </label>
            <input
              type="password"
              className="form-control"
              id="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <button type="submit" className="btn btn-primary">
            Login
          </button>
        </form>
        {errorMessage && <p>{errorMessage}</p>}
      </div>
      <div className="col-lg-6">
        <video
          src="https://cdn.dribbble.com/userupload/4308814/file/original-27dcdfe3b29c9a6d02708e0ba50be957.mp4"
          autoPlay
          loop
          muted
          style={{ maxWidth: 800, opacity: 0.6 }}
        />
      </div>
    </div>
  </div>
);
}

export default LoginPage;
