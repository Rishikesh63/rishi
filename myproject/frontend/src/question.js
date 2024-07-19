import React,{useState} from "react";
import axios from "axios";
import QuestionList from "./getdata";
import DeleteQuestionForm from "./DeleteData";
import AddQuestion from "./addQues";
const QuestionForm = ()=>{
    return(
        <div>
       <AddQuestion></AddQuestion>
       <DeleteQuestionForm/>
       <QuestionList/>
        </div>
    );
}

export default QuestionForm;