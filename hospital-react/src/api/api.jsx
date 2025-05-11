// File: src/api.js

const API_BASE_URL = "http://127.0.0.1:8000/api";

export const loginUser = async (username, password) => {
  const response = await fetch(`${API_BASE_URL}/auth/login/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });
  return await response.json();
};

export const registerUser = async (userData) => {
  const response = await fetch(`${API_BASE_URL}/auth/register/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(userData)
  });
  return await response.json();
};

export const fetchUserProfile = async (token) => {
  const response = await fetch(`${API_BASE_URL}/auth/profile/`, {
    method: "GET",
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });
  if (!response.ok) {
    throw new Error("Failed to fetch profile");
  }
  return await response.json();
};