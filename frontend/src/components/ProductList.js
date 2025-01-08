import React from "react";
import RecommendationCard from "./RecommendationCard";

const ProductList = ({ products }) => {
  return (
    <div className="product-list">
      {products.map((product) => (
        <RecommendationCard key={product.product_id} product={product} />
      ))}
    </div>
  );
};

export default ProductList;
