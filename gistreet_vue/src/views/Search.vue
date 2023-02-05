<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title is-1">Search</h1>

                <h2 class="subtitle is-3">Search term: "{{ query }}"</h2>
            </div>
            <ProductBox v-for="product in products" :key="product.id" :product="product" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import ProductBox from '@/components/ProductBox.vue';
export default {
    name: 'Search',
    components: {
        ProductBox
    },
    data() {
        return {
            query: '',
            products: []
        }
    },
    mounted() {
        document.title = 'Search | Gistreet'

        //get info from url
        let uri = window.location.search.substring(1);
        //get parameters from url
        let params = new URLSearchParams(uri);

        //get query from url
        if (params.get('query')) {
            //reference to value of query
            this.query = params.get('query');
            //create functionality to search
            this.search();
        }
    },
    methods: {
        async search() {
            this.$store.commit('setIsLoading', true);

            await axios
                .post('/api/v1/products/search/', { 'query': this.query })
                .then(response => {
                    this.products = response.data;
                })
                .catch(error => {
                    console.log(error);
                });

            this.$store.commit('setIsLoading', false);
        }
    }
}
</script>