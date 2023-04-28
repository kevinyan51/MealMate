import React, { useEffect, useState } from 'react';
import { useToken } from '../components/Auth';
import { Container, Row, Col } from 'react-bootstrap';
// import { Avatar } from '@mui/material';
// import { useNavigate } from 'react-router-dom';

const UserProfilePage = () => {
  const { user } = useToken();
  // const navigate = useNavigate();

  const [selectedAvatar, setSelectedAvatar] = useState('');
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [emailValid, setEmailValid] = useState(true);
  const [success, setSuccess] = useState(false);

  const [avatarOptions, setAvatarOptions] = useState([
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Boy_headphones_lti3xz.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Woman_j4rs6u.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Woman_muslim_jf0peb.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Astronaut_dlwnxg.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Afroamerican_lb2kxl.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Scientist_kqoouj.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Girl_zj4ylc.png',
  ]);
  useEffect(() => {
    if (user) {
      setFirstName(user.first_name);
      setLastName(user.last_name);
      setEmail(user.email);
      if (user.picture_url) {
        setSelectedAvatar(user.picture_url);
      } else {
        setSelectedAvatar(avatarOptions[0]);
      }
    }
  }, [user]);

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
    setEmailValid(event.target.checkValidity());
  };

  const handleFirstNameChange = (event) => {
    setFirstName(event.target.value);
  };

  const handleLastNameChange = (event) => {
    setLastName(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const payload = {
      first_name: firstName,
      last_name: lastName,
      username: user?.username,
      email,
      password,
      picture_url: selectedAvatar,
      role_id: user?.role_id,

      // class UserIn(BaseModel):
      // first_name: str
      // last_name: str
      // username: str
      // email: str
      // password: str
      // picture_url: str
      // role_id: int
    };

    try {
      const updateUserUrl = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/users/${user?.id}`;
      const formData = new FormData();
      formData.append('first_name', firstName);
      formData.append('last_name', lastName);
      formData.append('username', user?.username);
      formData.append('email', email);
      formData.append('password', password);
      formData.append('picture_url', selectedAvatar);
      formData.append('role_id', user?.role_id);
      console.log('payload', payload);
      const response = await fetch(updateUserUrl, {
        method: 'PUT',
        headers: {
          // credentials: 'include',
          'Content-Type': 'application/json',
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
        body: JSON.stringify(payload),
        // body: formData,
      });
      if (!response.ok) {
        throw new Error('Unable to update user profile');
      }
      setSuccess(true);
    } catch (error) {
      console.error(error);
      setSuccess(false);
    }
  };

  return (
    <Container>
      <Row className="justify-content-center mt-5">
        <Col md={8}>
          <h1 className="text-center mb-4">User Profile Page</h1>
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label htmlFor="userId" className="form-label">
                User ID:
              </label>
              <input
                type="text"
                className="form-control"
                id="userId"
                defaultValue={user?.id}
                disabled
              />
            </div>
            <div className="mb-3">
              <label htmlFor="userId" className="form-label">
                User Role:
              </label>
              <input
                type="text"
                className="form-control"
                id="userId"
                defaultValue={user?.role_id === 1 ? 'Subscriber' : 'Chef'}
                disabled
              />
            </div>
            <div className="mb-3">
              <label htmlFor="username" className="form-label">
                Username:
              </label>
              <input
                type="text"
                className="form-control"
                id="username"
                defaultValue={user?.username}
                disabled
              />
            </div>
            <div className="mb-3">
              <label htmlFor="firstName" className="form-label">
                User First Name:
              </label>
              <input
                type="text"
                className="form-control"
                id="firstName"
                defaultValue={user?.first_name}
                onChange={handleFirstNameChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="lastName" className="form-label">
                User Last Name:
              </label>
              <input
                type="text"
                className="form-control"
                id="lastName"
                defaultValue={user?.last_name}
                onChange={handleLastNameChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="email" className="form-label">
                User Email:
              </label>
              <input
                type="email"
                className={`form-control ${emailValid ? '' : 'is-invalid'}`}
                id="email"
                defaultValue={user?.email}
                onChange={handleEmailChange}
                required
              />
              <div className="invalid-feedback">
                Please enter a valid email address
              </div>
            </div>
            <div className="mb-3">
              <label htmlFor="password" className="form-label">
                Password:
              </label>
              <input
                type="password"
                className="form-control"
                id="password"
                value={password}
                onChange={handlePasswordChange}
              />
            </div>
            <div className="mb-3">
              <label htmlFor="pictureUrl" className="form-label">
                Select Avatar:
              </label>
              <div className="d-flex flex-wrap mb-2">
                {avatarOptions.map((url) => (
                  // <Avatar alt="Avatar" src={url} key={url} />
                  <div
                    key={url}
                    className={`avatar-option mx-2 my-1 ${
                      selectedAvatar === url
                        ? 'border border-primary rounded-circle'
                        : ''
                    }`}
                    onClick={() => setSelectedAvatar(url)}
                  >
                    <img
                      src={url}
                      width={70}
                      height={70}
                      alt="Avatar"
                      className="rounded-circle"
                    />
                    {selectedAvatar === url && (
                      <div className="selected-overlay">
                        <i className="bi bi-check-circle-fill"></i>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
            <div className="d-grid">
              <button
                type="submit"
                className="btn btn-success"
                disabled={!emailValid || firstName === '' || lastName === ''}
              >
                Update Profile
              </button>
            </div>
            {success && (
              <div className="alert alert-success mt-3" role="alert">
                Your profile has been updated successfully!
              </div>
            )}
          </form>
        </Col>
      </Row>
    </Container>
  );
};

export default UserProfilePage;
