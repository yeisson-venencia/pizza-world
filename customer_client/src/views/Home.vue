<template>
  <welcome-section></welcome-section>
</template>

<script>
// @ is an alias to /src
import WelcomeSection from "./../components/home/WelcomeSection";

export default {
  name: "Home",
  components: { "welcome-section": WelcomeSection },
};
</script>

<style lang="scss" scoped></style>
