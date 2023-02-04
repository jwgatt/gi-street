<template>
  <div class="home">
    <section class="hero is-small is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title">
          Welcome to GiStreet
        </p>
        <p class="subtitle">
          The best place to buy and sell your used items
        </p>
      </div>
    </section>

    <div class="columns is-multiline has-text-centered">
      <div class="column is-12">
        <h1 class="is-size-3">Latest Products</h1>
      </div>
    </div>

    <ProductBox v-for="product in latestProducts" v-bind:key="product.id" v-bind:product="product" />

  </div>
</template>

<script>
import ProductBox from '@/components/ProductBox.vue'
import axios from 'axios'
export default {
  name: 'Home',
  data() {
    return {
      latestProducts: [],
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getLatestProducts()
    document.title = 'Home | Gistreet'
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios
        .get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>
