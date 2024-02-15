<template>
  <div class="home">


    <div class="product-cards-container">
      <ProductList v-for="product in items" :key="product.id" :product="product" v-on:add-to-cart="addToCart($event)"/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import items from '../data/items.js';
import ProductList from '../components/ProductList.vue';

export default {
  name: 'HomeView',
  components: {
    ProductList

  },
  data () {
    return{
      items: items,
      product: null
    }
  },
  methods: {
    addToCart(product) {
      this.product = product;
      console.log(this.product);
    }
  }
};
</script>

<style lang="scss">
  .product-cards-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
  }
</style>