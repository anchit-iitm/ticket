<!-- <template>
    <div>
        <h2>Book a Ticket</h2>
        <form @submit.prevent="bookTicket">
            <label>Select Number of Tickets:</label>
            <input type="number" v-model="numTickets" min="1" :max="availableTickets" required>
            <button type="submit">Book Tickets</button>
        </form>
        <p v-if="message">{{ message }}</p>
    </div>
</template>
  
<script>
import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export default {
    data() {
        return {
            numTickets: 1,
            availableTickets: 0, // value based on API response or computed property or restricted by the backend
            showId: this.$route.params.showId, // value based on the selected show
            message: '',
        };
    },
    created() {
        this.authToken = localStorage.getItem('authToken');
        if (this.authToken) {
            console.log(this.$store.state.userRole);
        } else {
            this.$router.push('/login');
        }
    },
    methods: {
        fetchAvailableTickets() {
            axios
                .get(`${API_BASE_URL}/show/${this.showId}/available-tickets`)
                .then(response => {
                    this.availableTickets = response.data.total_tickets;
                })
                .catch(error => {
                    console.error(error);
                });
        },
        bookTicket() {
            const bookingData = {
                show_id: this.showId,
                number_of_tickets: this.numTickets,
            };
            axios
                .post(`${API_BASE_URL}/bookings`, {
                    uid: localStorage.getItem('userId'),
                    show_id: this.showId,
                    number_of_tickets: this.numTickets
                }, {
                    headers: {
                        Authorization: `${this.authToken}`,
                    },
                })
                .then(response => {
                    this.message = response.data.message;
                    // redirect to /home after 1 second
                    setTimeout(() => {
                        this.$router.push('/home');
                    }, 1000);
                })
                .catch(error => {
                    this.message = error.response.data.message;
                });
        },
    },
};
</script> -->
<template>
    <div>
        <h2>Book a Ticket</h2>
        <form v-if="availableTickets > 0" @submit.prevent="bookTicket">
            <label>Select Number of Tickets:</label>
            <input type="number" v-model="numTickets" min="1" :max="availableTickets" required>
            <button type="submit">Book Tickets</button>
        </form>
        <p v-else>Loading available tickets...</p>
        <p v-if="message">{{ message }}</p>
    </div>
</template>
  
<script>
import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000/api';

export default {
    data() {
        return {
            numTickets: 1,
            availableTickets: 0,
            showId: this.$route.params.showId,
            message: '',
        };
    },
    created() {
        this.authToken = localStorage.getItem('authToken');
        if (this.authToken) {
            console.log(this.$store.state.userRole);
            this.fetchAvailableTickets();
        } else {
            this.$router.push('/login');
        }
    },
    methods: {
        fetchAvailableTickets() {
            axios
                .get(`${API_BASE_URL}/show/${this.showId}`, {
                    headers: {
                        Authorization: `${this.authToken}`,
                    },
                })
                .then(response => {
                    this.availableTickets = response.data.total_tickets;
                })
                .catch(error => {
                    console.error(error);
                });
        },
        bookTicket() {
            const bookingData = {
                show_id: this.showId,
                number_of_tickets: this.numTickets,
            };
            axios
                .post(`${API_BASE_URL}/bookings`, {
                    uid: localStorage.getItem('userId'),
                    show_id: this.showId,
                    number_of_tickets: this.numTickets
                }, {
                    headers: {
                        Authorization: `${this.authToken}`,
                    },
                })
                .then(response => {
                    this.message = response.data.message;
                    setTimeout(() => {
                        this.$router.push('/home');
                    }, 1000);
                })
                .catch(error => {
                    this.message = error.response.data.message;
                });
        },
    },
};
</script>
