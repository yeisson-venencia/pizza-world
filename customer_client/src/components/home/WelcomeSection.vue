<template>
  <v-row class="home-container">
    <v-col class="home-col" align="center">
      <v-row class="home-message-container" align="center">
        <v-col class="home-slogan">
          <h1>THE ONLY PLACE IN THE WORLD</h1>
          <h2>"... with the best taste in the Pizza!!!"</h2>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<style lang="scss" scoped>
@import "../../styles/main.scss";
.home-container {
  background-image: url("../../assets/home_main.jpg");
  background-position: bottom;
  margin: 0;
  background-size: cover;
  height: 100%;
  font-size: 22px;
  width: 100%;
}

.home-col {
  background: rgb(20, 24, 19, 0.6);
}

.home-message-container {
  margin: 0;
  padding: 0;
  height: 100%;
}

.home-slogan {
  color: rgb(236, 234, 234);
  font-size: 150%;
}
</style>
