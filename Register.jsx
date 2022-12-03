import React, {useState} from "react";
export const Register = (props) => {
    const[email, setEmail] = useState("");
    const[pass, setPass] = useState("");
    const[name, SetName] = useState("")

    const handleSubmit = (e) => {
        e.preventDefault(); //if dont page get reloaded and lose state
        console.log(email);

    }
    return (
        <div className = 'auth-from-container'>
            <form className = "register-form" onSubmit ={handleSubmit}>
                <label htmlFor ="name">Full name</label>
                <input value = {name} name="name" id = "name" placeholder = "fullname"/>
                <label htmlFor ="email">email</label>
                <input value = {email} onChange ={(e) => setEmail(e.target.value)}type = "email" placeholder = "e.g youremail@gmail.com" id = "email" name = "email"/>
                <label htmlFor ="password">password</label>
                <input value = {pass} type = "password" placeholder = "******" id = "password" name = "password"/>
                <button type = "submit">Register</button>
            </form>
            <button onClick ={()=> props.onFormSwitch("login")}>Already have an account? Login here</button>
        </div>
    )
}