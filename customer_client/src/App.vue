<template>
  <v-app>
    <the-nav></the-nav>
    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import TheNav from "./components/common/TheNav";
export default {
  name: "App",
  components: {
    "the-nav": TheNav,
  },
};
</script>

<style lang="scss">
@import "./styles/main.scss";
</style>
