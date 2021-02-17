<template>
  <v-row
    class="home-container about-container"
    align="center"
    justify="center"
    id="about"
  >
    <v-col class="column-container">
      <v-row class="about-text-container" align="end">
        <v-col align="center">
          <h2>At Pizza World...</h2>
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
        <div class="about-image about-image-message">
          <p>
            " ...Come and spend a great time with your friend sharing a tasty
            Pizza!!!"
          </p>
        </div>
        <div class="about-image about-image-logo">
          <v-img
            src="../assets/pizza_world_logo.png"
            width="100%"
            height="100%"
          ></v-img>
        </div>
        <div class="about-image">
          <v-img
            src="../assets/share_pizza.jpg"
            width="100%"
            height="100%"
            class="about-image-share"
          ></v-img>
        </div>
      </v-row>
    </v-col>
  </v-row>
</template>
