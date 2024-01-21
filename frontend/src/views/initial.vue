<template>
    <div>
        <h1>Welcome to Dashboard</h1>
        <div v-if="userDetails && userDetails.roles && userDetails.roles.includes('admin')">
            <p>User ID: {{ userDetails.id }}</p>
            <p>Email: {{ userDetails.email }}</p>
            <p>You are an admin!</p>
        </div>
        <div v-else>
            <p>You are not an admin.</p>
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
            authToken: '',
            userDetails: null,
        };
    },
    created() {
        this.authToken = getAuthTokenFromCookie();
        if (this.authToken) {
            this.getDashboardData();
        } else {
            this.$router.push('/login');
        }
    },
    methods: {
        getDashboardData() {
            axios
                .get(`${API_BASE_URL}/details`, {
                    headers: {
                        Authorization: `${this.authToken}`,
                    },
                })
                .then(response => {
                    this.userDetails = response.data;
                })
                .catch(error => {
                    console.error('Error fetching user details:', error);
                });
        },
    },
};
</script>