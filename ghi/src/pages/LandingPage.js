import React from 'react';
import { useNavigate } from 'react-router-dom';
import Button from '@mui/material/Button';
import { Carousel } from 'bootstrap'
import { COLORS } from '../utils/constants';

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
      <div style={{ position: 'relative', marginBottom: '40px' }}>
        <img src="https://www.factor75.com/assets/factor/images/banners/homepage/home-banner-lg_v1.jpg" style={{ height: '15%', width: '100%' }}/>
        <div style={{ position: 'absolute', top: '40%', left: '50%', transform: 'translate(-50%, -50%)' }}>
          <h1 style={{ fontSize: '3rem', fontWeight: 'bold', textAlign: 'center', color: 'black' }}> Healthy Eating, Made Easy. </h1>
          <p style={{ fontSize: '1.5rem', textAlign: 'center', color: 'black' }}> Fresh, Ready-Made Meals Delivered to Your Doorstep </p>
          <Button variant="contained" size="large" onClick={signUp} style={{display: 'block', margin: 'auto', marginTop: '2rem', backgroundColor: '#368C2A', color: 'white'}}> Get Started </Button>
        </div>
      </div>
      <div style={{ maxWidth: '300px', margin: 'auto' }}>
        <div style={{ display: 'flex', justifyContent: 'center' }}>
          <h2 style={{ textAlign: 'center', paddingBottom: '30px', fontWeight: 'bold' }}>How It Works</h2>
        </div>
      </div>

      <div style={{margin: '50px'}}>
  <div className="container">
    <div className="row">
      <div className="col-sm text-center">
      <img src="https://images.everyplate.com/f_auto,fl_lossy,q_auto,w_500/everyplate_contentful/5mIz4fhIwitKy0V8umaywu/17b2c4a9129cf0c56f8dc21be71da703/White-Label_Landing-Page_Block-1-Pick-Your-Meals-Icon_1.svg" style={{width: "100px", paddingBottom: '20px'}}/>
      <p style={{fontSize: '1.2rem', fontWeight: 'bold'}}>Pick Your Meals</p>
      <p>A new menu of 30+ dietitian-designed options every week.</p>
    </div>
    <div className="col-sm text-center">
      <img src="https://images.everyplate.com/f_auto,fl_lossy,q_auto,w_500/everyplate_contentful/4A5vCP38CuhG8V0z96ujxR/a6006269636332a017fa1b8705aeea3e/White-Label_Landing-Page_Block-1-We-Cook-Them-Icon.svg" style={{width: "100px", paddingBottom: '20px'}}/>
      <p style={{fontSize: '1.2rem', fontWeight: 'bold'}}> Cooked to Perfection</p>
      <p>Our gourmet chefs do the prep, so you can do you</p>
    </div>
    <div className="col-sm text-center">
      <img src= "https://images.everyplate.com/f_auto,fl_lossy,q_auto,w_500/everyplate_contentful/5S5qvlJQpFSJUxXncSaoN/91684bd38e81074d72df922fef3b4a2c/White-Label_Landing-Page_Block-1_Heat-Eat-Enjoy-Icon.svg" style={{width: "100px", paddingBottom: '20px'}}/>
      <p style={{fontSize: '1.2rem', fontWeight: 'bold'}}> Heat, Eat & Enjoy</p>
      <p>No prep. No mess. Our meals arrive ready to heat and eat in minutes.</p>
    </div>
  </div>
</div>
</div>

<div style={{ backgroundColor: COLORS.lightGreen , paddingTop: '20px', paddingBottom: '20px' }}>
<div>
        <div style={{ maxWidth: '300px', margin: 'auto' }}>
        <div style={{ display: 'flex', justifyContent: 'center' }}>
          <span> <h3 style={{ textAlign: 'center', paddingBottom: '70px', fontWeight: 'bold' }}>Fresh. Nutritious. Satisfying.</h3></span>
        </div>
      </div>
</div>

<div className="container" style={{ paddingBottom: '70px'}}>
  <div className="row">
    <div className="col-sm text-center">
      <p style={{paddingBottom: '20px', fontSize: '1.2rem', fontWeight: 'bold'}}>Fresh, Never-Frozen Meals</p>
      <p>We only use premium ingredients from our network of trusted partners. All meals are Chef-prepared and Dietitian-approved.</p>
    </div>
    <div className="col-sm text-center">
      <p style={{paddingBottom: '20px', fontSize: '1.2rem', fontWeight: 'bold'}}> Cooked to Perfection</p>
      <p>Our gourmet chefs do the prep, so you can do you</p>
        <Button variant="contained" size="large" onClick={signUp} style={{display: 'block', margin: 'auto',marginTop: '2rem', backgroundColor: '#368C2A',color: 'white'}}>Get Started</Button>
    </div>
    <div className="col-sm text-center">
      <p style={{paddingBottom: '20px', fontSize: '1.2rem', fontWeight: 'bold'}}> Heat, Eat & Enjoy</p>
      <p>No prep. No mess. Our meals arrive ready to heat and eat in minutes.</p>
    </div>
  </div>
</div>
</div>
   <div style={{ maxWidth: '300px', margin: 'auto' }}>
        <div style={{ display: 'flex', justifyContent: 'center' }}>
          <h2 style={{ textAlign: 'center', paddingBottom: '5px', paddingTop: '20px', fontWeight: 'bold' }}>Explore Some of Our Meals</h2>
        </div>
      </div>
<div>
  <div id="carouselExampleIndicators" className="carousel slide" data-bs-ride="carousel" style={{maxWidth: "500px", margin: "auto"}}>
  <div className="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" className="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="2" aria-label="Slide 3"></button>
  </div>
  <div className="carousel-inner">
    <div className="carousel-item active">
      <img className="icon" src="https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/641e69c2deca2fd86f0d0421-8939fc94.jpg" className="d-block w-100" alt="meal1"/>
    </div>
    <div className="carousel-item">
      <img src="https://img.hellofresh.com/w_1080,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/641e6043383e0665f80afd5e-c7176d1e.jpg" className="d-block w-100" alt="meal2" />
    </div>
    <div className="carousel-item">
      <img src="https://img.hellofresh.com/w_1200,q_auto,f_auto,c_limit,fl_lossy/q_auto/recipes/image/640b7b6fe0314bf19203476d-3ea62b2b.jpg" className="d-block w-100" alt="meal2" />
    </div>
  </div>
  <button className="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span className="carousel-control-prev-icon" aria-hidden="true"></span>
    <span className="visually-hidden">Previous</span>
  </button>
  <button className="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span className="carousel-control-next-icon" aria-hidden="true"></span>
    <span className="visually-hidden">Next</span>
  </button>
</div>
</div>
<span style={{ display: 'flex', justifyContent: 'center', paddingBottom: '5px', paddingTop: '5px', }}>
        <Button variant="outlined" onClick={() => logIn()}  style={{ backgroundColor: '#368C2A',color: 'white'}}>Login </Button>
        <Button variant="outlined" onClick={() => signUp()}  style={{backgroundColor: '#368C2A',color: 'white'}}>Get Started </Button >
</span>
</div>
)
};

export default LandingPage;
