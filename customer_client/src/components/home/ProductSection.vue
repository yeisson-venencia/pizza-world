<template>
  <v-row
    class="home-container products-container"
    align="center"
    justify="space-around"
  >
    <v-card
      color="grey"
      max-width="375"
      v-for="product in products"
      :key="product.title"
    >
      <v-img height="300" :src="resolve_img_url(product.imagePath)"></v-img>
      <v-card-title>{{ product.title }}</v-card-title>
      <v-card-subtitle> {{ product.subtitle }}</v-card-subtitle>
      <v-card-text>{{ product.text }}</v-card-text>
    </v-card>
  </v-row>
</template>

<script>
export default {
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
@import "../../styles/main.scss";
.products-container {
  background-color: rgb(244, 140, 6, 0.4);
}
</style>
