import React,{useState} from "react";
import axios from "axios";
import QuestionList from "./getdata";
import DeleteQuestionForm from "./DeleteData";
const AddQuestion = ()=>{
    const [questionText,setQuestionText] = useState('');
    const [pubDate,setPubDate] = useState('');

    const handleSubmit = async (e)=>{
        e.preventDefault();

        try{
            await axios.post('http://127.0.0.1:8000/questions/',{
                question_text:questionText,
                pub_date:pubDate
            });

        }
        catch(error){
         console.log("error found is:",error)
        }
    };
    return(
        <div>
         <li className="nav-item">
              <a className="nav-link" href="http://127.0.0.1:8000/" color="black"><h1>GO TO HOME</h1></a>
            </li>

        <form onSubmit={handleSubmit}>
        <label>
            Question Text:
            <input type="text"
            value={questionText}
            onChange={(e)=>setQuestionText(e.target.value)}
            
            />
            <script>console.log(e.target.value)</script>
        </label>
        <br/>
        <label>
            Publication Date:
            <input
                type="date"
                value={pubDate}
                onChange={(e)=>setPubDate(e.target.value)}
                />
        </label>
        <br></br>
        <button type="submit">Submit</button>
        </form>
       </div>
    );
}

export default AddQuestion;