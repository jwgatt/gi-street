<template>
  <div class="home">
    <section class="hero is-primary">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            Welcome to GiStreet
          </h1>
          <h2 class="subtitle">
            The best place to buy and sell your used items
          </h2>
        </div>
      </div>
    </section>

    <div class="column is-multiline">
      <div class="column is-12">
        <h1 class="is-size-2 has-text-centered">Latest Products</h1>
      </div>

      <div class="column is-3" v-for="product in latestProduct" v-bind:key="product.id">
        <div class="box">
          <figure class="image is-4by3">
            <img v-bind:src="product.image" alt="Placeholder image">
          </figure>

          <h3 class="is-size-4 has-text-centered">{{ product.name }}</h3>
          <p class="is-size-6 has-text-centered">{{ product.price }}</p>

          <router-link v-bind:to="product.get_absolute_url" class="button is-info is-fullwidth">View
            details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
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
    getLatestProducts() {
      axios.get('/api/v1/latest-products/')
        .then(response => {
          this.latestProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
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
