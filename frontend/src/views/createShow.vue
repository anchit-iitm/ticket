<template>
    <div class="create-show">
        <h1>Create a Show</h1>
        <form @submit.prevent="createShow">
            <div>
                <label>Show Name:</label>
                <input type="text" v-model="name" required />
            </div>
            <div>
                <label>Description:</label>
                <textarea v-model="description" required></textarea>
            </div>
            <div>
                <label>Rating:</label>
                <input type="number" v-model="rating" min="0" max="5" step="0.1" required />
            </div>
            <div>
                <label>Tags:</label>
                <input type="text" v-model="tags" required />
            </div>
            <div>
                <label>Ticket Price:</label>
                <input type="number" v-model="ticketPrice" min="0" step="0.1" required />
            </div>
            <div>
                <label>Total Tickets:</label>
                <input type="number" v-model="total_tickets" min="1" required />
            </div>
            <!-- <div>
                <label>Venue ID:</label>
                <input type="number" v-model="venueId" required />
            </div> -->
            <button type="submit">Create Show</button>
        </form>
        <p v-if="message">{{ message }}</p>
    </div>
</template>
  
<script>
import axios from 'axios';
import { getAuthTokenFromCookie } from '../functions/auth';

const API_BASE_URL = 'http://localhost:5000/api';
export default {
    name: 'CreateShow',
    data() {
        return {
            name: '',
            description: '',  
            rating: 0,
            tags: '',
            ticketPrice: 0,
            total_tickets: 0,
            venueId: this.$route.params.venueId, // Populate venueId from route params
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
        createShow() {
            axios
                .post(`${API_BASE_URL}/shows`, {
                    name: this.name,
                    description: this.description,
                    rating: this.rating,
                    tags: this.tags,
                    ticket_price: this.ticketPrice,
                    total_tickets: this.total_tickets,
                    venue_id: this.venueId,
                }, {
                    headers: {
                        Authorization: `${this.authToken}`,
                    },
                })
                .then(response => {
                    this.message = response.data.message;
                    // Clear the form fields after successful show creation
                    this.name = '';
                    this.description = '';
                    this.rating = 0;
                    this.tags = '';
                    this.ticketPrice = 0;
                    this.total_tickets = 0;
                    this.venueId = 0;
                    this.$router.push('/dashboard');
                })
                .catch(error => {
                    this.message = 'An error occurred while creating the show';
                });
        },
    },
};
</script>
  