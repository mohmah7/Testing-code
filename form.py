def index():

	return """
<html><head>
<title>Formular</title>
</head>
<body>
<FORM value="form" action="get_info" method="post">
  <P>
	<LABEL for="firstname">First Name: </LABEL>
	<INPUT type="text" name="firstname"><BR>
	<LABEL for="lastname">Last Name: </LABEL>
	<INPUT type="text" name="lastname"><BR>
	<LABEL for="email">email: </LABEL>
	<INPUT type="text" name="email"><BR>
	<INPUT type="radio" name="gender" value="Male">Male<BR>
	<INPUT type="radio" name="gender" value="Female">Female<BR>
	<INPUT type="submit" value="Send"> <INPUT type="reset">
  </P>
</FORM>
<FORM value="form" action="fibonacci" method="post">
   <P>
         <LABEL for="enternumber">Enter numbers:</LABEL>
	 <INPUT type="text "  name ="enternumber"><BR>
	 <INPUT type="submit" value="Send">
   </P>
</FORM>
</body>
</html>
"""

def  fibonacci(req):
	info = req.form
	number = int(info['enternumber'])
	
	a , b , c = 0 , 1 , 0
	while c < number: 
		a , b = b , a + b
		c += 1
	result = a 
	return """
<html><head>
<title> Fibonacci  Serious</title>
</head>
<body>
<h1>  The numbers are  </h1>
<hr>
Thanks for using our service:<br>
The number you entered is : %s <br>
Fibonacci is : %s <br>
<FORM value="form" action="index" method="post">
   <P>
	 <INPUT type="submit" value="Return to index page">
   </P>
</FORM>


</body>
</html>
""" %(number, result)


def get_info(req):
	info = req.form
	first = info['firstname']
	last = info['lastname']
	email = info['email']
	gender = info['gender']
	return """
<html><head>
<title>POST method using mod_python</title>
</head>
<body>
<h1>POST Method using mod_python</h1>
<hr>
Thanks for using our service:<br>
Your first name: %s <br>
Your last name: %s <br>
Your email address: %s <br>
Your gender: %s <br>
</body>
</html>
""" %(first, last.upper(), email, gender.lower())
