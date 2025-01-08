// src/api.js
import axios from "axios";

const API_BASE_URL = "http://localhost:8000/api/";

export const fetchRecommendations = async (
  userId,
  strategy = "collaborative"
) => {
  const response = await axios.get(
    `${API_BASE_URL}recommendations/${userId}/?strategy=${strategy}`
  );
  return response.data.recommendations;
};

export const postInteraction = async (interactionData) => {
  const response = await axios.post(
    `${API_BASE_URL}interactions/`,
    interactionData
  );
  return response.data;
};
