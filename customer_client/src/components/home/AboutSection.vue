<template>
  <v-row class="home-container about-container" align="center" justify="center">
    <v-col class="column-container">
      <v-row class="about-text-container" align="end">
        <v-col align="center">
          <h2>Our company</h2>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod quos
            modi id dolorum eius dolores nobis laborum omnis molestiae dolore.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Quod quos
            modi id dolorum eius dolores nobis laborum omnis molestiae dolore.
          </p>
        </v-col>
      </v-row>

      <v-row
        class="about-images-container"
        align="center"
        justify="space-around"
      >
        <div class="about-image about-image-message"></div>
        <div class="about-image about-image-logo"></div>
        <div class="about-image"></div>
      </v-row>
    </v-col>
  </v-row>
</template>

<style lang="scss" scoped>
@import "../../styles/main.scss";
.about-container {
  background-color: #e0e0e0;
}

.column-container {
  max-width: 80%;
  height: 90%;
}

.about-text-container {
  height: 40%;
}

.about-images-container {
  background-color: white;
  height: 60%;
}

.about-image {
  background-color: $success-color;
  width: 25%;
  height: 90%;
  border-radius: 12px;
}
</style>
