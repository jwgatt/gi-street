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

            </div>

            <div class="column is-6">
                <div class="field">
                    <label class="label">Address</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="Address" v-model="address">
                    </div>
                </div>
                <div class="field">
                    <label class="label">Post code</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="Postal code" v-model="postal_code">
                    </div>
                </div>
                <div class="field">
                    <label class="label">Phone</label>
                    <div class="control">
                        <input class="input" type="text" placeholder="Phone" v-model="phone">
                    </div>
                </div>
            </div>

            <div class="notification is-warning column is-6" v-if="errors.length">
                <p v-for="error in errors" :key="error">{{ error }}</p>
            </div>

            <hr>

        </div>
        <!-- placeholder for stripe -->
        <div id="card-element" class="mb-3"></div>

        <template v-if="cartTotalLength > 0">
            <button class="button is-dark" @click="submitForm()">Pay with Stripe</button>
        </template>
    </div>
</template>

<script>

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
            errors: [],
            phone: '',
            user: '',
            items: [],
        };
    },
    mounted() {
        document.title = "Checkout";

        this.cart = this.$store.state.cart;

        //if products in cart, continue
        if (this.cartTotalLength > 0) {
            //create new instance of stripe
            this.stripe = Stripe('pk_test_51MYj4qIjAuYVnrXSYPdvfaIJZYUNdNQDBPQ5AsN5Ii9eG91U8b2KzKPjavCOKWeknjt6k6SyUKHFbNzPgzunQtE900luGCxT1G')
            //new instance of elements
            const elements = this.stripe.elements();
            //hide postal code
            this.card = elements.create('card', { hidePostalCode: true });

            //mount card element
            this.card.mount('#card-element');
        }
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

            if (!this.errors.length) {

                this.stripe.createToken(this.card).then(result => {
                    if (result.error) {

                        this.errors.push(result.error.message);

                    } else {
                        this.stripeTokenHandler(result.token);
                    }
                })
            }
        },
        async stripeTokenHandler(token) {
            const items = []

            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i];
                const obj = {
                    product_id: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity,
                }
                items.push(obj);
            }

            const data = {
                'first_name': this.first_name,
                'last_name': this.last_name,
                'email': this.email,
                'address': this.address,
                'postal_code': this.postal_code,
                'items': this.items,
                'stripe_token': token.id,
                'phone': this.phone,
                'user': '1',
            }

            await fetch('http://localhost:8000/api/v1/checkout/', {
                method: 'POST',
                credentials: 'same-origin',
                headers: {
                    'Authorization': 'Token ' + '0b3fe5cdc942bd4875cebcd1118f7b3e6d745da6',
                    'Content-Type': 'application/json',
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': this.$store.state.csrfToken,
                },

                body: JSON.stringify(data),

            })
                .then(response => {
                    this.$store.commit('clearCart');
                    this.$router.push('/cart/success/');
                })
                .catch(error => {
                    this.errors.push('Something went wrong, please try again later');
                });
        }
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
