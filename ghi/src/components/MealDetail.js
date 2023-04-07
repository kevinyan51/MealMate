import React, { useState, useEffect} from 'react';
import { useParams } from 'react-router-dom'



const MealDetail = () => {

  const [meal, setMeal] = useState({});
  const id = useParams().mealId;
  const mealUrl = `http://localhost:8000/api/meals/${id}/`



  const fetchMeal = async () => {
    const response = await fetch(mealUrl);
    if (response.ok){
      const data = await response.json()
      setMeal(data);
    } else {
      throw new Error('error getting Meal')
    }
  }


    useEffect(() => {
        fetchMeal();
        }, []);

return (
    <div>
    <div className="card mb-3">
    <h2 className="card-title">{meal.name}</h2>
    <p className="card-text">{meal.name2}</p>
    <img className="card-img-top" src={meal.picture_url} style={{width: '550px', height: '325px'}} alt="meal" />
    <div className="card-body">
          <p className="card-text"><small>
            {meal.calories && <span className="calories">{meal.calories} calories    </span>}
            {meal.is_keto && <span className="category">Keto      </span>}
            {meal.is_vegan && <span className="category">      Vegan      </span>}
            {meal.is_chef_choice && <span className="category">      Chef's Choice      </span>}
            {meal.is_spicy && <span className="category">      Spicy      </span>}
            {meal.has_cheese && <span className="category">      Cheese      </span>}
          </small></p>
        <p className="card-text"><small >by {meal.first_name} {meal.last_name}</small></p>
        <p className="card-text"><small className="text-muted">${meal.price}</small></p>
    </div>
    </div>

        <div className="card">
        <p className="card-text"> {meal.description} </p>
        <p className="card-text"> {meal.ingredients} </p>
        </div>
</div>
  );
}

export default MealDetail;
