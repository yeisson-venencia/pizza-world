<template>
  <v-row class="home-container" align="center" justify="space-around">
    <v-card max-width="374" v-for="product in products" :key="product.title">
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

<style scoped></style>
