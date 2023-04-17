import React from 'react';
import MealDetail from '../components/MealDetail'
import { useNavigate, useParams } from 'react-router-dom';


const ChefMealDetailPage = () => {

  const id = useParams().mealId;
  const userId = useParams().userId;

  console.log(id)
  console.log(userId)

  const navigate = useNavigate();

  const editMeal = (id) => {
        navigate(`/meals/${id}/edit`);
        };

  const deleteMeal = async (id) => {
        fetch(`http://localhost:8000/api/meals/${id}/`,{
            method: "DELETE"
            });

        navigate(`/meals`)
        window.location.reload();
        };



  return (
    <div>
      <MealDetail />
      <div style={{ display: 'inline-block' }}>
        <button onClick={() => editMeal(id)} type="button" className="btn btn-warning">
          Edit
        </button>
      </div>
      <div style={{ display: 'inline-block' }}>
        <button type="button" className="btn btn-danger" data-bs-toggle="modal" data-bs-target="#static" >
          Delete
        </button>
        <div id="static" className="modal" tabIndex="-1">
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Delete Meal</h5>
                <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div className="modal-body">
                <p>Are you sure you want to delete the meal? This will permanently remove the meal.</p>
              </div>
              <div className="modal-footer">
                <button type="button" className="btn btn-secondary" data-bs-dismiss="modal">
                  Cancel
                </button>
                <button onClick={() => deleteMeal(id)} type="button" className="btn btn-danger">
                  Delete
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChefMealDetailPage;
