<template>
  <MainCarousel />
  <div class="home">



    <!-- <article class="message is-info">
      <div class="message-header">
        <p>Info</p>
        <button class="delete" aria-label="delete"></button>
      </div>
      <div class="message-body">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        <strong>Pellentesque risus mi</strong>, tempus quis placerat ut, porta nec
        nulla. Vestibulum rhoncus ac ex sit amet fringilla. Nullam gravida purus
        diam, et dictum <a>felis venenatis</a> efficitur. Aenean ac
        <em>eleifend lacus</em>, in mollis lectus. Donec sodales, arcu et
        sollicitudin porttitor, tortor urna tempor ligula, id porttitor mi magna a
        neque. Donec dui urna, vehicula et sem eget, facilisis sodales sem.
      </div>
    </article> -->
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">جدیدترین ها</h2>
        <div class="is-loading-bar has-text-centered" v-bind:class="{ 'is-loading': $store.state.isLoading }">
          <div class="lds-dual-ring"></div>
        </div>
      </div>

      <!-- <div class="column is-3" v-for="product in latestProducts" v-bind:key="product.id">
        <div class="box">
          <figure class="image mb-4">
            <img :src="product.get_thumbnail">
            <img v-bind:src="product.get_tumbnail">
          </figure>
          <h3 class="is-size-4">{{ product.name }}</h3>
          <p>تومان
          <p class="is-size-6 has-text-grey">{{ product.price }}</p>
          <p class="is-size-6 has-text-grey">{{ product.date_added }}</p>
          </p>
          <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">نمایش گزینه ها</router-link>
        </div>
      </div> -->
      <ProductBox v-for="product in latestProducts" v-bind:key="product.id" v-bind:product="product" dirt="rtl"/>
      <!-- <ProductBox v-for="product in uniqueLatestProducts" :key="product.id" :product="product" /> -->

    </div>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">محبوب ترین ها</h2>
        <div class="is-loading-bar has-text-centered" v-bind:class="{ 'is-loading': $store.state.isLoading }">
          <div class="lds-dual-ring"></div>
        </div>
      </div>

      <!-- <div class="column is-3" v-for="product in latestProducts" v-bind:key="product.id">
        <div class="box">
          <figure class="image mb-4">
            <img :src="product.get_thumbnail">
            <img v-bind:src="product.get_tumbnail">
          </figure>
          <h3 class="is-size-4">{{ product.name }}</h3>
          <p>تومان
          <p class="is-size-6 has-text-grey">{{ product.price }}</p>
          <p class="is-size-6 has-text-grey">{{ product.date_added }}</p>
          </p>
          <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">نمایش گزینه ها</router-link>
        </div>
      </div> -->
      <!-- <ProductBox v-for="product in popularProducts" v-bind:key="product.id" v-bind:product="product" /> -->
      <!-- <ProductBox v-if="popularProducts.length > 0" :product="popularProducts[0]" /> -->
      <!-- <ProductBox v-if="latestProducts.length > 0" :product="latestProducts[latestProducts.length - 1]" /> -->
      <ProductBox v-for="product in uniquePopularProducts" :key="product.id" :product="product" />

      <!-- <ProductBox v-for="(product, index) in popularProducts.slice(0, 4)" v-bind:key="index" v-bind:product="product" />
      <ProductBox v-if="popularProducts.length > 0" v-bind:product="popularProducts[0]" /> -->


    </div>
  </div>
</template>

<script>
// import router from '@/router'
import axios from 'axios'

import ProductBox from '@/components/ProductBox'
// import MainCarousel from '@/components/MainCarousel'
import MainCarousel from '@/components/MainCarousel';
// import Slide from '@/components/Slide';

export default {
  name: 'Home',
  data() {
    return {
      latestProducts: [],
      popularProducts: []
    }
  },
  components: {
    ProductBox,
    MainCarousel
  },
  // setup() {
  //   const carouselSlides = ["bg-4", "bg-5", "bg-6"];

  //   return { carouselSlides };
  // },
  mounted() {
    this.getLatestProducts()
    this.getPopularProducts()
    document.title = 'خانه | صنایع دستی'

  },
  computed: {
    uniqueLatestProducts() {
      return this.filterUniqueProducts(this.latestProducts);
    },
    uniquePopularProducts() {
      return this.filterUniqueProducts(this.popularProducts);
    }
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit('setIsLoading', true)

      await axios.get('/api/v1/latest-products/').then(response => {
        this.latestProducts = response.data
      })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)

    },
    async getPopularProducts() {
      this.$store.commit('setIsLoading', true)

      await axios.get('/api/v1/toprated-products/').then(response => {
        this.popularProducts = response.data
        console.log('API Response:', response.data); // Log the API response for debugging
      })
        .catch(error => {
          console.log(error)
        })
      this.$store.commit('setIsLoading', false)

    },
    filterUniqueProducts(products) {
      const productMap = {};
      products.forEach(product => {
        productMap[product.id] = product;
      });
      return Object.values(productMap);
    }

  }
}
</script>
<!-- <style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: 1.25rem;
  margin-right: 1.25rem;
}
</style> -->