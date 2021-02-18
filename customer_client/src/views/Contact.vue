<template>
  <v-row id="contact" class="home-container contact-container" justify="center">
    <v-col class="contact-info-container">
      <v-row>
        <v-col align="center">
          <h1>HELP US TO IMPROVE</h1>
          <h3>Please Leave us your recomendation here</h3>
        </v-col>
      </v-row>
      <v-row aligh="center" justify="center">
        <v-col class="text-contaniner" align="center">
          <v-textarea auto-grow filled rows="6" row-height="20"></v-textarea>
          <v-btn class="full-width">Send suggestion</v-btn>
        </v-col>
      </v-row>
    </v-col>
  </v-row>
</template>

<style lang="scss">
.contact-container {
  background-color: #e0e0e0;
}
.contact-info-container {
  max-width: 60%;
  height: 100%;
  background-color: white;
  padding-top: 7%;
}

.text-contaniner {
  max-width: 70%;
}

.full-width {
  width: 100%;
}
</style>
