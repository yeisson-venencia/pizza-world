<template>
  <v-card color="grey" max-width="375">
    <v-img height="300" :src="image"></v-img>
    <v-card-title>{{ title }}</v-card-title>
    <v-card-subtitle> {{ subtitle }}</v-card-subtitle>
    <v-card-text>{{ text }}</v-card-text>
  </v-card>
</template>

<script>
export default {
  props: {
    image: String,
    title: String,
    subtitle: String,
    text: String,
  },
};
</script>
