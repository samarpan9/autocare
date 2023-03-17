// JavaScript code for form validation

const form = document.querySelector('form');
const username = document.querySelector('input[type="text"]');
const password = document.querySelector('input[type="password"]');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  // Check if username and password are not empty
  if (username.value.trim() === '' || password.value.trim() === '') {
    alert('Please enter both username and password.');
    return;
  }

  // If username and password are entered, submit the form
  form.submit();
});
