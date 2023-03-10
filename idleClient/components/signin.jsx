import Form from 'react-bootstrap/Form';
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import Button from 'react-bootstrap/Button';
import axios from 'axios'

function SignInComp(){

	const signIn=async(event)=>{
		event.preventDefault()
		let username=document.getElementById("signInUserName").value
		let password=document.getElementById("signInPassword").value
		console.log(username, password)
		let myResponse=await axios.post('signIn/',{
		  'username':username,
		  'password':password
		})
	
		console.log(myResponse.data)
 	if (myResponse.data["signIn"]==true){
    window.location.href="/"
  	}
    else{
        alert("incorrect input")
    }
	}

	return (
	<>

	{/* SIGN IN */}
	<div className='box position-absolute top-50 start-50 translate-middle'>
        <Form onSubmit={signIn}>
      <FloatingLabel controlId="signInUserName" label="Email address" className="mb-3">
        <Form.Control type="email" placeholder="" />
      </FloatingLabel>

	<div className='input-group'>
      <FloatingLabel controlId="signInPassword" label="Password">
        <Form.Control type="password" placeholder="" />
      </FloatingLabel>
	<Button onClick={signIn} className='input-group-append'>Sign in</Button>
	</div>
	</Form>	
	</div>
      {/* SIGN IN */}

	</>
	)
}
export default SignInComp