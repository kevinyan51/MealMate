import { createContext, useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

let internalToken = null;

export function getToken() {
  return internalToken;
}

export async function getTokenInternal() {
  const url = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/token`;
  try {
    const response = await fetch(url, {
      credentials: "include",
    });
    if (response.ok) {
      const data = await response.json();
      return { account: data?.account, access_token: data?.access_token };
    }
  } catch (e) {
    console.error("error getting token", e);
  }
  return { account: null, access_token: null };
}

function handleErrorMessage(error) {
  if ("error" in error) {
    error = error.error;
    try {
      error = JSON.parse(error);
      if ("__all__" in error) {
        error = error.__all__;
      }
    } catch {}
  }
  if (Array.isArray(error)) {
    error = error.join("<br>");
  } else if (typeof error === "object") {
    error = Object.entries(error).reduce(
      (acc, x) => `${acc}<br>${x[0]}: ${x[1]}`,
      ""
    );
  }
  return error;
}

export const AuthContext = createContext({
  token: null,
  setToken: () => null,
});

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(null);
  const [user, setUser] = useState(null);

  return (
    <AuthContext.Provider value={{ user, setUser, token, setToken }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuthContext = () => useContext(AuthContext);

export function useToken() {
  const { token, setToken, user, setUser } = useAuthContext();
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchToken() {
      const { account, access_token } = await getTokenInternal();
      setToken(access_token);
      setUser(account);
    }
    if (!token) {
      fetchToken();
    }
  }, [setToken, token]);

  async function logout() {
    if (token) {
      const url = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/token`;
      await fetch(url, { method: "delete", credentials: "include" });
      internalToken = null;
      setToken(null);
      setUser(null);
      navigate("/");
    }
  }

  async function login(username, password) {
    const url = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/token`;
    const form = new FormData();
    form.append("username", username);
    form.append("password", password);
    const response = await fetch(url, {
      method: "post",
      credentials: "include",
      body: form,
    });
    if (response.ok) {
      const { access_token, account } = await getTokenInternal();
      setToken(access_token);
      setUser(account);
      return access_token;
    }
    let error = await response.json();
    return handleErrorMessage(error);
  }

  async function signup({
    firstName,
    lastName,
    username,
    email,
    password,
    pictureUrl,
    roleId,
  }) {
    const url = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/users`;
    console.log(url) // CHECKING FOR DEBUG
    const response = await fetch(url, {
      method: "post",
      body: JSON.stringify({
        first_name: firstName,
        last_name: lastName,
        username,
        email,
        password,
        picture_url: pictureUrl,
        role_id: roleId,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (response.ok) {
      await login(username, password);
      console.log("Signup Successful");
    } else if (response.status >= 400 && response.status < 600) {
      const body = await response.json();
      throw Error(body.detail);
    } else {
      throw Error(`Unexpected response status: ${response.status}`);
    }
  }

  async function update(
    firstName,
    lastName,
    password,
    username,
    email,
    pictureUrl
  ) {
    const url = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/users`;
    const response = await fetch(url, {
      method: "put",
      body: JSON.stringify({
        first_name: firstName,
        last_name: lastName,
        username,
        email,
        password,
        picture_url: pictureUrl,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (response.ok) {
      await login(username, password);
    }
    return false;
  }

  return { token, login, logout, signup, update, user };
}

export const useUser = (token) => {
  const [user, setUser] = useState();

  useEffect(() => {
    if (!token) {
      return;
    }

    async function getUser() {
      const url = `${process.env.REACT_APP_USER_SERVICE_API_HOST}/api/users`;
      const response = await fetch(url, {
        credentials: "include",
      });
      if (response.ok) {
        const newUser = await response.json();
        setUser(newUser);
      }
    }

    getUser();
  }, [token]);

  return user;
};
