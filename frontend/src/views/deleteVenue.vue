<template>
    <div>
        <h3>You are about to delete the venue which would eventually result into deleting all the shows associated with this venue, are you sure about it</h3>
        <button @click="deleteVenue">Delete Venue and Shows</button>
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
            venueId: null,
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
        this.venueId = this.$route.params.venueId;
    },
    methods: {
        deleteVenue() {
            axios
                .delete(`${API_BASE_URL}/venue/${this.venueId}`, {
                    headers: {
                        Authorization: `${this.authToken}`,
                    },
                })
                .then(response => {
                    this.message = response.data.message;
                    this.$router.push('/dashboard'); // Redirect after deletion
                })
                .catch(error => {
                    console.error('Error deleting venue:', error);
                    this.message = error.message;
                });
        },
    },
};
</script>
