<template>
  <v-row class="home-container"> </v-row>
  <!-- <div class="home">
    <v-img src="../assets/home_main.jpg" max-height="550"> </v-img>
  </div> -->
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
};
</script>

<style lang="scss" scoped>
.home-container {
  background-image: url("../assets/home_main.jpg");
  background-position: bottom;
  margin: 0;
  background-size: cover;
  height: 100%;
  font-size: 22px;
  width: 100%;
}
</style>
