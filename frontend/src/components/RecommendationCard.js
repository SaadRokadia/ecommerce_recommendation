import React from "react";

const RecommendationCard = ({ product }) => {
  return (
    <div className="card">
      <h3>{product.name}</h3>
      <p>{product.features.description}</p>
    </div>
  );
};

export default RecommendationCard;
