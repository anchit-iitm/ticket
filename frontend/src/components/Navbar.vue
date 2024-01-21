<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <!-- Show the navbar brand link only on pages other than login and register -->
      <router-link class="navbar-brand" to="/">Navbar</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <!-- Add other navbar items here -->
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" v-if="showNavbarItems1" to="/about">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" v-if="showNavbarItems"
              to="/dashboard">Dashboard</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" v-if="showNavbarItems"
              to="/search">Search</router-link>
          </li>
          <!-- <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" v-if="showNavbarItems"
              to="/export">Export CSV</router-link>
          </li> -->
          <li class="nav-item">
            <router-link class="nav-link" v-if="showNavbarBrand" to="/login">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" v-if="showNavbarBrand" to="/register">Register</router-link>
          </li>
          <li class="nav-item" v-if="showNavbarItemsUser">
            <router-link class="nav-link active" aria-current="page"
              to="/home">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" v-if="showNavbarItemsUser"
              to="/search">Search</router-link>
          </li>
        </ul>
      </div>
      <div><form class="d-flex" role="search" v-if="ok">
        <!-- Add the search form here -->
        <!-- <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-primary" type="submit">Search</button> -->
        <div class="row">
          <div class="col">
            <input type="search" class="form-control" placeholder="Search..." aria-label="Search">
          </div>
          <div class="col">
            <button class="btn btn-primary" type="submit">Search</button>
          </div>
        </div>
      </form></div>
      <button @click="logoutUser" class="btn btn-danger mx-auto m-2">Logout</button>
    </div>
  </nav>
</template>

<script>
import axios from 'axios';
import { mapMutations } from 'vuex'; // Import the mapMutations function
const API_BASE_URL = 'http://localhost:5000/api';
export default {
  name: 'Navbar',
  computed: {
    showNavbarBrand() {
      return this.$route.name === 'login' || this.$route.name === 'register';
    },
    logpagecheck() {
      return this.$route.name !== 'login' && this.$route.name !== 'register';
    },
    showNavbarItems() {
      return this.$route.name === 'dashboard';
    },
    showNavbarItemsUser() {
      return this.$route.name === 'userdashboard' || this.$route.name === 'search';
    },
  },
  methods: {
    logoutUser() {
      axios.post(`${API_BASE_URL}/logout`,{
        uid: localStorage.getItem('userId'),
      })
        .then(response => {
          // Clear the authentication token from the cookie
          // this.clearAuthTokenFromCookie();
          // clear the user object from the local storage
          localStorage.removeItem('userRole');
          localStorage.removeItem('authToken');
          localStorage.removeItem('userId');
          // Redirect to the login page or any other page after logout
          this.$router.push('/');
        })
        .catch(error => {
          console.error('Logout error:', error);
          // Handle logout error if needed
        });
    },
    // clearAuthTokenFromCookie() {
    //   // Clear the authToken cookie
    //   document.cookie = 'authToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; secure; samesite=none';
    // },
  },
};
</script>

