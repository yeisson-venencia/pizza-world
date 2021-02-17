<template>
  <v-row
    class="home-container about-container"
    alingn="center"
    justify="center"
  >
    <v-col class="column-container" align="center">
      <v-row>
        <v-col align="center">
          <h2>Our company</h2>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dicta,
            magni!
          </p>
        </v-col>
      </v-row>

      <v-row aling="center" justify="space-around">
        <div class="test"></div>
        <div class="test"></div>
        <div class="test"></div>
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
}

.test {
  background-color: $success-color;
  width: 300px;
  height: 300px;
  border-radius: 20px;
}
</style>
