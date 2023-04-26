import React, { useEffect, useState } from 'react';
import { useToken } from '../components/Auth';
import { useNavigate } from 'react-router-dom';

function SignupPage() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [pictureUrl, setPictureUrl] = useState('');
  const [roleId, setRoleId] = useState(1);
  const [roleId, setRoleId] = useState(1);
  const { signup, token } = useToken();
  const navigate = useNavigate();

  useEffect(() => {
    if (token) {
      navigate('/');
    }
  }, [token]);

  const handleSubmit = async (event) => {
    event.preventDefault();
    // const data = {};
    // data.first_name = firstName;
    // data.last_name = lastName;
    // data.username = username;
    // data.email = email;
    // data.password = password;
    // data.picture_url = pictureUrl;
    // data.role_id = roleId;

    // const userUrl =  `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/users`;
    // const fetchConfig = {
    //   method: 'post',
    //   body: JSON.stringify(data),
    //   headers: {
    //     'Content-Type': 'application/json',
    //   },
    // };

    // const response = await fetch(userUrl, fetchConfig);
    const response = await signup({
      firstName,
      lastName,
      username,
      email,
      password,
      pictureUrl,
      roleId,
    });
    if (response.ok) {
      setFirstName('');
      setLastName('');
      setUsername('');
      setEmail('');
      setPassword('');
      setPictureUrl('');
      setRoleId(1);
      setRoleId(1);
    }
  };

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Signup</h1>
          <form onSubmit={handleSubmit}>
            <div className="form-floating mb-3">
              <input
                onChange={(e) => setFirstName(e.target.value)}
                value={firstName}
                placeholder="First Name"
                required
                type="text"
                name="firstName"
                id="firstName"
                className="form-control"
              />
              <label htmlFor="firstName">First Name</label>
            </div>

            <div className="form-floating mb-3">
              <input
                onChange={(e) => setLastName(e.target.value)}
                value={lastName}
                placeholder="Last Name"
                required
                type="text"
                name="lastName"
                id="lastName"
                className="form-control"
              />
              <label htmlFor="lastName">Last Name</label>
            </div>

            <div className="form-floating mb-3">
              <input
                onChange={(e) => setUsername(e.target.value)}
                value={username}
                placeholder="Username"
                required
                type="text"
                name="username"
                id="username"
                className="form-control"
              />
              <label htmlFor="username">Username</label>
            </div>

            <div className="form-floating mb-3">
              <input
                onChange={(e) => setEmail(e.target.value)}
                value={email}
                placeholder="Email"
                required
                type="text"
                name="email"
                id="email"
                className="form-control"
              />
              <label htmlFor="email">Email</label>
            </div>

            <div className="form-floating mb-3">
              <input
                onChange={(e) => setPassword(e.target.value)}
                value={password}
                placeholder="Password"
                required
                type="password"
                type="password"
                name="password"
                id="password"
                className="form-control"
              />
              <label htmlFor="password">Password</label>
            </div>

            <div className="form-floating mb-3">
              <select
              <select
                onChange={(e) => setPictureUrl(e.target.value)}
                value={pictureUrl}
                required
                name="pictureUrl"
                id="pictureUrl"
                className="form-select"
              >
                <option value="">Choose an avatar</option>
                <option value="https://img.freepik.com/premium-vector/african-american-woman-avatar-with-glasses-portrait-young-girl-vector-illustration-face_217290-1034.jpg?w=2000">Female Avatar</option>
                <option value="https://img.freepik.com/premium-vector/brunette-man-avatar-portrait-young-guy-vector-illustration-face_217290-1035.jpg?w=2000">Male Avatar</option>
                <option value="https://thestayathomechef.com/wp-content/uploads/2016/06/Fried-Chicken-4-1.jpg">Let me be Fried Chicken instead</option>
              </select>
              <label htmlFor="pictureUrl">Choose an Avatar</label>
            </div>

            <div className="form-check form-switch mb-3">
            <div className="form-check form-switch mb-3">
              <input
                onChange={(e) => setRoleId(e.target.checked ? 2 : 1)}
                checked={roleId === 2}
                type="checkbox"
                name="RoleId"
                onChange={(e) => setRoleId(e.target.checked ? 2 : 1)}
                checked={roleId === 2}
                type="checkbox"
                name="RoleId"
                id="roleId"
                className="form-check-input"
                className="form-check-input"
              />
              <label htmlFor="roleId" className="form-check-label">
                {roleId === 2 ? "Chef" : "Subscriber"}
              </label>
            </div>

            <button className="btn btn-primary">Create</button>
          </form>
        </div>
      </div>
    </div>
  );
}

export default SignupPage;
