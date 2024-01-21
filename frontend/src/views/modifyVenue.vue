<template>
  <div class="modify-venue">
    <h1>Modify Venue {{ venue.name }}</h1>
    <div v-if="venue">
      <div class="mb-3">
        <label for="capacity" class="form-label">Capacity</label>
        <input v-model="updatedVenue.capacity" type="number" class="form-control" id="capacity" required>
      </div>
      <div class="mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea v-model="updatedVenue.description" class="form-control" id="description" rows="3"></textarea>
      </div>
      <button @click="updateVenue" class="btn btn-primary">Update Venue</button>
    </div>
    <p v-if="message">{{ message }}</p>
  </div>
</template>
  
<script>
import axios from 'axios';
const API_BASE_URL = 'http://localhost:5000/api';

export default {
  data() {
    return {
      venue: {},
      updatedVenue: {
        capacity: null,
        description: '',
      },
      message: '',
    };
  },
  created() {
    this.getVenueDetails();
  },
  methods: {
    getVenueDetails() {
      // Replace venueId with the actual ID of the venue to be modified
      const venueId = this.$route.params.venueId;
      axios
        .get(`${API_BASE_URL}/venue/${venueId}`, {
          headers: {
            Authorization: `${localStorage.getItem('authToken')}`,
          },
        })
        .then(response => {
          this.venue = response.data;
          this.updatedVenue.capacity = this.venue.capacity;
          this.updatedVenue.description = this.venue.description;
        })
        .catch(error => {
          console.error('Error fetching venue details:', error);
        });
    },
    updateVenue() {
      // Replace venueId with the actual ID of the venue to be modified
      const venueId = this.$route.params.venueId;
      axios
        .put(`${API_BASE_URL}/venue/${venueId}`, this.updatedVenue, {
          headers: {
            Authorization: `${localStorage.getItem('authToken')}`,
          },
        })
        .then(response => {
          this.message = response.data.message;
          this.$router.push('/dashboard');
        })
        .catch(error => {
          this.message = error.message;
        });
    },
  },
};
</script>