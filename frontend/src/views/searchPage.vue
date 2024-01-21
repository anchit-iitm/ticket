<template>
    <div class="search-page">
      <h2>Search Theatres and Shows</h2>
      
      <!-- Search theatres by location -->
      <div>
        <h3>Search Theatres by Location</h3>
        <input type="text" v-model="location" placeholder="Enter location">
        <button @click="searchTheatresByLocation">Search</button>
        <div v-if="theatres.length > 0">
          <h4>Search Results - Theatres</h4>
          <ol>
            <li v-for="theatre in theatres" :key="theatre.id">
              <hr>
              <h5>Theatre Name: {{ theatre.name }}</h5>
              <p>Address: {{ theatre.address }}</p>
              <p>Description: {{ theatre.description }}</p>
              <p>Capacity: {{ theatre.capacity }}</p>
            </li>
          </ol>
        </div>
      </div>
      
      <!-- Search shows by tags and rating -->
      <div>
        <h3>Search Shows by Tags and Rating</h3>
        <p>works with only tags or both</p>
        <input type="text" v-model="tags" placeholder="Enter tags">
        <input type="number" v-model="minRating" placeholder="Min Rating">
        <button @click="searchShowsByTagsAndRating">Search</button>
        <div v-if="shows.length > 0">
          <h4>Search Results - Shows</h4>
          <ol>
            <li v-for="show in shows" :key="show.id">
              <hr>
              <h5>{{ show.name }}</h5>
              <p>{{ show.description }}</p>
              <p>Rating: {{ show.rating }}</p>
              <p>Tags: {{ show.tags }}</p>
              <p>Available Tickets: {{ show.avail_ticket }}</p>
              <p>Total Tickets: {{ show.total_tickets }}</p>
              <p>Ticket Price: {{ show.ticket_price }}</p>
            </li>
          </ol>
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
        location: '',
        theatres: [],
        tags: '',
        minRating: null,
        shows: [],
      };
    },
    methods: {
      searchTheatresByLocation() {
        axios
          .get(`${API_BASE_URL}/search/theatres`, {
            params: {
              location: this.location,
            },
          })
          .then(response => {
            this.theatres = response.data;
          })
          .catch(error => {
            console.error('Error searching theatres:', error);
          });
      },
      searchShowsByTagsAndRating() {
        axios
          .get(`${API_BASE_URL}/search/shows`, {
            params: {
              tags: this.tags,
              rating: this.minRating,
            },
          })
          .then(response => {
            this.shows = response.data;
          })
          .catch(error => {
            console.error('Error searching shows:', error);
          });
      },
    },
  };
  </script>
  
  <style>
  /* Add your custom styles here */
  </style>
  