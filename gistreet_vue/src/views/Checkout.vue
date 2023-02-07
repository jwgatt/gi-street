<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title is-1">Checkout</h1>
            </div>
        </div>

        <div class="column is-12 box">
            <table class="table is-fullwidth">
                <thead>
                    <tr>
                        <th>Product</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Total</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="item in cart.items" :key="item.product.id">
                        <td>{{ item.product.name }}</td>
                        <td>{{ item.product.price }}</td>
                        <td>{{ item.quantity }}</td>
                        <td>{{ getItemTotal(item).toFixed(2) }}</td>
                    </tr>
                </tbody>

                <tfoot>
                    <tr>
                        <td colspan="2">Total</td>
                        <td>{{ cartTotalLength }}</td>
                        <td>{{ cartTotalPrice.toFixed(2) }}</td>
                    </tr>
                </tfoot>
            </table>
        </div>

        <div class="column is-12 box">
            <h2 class="subtitle is-2">Payment details</h2>
            <div class="field">
                <label class="label">Card number</label>
                <div class="control">
                    <input class="input" type="text" placeholder="Card number" v-model="card.number">
                </div>
            </div>
            <div class="field">
                <label class="label">Expiration date</label>
                <div class="control">
                    <input class="input" type="text" placeholder="Expiration date" v-model="card.exp_month">
                </div>
            </div>
            <div class="field">
                <label class="label">CVC</label>
                <div class="control">
                    <input class="input" type="text" placeholder="CVC" v-model="card.cvc">
                </div>
            </div>
        </div>

        <h2 class="subtitle is-2">Shipping details</h2>
        <div class="columns is-multiline box">
            <div class="column is-6">
                <div class="field">
                    <label class="label">First name</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="First name" v-model="first_name">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Last name</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="Last name" v-model="last_name">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Email</label>
                    <div class="control">
                        <input class="input" type="email" placeholder="Email" v-model="email">
                    </div>
                </div>

                <div class="field">
                    <label class="label">Address</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="Address" v-model="address">
                    </div>
                </div>
            </div>

            <div class="column is-6">
                <div class="field">
                    <label class="label">Postal code</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="Postal code" v-model="card.postal_code">
                    </div>
                </div>
            </div>

            <div class="notification is-warning column is-6" v-if="errors.length">
                <p v-for="error in errors" :key="error">{{ error }}</p>
            </div>

            <hr>

        </div>
        <!--             placeholder for stripe -->
        <div id="card-element"></div>

        <template v-if="cartTotalLength > 0">
            <button class="button is-dark" @click="submitForm">Pay with Stripe</button>
        </template>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "Checkout",
    data() {
        return {
            cart: {
                items: [],
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            address: '',
            place: '',
            errors: {},
        };
    },
    mounted() {
        document.title = "Checkout";

        this.cart = this.$store.state.cart;
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price;
        },
        submitForm() {
            this.errors = [];
            if (!this.first_name) {
                this.errors.push('First name is required');
            }
            if (!this.last_name) {
                this.errors.push('Last name is required');
            }
            if (!this.email) {
                this.errors.push('Email is required');
            }
            if (!this.address) {
                this.errors.push('Address is required');
            }

        },
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.quantity;
            }, 0);
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => {
                return acc += curVal.product.price * curVal.quantity;
            }, 0);
        },
    },
};
</script>
