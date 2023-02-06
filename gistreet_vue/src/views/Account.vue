<template>
    <div class="account-page">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My Account</h1>
            </div>

            <div class="column is-12">
                <button class="button is-danger" @click="logout()">Logout</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: "Account",
    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')

            this.$store.commit('removeToken')

            this.$router.push('/')
        }
    }
}

</script>