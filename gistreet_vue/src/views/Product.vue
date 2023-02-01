<template >
    <div class="product-page">
        <div class="columns is-multiline">
            <div class="column is-12">
                <figure class="image is-4by3">
                    <img v-bind:src="product.get_image" alt="altImage" />
                </figure>

                <h1 class="title">{{ product.name }}</h1>

                <p>{{ product.description }}</p>
            </div>

            <div class="column is-12">
                <h3 class="subtitle is-size-4 has-text-centered">Reviews</h3>

                <p><strong>Price:</strong>${{ product.price }}</p>

                <div class="field has-addons">
                    <div class="control">
                        <input class="input" type="number" min="1" v-model="quantity">
                    </div>

                    <div class="control">
                        <a class="button is-dark" @click="addToCart">
                            Add to cart
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { toast } from 'bulma-toast'
import axios from 'axios'

export default {
    name: 'Product',
    data() {
        return {
            product: {},
            quantity: 1,
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {

        // async so when getProduct finishes loading bar set to false
        async getProduct() {
            this.$store.commit('setIsLoading', true)

            const catagory_slug = this.$route.params.catagory_slug
            const product_slug = this.$route.params.product_slug

            await axios
                .get(`/api/v1/products/${catagory_slug}/${product_slug}`)
                .then(response => {
                    this.product = response.data

                    document.title=`${this.product.name} | Gistreet`
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },

        addToCart() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: `${this.product.name} added to cart`,
                type: 'is-success',
                position: 'top-right',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
            })
        },
    }
}
</script>