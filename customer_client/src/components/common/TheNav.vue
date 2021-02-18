<template>
  <v-app-bar app class="navbar-color">
    <v-img
      src="../../assets/pizza_world_logo_text.png"
      max-width="160"
      @click="go_home()"
      class="logo-pointer"
    ></v-img>
    <v-spacer></v-spacer>
    <v-row>
      <v-btn
        v-for="section in views"
        :key="section.label"
        plain
        color="black"
        :to="section.link"
      >
        <h2>{{ section.label }}</h2>
      </v-btn>
    </v-row>
    <v-spacer> </v-spacer>
    <v-btn plain color="black"><h2>Log in</h2></v-btn>
  </v-app-bar>
</template>

<script>
export default {
  data() {
    return {
      views: [
        { link: "/", label: "Home" },
        { link: "/products", label: "Products" },
        { link: "/about", label: "About" },
        { link: "/contact", label: "Contact us" },
        { link: "/order", label: "Order" },
      ],
    };
  },
  methods: {
    go_home() {
      this.$router.push("/");
    },
  },
};
</script>
