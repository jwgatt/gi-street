<template>
    <div class="account-page">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My Account</h1>
            </div>

            <div class="column is-12">
                <OrderSummary :order="myOrder" />
            </div>

            <div class="column is-12">
                <button class="button is-danger" @click="logout()">Logout</button>
            </div>
        </div>
    </div>
</template>

<script>
import OrderSummary from '../components/OrderSummary.vue'
import axios from 'axios';
export default {
    name: "Account",
    components: {
        OrderSummary
    },
    data() {
        return {
            myOrder: {
                id: 1,
                quantity: 1,
                price: 1,
                items: [
                    'item1',
                    'item2',
                    'item3',
                    'item4',
                ]
            },
        }
    },
    mounted() {
        document.title = "My Account  | Gistreet"
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
            this.$store.commit('setIsLoading', true)

            await fetch('http://localhost:8000/api/v1/orders/', {
                credentials: 'same-origin',
                headers: {
                    'Authorization': 'Token ' + localStorage.getItem('token'),
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': this.$store.state.csrfToken,
                },
            })
                .then(data => {
                    console.log(data);
                    this.orders = data.orders;
                }).catch(error => {
                    console.log(error);
                });

            this.$store.commit('setIsLoading', false)
        }
    },
}
</script>