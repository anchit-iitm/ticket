<template>
  <div class="register">
    <h1>User registration</h1>
    <form @submit.prevent="registerUser">
      <div>
        <label>Email:</label>
        <input type="email" v-model="email" required />
      </div><br>
      <div>
        <label>Password:</label>
        <input type="password" v-model="password" required />
      </div>
      <button type="submit">Register</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';
import router from '../router'; // Import the router object from the Vue Router instance
const API_BASE_URL = 'http://localhost:5000/api'; // API base URL here

export default {
  data() {
    return {
      email: '',
      password: '',
      message: ''
    };
  },
  methods: {
    registerUser() {
      // Call the API function to register the user
      axios
        .post(`${API_BASE_URL}/register`, {
          email: this.email,
          password: this.password,
        })
        .then((response) => {
          this.message = response.data.message;
          // Clear the form fields after successful registration
          this.email = '';
          this.password = '';
          router.push('/login'); // Use the router object to navigate to '/login'
        })
        .catch((error) => {
          this.message = error.message;
        });
    },
  },
};
</script>
