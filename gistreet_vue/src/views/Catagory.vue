<template>
    <div class="page-catagory">
        <div class="columns is-multiline">
            <div class="is-12">
                <h2 class="title is-2">{{ catagory.name }}</h2>
            </div>

            <div class="column is-3" v-for="product in catagory.products" v-bind:key="product.id">
                <div class="box">
                    <figure class="image is-4by3">
                        <img :src="product.get_thumbnail">
                    </figure>

                    <h3 class="is-size-4 ">{{ product.name }}</h3>
                    <p class="is-size-3 ">${{ product.price }}</p>

                    <router-link v-bind:to="product.get_absolute_url" class="button is-info is-fullwidth">View
                        details</router-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { toast } from 'bulma-toast';

export default {
    name: 'Catagory',
    data() {
        return {
            catagory: {
                products: []
            }
        }
    },
    mounted() {
        this.getCatagory();
    },
    methods: {
        // async because we want to use loading bar
        async getCatagory() {
            const catagorySlug = this.$route.params.catagory_slug;

            this.$store.commit('setIsLoading', true);

            axios.get(`/api/v1/products/${catagorySlug}/`)
                .then(response => {
                    this.catagory = response.data;

                    document.title = this.catagory.name;
                })
                .catch(error => {
                    toast({
                        message: 'Error getting catagory',
                        type: 'is-danger',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 5000,
                    });
                });

            this.$store.commit('setIsLoading', false);
        }
    }
}
</script>