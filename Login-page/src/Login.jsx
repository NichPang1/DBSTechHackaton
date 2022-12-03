import React, {useState} from "react"

export const Login = (props) => {
    const [email, setEmail] = useState ("");
    const [pass, setPass] = useState("");

    const handleSubmit = (e) => {
        e.preventDefault(); //if dont page get reloaded and lose state
        console.log(email);

    }
    return (
        <div className = 'auth-from-container'>
            <form className = "login-form" onSubmit ={handleSubmit}>
                <label htmlFor ="email">Email</label>
                <input value = {email} onChange ={(e) => setEmail(e.target.value)}type = "email" placeholder = "e.g youremail@gmail.com" id = "email" name = "email"/>
                <label htmlFor ="password">Password</label>
                <input value = {pass} onChange ={(e) => setPass(e.target.value)} type = "password" placeholder = "******" id = "password" name = "password"/>
                <button type = "submit">Log in</button>
            </form>
            <a  onClick ={() => props.onFormSwitch("register")}>Dont have an account? Register here</a>
        </div>
    )
}
