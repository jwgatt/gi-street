<template>
    <div class="account-page">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My Account</h1>
            </div>

            <div class="column is-12">
                <h2 class="subtitle">Username: {{ $store.state.username }}</h2>
                <OrderSummary v-for="order in orders" :key="order.id" :order="order" />
            </div>

            <div class="column is-12">
                <button class="button is-danger" @click="logout()">Logout</button>
            </div>
        </div>
    </div>
</template>

<script>
import OrderSummary from '../views/OrderSummary.vue'
import axios from 'axios';
export default {
    name: "Account",
    components: {
        OrderSummary
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = "My Account  | Gistreet";

        this.getMyOrders()
    },
    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ""

            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')

            this.$store.commit('removeToken')

            this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('setLoading', true)

            axios.get('/api/v1/orders/')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setLoading', false)
        }
    },
    mounted() {
        document.title = "My Account  | Gistreet";
    }
}

</script>