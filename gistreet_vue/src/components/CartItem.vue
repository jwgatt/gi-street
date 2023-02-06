<template>
    <tr>
        <td>
            <router-link :to="item.product.get_absolute_url">
                {{ item.product.name }}
            </router-link>
        </td>
        <td>
            ${{ item.product.price }}
        </td>
        <td>
            {{ item.quantity }}
            <a @click="incrementQuantity(item)" class="button is-small">+</a>
            <a @click="decrementQuantity(item)" class="button is-small">-</a>
        </td>
        <td>
            ${{ getItemTotal(item).toFixed(2) }}
        </td>
        <td><button class="delete" @click="removeFromCart(item)">
            </button></td>
    </tr>
</template>

<script>
export default {
    name: "CartItem",
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price;
        },
        incrementQuantity(item) {
            item.quantity += 1;
                this.updateCart();
        },
        decrementQuantity(item) {
            if (item.quantity > 1) {
                item.quantity -= 1;
            }

            this.updateCart();
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.state.cart));
        },
        removeFromCart(item) {
            //use emit to remove item, since we are inside the component
            this.$emit('removeFromCart', item)

            this.updateCart()
        }
    }
}
</script>