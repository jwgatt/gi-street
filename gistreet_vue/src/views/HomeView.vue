<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
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

      <div class="column is-3" v-for="product in latestProducts" v-bind:key="product.id">
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
import axios from 'axios'
export default {
  name: 'Home',
  data() {
    return {
      latestProducts: [],
    }
  },
  components: {
  },
  mounted() {
    this.getLatestProducts()
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

<style scoped>
.image {
  margin-top: 1.5rem;
  margin-left: 1.5rem;
  margin-right: 1.5rem;
}
</style>
