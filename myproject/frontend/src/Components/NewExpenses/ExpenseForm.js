import React, { useState } from "react";
import axios from 'axios'; // Import axios library
import './ExpenseForm.css';

const ExpenseForm = (props) => {
    const [enteredTitle, setEnteredTitle] = useState('');
    const [enteredAmount, setEnteredAmount] = useState('');
    const [enteredDate, setEnteredDate] = useState('');

    const titleChangeHandler = (event) => {
        setEnteredTitle(event.target.value);
    };

    const amountChangeHandler = (event) => {
        setEnteredAmount(event.target.value);
    };

    const dateChangeHandler = (event) => {
        setEnteredDate(event.target.value);
    };

    const submitHandler = async (event) => {
        event.preventDefault();

        try {
            await axios.post('http://127.0.0.1:8000/create-expense/', {//complete url it is very important even not miss / 
                title: enteredTitle,
                amount: enteredAmount,
                date: enteredDate
            });

            // Optionally, you can perform additional actions upon successful submission
            // For example, clear input fields or update state
            setEnteredTitle('');
            setEnteredAmount('');
            setEnteredDate('');
        } catch (error) {
            console.error('Error creating expense:', error);
            // Optionally, handle error (e.g., display error message)
        }
    };

    return (
        <form onSubmit={submitHandler}>
            <div className="new-expense_controls">
                <div className="new-expense_control">
                    <label>Title</label>
                    <input type="text" value={enteredTitle} onChange={titleChangeHandler} />
                </div>
                <div className="new-expense_control">
                    <label>Amount</label>
                    <input type="number" value={enteredAmount} min={0.01} step={0.01} onChange={amountChangeHandler} />
                </div>
                <div className="new-expense_control">
                    <label>Date</label>
                    <input type="date" value={enteredDate} onChange={dateChangeHandler} />
                </div>
            </div>
            <div className="new-expense_actions">
                <button type="submit">Add Expense</button>
            </div>
        </form>
    );
};

export default ExpenseForm;
