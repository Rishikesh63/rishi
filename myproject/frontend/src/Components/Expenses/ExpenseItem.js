import './ExpenseItem.css';

import ExpenseDate from './ExpenseDate';
const ExpenseItem=(props)=>{
    return(
        <div  className='expense-item'>
        <ExpenseDate date={new Date(props.date)}/>
            {/* <div>{props.date.toISOString()}</div> */}
            <div  className='expense-item_description'>
              <h2> {props.title}</h2> </div>   
                <div className='expense-item_price'> ${props.amount}</div>              
        </div>
    )
 
} 
export default ExpenseItem; 




 

