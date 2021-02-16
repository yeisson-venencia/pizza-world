<template>
  <v-app-bar app color="red" dark>
    <v-img src="../../assets/pizza_world_logo_text.png" max-width="160"></v-img>
    <v-spacer></v-spacer>
    <v-row>
      <v-btn
        v-for="section in views"
        :key="section.label"
        plain
        :to="section.link"
        color="black"
        ><h2>{{ section.label }}</h2></v-btn
      >
    </v-row>
    <v-spacer> </v-spacer>
    <v-btn>Log In</v-btn>
  </v-app-bar>
</template>

<script>
export default {
  data() {
    return {
      views: [
        { link: "/", label: "Home" },
        { link: "/product", label: "Product" },
        { link: "/order", label: "Order" },
        { link: "/about", label: "About" },
        { link: "/contanct", label: "Contact us" },
      ],
    };
  },
};
</script>
