import React, { useState, useEffect } from 'react';
import axios from 'axios';

const QuestionList = () => {
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    const fetchData = async() => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/questions/');
        setQuestions(response.data);
      } catch (error) {
        console.log("error found is:",error);
      }
    };

    fetchData();
  },[]); 

  return (
    <div>
      <h2>Questions:</h2>
      <ul>
        {questions.map((question) => (
          <li key={question.id}>{question.id}.{question.question_text}</li>
        ))}
      </ul>
    </div>
  );
};

export default QuestionList;