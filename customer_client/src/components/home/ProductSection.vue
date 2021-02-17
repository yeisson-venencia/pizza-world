<template>
  <v-row
    class="home-container products-container"
    align="center"
    justify="space-around"
    id="product"
  >
    <product-card
      v-for="product in products"
      :key="product.title"
      :image="resolve_img_url(product.imagePath)"
      :title="product.title"
      :subtitle="product.subtitle"
      :text="product.text"
    >
    </product-card>
  </v-row>
</template>

<script>
import ProductCard from "./ProductCard";

export default {
  components: {
    "product-card": ProductCard,
  },
  data() {
    return {
      products: [
        {
          imagePath: "pizza.jpg",
          title: "Pizzas",
          subtitle: "The best pizzas in the area",
          text: "Cooked with the most aromatic ingredients",
        },
        {
          imagePath: "milkshake.jpg",
          title: "Milkshakes",
          subtitle: "The best pizzas in the area",
          text: "Cooked with the most aromatic ingredients",
        },
        {
          imagePath: "dessert.jpg",
          title: "Desserts",
          subtitle: "The best pizzas in the area",
          text: "Cooked with the most aromatic ingredients",
        },
      ],
    };
  },
  methods: {
    resolve_img_url(path) {
      const images = require.context("../../assets", false, /\.png$|\.jpg$/);
      return images("./" + path);
    },
  },
};
</script>

<style lang="scss" scoped>
/* @import "../../styles/main.scss"; */
</style>
