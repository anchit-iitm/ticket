<template>
  <div>
    <h1>Create New Venue</h1>
    <form @submit.prevent="createVenue">
      <div class="mb-3">
        <label for="name" class="form-label">Name</label>
        <input v-model="venueData.name" type="text" class="form-control" id="name" required>
      </div>
      <div class="mb-3">
        <label for="address" class="form-label">Address</label>
        <input v-model="venueData.address" type="text" class="form-control" id="address" required>
      </div>
      <div class="mb-3">
        <label for="capacity" class="form-label">Capacity</label>
        <input v-model="venueData.capacity" type="number" class="form-control" id="capacity" required>
      </div>
      <div class="mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea v-model="venueData.description" class="form-control" id="description" rows="3"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Create Venue</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>
  
<script>
import axios from 'axios';
import { getAuthTokenFromCookie } from '../functions/auth';

const API_BASE_URL = 'http://localhost:5000/api';

export default {
  data() {
    return {
      venueData: {
        name: '',
        address: '',
        capacity: null,
        description: '',
      },
      message: '',
    };
  },
  created() {
        this.authToken = localStorage.getItem('authToken');
        if (this.authToken) {
            console.log("working");
        } else {
            this.$router.push('/login');
        }
        // console.log(this.$route.params.venueId);
        // console.log(this.authToken);
    },
  methods: {
    createVenue() {
      axios
        .post(`${API_BASE_URL}/create-venue`, this.venueData, {
                    headers: {
                        Authorization: `${this.authToken}`,
                    },
                })
        .then(response => {
          this.message = response.data.message;
          // Clear the form fields after successful venue creation
          this.venueData.name = '';
          this.venueData.address = '';
          this.venueData.capacity = null;
          this.venueData.description = '';
          this.$router.push('/dashboard');
        })
        .catch(error => {
          this.message = error.message;
        });
    },
  },
};
</script>
  
<style>
/* Add any custom styles here if needed */
</style>
  