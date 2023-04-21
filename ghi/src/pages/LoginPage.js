import { useState } from "react";
import { loginUser } from "./Auth";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await loginUser({ username, password });
      localStorage.setItem("token", response.token);
      setErrorMessage("");
    } catch (error) {
      setErrorMessage("Cannot login");
    }
  };

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      // redirect to home page
      window.location.href = "/";
    }
  }, []);

  return (
    <div>
      <form onSubmit={handleLogin}>
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
      {errorMessage && <p>{errorMessage}</p>}
    </div>
  );
}

export default LoginPage;
