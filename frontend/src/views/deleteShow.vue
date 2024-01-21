<template>
    <div>
        <h3>You are about to delete the show, are you sure about it</h3>
        <button @click="deleteShow">Delete Show</button>
        <p v-if="message">{{ message }}</p>
    </div>
</template>

<script>
import { getAuthTokenFromCookie } from '../functions/auth';
import axios from 'axios';
const API_BASE_URL = 'http://localhost:5000/api';

export default {
    data() {
        return {
            venueId: null,
            showId: null,
            message: '',
        };
    },
    created() {this.authToken = localStorage.getItem('authToken');
        if (this.authToken) {
            console.log("working");
        } else {
            this.$router.push('/login');
        }
        this.venueId = this.$route.params.venueId;
        this.showId = this.$route.params.showId;
    },
    methods: {
        deleteShow() {
            const showId = this.$route.params.showId;
            const venueId = this.$route.params.venueId;
            axios
                .delete(`${API_BASE_URL}/venue/${venueId}/show/${showId}`, {
                    headers: {
                        Authorization: `${this.authToken}`,
                    },
                })
                .then(response => {
                    this.message = response.data.message;
                    this.$router.push('/dashboard'); // Redirect after deletion
                })
                .catch(error => {
                    console.error('Error deleting show:', error);
                    this.message = error.message;
                });
        },
    },
};
</script>
