<template >
    <div class="product-page">
        <div class="columns is-multiline">
            <div class="column is-12">
                <figure class="image is-4by3">
                    <img v-bind:src="product.get_image">
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
                        <a class="button is-info">
                            Add to cart
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
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
        getProduct() {
            const catagory_slug = this.$route.params.catagory_slug
            const product_slug = this.$route.params.product_slug

            axios.get(`/api/v1/${catagory_slug}/${product_slug}/`)
                .then(response => {
                    this.product = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}
</script>