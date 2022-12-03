Create your python virtual environment
```
py -m venv venv
```
Activate the virtual environment

Git bash:
```
source venv/Scripts/activate
```
Command prompt:
```
.\venv\Scripts\activate
```
Deactivate the venv:
```
deactivate
```
install the dependencies
```
pip install -r requirements.txt
```
Exporting requirements.txt
```
pip freeze > requirements.txt
```
Run the flask app
```
flask --app app --debug run
```

**Notes**
1. app.route without any methods defaults to only GET method.
2. indicate methods by including another parameter e.g. 
```
@app.route('/upload', methods=['GET', 'POST'])
```
3. Getting request stuff:

Get body of request
```
body = request.get_json()
body['user_id']
```

Get params of request (e.g. ?item=1)
```
args = request.args
args.get('item')
```
4. Login example with axios:
```
const testLogin = async () => {
    const response = await axios.post("http://127.0.0.1:5000/login", {},
    {
        headers: {
            "Authorization": `Basic ${Buffer.from('username:password').toString('base64')}`
        }
    })
    console.log(response)
}
OR
const testLogin = async () => {
    const response = await axios.post("http://127.0.0.1:5000/login", {},
    {
        auth: {
            username: uname,
            password: pass
        }
    })
    console.log(response)
}
testLogin()
```
5. Example to get users (attach token in headers)
```
    const getUsers = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:5000/users",
                {
                    headers: {
                        "Authorization": `Bearer ${token}`
                    }
                })
                console.log(response)
            setUserList(response.data)
        } catch (e) {
            console.log(e)
        }
    }
```