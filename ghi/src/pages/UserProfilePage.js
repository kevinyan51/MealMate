import React, { useEffect, useState } from 'react';
import { useToken } from '../components/Auth';
import { Container, Row, Col } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';

const UserProfilePage = () => {
  const { user } = useToken();
  const navigate = useNavigate();

  const [selectedAvatar, setSelectedAvatar] = useState(user?.picture_url);
  const [firstName, setFirstName] = useState(user?.first_name);
  const [lastName, setLastName] = useState(user?.last_name);
  const [email, setEmail] = useState(user?.email);
  const [password, setPassword] = useState('');
  const [emailValid, setEmailValid] = useState(true);
  const [success, setSuccess] = useState(false);

  const avatarOptions = [
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Boy_headphones_lti3xz.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Woman_j4rs6u.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Woman_muslim_jf0peb.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Astronaut_dlwnxg.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Afroamerican_lb2kxl.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Scientist_kqoouj.png',
    'https://res.cloudinary.com/dfdnr2jby/image/upload/v1682569873/Girl_zj4ylc.png',
  ];

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
      firstname: firstName,
      last_name: lastName,
      email,
      picture_url: selectedAvatar,
      password,
    };

    try {
      const updateUserUrl = `${process.env.REACT_APP_API_URL}/api/users/${user?.id}`;
      const response = await fetch(updateUserUrl, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
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
              <label htmlFor="username" className="form-label">
                Username:
              </label>
              <input
                type="text"
                className="form-control"
                id="username"
                defaultValue={user?.username}
                readOnly
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
                  <div
                    key={url}
                    className={`avatar-option mx-2 my-1 ${
                      selectedAvatar === url
                        ? 'border border-primary rounded-circle'
                        : ''
                    }`}
                    onClick={() => setSelectedAvatar(url)}
                  >
                    <img src={url} alt="Avatar" className="rounded-circle" />
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
