import React from 'react';
import { Carousel } from 'bootstrap'
import { useNavigate, useParams } from 'react-router-dom';

const LandingPage = () => {

const navigate = useNavigate();

const logIn = () => {
  navigate(`/login`)
}
const signUp= () => {
  navigate(`/signup`)
}

  return (
  <div>
        <div id="carouselExampleCaptions" className="carousel slide" data-bs-ride="carousel">
  <div className="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div className="carousel-inner">
    <div className="carousel-item active">
      <img src="https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/641e69c2deca2fd86f0d0421-8939fc94.jpg" className="d-block w-100" alt="meal1" />
      <div className="carousel-caption d-none d-md-block">
        <h5>First slide label</h5>
        <p>Some representative placeholder content for the first slide.</p>
      </div>
    </div>
    <div className="carousel-item">
      <img src="https://img.hellofresh.com/w_1200,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/640b6cea8fbd1f824e04997b-2071566c.jpg" className="d-block w-100" alt="meal2" />
      <div className="carousel-caption d-none d-md-block">
        <h5>Second slide label</h5>
        <p>Some representative placeholder content for the second slide.</p>
      </div>
    </div>
    <div className="carousel-item">
      <img src="https://img.hellofresh.com/w_1200,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/640b7b6fe0314bf19203476d-3ea62b2b.jpg" className="d-block w-100" alt="meal2" />
      <div className="carousel-caption d-none d-md-block">
        <h5>Third slide label</h5>
        <p>Some representative placeholder content for the third slide.</p>
      </div>
    </div>
  </div>
  <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
    <span className="carousel-control-prev-icon" aria-hidden="true"></span>
    <span className="visually-hidden">Previous</span>
  </button>
  <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
    <span className="carousel-control-next-icon" aria-hidden="true"></span>
    <span className="visually-hidden">Next</span>
  </button>
</div>
<span>
<button onClick={() => logIn()} type="button" className="btn btn-link">
          Login
        </button>

<button onClick={() => signUp()} type="button" className="btn btn-link">
          Sign Up
        </button>
</span>
</div>
  )
};

export default LandingPage;
