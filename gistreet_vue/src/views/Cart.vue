<template>
    <div class="page-cart">
        <div columns is-multiline>
            <div class="column is-12 box">

                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Quantity</th>
                            <th>Price</th>
                            <th>Total</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <CartItem v-for="item in cart.items" v-bind:key="item.product.id" v-bind:initialItem="item" />
                    </tbody>
                </table>
                <p v-else>Your cart is empty.</p>
            </div>

            <div class="column is-12 box">
                <h2 class="subtitle">Summary</h2>
                <strong>${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items
                <hr>
                <RouterLink to="/cart/checkout" class="button is-primary is-fullwidth">Checkout</RouterLink>
            </div>
        </div>
    </div>
</template>

<script>
import CartItem from '@/components/CartItem.vue';
import axios from 'axios';
export default {
    name: "Cart",
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        };
    },
    mounted() {
        this.cart = this.$store.state.cart;
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((acc, curVal) => { return acc += curVal.quantity }, 0);
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, curVal) => { return acc += curVal.quantity * curVal.product.price }, 0);
        }
    },
}
</script>