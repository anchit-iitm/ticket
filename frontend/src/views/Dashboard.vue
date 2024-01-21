<template>
    <!-- <ul class="nav">
        <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Active</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item">
            <a class="nav-link disabled">Disabled</a>
        </li>
    </ul> -->

    <div class="p-3 mb-2 bg-info-subtle text-emphasis-info">
        <div v-if="venuesData">
            <div v-if="flashMessage" class="alert alert-success">{{ flashMessage }}</div>
            <h1>Admin Dashboard</h1>
            <RouterLink class="link-opacity-25-hover" title="create venue" to="/createvenue">Create a new venue
                </RouterLink>
            <div v-for="venue in venuesData" :key="venue.id" class="card mb-3">
                <div class="card-header">{{ venue.name }}
                    <p class="card-text">
                    <div><strong>Address:</strong>
                        {{ venue.address }}
                    </div>
                    <div><strong>Capacity:</strong>
                        <Router-Link class="link-opacity-25-hover" title="edit" :to="`/modifyvenue/${venue.id}`">
                            {{ venue.capacity }}
                        </Router-Link>
                    </div>
                    <div><strong>Description:</strong> <Router-Link class="link-opacity-25-hover" title="edit"
                            :to="`/modifyvenue/${venue.id}`">
                            {{ venue.description }}
                        </Router-Link></div>
                    <Router-Link :to="{ name: 'createshow', params: { venueId: venue.id } }">Create a show for this
                        venue</Router-Link> -
                    <Router-link :to="{ name: 'deletevenue', params: { venueId: venue.id } }">Delete Venue and
                        Shows</Router-link> - 
                        <button @click="exportTheatreCSV(venue.id)" class="btn btn-primary">Export Theatre CSV</button>

                    </p>
                </div>
                <div class="card-body">
                    <h3>Shows:</h3>
                    <ul class="list-group">
                        <li v-for="show in venue.shows" :key="show.id" class="list-group-item">
                            Name: {{ show.name }} - Description: {{ show.description }} - Rating: {{ show.rating }} - Tags:
                            {{ show.tags }} - Ticket Price:
                            {{ show.ticket_price }} - Tickets: {{ show.avialable_tickets }} out of {{ show.total_tickets }}
                            - <router-link
                                :to="{ name: 'modifyshow', params: { venueId: venue.id, showId: show.id } }">Modify</router-link>
                            - <router-link
                                :to="{ name: 'deleteshow', params: { venueId: venue.id, showId: show.id } }">Delete</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
import axios from 'axios';
import { getAuthTokenFromCookie } from '../functions/auth';

const API_BASE_URL = 'http://localhost:5000/api';

export default {
    data() {
        return {
            venuesData: null,
            flashMessage: '',
        };
    },
    created() {
        this.authToken = localStorage.getItem('authToken');
        if (this.authToken) {
            this.getVenuesAndShows();
            // console.log(this.$store.state.userRole);
        } else {
            this.$router.push('/login');
        }
    },
    methods: {
        getVenuesAndShows() {
            axios
                .get(`${API_BASE_URL}/venues-and-shows`, {
                    headers: {
                        Authorization: `${this.authToken}`,
                    },
                })
                .then(response => {
                    this.venuesData = response.data;
                })
                .catch(error => {
                    console.error('Error fetching venues and shows:', error);
                });
        },
        logoutUser() {
            axios.post(`${API_BASE_URL}/logout`, {
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
                    this.$router.push('/login');
                })
                .catch(error => {
                    console.error('Logout error:', error);
                    // Handle logout error if needed
                });
        },
        exportTheatreCSV(theatre_id) {
            axios
                .post(`${API_BASE_URL}/export-theatre-csv/${theatre_id}`)
                .then(response => {
                    console.log(response.data);
                    this.flashMessage = response.data.message; // Log the response message or handle it as needed
                    // Clear the flash message after 15 seconds
                setTimeout(() => {
                    this.flashMessage = '';
                }, 15000); // 15000 milliseconds = 15 seconds
                })
                .catch(error => {
                    console.error('Error triggering CSV export:', error);
                    // Handle error if needed
                });
        },
    },
};
</script>
  
  