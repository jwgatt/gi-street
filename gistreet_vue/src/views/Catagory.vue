<template>
    <div class="page-catagory">
        <div class="columns is-multiline">
            <div class="is-12">
                <h2 class="title is-2">{{ catagory.name }}</h2>
            </div>

            <ProductBox v-for="product in catagory.products" v-bind:key="product.id" v-bind:product="product" />
        </div>
    </div>
</template>

<script>
import ProductBox from '@/components/ProductBox.vue';
import axios from 'axios';
import { toast } from 'bulma-toast';

export default {
    name: "Catagory",
    data() {
        return {
            catagory: {
                products: []
            }
        };
    },
    components: {
        ProductBox
    },
    mounted() {
        this.getCatagory();
    },
    //setup lifecycle method to watch for all route changes on catagory route
    watch: {
        $route(to, from) {
            if (to.name === 'Catagory') {
                this.getCatagory();
            }
        }
    },
    methods: {
        // async because we want to use loading bar
        async getCatagory() {
            const catagorySlug = this.$route.params.catagory_slug;
            this.$store.commit("setIsLoading", true);
            axios.get(`/api/v1/products/${catagorySlug}/`)
                .then(response => {
                    this.catagory = response.data;
                    document.title = this.catagory.name;
                })
                .catch(error => {
                    toast({
                        message: "Error getting catagory",
                        type: "is-danger",
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 5000,
                    });
                });
            this.$store.commit("setIsLoading", false);
        }
    },
    components: { ProductBox }
}
</script>