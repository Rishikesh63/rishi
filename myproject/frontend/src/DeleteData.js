import React, { useState } from 'react';
import axios from 'axios';

const DeleteQuestionForm = () => {
  const [questionId, setQuestionId] = useState('');
  const [message, setMessage] = useState('');
  const handleDelete = async () => {
    try {
      console.log('Deleting question with ID:', questionId);
      const questionIdInteger = parseInt(questionId, 10);
      console.log('Converted question ID:', questionIdInteger);
      await axios.delete(`http://127.0.0.1:8000/question/${questionIdInteger}/delete`);
      setMessage('Question deleted successfully.');
    } catch (error) {
      console.error('Error found during deleting question:', error);
      if (error.response && error.response.status === 404) {
        setMessage('Question not found. Please check the ID and try again.');
      } else {
        setMessage('Error deleting question. Please check the ID and try again.');
      }
    }
  };
  

  return (
    <div>
      <h2>Delete Question</h2>
      <label>
        Question ID:
        <input type="number" value={questionId} onChange={(e) => setQuestionId(e.target.value)} />
      </label>
      <button onClick={handleDelete}>Delete</button>
      <p>{message}</p>
    </div>
  );
};

export default DeleteQuestionForm;
