import React, {useState} from 'react';

const MealCreatePage = () => {
  const [chef, setChef] = useState('')
  const [name, setName] = useState('');
  const [name2, setName2] = useState('');
  const [picture_url, setPicture_URL] = useState('');
  const [description, setDescription] = useState('');
  const [instruction, setInstruction] = useState('');
  const [ingredient, setIngredient] = useState('');
  const [calorie, setCalorie] = useState('');
  const [keto, setKeto] = useState('');
  const [vegan, setVegan] = useState('');
  const [choice, setChoice] = useState('');
  const [spicy, setSpicy] = useState('');
  const [cheese, setCheese] = useState('');
  const [price, setPrice] = useState(9.99);
  const handleChef = event => {
    const value = event.target.value
    setChef(value)
  }
  const handleNameChange = event => {
    const value = event.target.value
    setName(value)
  }
  const handleNameChange2 = event => {
    const value = event.target.value
    setName2(value)
  }
  const handlePicture_URL = (event) => {
    const value = event.target.value;
    setPicture_URL(value);
  }
  const handleDescription = (event) => {
    const value = event.target.value;
    setDescription(value);
  }
  const handleInstruction = (event) => {
    const value = event.target.value;
    setInstruction(value);
  }
  const handleIngredient = (event) => {
    const value = event.target.value;
    setIngredient(value);
  }
  const handleCalorie = (event) => {
    const value = event.target.value;
    setCalorie(value);
  }
  const handleKeto = (event) => {
    const value = event.target.value;
    setKeto(value);
  }
  const handleVegan = (event) => {
    const value = event.target.value;
    setVegan(value);
  }
  const handleChoice = (event) => {
    const value = event.target.value;
    setChoice(value);
  }
  const handleSpicy = (event) => {
    const value = event.target.value;
    setSpicy(value);
  }
  const handleCheese= (event) => {
    const value = event.target.value;
    setCheese(value);
  }
  const handlePrice= (event) => {
    const value = event.target.value;
    setPrice(value);
  }
  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = {};
    data.chef_id = chef
    data.name = name
    data.name2 = name2
    data.picture_url = picture_url
    data.description = description
    data.instructions = instruction
    data.ingredients = ingredient
    data.calories = calorie
    data.is_keto = keto
    data.is_vegan = vegan
    data.is_chef_choice = choice
    data.is_spicy = spicy
    data.has_cheese = cheese
    data.price = price
    const mealUrl = 'http://localhost:8000/api/meals/';
        const fetchConfig = {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
        }
        const response = await fetch(mealUrl, fetchConfig);
        if (response.ok) {
            const newMeal = await response.json();
            setChef('');
            setName('');
            setName2('');
            setPicture_URL('');
            setDescription('');
            setInstruction('');
            setIngredient('');
            setCalorie('');
            setKeto('');
            setVegan('');
            setChoice('');
            setSpicy('');
            setCheese('');
            setPrice(9.99);
        }
  }

  return(
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1>Create a meal</h1>
          <form onSubmit={handleSubmit}>
            <div className="form-floating mb-3">
              <input value={chef} onChange={handleChef} id="chef_id" placeholder="chef_id" required type="text" className="form-control" />
              <label>Chef ID</label>
            </div>
            <div className="form-floating mb-3">
              <input value={name} onChange={handleNameChange} id="name" placeholder="name" required type="text" className="form-control" />
              <label>Meal Name</label>
            </div>
            <div className="form-floating mb-3">
              <input value={name2} onChange={handleNameChange2} id="name2" placeholder="name2" required type="text" className="form-control" />
              <label>Meal Subtitle</label>
            </div>
            <div className="form-floating mb-3">
              <input onChange={handlePicture_URL} value={picture_url} placeholder="picture_url" required type="text" name="picture_url" id="picture_url" className="form-control" />
              <label htmlFor="picture_url">Picture URL</label>
            </div>
            <div className="form-floating mb-3">
              <textarea onChange={handleDescription} value={description} className="form-control" id="description" name="description" rows="15"></textarea>
                <label className="form-label">Description</label>
            </div>
            <div className="form-floating mb-3">
              <textarea onChange={handleInstruction} value={instruction} className="form-control" id="instructions" name="instructions" rows="15"></textarea>
                <label className="form-label">Instructions</label>
            </div>
            <div className="form-floating mb-3">
              <textarea onChange={handleIngredient} value={ingredient} className="form-control" id="ingredients" name="ingredients" rows="15"></textarea>
                <label className="form-label">Ingredients</label>
            </div>
            <div className="form-floating mb-3">
              <input onChange={handleCalorie} value={calorie} id="calories" placeholder="calories" required type="number" className="form-control" />
              <label>Calories</label>
            </div>
            <div className="form-floating mb-3">
              <input value={keto} onChange={handleKeto} id="is_keto" placeholder="is_keto" required type="text" className="form-control" />
              <label>Keto?</label>
            </div>
            <div className="form-floating mb-3">
              <input value={vegan} onChange={handleVegan} id="is_vegan" placeholder="is_vegan" required type="text" className="form-control" />
              <label>Vegan?</label>
            </div>
            <div className="form-floating mb-3">
              <input value={choice} onChange={handleChoice} id="is_chef_choice" placeholder="is_chef_choice" required type="text" className="form-control" />
              <label>Chef Choice?</label>
            </div>
            <div className="form-floating mb-3">
              <input value={spicy} onChange={handleSpicy} id="is_spicy" placeholder="is_spicy" required type="text" className="form-control" />
              <label>Spicy?</label>
            </div>
            <div className="form-floating mb-3">
              <input value={cheese} onChange={handleCheese} id="has_cheese" placeholder="has_cheese" required type="text" className="form-control" />
              <label>Has Cheese?</label>
            </div>
            <div className="form-floating mb-3">
              <input value={price} onChange={handlePrice} id="has_cheese" placeholder="has_cheese" type="number" className="form-control" />
              <label>Price</label>
            </div>
            <button className="btn btn-primary">Create</button>
          </form>
        </div>
      </div>
    </div>
  )
};

export default MealCreatePage;
