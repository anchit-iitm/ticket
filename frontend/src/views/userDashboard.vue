<template>
    <div class="user-dashboard">
      <h1>Welcome to Your Dashboard</h1>
      <div class="venue-cards">
        <!-- Loop through venues and show venue cards -->
        <div v-for="venue in venues" :key="venue.id" class="venue-card">
          <h2>{{ venue.name }}</h2>
          <p>Address: {{ venue.address }}</p>
          <div class="show-cards">
            <!-- Loop through shows of the current venue and show show cards -->
            <div v-for="show in venue.shows" :key="show.id" class="show-card">
              <h3>{{ show.title }}</h3>
              <p>{{ show.description }}</p>
              <p>Rating: {{ show.rating }}</p>
              <p>Tags: {{ show.tags }}</p>
              <p>Ticket Price: ${{ show.ticket_price }}</p>
              <p>Tickets: {{ show.total_tickets }}</p>
              <Router-link v-if="show.total_tickets >= 1" :to="'/booking/' + show.id">Book Tickets</Router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  const API_BASE_URL = 'http://localhost:5000/api';
  
  export default {
    data() {
      return {
        venues: [],
      };
    },
    created() {
      this.fetchVenues();
    },
    methods: {
      fetchVenues() {
        axios
          .get(`${API_BASE_URL}/venues`, {
                    headers: {
                        Authorization: `${localStorage.getItem('authToken')}`,
                    },
                })
          .then(response => {
            this.venues = response.data;
          })
          .catch(error => {
            console.error('Error fetching venues:', error);
          });
      },
    },
  };
  </script>
  
  <style>
  .user-dashboard {
    margin: 20px;
  }
  
  .venue-cards {
    display: flex;
    flex-wrap: wrap;
  }
  
  .venue-card {
    border: 1px solid #ccc;
    margin: 10px;
    padding: 10px;
  }
  
  .show-cards {
    display: flex;
    flex-wrap: wrap;
  }
  
  .show-card {
    border: 1px solid #ddd;
    margin: 5px;
    padding: 5px;
  }
  </style>