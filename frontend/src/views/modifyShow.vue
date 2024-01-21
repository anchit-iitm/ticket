<template>
    <div class="modify-show">
        <h1>Update the Show : {{ show.name }}</h1>
        <div v-if="show">
            <div class="mb-3">
                <label for="name" class="form-label">Show Name: </label>
                <input type="text" v-model="updatedShow.name" disabled class="form-control" id="name" />
            </div>
            <div class="mb-3">
                <label for="description" class="form-label">Description:</label>
                <textarea v-model="updatedShow.description" required class="form-control" id="description"></textarea>
            </div>
            <div class="mb-3">
                <label for="rating" class="form-label">Rating:</label>
                <input type="number" v-model="updatedShow.rating" min="0" max="5" step="0.1" required class="form-control"
                    id="rating" />
            </div>
            <div class="mb-3">
                <label for="tags" class="form-label">Tags:</label>
                <input type="text" v-model="updatedShow.tags" required class="form-control" id="tags" />
            </div>
            <div class="mb-3">
                <label for="price" class="form-label">Ticket Price:</label>
                <input type="number" v-model="updatedShow.ticketPrice" step="0.01" required class="form-control"
                    id="price" />
            </div>
            <div class="mb-3">
                <label for="total_tickets" class="form-label">Total Tickets:</label>
                <input type="number" v-model="updatedShow.total_tickets" required class="form-control"
                    id="total_tickets" />
            </div>
            <button @click="modifyShow" class="btn btn-primary">Update Show</button>
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
            venueId: null,
            showId: null,
            show: {},
            updatedShow: {
                name: '',
                description: '',
                rating: 0,
                tags: '',
                ticketPrice: 0,
                venue_id: 0,
                total_tickets: 0,
            },
            message: '',
        };
    },
    created() {
        this.venueId = this.$route.params.venueId;
        this.showId = this.$route.params.showId;
        this.getShowDetails();
    },
    methods: {
        getShowDetails() {
            const showId = this.$route.params.showId;
            const venueId = this.$route.params.venueId;
            axios
                .get(`${API_BASE_URL}/venue/${this.venueId}/show/${this.showId}`, {
                    headers: {
                        Authorization: `${localStorage.getItem('authToken')}`,
                    },
                })
                .then(response => {
                    this.show = response.data;
                    this.updatedShow.name = this.show.name;
                    this.updatedShow.description = this.show.description;
                    this.updatedShow.rating = this.show.rating;
                    this.updatedShow.tags = this.show.tags;
                    this.updatedShow.ticketPrice = this.show.ticket_price;
                    this.updatedShow.venue_id = this.show.venue_id;
                    this.updatedShow.total_tickets = this.show.total_tickets;
                })
                .catch(error => {
                    console.error('Error fetching show details:', error);
                });
        },

        modifyShow() {
            const showId = this.$route.params.showId;
            const venueId = this.$route.params.venueId;
            // console.log(this.updatedShow);
            axios
                .put(`${API_BASE_URL}/venue/${this.venueId}/show/${this.showId}`, {
                    name: this.updatedShow.name,
                    description: this.updatedShow.description,
                    rating: this.updatedShow.rating,
                    tags: this.updatedShow.tags,
                    ticket_price: this.updatedShow.ticketPrice,
                    venue_id: this.updatedShow.venueId,
                    total_tickets: this.updatedShow.total_tickets,
                }, {
                    headers: {
                        Authorization: `${localStorage.getItem('authToken')}`,
                    },
                })
                .then(response => {
                    this.message = response.data.message;
                    // console.log(this.updatedShow);
                    this.$router.push('/dashboard');
                })
                .catch(error => {
                    console.error('Error modifying show:', error);
                    this.message = error.message;
                });
        },
    },
};
</script>
  