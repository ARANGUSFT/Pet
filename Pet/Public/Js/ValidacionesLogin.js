let usernameField = document.getElementById('username'),
	emailField = document.getElementById('email'),
	passwordField = document.getElementById('password'),
	submitButton = document.getElementById('submit');

function isUsernameValid(username) {
	return username.length >= 5;
}

function isEmailValid(email) {
	return /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$/i.test(email);
}

function isPasswordValid(password) {
	/*
	Must contain at least one number and one uppercase and lowercase letter, and
	at least 8 or more characters.
	 */
	return /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/.test(password);
}

function validateUsernameField(event) {
	let value = usernameField.value;

	if (isUsernameValid(value)) {
		usernameField.classList.add('valid');
	} else {
		usernameField.classList.remove('valid');
	}
}

function validateEmailField(event) {
	let value = emailField.value;

	if (isEmailValid(value)) {
		emailField.classList.add('valid');
	} else {
		emailField.classList.remove('valid');
	}
}

function validatePasswordField(event) {
	let password = passwordField.value;

	if (isPasswordValid(password)) {
		passwordField.classList.add('valid');
	} else {
		passwordField.classList.remove('valid');
	}
}

usernameField.addEventListener('keyup', validateUsernameField);
emailField.addEventListener('keyup', validateEmailField);
passwordField.addEventListener('keyup', validatePasswordField);

submitButton.addEventListener('click', function(event) {
	event.preventDefault();
});

/* Self invoking function */
(function() {
	validateUsernameField();
	validateEmailField();
	validatePasswordField();
})();