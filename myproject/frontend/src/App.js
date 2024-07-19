import Expenses from './Components/Expenses/Expenses';
import React, { useEffect, useState } from 'react';
import NewExpense from './Components/NewExpenses/NewExpense'
import axios from 'axios';


const  App=()=>{ 

    const [expenses,setexpenses]=useState([]);
  
 useEffect(()=>{
    const fetchData = async() => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/create-expense/');
        console.log("response is:",response.data);
        setexpenses(response.data);
      }
        catch (error) {
            console.log("error found is:",error);
        };

     }
    fetchData();
 },[]); 
   const addExpenseHandler=(expense)=>{
       const updatedExpense=[expense,...expenses]
       setexpenses(updatedExpense)
}
    return (
        <div>
        <NewExpense onAddExpense={addExpenseHandler}/>
         <Expenses item={expenses}/>
        </div>
    )
}

export default App;  
 
