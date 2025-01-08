// src/pages/RecommendationsPage.js
import React, { useEffect, useState } from "react";
import { fetchRecommendations } from "../api";
import ProductList from "../components/ProductList";
import "../styles/RecommendationsPage.css";

const RecommendationsPage = () => {
  const [userId, setUserId] = useState("user123");
  const [strategy, setStrategy] = useState("collaborative");
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const data = await fetchRecommendations(userId, strategy);
      setProducts(data);
    };
    fetchData();
  }, [userId, strategy]);

  return (
    <div className="recommendations-page">
      <h2>Personalized Recommendations</h2>
      <div className="controls">
        <input
          type="text"
          placeholder="User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
        />
        <select value={strategy} onChange={(e) => setStrategy(e.target.value)}>
          <option value="collaborative">Collaborative Filtering</option>
          <option value="content">Content-Based Filtering</option>
        </select>
      </div>
      <ProductList products={products} />
    </div>
  );
};

export default RecommendationsPage;
