// src/components/InteractionForm.js
import React, { useState } from "react";
import { postInteraction } from "../api";
import "./InteractionForm.css";

const InteractionForm = () => {
  const [userId, setUserId] = useState("");
  const [productId, setProductId] = useState("");
  const [interactionType, setInteractionType] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await postInteraction({
        user_id: userId,
        product_id: productId,
        interaction_type: interactionType,
      });
      alert("Interaction logged successfully!");
    } catch (error) {
      alert("Error logging interaction.");
    }
  };

  return (
    <form className="interaction-form" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="User ID"
        value={userId}
        onChange={(e) => setUserId(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="Product ID"
        value={productId}
        onChange={(e) => setProductId(e.target.value)}
        required
      />
      <select
        value={interactionType}
        onChange={(e) => setInteractionType(e.target.value)}
        required
      >
        <option value="">Select Interaction</option>
        <option value="click">Click</option>
        <option value="purchase">Purchase</option>
      </select>
      <button type="submit">Log Interaction</button>
    </form>
  );
};

export default InteractionForm;
