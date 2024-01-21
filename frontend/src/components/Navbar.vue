<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <router-link class="navbar-brand" v-if="showNavbarBrand" to="/">Navbar</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" v-if="showNavbarItems" to="/dashboard">Dashboard</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" v-if="showNavbarItems" to="/search">Search</router-link>
          </li>
          <li class="nav-item" v-if="showNavbarItemsUser">
            <router-link class="nav-link active" aria-current="page" to="/home">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link active" aria-current="page" v-if="showNavbarItemsUser" to="/search">Search</router-link>
          </li>
        </ul>
      </div>
      <div>
        <form class="d-flex" role="search" v-if="showSearchForm">
          <div class="row">
            <div class="col">
              <input type="search" class="form-control" placeholder="Search..." aria-label="Search">
            </div>
            <div class="col">
              <button class="btn btn-primary" type="submit">Search</button>
            </div>
          </div>
        </form>
      </div>
      <button @click="logoutUser" class="btn btn-danger mx-auto m-2">Logout</button>
    </div>
  </nav>
</template>

<script>
import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export default {
  name: 'Navbar',
  computed: {
    showNavbarBrand() {
      return this.$route.name === 'login' || this.$route.name === 'register';
    },
    showNavbarItems() {
      return this.userRole === 'admin' && (this.$route.name === 'dashboard' || this.$route.name === 'search');
    },
    showNavbarItemsUser() {
      return this.userRole === 'user' && (this.$route.name === 'userdashboard' || this.$route.name === 'search');
    },
    showSearchForm() {
      return this.userRole === 'user' || this.$route.name === 'search';
    },
    userRole() {
      return localStorage.getItem('userRole');
    },
  },
  methods: {
    logoutUser() {
      axios.post(`${API_BASE_URL}/logout`, {
        uid: localStorage.getItem('userId'),
      })
        .then(response => {
          localStorage.removeItem('userRole');
          localStorage.removeItem('authToken');
          localStorage.removeItem('userId');
          this.$router.push('/');
        })
        .catch(error => {
          console.error('Logout error:', error);
        });
    },
  },
};
</script>
