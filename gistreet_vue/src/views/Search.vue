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

        let uri = window.location.search.substring(1);
        let params = new URLSearchParams(uri);

        if (params.get('query')) {
            this.query = params.get('query');
            this.search();
        }
    },
    methods: {
        search() {

        }
    }
}
</script>