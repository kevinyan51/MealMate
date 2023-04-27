import React, { useState, useEffect } from "react";

function ChefListPage() {
  const [users, setUsers] = useState([]);


  useEffect(() => {
    fetch(`${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/users`)
      .then((response) => response.json())
      .then((data) => setUsers(data));
  }, []);

  return (
    <div className="container">
      <h1 className="test-center my-4">Chef List</h1>
      <ul className="list-unstyled">
        {users.filter((u) => u.role_id===2).map((user) => (
          <li key={user.id}>
            <img src={user.picture_url} alt={user.first_name} className="chef-img"/>
            <div className="media-body">
              <h2 className="mt-0">Chef {user.first_name}</h2>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ChefListPage;
